import streamlit as st

from src.components.ui import inject_css
from src.pages import country_page, fate_page, global_waste, historical, india_focus, methodology, ocean_page, overview, sector_page, waste_gdp_page

st.set_page_config(page_title="Global Plastic Analytics", page_icon="♻", layout="wide", initial_sidebar_state="expanded")
inject_css()
with st.sidebar:
    st.markdown('<div class="brand"><div class="brand-title">GLOBAL PLASTIC<br>ANALYTICS</div><div class="brand-copy">Data-driven insights into plastic production, waste and environmental impact</div></div>', unsafe_allow_html=True)
    st.caption("Explore the evidence by question")

navigation = st.navigation({
    "OVERVIEW": [st.Page(overview, title="Executive Overview")],
    "ANALYSIS": [
        st.Page(historical, title="Historical Trends"),
        st.Page(global_waste, title="Global Plastic Waste"),
        st.Page(waste_gdp_page, title="Waste & GDP Analysis"),
        st.Page(fate_page, title="Waste Management & Fate"),
        st.Page(sector_page, title="Industrial Sector Analysis"),
        st.Page(ocean_page, title="Ocean Plastic & Rivers"),
    ],
    "EXPLORATION": [
        st.Page(country_page, title="Country Explorer"),
        st.Page(india_focus, title="India Focus"),
    ],
    "REFERENCE": [st.Page(methodology, title="Methodology & Sources")],
})
navigation.run()
