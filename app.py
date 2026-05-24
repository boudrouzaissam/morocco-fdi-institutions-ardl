import streamlit as st
import pandas as pd
from pathlib import Path

# =====================================================
# Page configuration
# =====================================================

st.set_page_config(
    page_title="Morocco FDI & Institutions",
    page_icon="📊",
    layout="wide"
)

# =====================================================
# Header
# =====================================================

st.title("Morocco FDI, Institutions and Economic Attractiveness")
st.subheader("ARDL/ECM analysis of institutional improvement and FDI inflows")

st.markdown(
    """
    This dashboard presents the main empirical findings of an ARDL/ECM analysis
    on the relationship between institutional improvement and foreign direct investment inflows in Morocco.
    """
)

st.divider()

# =====================================================
# Key empirical findings
# =====================================================

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

# =====================================================
# Research question and hypotheses
# =====================================================

st.header("Research question and hypotheses")

st.markdown(
    """
    **Research question**

    To what extent does institutional improvement influence the attractiveness of Morocco for foreign direct investment?

    **Hypotheses**

    - **H0:** Institutional improvement has no significant effect on FDI inflows in Morocco.
    - **H1:** Institutional improvement has a positive and significant effect on FDI inflows in Morocco.
    """
)

st.divider()

# =====================================================
# Empirical model
# =====================================================

st.header("Empirical model")

st.latex(
    r"LIDE_t = f(\Delta FRAZER_t,\ CHANGE\_INSTAB_t,\ GDP_t,\ OPEN\_SERVICES_t)"
)

st.markdown(
    """
    **Selected specification:** ARDL(2,2,2,3,3)

    **Variables**

    - `LIDE`: logarithm of FDI inflows  
    - `ΔFRAZER`: annual change in the Fraser Economic Freedom Index  
    - `CHANGE_INSTAB`: exchange rate instability  
    - `GDP`: economic growth  
    - `OPEN_SERVICES`: services openness  

    The model is estimated using annual Moroccan data for the period **1996–2024**.
    """
)

st.divider()

# =====================================================
# Data sources
# =====================================================

st.header("Data sources")

sources = pd.DataFrame({
    "Source": [
        "World Bank – World Development Indicators",
        "Fraser Institute – Economic Freedom of the World Index",
        "Author’s calculations"
    ],
    "Variables / Use": [
        "FDI inflows, GDP, services openness",
        "FRAZER index and annual change in FRAZER",
        "Log transformation of FDI, exchange-rate instability, final ARDL dataset"
    ]
})

st.dataframe(sources, use_container_width=True)

# Show source dashboard image if available
source_fig = Path("sources_donnees_ardl_clean.png")
if source_fig.exists():
    st.image(str(source_fig), use_container_width=True)

st.divider()

# =====================================================
# Stationarity tests
# =====================================================

st.header("Stationarity tests")

st.markdown(
    """
    Before estimating the ARDL model, stationarity tests were conducted to verify
    the integration order of the variables. The results show that the variables are
    integrated of order I(0) or I(1), which supports the use of the ARDL approach.
    """
)

stationarity = pd.DataFrame({
    "Variable": [
        "LIDE",
        "ΔFRAZER",
        "CHANGE_INSTAB",
        "GDP",
        "OPEN_SERVICES"
    ],
    "Interpretation": [
        "Stationary after first difference",
        "Stationary in level",
        "Stationary in level",
        "Compatible with I(0) / I(1)",
        "Stationary after first difference"
    ],
    "Order of integration": [
        "I(1)",
        "I(0)",
        "I(0)",
        "I(0) / I(1)",
        "I(1)"
    ],
    "Decision": [
        "Accepted for ARDL",
        "Accepted for ARDL",
        "Accepted for ARDL",
        "Accepted for ARDL",
        "Accepted for ARDL"
    ]
})

st.dataframe(stationarity, use_container_width=True)

st.success(
    "Conclusion: none of the variables is integrated of order I(2), which justifies the use of the ARDL model."
)

st.divider()

# =====================================================
# Long-run results
# =====================================================

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

# Long-run visuals
fig_longrun_1 = Path("impact_cards_long_terme_IDE.png")
fig_longrun_2 = Path("dashboard_conclusion_empirique_resultats.png")

if fig_longrun_1.exists():
    st.image(str(fig_longrun_1), use_container_width=True)

if fig_longrun_2.exists():
    st.image(str(fig_longrun_2), use_container_width=True)

st.divider()

# =====================================================
# Short-run dynamics
# =====================================================

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

fig_short_run = Path("court_terme_ecm_dashboard_IDE.png")
if fig_short_run.exists():
    st.image(str(fig_short_run), use_container_width=True)

st.divider()

# =====================================================
# Post-estimation diagnostics
# =====================================================

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
    ],
    "Interpretation": [
        "Residuals are normally distributed.",
        "No problematic serial correlation is detected.",
        "The variance of residuals is stable.",
        "The long-run relationship is dynamically confirmed."
    ]
})

st.dataframe(diagnostics, use_container_width=True)

fig_diag = Path("dashboard_tests_post_estimation.png")
if fig_diag.exists():
    st.image(str(fig_diag), use_container_width=True)

st.divider()

# =====================================================
# Empirical conclusion
# =====================================================

st.header("Empirical conclusion")

st.markdown(
    """
    The empirical results suggest that FDI inflows in Morocco respond more clearly
    to **institutional improvements** than to the absolute level of institutional quality.

    The effect appears progressively in the short run and becomes more robust in the long run.
    GDP and services openness also appear as important long-run determinants of FDI attractiveness.
    """
)

dashboard_conclusion = Path("dashboard_conclusion_empirique.png")
if dashboard_conclusion.exists():
    st.image(str(dashboard_conclusion), use_container_width=True)

st.divider()

# =====================================================
# Policy-oriented recommendations
# =====================================================

st.header("Policy-oriented recommendations")

recommendations = pd.DataFrame({
    "Recommendation": [
        "Develop a national digital economic diplomacy strategy",
        "Strengthen Morocco’s international positioning",
        "Encourage high-value-added investments",
        "Implement differentiated territorial governance",
        "Accelerate digital government transformation",
        "Modernize administrative procedures"
    ],
    "Purpose": [
        "Increase Morocco’s attractiveness for foreign investors.",
        "Promote Morocco as a digital, innovative and strategic economy.",
        "Target technology, digital and energy-transition sectors.",
        "Strengthen regional attractiveness and strategic economic hubs.",
        "Improve Morocco’s international competitiveness.",
        "Reduce transaction costs for national and international investors."
    ]
})

st.dataframe(recommendations, use_container_width=True)

fig_reco = Path("dashboard_recommandations_action_publique.png")
if fig_reco.exists():
    st.image(str(fig_reco), use_container_width=True)

st.divider()

# =====================================================
# Files and reproducibility
# =====================================================

st.header("Project files")

st.markdown(
    """
    The full notebook, data files, estimation outputs, diagnostic results and figures
    are available in the GitHub repository associated with this dashboard.
    """
)

available_files = [
    "ARDL_CONFERENCE_FINAL.ipynb",
    "ardl_data_dfrazer.csv",
    "ardl_results_dfrazer.csv",
    "ardl_longrun_dfrazer.csv",
    "ecm_results_dfrazer.csv",
    "diag_ardl_dfrazer.csv",
    "diag_ecm_dfrazer.csv",
    "model_summary_dfrazer.csv",
    "generate_figures.py"
]

files_table = pd.DataFrame({
    "File": available_files,
    "Status": ["Available" if Path(f).exists() else "Not found" for f in available_files]
})

st.dataframe(files_table, use_container_width=True)
