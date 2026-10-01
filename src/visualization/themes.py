from copy import deepcopy

import plotly.graph_objects as go

BASE_LAYOUT = {
    "font": {"family": "Inter, sans-serif", "color": "#17201c"},
    "paper_bgcolor": "rgba(0,0,0,0)",
    "plot_bgcolor": "rgba(0,0,0,0)",
    "margin": {"l": 16, "r": 16, "t": 54, "b": 16},
    "hovermode": "closest",
    "legend": {"orientation": "h", "y": 1.08, "x": 0},
}

COLORS = ["#0F3D2E", "#16A34A", "#2563EB", "#F59E0B", "#DC2626", "#64748B"]


def apply_plotly_theme(fig, **overrides):
    layout = deepcopy(BASE_LAYOUT)
    layout.update(overrides)
    fig.update_layout(**layout)
    fig.update_xaxes(showgrid=False, zeroline=False, tickfont={"size": 11})
    fig.update_yaxes(showgrid=True, gridcolor="#EEF1EF", zeroline=False, tickfont={"size": 11})
    return fig


def empty_figure(message="No data available for this view."):
    fig = go.Figure()
    fig.add_annotation(text=message, x=0.5, y=0.5, xref="paper", yref="paper", showarrow=False, font={"size": 15, "color": "#6B7280"})
    return apply_plotly_theme(fig, height=320, xaxis={"visible": False}, yaxis={"visible": False}, hovermode=False)
