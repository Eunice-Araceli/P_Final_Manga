from dash import dcc, html, dash_table, Input, Output, callback
import dash_bootstrap_components as dbc
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px
from BD import Constantes_BD as c

# CONEXION AL SQL
cadena_con = f"mysql+mysqlconnector://{c.USER}:{c.PASSWORD}@{c.HOST}/{c.DATABASE}"
engine = create_engine(cadena_con)

# CONSULTA DE DATOS EN SQL BASE
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
df_genero_status = pd.read_sql("""
    SELECT g.NOMBRE AS GENERO, m.STATUS, COUNT(*) AS TOTAL
    FROM mangas m
    JOIN manga_genero mg ON m.ID_MANGA = mg.ID_MANGA
    JOIN generos g ON mg.ID_GENERO = g.ID_GENERO
    WHERE m.STATUS IS NOT NULL
    GROUP BY g.NOMBRE, m.STATUS
""", con=engine)


#DATAS FRAME
mangas_publicados = df_manga[df_manga['ESTRENO'].notnull()].shape[0]
mangas_finalizados = df_manga[df_manga['STATUS'].str.contains("Finished", na=False)].shape[0]
mangas_en_emision = df_manga[df_manga['STATUS'].str.contains("Publishing", na=False)].shape[0]

#CIRCULOS INFORMATIVOS
def circle_card(title, value, color):
    return html.Div([
        html.H6(title, className="fw-bold mb-2"),
        html.H3(value, className="fw-bold")
    ], style={
        "background": color,
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

#GRAFICOS
def get_dashboard():
    #GRAFICO DE DISPERSION
    fig_dispersion = px.scatter(
        df_manga,
        x="VOLUMENES",
        y="LECTORES",
        title="⭐ Impacto de los volumenes sobre la popularidad ⭐",
        labels={"VOLUMENES": "Volúmenes", "LECTORES": "Lectores"},
        template="plotly_white"
    )
    fig_dispersion.update_traces(marker=dict(color="#1f77b4"))

    #GRAFICOS POR GENERO U ESTADO EN BARRAS
    fig_genero_status = px.bar(
        df_genero_status,
        x="GENERO",
        y="TOTAL",
        color="STATUS",
        barmode="stack",
        title="👨🏻‍💻 Cantidad de mangas por genero y publicacion 👩🏻‍💻",
        template="plotly_dark",
        color_discrete_sequence=px.colors.cmocean.dense
    )
    fig_genero_status.update_layout(xaxis_tickangle=-45)

    return dbc.Container([
        html.H2("📊 Estadisticas del contenido manga 🌎", className="text-center text-white fw-bold mb-4"),

        dbc.Row([
            dbc.Col(circle_card("💻 Publicados", f"{mangas_publicados}", "#007bff"), md=4),
            dbc.Col(circle_card("✅ Finalizados", f"{mangas_finalizados}", "#17a2b8"), md=4),
            dbc.Col(circle_card("📅 En emision", f"{mangas_en_emision}", "#6f42c1"), md=4),
        ], className="mb-5"),

        dbc.Row([
            dbc.Col([
                html.H5("📚 Cantidad de mangas por genero y publicacion 💻", className="fw-bold mb-2 text-white"),
                dcc.Graph(figure=fig_genero_status)
            ])
        ], className="mb-4"),

        dbc.Row([
            dbc.Col([
                html.H5("📈 Relacion entre volumenes y lectores 💻", className="fw-bold mb-2 text-white"),
                dcc.Graph(figure=fig_dispersion)
            ])
        ])

    ], fluid=True, className="p-4 bg-info")