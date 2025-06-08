from dash import dcc, html, dash_table, Input, Output, callback
import dash_bootstrap_components as dbc
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

# CONEXION AL SQL
engine = create_engine("mysql+mysqlconnector://root:123456@localhost/manga")

# CONSULTA DE DATOS
df_manga = pd.read_sql("SELECT * FROM mangas", con=engine)
df_genero = pd.read_sql("""
    SELECT g.NOMBRE AS GENERO, COUNT(*) AS TOTAL
    FROM manga_genero mg
    JOIN generos g ON mg.ID_GENERO = g.ID_GENERO
    GROUP BY g.NOMBRE
""", con=engine)
df_tema = pd.read_sql("""
    SELECT t.NOMBRE AS TEMA, COUNT(*) AS TOTAL
    FROM manga_tema mt
    JOIN temas t ON mt.ID_TEMA = t.ID_TEMA
    GROUP BY t.NOMBRE
""", con=engine)

# METRICAS NUEVAS
mangas_publicados = df_manga[df_manga['ESTRENO'].notnull()].shape[0]
mangas_finalizados = df_manga[df_manga['STATUS'].str.contains("Finished", na=False)].shape[0]
mangas_en_emision = df_manga[df_manga['STATUS'].str.contains("Publishing", na=False)].shape[0]

# ESTILO DE LOS CIRCULOS CON TEXTO
circle_card = lambda title, value, bg: html.Div([
    html.H6(title, className="fw-bold mb-2"),
    html.H3(value, className="fw-bold")
], style={
    "background": bg,
    "color": "white",
    "borderRadius": "50%",
    "width": "160px",
    "height": "160px",
    "display": "flex",
    "flexDirection": "column",
    "alignItems": "center",
    "justifyContent": "center",
    "textAlign": "center",
    "boxShadow": "0 0 10px rgba(0,0,0,0.4)",
    "margin": "0 auto"
})

# TABLAS PRINCIPALES
def get_dashboard():
    return dbc.Container([
        html.H2("estadisticas de contenido manga", className="text-center text-primary fw-bold mb-4"),

        # ESTILOS DE FORMA CIRCULAR
        dbc.Row([
            dbc.Col(circle_card("📘 mangas publicados", f"{mangas_publicados}", "#17a2b8"), md=4),
            dbc.Col(circle_card("✅ mangas finalizados", f"{mangas_finalizados}", "#28a745"), md=4),
            dbc.Col(circle_card("📅 en emision", f"{mangas_en_emision}", "#ffc107"), md=4),
        ], className="mb-5"),

        # TABLAS DE GENEROS Y TEMAS
        dbc.Row([
            dbc.Col([
                html.H5("top generos asociados", className="fw-bold"),
                dash_table.DataTable(
                    columns=[{"name": i, "id": i} for i in df_genero.columns],
                    data=df_genero.to_dict("records"),
                    style_table={"overflowX": "auto"},
                    style_cell={"textAlign": "center"},
                    page_size=10
                )
            ], md=6),

            dbc.Col([
                html.H5("temas recurrentes en manga", className="fw-bold"),
                dash_table.DataTable(
                    columns=[{"name": i, "id": i} for i in df_tema.columns],
                    data=df_tema.to_dict("records"),
                    style_table={"overflowX": "auto"},
                    style_cell={"textAlign": "center"},
                    page_size=10
                )
            ], md=6)
        ], className="mb-4"),

        # GRAFICO DE DISPERSION
        dbc.Row([
            dbc.Col([
                html.H5("relacion entre lectores y volumenes", className="fw-bold mb-2 text-dark"),
                dcc.Graph(figure=px.scatter(
                    df_manga,
                    x="VOLUMENES",
                    y="LECTORES",
                    title="impacto de los volumenes sobre la popularidad",
                    labels={"VOLUMENES": "volumenes", "LECTORES": "lectores"},
                    template="plotly_dark"
                ))
            ], md=12)
        ])
    ], fluid=True, className="p-4 bg-light")
