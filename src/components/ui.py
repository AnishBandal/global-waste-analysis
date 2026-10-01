import html

import streamlit as st


def inject_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    html, body, [class*="css"] { font-family: Inter, sans-serif; }
    .stApp { background: #F7F9F8; color: #111827; }
    .block-container { max-width: 1480px; padding-top: 2.2rem; padding-bottom: 4rem; }
    [data-testid="stSidebar"] { background: #0F3D2E; }
    [data-testid="stSidebar"] * { color: #F3F8F5; }
    .brand { padding: 1rem 0 1.5rem; }
    .brand-title { font-size: 1.25rem; font-weight: 800; letter-spacing: .04em; line-height: 1.05; }
    .brand-copy { color: #B9D8C5; font-size: .78rem; line-height: 1.45; margin-top: .65rem; }
    .eyebrow { color: #16A34A; font-size: .75rem; font-weight: 700; letter-spacing: .12em; text-transform: uppercase; }
    h1 { font-size: 2.35rem !important; font-weight: 800 !important; letter-spacing: 0 !important; }
    h2, h3 { letter-spacing: 0 !important; }
    .subtitle { color: #6B7280; font-size: 1rem; margin-top: -.6rem; margin-bottom: 1.7rem; max-width: 780px; }
    .section-kicker { color: #0F3D2E; font-size: .72rem; font-weight: 800; letter-spacing: .12em; text-transform: uppercase; margin-top: 1.8rem; }
    .question { color: #111827; font-size: 1.18rem; font-weight: 700; line-height: 1.3; margin-top: .25rem; }
    .question-copy { color: #6B7280; font-size: .86rem; line-height: 1.5; margin: .35rem 0 .8rem; max-width: 760px; }
    .kpi, .fact, .insight, .empty-card { background: white; border: 1px solid #E5E7EB; border-radius: 14px; padding: 1rem 1.1rem; min-height: 112px; box-shadow: 0 3px 14px rgba(15,61,46,.05); }
    .kpi-label { color: #6B7280; font-size: .78rem; font-weight: 600; text-transform: uppercase; letter-spacing: .06em; }
    .kpi-value { color: #0F3D2E; font-size: 1.65rem; font-weight: 800; margin-top: .45rem; }
    .kpi-note { color: #6B7280; font-size: .75rem; margin-top: .2rem; }
    .fact-label { color: #16A34A; font-size: .72rem; font-weight: 800; letter-spacing: .08em; text-transform: uppercase; }
    .fact-value { color: #0F3D2E; font-size: 1.4rem; font-weight: 800; margin-top: .45rem; }
    .fact-copy { color: #6B7280; font-size: .78rem; line-height: 1.4; margin-top: .2rem; }
    .insight { border-left: 4px solid #2563EB; min-height: 0; }
    .insight-label { color: #2563EB; font-size: .72rem; font-weight: 800; letter-spacing: .08em; text-transform: uppercase; }
    .insight-copy { color: #24332B; font-size: .9rem; line-height: 1.5; margin-top: .35rem; }
    .empty-card { background: #EEF8F0; border-left: 4px solid #16A34A; color: #244C35; min-height: 0; }
    .chart-card { background: #FFFFFF; border: 1px solid #E5E7EB; border-radius: 14px; padding: .75rem .9rem .4rem; box-shadow: 0 3px 14px rgba(15,61,46,.04); }
    .source { color: #6B7280; font-size: .72rem; margin: .35rem 0 1.2rem; }
    .notice { background: #EEF8F0; border-left: 4px solid #16A34A; border-radius: 8px; color: #244C35; padding: .8rem 1rem; }
    div[data-testid="stVerticalBlockBorderWrapper"] { border-color: #E5E7EB; border-radius: 14px; }
    [data-testid="stMetricValue"] { color: #0F3D2E; }
    </style>
    """, unsafe_allow_html=True)


def page_header(eyebrow, title, subtitle):
    st.markdown(f'<div class="eyebrow">{html.escape(str(eyebrow))}</div>', unsafe_allow_html=True)
    st.title(title)
    st.markdown(f'<div class="subtitle">{html.escape(str(subtitle))}</div>', unsafe_allow_html=True)


def kpi(label, value, note=""):
    st.markdown(f'<div class="kpi"><div class="kpi-label">{html.escape(str(label))}</div><div class="kpi-value">{html.escape(str(value))}</div><div class="kpi-note">{html.escape(str(note))}</div></div>', unsafe_allow_html=True)


def fact_card(label, value, copy):
    st.markdown(f'<div class="fact"><div class="fact-label">{html.escape(str(label))}</div><div class="fact-value">{html.escape(str(value))}</div><div class="fact-copy">{html.escape(str(copy))}</div></div>', unsafe_allow_html=True)


def insight_card(copy, label="Key insight"):
    st.markdown(f'<div class="insight"><div class="insight-label">{html.escape(str(label))}</div><div class="insight-copy">{html.escape(str(copy))}</div></div>', unsafe_allow_html=True)


def question(title, explanation=""):
    st.markdown(f'<div class="section-kicker">Analytical question</div><div class="question">{html.escape(str(title))}</div><div class="question-copy">{html.escape(str(explanation))}</div>', unsafe_allow_html=True)


def chart_card(title, figure, explanation="", source=None):
    with st.container(border=True):
        st.markdown(f'<div class="question">{html.escape(str(title))}</div><div class="question-copy">{html.escape(str(explanation))}</div>', unsafe_allow_html=True)
        st.plotly_chart(figure, use_container_width=True, config={"displayModeBar": "hover", "displaylogo": False, "modeBarButtonsToRemove": ["lasso2d", "select2d"]})
        if source:
            source_line(*source)


def source_line(dataset, unit, coverage):
    st.markdown(f'<div class="source">Source: Our World in Data &nbsp;·&nbsp; Dataset: {html.escape(str(dataset))} &nbsp;·&nbsp; Unit: {html.escape(str(unit))} &nbsp;·&nbsp; Coverage: {html.escape(str(coverage))}</div>', unsafe_allow_html=True)


def empty_state(message="No data available for this selection."):
    st.markdown(f'<div class="empty-card"><strong>Insufficient data for this visualization</strong><br>{html.escape(str(message))}</div>', unsafe_allow_html=True)


def compact_number(value):
    if value is None:
        return "No data"
    value = float(value)
    for divisor, suffix in ((1_000_000_000, "B"), (1_000_000, "M"), (1_000, "K")):
        if abs(value) >= divisor:
            return f"{value / divisor:.1f} {suffix}"
    return f"{value:,.1f}"


def format_value(value, unit=""):
    if value is None:
        return "No data"
    suffix = ""
    magnitude = abs(float(value))
    if magnitude >= 1_000_000_000:
        value, suffix = float(value) / 1_000_000_000, "B"
    elif magnitude >= 1_000_000:
        value, suffix = float(value) / 1_000_000, "M"
    elif magnitude >= 1_000:
        value, suffix = float(value) / 1_000, "K"
    else:
        value = float(value)
    return f"{value:,.2f} {suffix} {unit}".strip()
