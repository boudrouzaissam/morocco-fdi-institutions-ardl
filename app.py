import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="Morocco FDI & Institutions",
    page_icon="📊",
    layout="wide"
)

st.title("Morocco FDI, Institutions and Economic Attractiveness")
st.subheader("ARDL/ECM analysis of institutional improvement and FDI inflows")

st.markdown(
    """
    This dashboard presents the main empirical findings of an ARDL/ECM analysis
    on the relationship between institutional improvement and foreign direct investment inflows in Morocco.
    """
)

st.divider()

# =========================
# Key findings
# =========================

st.header("Key empirical findings")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Institutional improvement",
        value="+4.04%",
        delta="Long-run effect for +0.01 point in ΔFRAZER"
    )

with col2:
    st.metric(
        label="Economic growth",
        value="+12.37%",
        delta="Long-run effect for +1 point of GDP"
    )

with col3:
    st.metric(
        label="Services openness",
        value="+13.82%",
        delta="Long-run effect for +1 point"
    )

st.info(
    "Exchange rate instability is not statistically significant in the long-run specification."
)

st.divider()

# =========================
# Model overview
# =========================

st.header("Empirical model")

st.latex(r"LIDE_t = f(\Delta FRAZER_t,\ CHANGE\_INSTAB_t,\ GDP_t,\ OPEN\_SERVICES_t)")

st.markdown(
    """
    **Selected specification:** ARDL(2,2,2,3,3)

    - `LIDE`: logarithm of FDI inflows  
    - `ΔFRAZER`: annual change in the Fraser Economic Freedom Index  
    - `CHANGE_INSTAB`: exchange rate instability  
    - `GDP`: economic growth  
    - `OPEN_SERVICES`: services openness  
    """
)

st.divider()

# =========================
# Long-run results
# =========================

st.header("Long-run results")

longrun = pd.DataFrame({
    "Factor": [
        "Institutional improvement (ΔFRAZER)",
        "Economic growth (GDP)",
        "Services openness",
        "Exchange rate instability"
    ],
    "Estimated effect": [
        "+4.04% for +0.01 point",
        "+12.37% for +1 point",
        "+13.82% for +1 point",
        "Not statistically significant"
    ],
    "Interpretation": [
        "Institutional improvements are positively associated with FDI inflows.",
        "A more dynamic economy attracts more FDI.",
        "Services openness strengthens economic attractiveness.",
        "The effect is not clearly confirmed in this model."
    ]
})

st.dataframe(longrun, use_container_width=True)

st.divider()

# =========================
# Short-run dynamics
# =========================

st.header("Short-run dynamics")

short_run = pd.DataFrame({
    "Horizon": [
        "Immediate effect",
        "After 1 year",
        "After 2 years"
    ],
    "Estimated effect": [
        "Not clearly confirmed",
        "+5.38%",
        "+3.73%"
    ],
    "Interpretation": [
        "Investors do not necessarily react immediately.",
        "Positive delayed reaction to institutional improvement.",
        "The effect continues progressively over time."
    ]
})

st.dataframe(short_run, use_container_width=True)

st.success(
    "The error correction term is negative and significant, supporting a dynamic long-run relationship."
)

st.divider()

# =========================
# Post-estimation diagnostics
# =========================

st.header("Post-estimation diagnostics")

diagnostics = pd.DataFrame({
    "Test": [
        "Jarque-Bera",
        "Ljung-Box",
        "Breusch-Pagan",
        "Error Correction Term"
    ],
    "Purpose": [
        "Normality of residuals",
        "Autocorrelation",
        "Heteroskedasticity",
        "Dynamic adjustment"
    ],
    "Result": [
        "Accepted",
        "No autocorrelation detected",
        "No heteroskedasticity detected",
        "Negative and significant"
    ]
})

st.dataframe(diagnostics, use_container_width=True)

st.divider()

# =========================
# Figures
# =========================

st.header("Visual dashboards")

figure_files = [
    "dashboard_conclusion_empirique_resultats.png",
    "dashboard_tests_post_estimation.png",
    "impact_cards_long_terme_IDE.png",
    "court_terme_ecm_dashboard_IDE.png",
    "stationnarite_validation_ardl.png",
    "sources_donnees_ardl_clean.png",
]

for fig in figure_files:
    path = Path(fig)
    if path.exists():
        st.image(str(path), use_container_width=True)
    else:
        st.warning(f"Figure not found: {fig}")

st.divider()

st.header("Conclusion")

st.markdown(
    """
    The results suggest that FDI inflows in Morocco respond more clearly to
    **institutional improvements** than to the absolute level of institutional quality.
    The effect appears progressively in the short run and becomes more robust in the long run.
    """
)
