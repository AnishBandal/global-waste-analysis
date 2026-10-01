# Global Plastic Waste: Data Analysis & Visualization

An interactive Streamlit dashboard for exploring plastic production, waste generation, waste management, industrial applications, and ocean pollution using datasets downloaded from [Our World in Data](https://ourworldindata.org/).

## Objectives

- Trace global plastic production from 1950 to 2019.
- Compare plastic waste and disposal outcomes across countries and regions.
- Examine observed relationships between plastic waste and GDP per capita.
- Explore industrial sectors, ocean emissions, and major contributing rivers.
- Provide a focused India comparison using available observations.

## Technology

Python, Streamlit, Pandas, NumPy, and Plotly. The interface uses Inter and a reusable green environmental analytics design system.

## Project structure

```text
app.py
pages/                         Streamlit analytical pages
src/data/                      Registry, cached loader, cleaning, validation
src/analysis/                  Descriptive statistics and correlations
src/visualization/             Plotly theme and chart builders
src/components/                Shared UI components
 data/                         OWID CSV, metadata, and readme packages
```

## Installation and running

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Datasets

The repository contains ten OWID packages: global plastics production; per-capita plastic waste; mismanaged plastic waste per capita; plastic waste versus GDP per capita; ocean plastic waste versus GDP; plastic fate; fate shares; industrial-sector waste; country shares of ocean emissions; top rivers; and cumulative plastic exports. Dataset-specific metadata and source citations remain alongside each CSV.

Coverage is not uniform. Production is 1950–2019, fate tables are 2000–2019, per-capita waste is a 2010 snapshot, and several ocean/sector indicators are 2019 snapshots. The dashboard displays observed coverage rather than implying that all data is current or continuous.

## Analysis and cleaning

CSV files are loaded through a cached registry-driven loader. Numeric columns are coerced safely, duplicate rows are removed, required columns are checked before chart creation, and missing values remain missing. No years, countries, coordinates, or statistics are fabricated. Descriptive statistics and Pearson correlations are calculated only from available observations.

## Limitations and future scope

Some datasets mix country and regional aggregates, so rankings explicitly filter to coded country rows where appropriate. The source data does not provide geographic coordinates for rivers, so the river page uses a ranked bar chart rather than a fabricated map. Future work could add automated data-package refreshes, richer country joins, and formal tests for analytical transformations.
