import pandas as pd
import streamlit as st

from .analysis.statistics import correlation, describe_series, percent_change
from .components.ui import chart_card, compact_number, empty_state, fact_card, insight_card, kpi, page_header, question, source_line
from .data.loader import load_dataset
from .data.registry import DATASET_REGISTRY
from .visualization.charts import area_chart, bar_chart, choropleth, histogram, line_chart, scatter_chart


def _coverage(df):
    if "Year" not in df or df["Year"].dropna().empty:
        return "not specified"
    return f"{int(df['Year'].min())}–{int(df['Year'].max())}"


def _metric_options(df):
    excluded = {"Entity", "Code", "Year", "World region according to OWID", "Population"}
    return [column for column in df.columns if column not in excluded and pd.api.types.is_numeric_dtype(df[column])]


def _source(key, df):
    spec = DATASET_REGISTRY[key]
    return spec["label"], spec["unit"], _coverage(df)


def _kpi_row(items):
    cols = st.columns(len(items))
    for col, (label, value, note) in zip(cols, items):
        with col:
            kpi(label, value, note)


def _fact_row(items):
    cols = st.columns(len(items))
    for col, (label, value, copy) in zip(cols, items):
        with col:
            fact_card(label, value, copy)


def overview():
    production = load_dataset("production")
    fate = load_dataset("fate")
    waste_gdp = load_dataset("waste_gdp")
    ocean = load_dataset("ocean_share")
    page_header("Global plastic waste", "GLOBAL PLASTIC WASTE", "Historical trends, waste generation and environmental impact")
    st.caption("A data-driven view of plastic production, waste management and ocean pollution using Our World in Data packages.")
    latest_production = production.iloc[-1, -1] if not production.empty else None
    latest_fate = fate[fate["Entity"].eq("World")].sort_values("Year") if "Entity" in fate else pd.DataFrame()
    waste_total = latest_fate[["Recycled", "Incinerated", "Mismanaged", "Landfilled"]].sum(axis=1).iloc[-1] if not latest_fate.empty else None
    _kpi_row([
        ("Global production", compact_number(latest_production), "tonnes in 2019"),
        ("Waste through fate system", compact_number(waste_total), "world total in 2019"),
        ("Datasets connected", str(len(DATASET_REGISTRY)), "OWID packages"),
        ("Production coverage", _coverage(production), "observed years"),
    ])
    question("How has global plastic production changed?", "The long-run production series provides the dashboard's historical baseline.")
    value = production.columns[-1] if not production.empty else ""
    chart_card("Annual production rises sharply after the mid-20th century", line_chart(production, "Year", value, "Annual global plastic production", y_title="Tonnes"), "Observed annual production; the series contains a documented gap in 1974.", _source("production", production))
    left, right = st.columns(2)
    with left:
        question("Which countries generated the most plastic waste?", "This ranking sums the four observed end-of-life categories for coded country rows in the latest year.")
        if not fate.empty:
            year = int(fate["Year"].max())
            ranked = fate[(fate["Year"] == year) & fate["Code"].notna() & ~fate["Code"].str.startswith("OWID_", na=False)].copy()
            ranked["Total waste"] = ranked[["Recycled", "Incinerated", "Mismanaged", "Landfilled"]].sum(axis=1)
            ranked = ranked.nlargest(10, "Total waste")
            chart_card(f"Top countries by total waste fate, {year}", bar_chart(ranked, "Entity", "Total waste", f"Top countries, {year}", "Tonnes"), "Horizontal bars make country ranking and value labels easy to scan.", _source("fate", fate))
            if not ranked.empty:
                insight_card(f"{ranked.iloc[-1]['Entity']} has the largest observed combined waste-fate total among the coded country rows in {year}.")
        else:
            empty_state()
    with right:
        question("Does plastic waste increase with income?", "The paired 2010 snapshot compares per-capita waste with GDP per capita; it is descriptive, not causal.")
        scatter = waste_gdp[(waste_gdp["Year"] == 2010)].dropna(subset=["Per capita plastic waste", "GDP per capita"]) if not waste_gdp.empty else pd.DataFrame()
        chart_card("Per-capita waste against GDP per capita, 2010", scatter_chart(scatter, "GDP per capita", "Per capita plastic waste", "Observed 2010 relationship", color="World region according to OWID", hover=["Year"]), "Each point is an entity with both indicators observed in 2010.", _source("waste_gdp", waste_gdp))
    question("Where is ocean plastic waste concentrated?", "The map shows country-coded observations only; regional aggregates are excluded from the map.")
    chart_card("Share of global plastic waste emitted to the ocean, 2019", choropleth(ocean, ocean.columns[-1] if not ocean.empty else "", "Share of global plastic waste emitted to the ocean, 2019"), "Color intensity represents the observed share of the global total.", _source("ocean_share", ocean))
    st.markdown('<div class="section-kicker">Key facts</div>', unsafe_allow_html=True)
    if not production.empty:
        first = production.iloc[0, -1]
        change = (latest_production - first) / first * 100 if first else None
        _fact_row([
            ("Long-run change", f"{change:,.0f}%" if change is not None else "No data", "Change in observed production from 1950 to 2019"),
            ("Latest production", compact_number(latest_production), "World production in the final observed year"),
            ("Ocean map", str(ocean["Entity"].nunique()) if "Entity" in ocean else "No data", "Entities in the 2019 ocean-share package"),
        ])


def historical():
    production = load_dataset("production")
    fate = load_dataset("fate")
    page_header("Analysis", "Historical trends", "Explore observed time series without filling missing years.")
    datasets = {"Global production": (production, production.columns[-1] if not production.empty else ""), "Waste fate": (fate[fate["Entity"].eq("World")] if not fate.empty else fate, "Mismanaged"), "Recycled waste": (fate[fate["Entity"].eq("World")] if not fate.empty else fate, "Recycled")}
    choice = st.selectbox("Metric", list(datasets))
    df, metric = datasets[choice]
    if df.empty or metric not in df:
        empty_state("This metric is not available in the selected dataset.")
        return
    years = sorted(df["Year"].dropna().unique().tolist())
    selected = st.slider("Observed year range", min_value=int(years[0]), max_value=int(years[-1]), value=(int(years[0]), int(years[-1]))) if len(years) > 1 else (int(years[0]), int(years[0]))
    filtered = df[df["Year"].between(*selected)]
    question("How has the selected indicator changed over time?", "The range control preserves the observed years and never interpolates missing historical values.")
    chart_card(choice, line_chart(filtered, "Year", metric, choice, y_title=DATASET_REGISTRY["production"]["unit"] if choice == "Global production" else "Tonnes"), f"Observed period: {selected[0]}–{selected[1]}.", _source("production" if choice == "Global production" else "fate", df))
    stats = describe_series(filtered[metric])
    _kpi_row([
        ("Minimum", compact_number(stats.get("minimum")), choice),
        ("Maximum", compact_number(stats.get("maximum")), choice),
        ("Mean", compact_number(stats.get("mean")), choice),
        ("Observed rows", str(stats.get("count", 0)), "rows in selected period"),
    ])
    if stats:
        change = percent_change(filtered[metric].dropna().iloc[0], filtered[metric].dropna().iloc[-1])
        insight_card(f"Across the selected observed period, {choice.lower()} changed by {change:,.1f}% from the first available value to the last." if change is not None else "A percentage change cannot be calculated from the selected observations.")


def global_waste():
    df = load_dataset("fate")
    page_header("Analysis", "Global plastic waste", "Rank countries using a single observed year and a selected waste measure.")
    if df.empty:
        empty_state(); return
    countries = df[df["Code"].notna() & ~df["Code"].str.startswith("OWID_", na=False)]
    year = st.selectbox("Year", sorted(countries["Year"].unique(), reverse=True))
    metric = st.selectbox("Metric", ["Recycled", "Incinerated", "Mismanaged", "Landfilled"])
    top_n = st.slider("Top N countries", 5, 20, 10)
    selected = countries[countries["Year"].eq(year)]
    filtered = selected.nlargest(top_n, metric)
    _kpi_row([
        ("Selected year", str(year), metric),
        ("Top country", filtered.iloc[0]["Entity"] if not filtered.empty else "No data", "highest observed value"),
        ("Top country value", compact_number(filtered.iloc[0][metric]) if not filtered.empty else "No data", "tonnes"),
        ("Countries with data", str(selected[metric].notna().sum()), "coded country rows"),
    ])
    question("Which countries generated the most plastic waste?", "The ranking uses one selected year and only coded country rows, avoiding mixed-year comparisons.")
    chart_card(f"Top {top_n} countries by {metric.lower()}, {year}", bar_chart(filtered, "Entity", metric, f"Top {top_n} countries by {metric.lower()}, {year}", "Tonnes"), "Labels show the observed tonnes for each country.", _source("fate", df))
    question("Where is this waste measure concentrated geographically?", "The map provides geographic context for the same selected year and metric.")
    chart_card(f"Geographic distribution of {metric.lower()}, {year}", choropleth(selected, metric, f"{metric}, {year}"), "Regional aggregates are omitted when no country code is present.", _source("fate", df))
    question("How widely do country values vary?", "The distribution shows the spread across coded countries in the selected year.")
    chart_card(f"Distribution of {metric.lower()}, {year}", histogram(selected, metric, f"Distribution of {metric.lower()}, {year}"), "Use the ranking above for identity and this distribution for spread.", _source("fate", df))
    if not filtered.empty:
        insight_card(f"{filtered.iloc[0]['Entity']} records the largest observed {metric.lower()} value in {year}: {compact_number(filtered.iloc[0][metric])} tonnes.")


def waste_gdp_page():
    df = load_dataset("waste_gdp")
    page_header("Analysis", "Waste & GDP analysis", "Compare plastic waste generation with GDP per capita for the observed 2010 plastic indicator.")
    if df.empty:
        empty_state(); return
    valid = df.dropna(subset=["Per capita plastic waste", "GDP per capita"])
    years = sorted(valid["Year"].unique())
    year = st.selectbox("Year with paired observations", years, index=len(years) - 1)
    selected = valid[valid["Year"].eq(year)]
    r, n = correlation(selected, "GDP per capita", "Per capita plastic waste")
    _kpi_row([
        ("Pearson correlation", f"{r:.2f}" if r is not None else "No data", f"n = {n}"),
        ("Countries analyzed", str(n), "paired observations"),
        ("Selected year", str(year), "paired indicator year"),
        ("Median waste", f"{selected['Per capita plastic waste'].median():.3f}" if not selected.empty else "No data", "kg/person/day"),
    ])
    question("Is plastic waste associated with GDP per capita?", "The scatter plot compares paired observations for the selected year. It describes association only.")
    chart_card(f"Plastic waste vs GDP per capita, {year}", scatter_chart(selected, "GDP per capita", "Per capita plastic waste", f"Plastic waste vs GDP per capita, {year}", color="World region according to OWID", hover=["Entity", "Year"]), "Points are colored by OWID world region and include only non-missing paired values.", _source("waste_gdp", df))
    st.caption("Correlation does not imply causation.")
    if not selected.empty:
        high = selected.loc[selected["Per capita plastic waste"].idxmax()]
        insight_card(f"The highest observed per-capita waste value in the selected year is {high['Per capita plastic waste']:.3f} kg/person/day for {high['Entity']}.")


def fate_page():
    df = load_dataset("fate_share")
    page_header("Analysis", "Waste management & fate", "Inspect the observed percentage distribution of plastic waste by end-of-life fate.")
    if df.empty:
        empty_state(); return
    entities = sorted(df["Entity"].dropna().unique())
    entity = st.selectbox("Entity", entities, index=entities.index("World") if "World" in entities else 0)
    selected = df[df["Entity"].eq(entity)].sort_values("Year")
    _kpi_row([
        ("Selected entity", entity, "fate-share series"),
        ("Latest year", str(int(selected["Year"].max())) if not selected.empty else "No data", "latest observed"),
        ("Mismanaged share", f"{selected.iloc[-1]['Mismanaged']:.1f}%" if not selected.empty else "No data", "latest observed"),
        ("Recycled share", f"{selected.iloc[-1]['Recycled']:.1f}%" if not selected.empty else "No data", "latest observed"),
    ])
    question("How has the waste-fate mix changed?", "The stacked area view shows the observed percentage composition by disposal method.")
    chart_card(f"Waste fate shares: {entity}", area_chart(selected, "Year", ["Recycled", "Incinerated", "Mismanaged", "Landfilled"], f"Waste fate shares: {entity}", percent=True), "Shares are percentages and should be read as composition, not tonnes.", _source("fate_share", df))
    latest = selected.tail(1).melt(id_vars=["Entity", "Year"], value_vars=["Recycled", "Incinerated", "Mismanaged", "Landfilled"], var_name="Category", value_name="Share")
    question("What is the latest observed disposal mix?", "A compact category ranking makes the latest composition easier to compare.")
    chart_card("Latest observed fate shares", bar_chart(latest, "Category", "Share", "Latest observed fate shares", "%"), "The four categories are compared within the selected entity and latest observed year.", _source("fate_share", df))


def sector_page():
    df = load_dataset("sector")
    page_header("Analysis", "Industrial sector analysis", "Compare 2019 plastic waste generation across applications and regions.")
    if df.empty:
        empty_state(); return
    region = st.selectbox("Region", [column for column in df.columns if column not in {"Entity", "Year"}], index=5)
    selected = df[df["Entity"].ne("Total")][["Entity", region]].rename(columns={region: "Tonnes"}).sort_values("Tonnes")
    _kpi_row([
        ("Region", region, "2019 sector table"),
        ("Largest sector", selected.iloc[-1]["Entity"] if not selected.empty else "No data", "highest observed value"),
        ("Largest value", compact_number(selected.iloc[-1]["Tonnes"]) if not selected.empty else "No data", "tonnes"),
        ("Sectors compared", str(len(selected)), "non-total applications"),
    ])
    question("Which industrial sectors generate the most plastic waste?", "The 2019 table is ranked by the selected region or aggregate.")
    chart_card(f"Plastic waste by industrial sector: {region}", bar_chart(selected, "Entity", "Tonnes", f"Plastic waste by industrial sector: {region}", "Tonnes"), "The total row is excluded so applications can be compared directly.", _source("sector", df))


def ocean_page():
    ocean = load_dataset("ocean_share")
    rivers = load_dataset("rivers")
    page_header("Analysis", "Ocean plastic & rivers", "Review country shares and the ranked river observations available in the OWID packages.")
    country = ocean[ocean["Code"].notna() & ~ocean["Code"].str.startswith("OWID_", na=False)].nlargest(10, ocean.columns[-1])
    top_rivers = rivers.nlargest(10, rivers.columns[-1])
    _kpi_row([
        ("Top country", country.iloc[0]["Entity"] if not country.empty else "No data", "largest observed ocean share"),
        ("Top country share", f"{country.iloc[0][ocean.columns[-1]]:.2f}%" if not country.empty else "No data", "of global ocean emissions"),
        ("Top river", top_rivers.iloc[0]["Entity"] if not top_rivers.empty else "No data", "largest recorded river share"),
        ("River share", f"{top_rivers.iloc[0][rivers.columns[-1]]:.2f}%" if not top_rivers.empty else "No data", "of global ocean emissions"),
    ])
    question("Which countries contribute the largest observed shares?", "The country ranking excludes OWID regional aggregates and uses the 2019 snapshot.")
    chart_card("Top country shares of plastic waste emitted to the ocean", bar_chart(country, "Entity", ocean.columns[-1], "Top country shares", "%"), "This is a share of the global estimate, not total tonnes emitted.", _source("ocean_share", ocean))
    question("Which rivers have the largest recorded contributions?", "The river dataset contains a single 2019 observation for each listed river or waterway.")
    chart_card("Top recorded river contributions", bar_chart(top_rivers, "Entity", rivers.columns[-1], "Top river observations", "%"), "River names are retained as published by OWID; no coordinates are inferred.", _source("rivers", rivers))
    question("Where are country-level shares distributed geographically?", "The map is useful for country context; river locations are intentionally not mapped because coordinates are absent.")
    chart_card("Country share of global ocean plastic waste", choropleth(ocean, ocean.columns[-1], "Country share of global ocean plastic waste"), "Only country-coded observations appear on the map.", _source("ocean_share", ocean))
    if not country.empty:
        insight_card(f"{country.iloc[0]['Entity']} has the largest country-coded observed share in this 2019 dataset at {country.iloc[0][ocean.columns[-1]]:.2f}%.")


def country_page(india=False):
    fate = load_dataset("fate")
    page_header("Exploration", "India focus" if india else "Country explorer", "A country-level view limited to indicators with observed values.")
    if fate.empty:
        empty_state(); return
    available = sorted(fate.loc[fate["Code"].notna() & ~fate["Code"].str.startswith("OWID_", na=False), "Entity"].unique())
    default = "India" if india and "India" in available else available[0]
    country = st.selectbox("Country", available, index=available.index(default))
    selected = fate[fate["Entity"].eq(country)].sort_values("Year")
    if selected.empty:
        empty_state("No data available for this country."); return
    latest = selected.iloc[-1]
    _kpi_row([(metric, compact_number(latest[metric]), f"tonnes in {int(latest['Year'])}") for metric in ["Recycled", "Incinerated", "Mismanaged", "Landfilled"]])
    question(f"How has {country}'s mismanaged plastic waste changed?", "The trend uses the country rows available in the annual waste-fate dataset.")
    chart_card(f"Mismanaged plastic waste: {country}", line_chart(selected, "Year", "Mismanaged", f"Mismanaged plastic waste: {country}", y_title="Tonnes"), "Observed annual values; no missing years are filled.", _source("fate", selected))
    total = latest[["Recycled", "Incinerated", "Mismanaged", "Landfilled"]].sum()
    _fact_row([
        ("Latest observed year", str(int(latest["Year"])), "annual waste-fate record"),
        ("Mismanaged share", f"{latest['Mismanaged'] / total * 100:.1f}%" if total else "No data", "of this country's observed fate total"),
        ("Recorded total", compact_number(total), "tonnes across fate categories"),
    ])
    if india:
        insight_card("India is shown using only the indicators and years present in the downloaded OWID country rows; no unsupported comparison is implied.", "India focus")


def india_focus():
    country_page(india=True)


def methodology():
    page_header("Reference", "Methodology & sources", "How this project uses and interprets the downloaded OWID data packages.")
    st.markdown("""
    **Project objective**  
    This dashboard supports exploratory analysis of plastic production, waste generation, waste fate, and ocean pollution indicators.

    **Data sources**  
    All datasets are downloaded from [Our World in Data](https://ourworldindata.org/) and retain their source metadata in `data/`.

    **Cleaning and validation**  
    CSVs are loaded with caching, numeric fields are coerced with invalid values becoming missing, duplicate rows are removed, and every chart checks that its required columns exist. Missing observations are left missing; no years or values are fabricated.

    **Statistical methods**  
    The dashboard calculates descriptive statistics, observed percentage changes where applicable, and Pearson correlations only from paired non-missing observations. Correlation is descriptive and does not imply causation.

    **Limitations**  
    Coverage varies substantially by dataset: production spans 1950–2019, fate spans 2000–2019, the plastic-waste per-capita snapshot is 2010, and many ocean indicators are 2019 only. Regional aggregates and country rows are not interchangeable.
    """)
    audits = []
    for key, spec in DATASET_REGISTRY.items():
        df = load_dataset(key)
        audit = {"Dataset": spec["label"], "Rows": len(df), "Coverage": _coverage(df), "Entities": df["Entity"].nunique() if "Entity" in df else "n/a", "Unit": spec["unit"]}
        audits.append(audit)
    st.dataframe(pd.DataFrame(audits), use_container_width=True, hide_index=True)
