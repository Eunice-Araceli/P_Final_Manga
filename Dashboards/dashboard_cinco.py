from sqlalchemy import create_engine
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, callback
from BD import Constantes_BD as c

# CONEXIÓN A LA BD
cadena_con = f"mysql+mysqlconnector://{c.USER}:{c.PASSWORD}@{c.HOST}/{c.DATABASE}"
engine = create_engine(cadena_con)

#CONSULTAS DE LA BASE DE DATOS SQL
df_rangos = pd.read_sql("""
    SELECT 
        d.NOMBRE AS DEMOGRAFIA,
        m.EDITORIAL,
        CASE 
            WHEN r.RANK BETWEEN 1 AND 5 THEN '1-5'
            WHEN r.RANK BETWEEN 6 AND 10 THEN '6-10'
            ELSE '11+'
        END AS RANGO,
        COUNT(*) AS TOTAL
    FROM ranks r
    JOIN mangas m ON r.ID_MANGA = m.ID_MANGA
    JOIN manga_demografia md ON md.ID_MANGA = m.ID_MANGA
    JOIN demografias d ON md.ID_DEMOGRAFIA = d.ID_DEMOGRAFIA
    WHERE m.EDITORIAL IS NOT NULL AND r.RANK IS NOT NULL
    GROUP BY d.NOMBRE, m.EDITORIAL, RANGO
    ORDER BY d.NOMBRE, RANGO, TOTAL DESC;
""", con=engine)

demografias = df_rangos["DEMOGRAFIA"].unique()

#GRAFICOS
def layout_editorial_por_rango_multiples():
    return dbc.Container([
        html.H1(" 📊 Editoriales por rango de manga", className="text-center text-white bg-primary p-3 mb-4 rounded"),
        html.P(" 👨🏻‍💻 Descubre que editoriales son mejor en rankings de mangas separadas por rango",
               className="lead text-center mb-4 text-white"),

        dbc.Row([
            dbc.Col([
                html.Label("📍 Selecciona una demografia:", className="fw-bold text-white"),
                dcc.Dropdown(
                    options=[{"label": d, "value": d} for d in demografias],
                    id="filtro_demografia_rango_multiple",
                    value="SEINEN" if "SEINEN" in demografias else demografias[0],
                    clearable=False
                )
            ], width=6)
        ], justify="center", className="mb-4"),

        dbc.Row([
            dbc.Col(dbc.Card([
                dbc.CardHeader("📍 Top editoriales  Rango 1–5", className="bg-primary text-white"),
                dbc.CardBody(dcc.Graph(id="grafica_rango_1_5"))
            ], className="mb-4 shadow"), width=12),

            dbc.Col(dbc.Card([
                dbc.CardHeader("📍 Top editoriales  Rango 6–10", className="bg-info text-white"),
                dbc.CardBody(dcc.Graph(id="grafica_rango_6_10"))
            ], className="mb-4 shadow"), width=12),

            dbc.Col(dbc.Card([
                dbc.CardHeader("📍 Top editoriales  Rango 11+", className="bg-secondary text-white"),
                dbc.CardBody(dcc.Graph(id="grafica_rango_11_mas"))
            ], className="mb-4 shadow"), width=12)
        ]),


    ], fluid=True, style={"backgroundColor": "#001f3f", "padding": "40px"})


@callback(
    Output("grafica_rango_1_5", "figure"),
    Output("grafica_rango_6_10", "figure"),
    Output("grafica_rango_11_mas", "figure"),
    Input("filtro_demografia_rango_multiple", "value")
)
def actualizar_graficas_por_rango(demografia):
    df_demo = df_rangos[df_rangos["DEMOGRAFIA"] == demografia]

    df_1_5 = df_demo[df_demo["RANGO"] == "1-5"]
    df_6_10 = df_demo[df_demo["RANGO"] == "6-10"]
    df_11_plus = df_demo[df_demo["RANGO"] == "11+"]

    fig1 = px.bar(df_1_5, x="EDITORIAL", y="TOTAL", title="Rango 1–5", template="plotly_white", color="TOTAL",
                  color_continuous_scale="Blues")
    fig1.update_layout(xaxis_tickangle=-45)

    fig2 = px.bar(df_6_10, x="EDITORIAL", y="TOTAL", title="Rango 6–10", template="plotly_white", color="TOTAL",
                  color_continuous_scale="Blues")
    fig2.update_layout(xaxis_tickangle=-45)

    fig3 = px.bar(df_11_plus, x="EDITORIAL", y="TOTAL", title="Rango 11 o más", template="plotly_white", color="TOTAL",
                  color_continuous_scale="Blues")
    fig3.update_layout(xaxis_tickangle=-45)

    return fig1, fig2, fig3
