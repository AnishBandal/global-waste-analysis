import pandas as pd
import plotly.express as px

from .themes import COLORS, apply_plotly_theme, empty_figure


def line_chart(df, x, y, title, color=None, y_title=None):
    if df.empty or x not in df or y not in df:
        return empty_figure()
    fig = px.line(df, x=x, y=y, color=color, title=None, markers=True, color_discrete_sequence=COLORS)
    fig.update_traces(hovertemplate=f"%{{x}}<br>{y}: %{{y:,.3s}}<extra></extra>")
    return apply_plotly_theme(fig, yaxis_title=y_title or y, height=350, margin={"l": 12, "r": 12, "t": 12, "b": 28})


def bar_chart(df, x, y, title, y_title=None, color=None):
    if df.empty or x not in df or y not in df:
        return empty_figure()
    horizontal = x in {"Entity", "Category"}
    ordered = df.sort_values(y, ascending=True if horizontal else False)
    fig = px.bar(ordered, x=y if horizontal else x, y=x if horizontal else y, color=color, title=None, orientation="h" if horizontal else "v", text=y if horizontal else None, color_discrete_sequence=COLORS)
    if horizontal:
        fig.update_traces(texttemplate="%{text:.3s}", textposition="outside", cliponaxis=False, hovertemplate=f"%{{y}}<br>{y}: %{{x:,.3s}}<extra></extra>")
        fig.update_xaxes(tickformat="~s", title=y_title or y)
        fig.update_yaxes(categoryorder="array", categoryarray=ordered[x].tolist(), title=None)
    else:
        fig.update_traces(hovertemplate=f"%{{x}}<br>{y}: %{{y:,.3s}}<extra></extra>")
    height = max(250, min(480, 190 + len(ordered) * 22))
    return apply_plotly_theme(fig, yaxis_title=None if horizontal else y_title or y, height=height, margin={"l": 8, "r": 34, "t": 12, "b": 30})


def scatter_chart(df, x, y, title, color=None, hover=None):
    if df.empty or x not in df or y not in df:
        return empty_figure()
    fig = px.scatter(df, x=x, y=y, color=color, hover_name="Entity" if "Entity" in df else None, hover_data=hover, title=None, color_discrete_sequence=COLORS)
    fig.update_traces(hovertemplate="%{hovertext}<br>%{x:,.2s}<br>%{y:,.3f}<extra></extra>")
    return apply_plotly_theme(fig, height=390, margin={"l": 12, "r": 12, "t": 12, "b": 28})


def area_chart(df, x, y_columns, title, percent=False):
    available = [column for column in y_columns if column in df.columns]
    if df.empty or x not in df or not available:
        return empty_figure()
    long_df = df[[x] + available].melt(x, var_name="Category", value_name="Value")
    fig = px.area(long_df, x=x, y="Value", color="Category", title=None, color_discrete_sequence=COLORS)
    return apply_plotly_theme(fig, yaxis_title="Percent" if percent else "Value", height=350, margin={"l": 12, "r": 12, "t": 12, "b": 28})


def histogram(df, column, title):
    if df.empty or column not in df:
        return empty_figure()
    fig = px.histogram(df, x=column, title=None, color_discrete_sequence=[COLORS[0]])
    return apply_plotly_theme(fig, height=300, margin={"l": 12, "r": 12, "t": 12, "b": 28})


def choropleth(df, value, title, year=None):
    required = {"Entity", "Code", value}
    if df.empty or not required.issubset(df.columns):
        return empty_figure("A country code and numeric value are required for the map.")
    map_df = df.dropna(subset=["Code", value]).copy()
    map_df = map_df[~map_df["Code"].str.startswith("OWID_", na=False)]
    if map_df.empty:
        return empty_figure("No country-level map data available.")
    fig = px.choropleth(map_df, locations="Code", color=value, hover_name="Entity", title=None, color_continuous_scale=["#DCFCE7", "#16A34A", "#0F3D2E"], scope="world")
    return apply_plotly_theme(fig, height=390, geo={"showframe": False, "showcoastlines": True, "projection_type": "natural earth"}, margin={"l": 0, "r": 0, "t": 12, "b": 0})
