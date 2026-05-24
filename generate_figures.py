"""
Generate presentation figures for the project:
Morocco FDI, Institutions and Economic Attractiveness — ARDL/ECM Analysis
"""

from pathlib import Path
import matplotlib.pyplot as plt


# =====================================================
# Project paths
# =====================================================

PROJECT_DIR = Path(__file__).resolve().parents[1]
FIGURES_DIR = PROJECT_DIR / "figures"
FIGURES_DIR.mkdir(exist_ok=True)


# =====================================================
# Figure 1: Long-run effects dashboard
# =====================================================

def long_run_effects_dashboard():
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.axis("off")

    fig.text(
        0.06, 0.93,
        "Dashboard – Conclusion empirique",
        fontsize=24,
        fontweight="bold"
    )

    fig.text(
        0.06, 0.89,
        "Synthèse des principaux résultats empiriques",
        fontsize=13
    )

    kpis = [
        {
            "title": "Amélioration institutionnelle",
            "value": "+4,04 %",
            "subtitle": "Effet long terme de ΔFRAZER",
            "detail": "Pour +0,01 point de FRAZER",
            "color": "#5B4B8A"
        },
        {
            "title": "Croissance économique",
            "value": "+12,37 %",
            "subtitle": "Effet long terme du GDP",
            "detail": "Pour +1 point de croissance",
            "color": "#2E7D32"
        },
        {
            "title": "Ouverture des services",
            "value": "+13,82 %",
            "subtitle": "Effet long terme",
            "detail": "Pour +1 point d’ouverture",
            "color": "#0277BD"
        }
    ]

    x_positions = [0.06, 0.37, 0.68]

    for x, item in zip(x_positions, kpis):
        rect = plt.Rectangle(
            (x, 0.58), 0.26, 0.25,
            transform=fig.transFigure,
            facecolor="#F4F6F8",
            edgecolor=item["color"],
            linewidth=2
        )
        fig.patches.append(rect)

        band = plt.Rectangle(
            (x, 0.80), 0.26, 0.03,
            transform=fig.transFigure,
            facecolor=item["color"],
            edgecolor=item["color"]
        )
        fig.patches.append(band)

        fig.text(x + 0.13, 0.745, item["title"], ha="center",
                 fontsize=13, fontweight="bold", color=item["color"])
        fig.text(x + 0.13, 0.675, item["value"], ha="center",
                 fontsize=28, fontweight="bold")
        fig.text(x + 0.13, 0.625, item["subtitle"], ha="center", fontsize=11)
        fig.text(x + 0.13, 0.595, item["detail"], ha="center", fontsize=10)

    fig.text(0.06, 0.50, "Résultats de court terme", fontsize=18, fontweight="bold")

    short_terms = [
        ("Effet immédiat", "Non clairement confirmé", "#9E9E9E"),
        ("Après 1 an", "+5,38 %", "#2E7D32"),
        ("Après 2 ans", "+3,73 %", "#4CAF50")
    ]

    for x, (title, value, color) in zip(x_positions, short_terms):
        rect = plt.Rectangle(
            (x, 0.34), 0.26, 0.11,
            transform=fig.transFigure,
            facecolor="#FAFBFC",
            edgecolor=color,
            linewidth=1.8
        )
        fig.patches.append(rect)

        fig.text(x + 0.13, 0.410, title, ha="center",
                 fontsize=12, fontweight="bold", color=color)
        fig.text(x + 0.13, 0.365, value, ha="center",
                 fontsize=18, fontweight="bold")

    fig.text(0.06, 0.27, "Validation dynamique", fontsize=18, fontweight="bold")

    validation = [
        {
            "title": "Terme de correction d’erreur",
            "value": "Négatif et significatif",
            "detail": "Retour vers l’équilibre de long terme",
            "color": "#1565C0"
        },
        {
            "title": "Diagnostics",
            "value": "Satisfaisants",
            "detail": "Normalité, autocorrélation et hétéroscédasticité acceptables",
            "color": "#5B4B8A"
        }
    ]

    x_positions_3 = [0.06, 0.53]

    for x, item in zip(x_positions_3, validation):
        rect = plt.Rectangle(
            (x, 0.11), 0.39, 0.12,
            transform=fig.transFigure,
            facecolor="#F4F6F8",
            edgecolor=item["color"],
            linewidth=2
        )
        fig.patches.append(rect)

        fig.text(x + 0.02, 0.190, item["title"],
                 fontsize=12, fontweight="bold", color=item["color"])
        fig.text(x + 0.02, 0.155, item["value"],
                 fontsize=16, fontweight="bold")
        fig.text(x + 0.02, 0.125, item["detail"], fontsize=10.5)

    output_path = FIGURES_DIR / "dashboard_conclusion_empirique_resultats.png"
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"Saved: {output_path}")


# =====================================================
# Figure 2: Post-estimation tests dashboard
# =====================================================

def post_estimation_tests_dashboard():
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.axis("off")

    fig.text(
        0.06, 0.93,
        "Dashboard – Tests post-estimation",
        fontsize=24,
        fontweight="bold"
    )

    fig.text(
        0.06, 0.89,
        "Validation statistique du modèle ARDL / ECM",
        fontsize=13
    )

    tests = [
        {
            "title": "Normalité des résidus",
            "test": "Jarque-Bera",
            "value": "p-value = 0,951",
            "conclusion": "Résidus normalement distribués",
            "color": "#2E7D32"
        },
        {
            "title": "Autocorrélation",
            "test": "Ljung-Box",
            "value": "Lag 1 = 0,520 | Lag 2 = 0,633 | Lag 3 = 0,733",
            "conclusion": "Pas d’autocorrélation détectée",
            "color": "#0277BD"
        },
        {
            "title": "Hétéroscédasticité",
            "test": "Breusch-Pagan",
            "value": "LM = 0,753 | F = 0,874",
            "conclusion": "Variance des erreurs stable",
            "color": "#F39C12"
        },
        {
            "title": "Ajustement dynamique",
            "test": "ECM",
            "value": "Terme négatif et significatif",
            "conclusion": "Relation de long terme confirmée",
            "color": "#5B4B8A"
        }
    ]

    positions = [(0.06, 0.58), (0.53, 0.58), (0.06, 0.28), (0.53, 0.28)]

    for (x, y), item in zip(positions, tests):
        rect = plt.Rectangle(
            (x, y), 0.39, 0.20,
            transform=fig.transFigure,
            facecolor="#F4F6F8",
            edgecolor=item["color"],
            linewidth=2
        )
        fig.patches.append(rect)

        band = plt.Rectangle(
            (x, y + 0.16), 0.39, 0.04,
            transform=fig.transFigure,
            facecolor=item["color"],
            edgecolor=item["color"]
        )
        fig.patches.append(band)

        circle = plt.Circle(
            (x + 0.035, y + 0.12), 0.018,
            transform=fig.transFigure,
            facecolor=item["color"],
            edgecolor="none"
        )
        fig.patches.append(circle)

        fig.text(x + 0.035, y + 0.12, "✓", ha="center", va="center",
                 fontsize=12, fontweight="bold", color="white")

        fig.text(x + 0.07, y + 0.125, item["title"],
                 fontsize=15, fontweight="bold", color=item["color"])
        fig.text(x + 0.07, y + 0.085, f"Test : {item['test']}", fontsize=11)
        fig.text(x + 0.07, y + 0.055, item["value"], fontsize=11.5, fontweight="bold")
        fig.text(x + 0.07, y + 0.020, item["conclusion"], fontsize=11)

    bottom = plt.Rectangle(
        (0.06, 0.08), 0.86, 0.10,
        transform=fig.transFigure,
        facecolor="#E8F5E9",
        edgecolor="#2E7D32",
        linewidth=2
    )
    fig.patches.append(bottom)

    fig.text(
        0.49, 0.125,
        "Conclusion générale : les tests post-estimation ne révèlent pas de problème statistique majeur.",
        ha="center",
        fontsize=13,
        fontweight="bold",
        color="#1B5E20"
    )

    output_path = FIGURES_DIR / "dashboard_tests_post_estimation.png"
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"Saved: {output_path}")


# =====================================================
# Main
# =====================================================

if __name__ == "__main__":
    long_run_effects_dashboard()
    post_estimation_tests_dashboard()