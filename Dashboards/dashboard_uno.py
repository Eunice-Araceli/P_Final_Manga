# Jazmin Alejandra Soriano Garcia
# 952
# 31/05/2025
# Primer Dashboard
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, callback
import pandas as pd

df = pd.read_csv("C:/Users/Lenovo/Downloads/manga.csv", sep=";")

def kpi():
    body = dbc.Container([

        html.H2("Comparación de ranking vs calificación", style={"color": "white"}),
        dbc.Card([
            dbc.CardBody([
                dbc.Label("Filtrar por Ranking:"),
                dcc.Dropdown(
                    options=[{"label": f"Top {i}", "value": i} for i in range(1, 21)],
                    value=10,
                    id="ddRanking"
                ),
            ])
        ], className="mb-4"),

        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H6("Manga con mejor calificación", className="card-title"),
                        html.H4(id="kpi-best-rating", className="card-text")
                    ])
                ], color="success", inverse=True)
            ]),

            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H6("Promedio de calificación", className="card-title"),
                        html.H4(id="kpi-average-rating", className="card-text")
                    ])
                ], color="danger", inverse=True)
            ]),

            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H6("Manga con mejor Ranking", className="card-title"),
                        html.H4(id="kpi-best-ranking", className="card-text")
                    ])
                ], color="info", inverse=True)
            ])
        ]),
        html.Br(),
        dbc.Row([
            dbc.Col(dcc.Graph(id="GraficaDispercion"), md=6),
            dbc.Col(dcc.Graph(id="GraficaBarras"), md=6)
        ])

    ])
    return body

@callback(
    Output("kpi-best-rating", "children"),
    Output("kpi-average-rating", "children"),
    Output("kpi-best-ranking", "children"),
    Output("GraficaDispercion", "figure"),
    Output("GraficaBarras", "figure"),
    Input("ddRanking", "value")
)
def actualizar(ranking_max):
    df_ranking = df[df["Rank"] <= ranking_max]

    best_rating = df_ranking.loc[df_ranking["Calificacion"].idxmax()]
    best_rating_text = f"{best_rating['Titulo']} ({best_rating['Calificacion']})"

    average_rating = f"{df_ranking['Calificacion'].mean():.2f}"

    best_ranking = df_ranking.loc[df_ranking["Rank"].idxmin()]
    best_ranking_text = f"{best_ranking['Titulo']} (Rank: {best_ranking['Rank']})"

    fig_dispersion = px.scatter(df_ranking, x="Rank", y="Calificacion",
                                size="Calificacion", color="Titulo",
                                hover_name="Titulo",  # Mostrar solo el título en hover
                                title="Ranking vs Calificación de Mangas",
                                labels={"Rank": "Ranking", "Calificacion": "Calificación"})

    fig_dispersion.update_layout(showlegend=False)

    fig_barras = px.bar(df_ranking, x="Titulo", y="Calificacion",
                        color="Titulo", title="Calificación de Mangas",
                        labels={"Titulo": "Manga", "Calificacion": "Calificación"})

    fig_barras.update_traces(
        hoverinfo="x+y+text",
        hovertext=df_ranking["Titulo"]
    )

    fig_barras.update_layout(showlegend=False)

    return best_rating_text, average_rating, best_ranking_text, fig_dispersion, fig_barras
