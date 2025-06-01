# Jazmin Alejandra Soriano Garcia
# 952
# 31/05/2025
# Segundo dashboard
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, callback
import pandas as pd


def kpi_tres():
    df_detalles = pd.read_csv("DataSet/data_manga.csv", sep=";")

    body = dbc.Container([
        html.H2("Información Detallada de Mangas", style={"color": "white"}),
        html.Br(),

        dbc.Row([
            dbc.Col([
                dbc.Label("Selecciona un Manga:"),
                dcc.Dropdown(
                    options=[{"label": titulo, "value": titulo} for titulo in df_detalles["Titulo"].dropna().unique()],
                    value=df_detalles["Titulo"].dropna().iloc[0],
                    id="dropdown-manga"
                )
            ], md=6),
        ]),
        html.Br(),

        dbc.Row([
            dbc.Col([
                html.H5("Detalles del Manga"),
                html.Div(id="detalles-manga", style={"color": "white"})
            ])
        ]),
        html.Br(),

        dbc.Row([
            dbc.Col([
                dcc.Graph(id="grafica-lectores")
            ])
        ])
    ])
    return body

@callback(
    Output("detalles-manga", "children"),
    Output("grafica-lectores", "figure"),
    Input("dropdown-manga", "value")
)
def actualizar_manga_info(titulo_seleccionado):
    df = pd.read_csv("DataSet/data_manga.csv", sep=";")

    manga = df[df["Titulo"] == titulo_seleccionado].iloc[0]

    detalles = html.Ul([
        html.Li(f"Volúmenes: {manga['Volumenes']}"),
        html.Li(f"Capítulos: {manga['Capitulos']}"),
        html.Li(f"Estado: {manga['Status']}"),
        html.Li(f"Año de Publicación: {manga['Año']}"),
        html.Li(f"Editorial: {manga['Editorial']}"),
        html.Li(f"Autor(es): {manga['Autor']}"),
        html.Li(f"Lectores: {manga['Lectores']}"),
        html.Li(f"Géneros: {manga['Generos']}"),
        html.Li(f"Temas: {manga['Temas']}"),
        html.Li(f"Demografía: {manga['Demografia']}")
    ])

    df["Lectores"] = df["Lectores"].str.replace(",", "", regex=False)
    df["Lectores"] = pd.to_numeric(df["Lectores"], errors="coerce")

    fig = px.bar(
        df.sort_values("Lectores", ascending=False).dropna(subset=["Lectores"]),
        x="Titulo", y="Lectores",
        title="Cantidad de Lectores por Manga",
        labels={"Lectores": "Número de Lectores"},
        color="Titulo"
    )
    fig.update_layout(showlegend=False)

    return detalles, fig
