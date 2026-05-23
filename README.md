# Morocco FDI, Institutions and Economic Attractiveness — ARDL/ECM Analysis

## Project overview

This project analyzes the relationship between institutional improvement and foreign direct investment inflows in Morocco using an ARDL/ECM framework.

The analysis focuses on whether improvements in institutional quality, measured by the annual change in the Fraser Economic Freedom Index, are associated with higher FDI inflows in Morocco.

## Research question

To what extent does institutional improvement influence the attractiveness of Morocco for foreign direct investment?

## Hypotheses

- **H0:** Institutional improvement has no significant effect on FDI inflows in Morocco.
- **H1:** Institutional improvement has a positive and significant effect on FDI inflows in Morocco.

## Data and variables

The analysis uses annual data for Morocco covering the period **1996–2024**.

| Variable | Description |
|---|---|
| `LIDE` | Logarithm of foreign direct investment inflows |
| `D_FRAZER` | Annual change in the Fraser Economic Freedom Index |
| `CHANGE_INSTAB` | Exchange rate instability |
| `GDP` | Economic growth |
| `OPEN_SERVICES` | Services openness |

## Data sources

The dataset is constructed using data from:

- World Bank — World Development Indicators
- Fraser Institute — Economic Freedom of the World Index
- Author’s calculations and transformations

## Methodology

The empirical analysis is based on an Autoregressive Distributed Lag model with an Error Correction Mechanism.

Selected specification:

`ARDL(2,2,2,3,3)`

Empirical model:

`LIDE = f(D_FRAZER, CHANGE_INSTAB, GDP, OPEN_SERVICES)`

The ARDL approach is used because it allows the analysis of both short-run and long-run relationships and is suitable when variables are integrated of order I(0) and I(1), provided that none is I(2).

## Main empirical findings

The main results suggest that:

- Institutional improvement has a positive and significant long-run effect on FDI inflows.
- A 0.01-point increase in `D_FRAZER` is associated with an estimated **4.04% increase** in FDI in the long run.
- GDP has a positive long-run effect of approximately **12.37%**.
- Services openness has a positive long-run effect of approximately **13.82%**.
- Exchange rate instability is not statistically significant in the long run.
- Short-run institutional effects appear progressively after one and two years.
- The error correction term is negative and significant, supporting the existence of a dynamic adjustment mechanism.
- Post-estimation diagnostics do not reveal major statistical problems.

## Repository structure

morocco-fdi-institutions-ardl/
- data/ : Final dataset
- results/ : Estimation outputs and diagnostic tests
- figures/ : Graphs and dashboards
- notebooks/ : Jupyter notebooks
- scripts/ : Python scripts
- README.md
- requirements.txt

## How to run the project

1. Clone the repository.
2. Install the required Python packages:

`pip install -r requirements.txt`

3. Open the notebook:

`notebooks/ARDL_CONFERENCE_FINAL.ipynb`

4. Run the cells to reproduce the analysis and figures.

## Limitations

This project estimates dynamic associations between institutional improvement and FDI inflows. The results should not be interpreted as definitive causal effects.

Main limitations include:

- Limited sample size due to annual data availability.
- Institutional quality is proxied by the Fraser Economic Freedom Index.
- Future work could test alternative institutional indicators, such as the Worldwide Governance Indicators.
- Further robustness checks could be added using alternative specifications or additional control variables.

## Author

**Aissam Boudrouz**  
Economist / Data Analyst  
PhD researcher in macroeconomics  
MBA student, Université du Québec en Outaouais