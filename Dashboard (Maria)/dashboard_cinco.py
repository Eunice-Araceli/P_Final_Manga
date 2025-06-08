from sqlalchemy import create_engine
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, callback

# CONEXION
engine = create_engine("mysql+mysqlconnector://root:123456@localhost/manga")

# CONSULTA DE LOS DATOS
df_editorial_demo = pd.read_sql("""
    SELECT d.NOMBRE AS DEMOGRAFIA, m.EDITORIAL, COUNT(*) AS TOTAL
    FROM manga_demografia md
    JOIN demografias d ON md.ID_DEMOGRAFIA = d.ID_DEMOGRAFIA
    JOIN mangas m ON md.ID_MANGA = m.ID_MANGA
    WHERE m.EDITORIAL IS NOT NULL
    GROUP BY d.NOMBRE, m.EDITORIAL
""", con=engine)

# LISTA DE DEMOGRAFIAS
demografias = df_editorial_demo["DEMOGRAFIA"].unique()

# CONTENIDO
def layout_editorial_por_demografia():
    return dbc.Container([
        html.Div([
            html.H1("analisis de editoriales por demografia", className="text-center text-white bg-primary p-3 mb-4 rounded"),
            html.P("explora cuantos mangas han sido publicados por editorial dentro de cada demografia.",
                   className="lead text-center mb-4"),
        ]),

        dbc.Row([
            dbc.Col([
                html.Label("selecciona una demografia:", className="fw-bold mb-2"),
                dcc.Dropdown(
                    options=[{"label": dem, "value": dem} for dem in demografias],
                    id="filtro_demografia",
                    value=demografias[0],
                    clearable=False,
                    className="mb-4"
                )
            ], width=6)
        ], justify="center"),

        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader("resultados"),
                    dbc.CardBody([
                        dcc.Graph(id="grafica_editorial_demo")
                    ])
                ], className="shadow-sm")
            ], width=12)
        ]),

        html.Footer([
            html.Hr(),
            html.P("2025 dashboard manga • todos los derechos reservados", className="text-center text-muted")
        ])
    ], fluid=True, className="bg-light p-4")


@callback(
    Output("grafica_editorial_demo", "figure"),
    Input("filtro_demografia", "value")
)
def actualizar_editorial_por_demografia(demo):
    df_filtrado = df_editorial_demo[df_editorial_demo["DEMOGRAFIA"] == demo]
    fig = px.bar(
        df_filtrado,
        x="EDITORIAL",
        y="TOTAL",
        title=f"mangas por editorial en la demografia: {demo}",
        template="plotly_white",
        labels={"EDITORIAL": "Editorial", "TOTAL": "Cantidad de mangas"},
        text_auto=True
    )
    fig.update_layout(xaxis_tickangle=-45)
    return fig
