from dash import dcc, html, dash_table, Input, Output, callback
import dash_bootstrap_components as dbc
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

# CONEXION DE SQL
import Constantes_BD as c

# CONEXION AL SQL
cadena_con = f"mysql+mysqlconnector://{c.USER}:{c.PASSWORD}@{c.HOST}/{c.DATABASE}"
engine = create_engine(cadena_con)

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

# NUEVA CONSULTA: Genero vs Status
df_genero_status = pd.read_sql("""
    SELECT g.NOMBRE AS GENERO, m.STATUS, COUNT(*) AS TOTAL
    FROM mangas m
    JOIN manga_genero mg ON m.ID_MANGA = mg.ID_MANGA
    JOIN generos g ON mg.ID_GENERO = g.ID_GENERO
    WHERE m.STATUS IS NOT NULL
    GROUP BY g.NOMBRE, m.STATUS
""", con=engine)

# METRICAS NUEVAS
mangas_publicados = df_manga[df_manga['ESTRENO'].notnull()].shape[0]
mangas_finalizados = df_manga[df_manga['STATUS'].str.contains("Finished", na=False)].shape[0]
mangas_en_emision = df_manga[df_manga['STATUS'].str.contains("Publishing", na=False)].shape[0]

# CÍRCULOS INFORMATIVOS
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

# LAYOUT
def get_dashboard():
    # Gráfico de barras (género)
    fig_genero = px.bar(
        df_genero.sort_values("TOTAL", ascending=True).tail(15),
        x="TOTAL",
        y="GENERO",
        orientation="h",
        title="Frecuencia por género",
        template="plotly_dark",
        color="TOTAL",
        color_continuous_scale="Blues"
    )

    # Gráfico de pastel (temas)
    pastel_colors = px.colors.sequential.Blues + px.colors.sequential.Purples
    fig_tema = px.pie(
        df_tema.sort_values("TOTAL", ascending=False).head(10),
        names="TEMA",
        values="TOTAL",
        title="Distribución de temas",
        hole=0.3,
        template="plotly_white",
        color_discrete_sequence=px.colors.sequential.Blues
    )

    # Gráfico de dispersión (volúmenes vs lectores)
    fig_dispersion = px.scatter(
        df_manga,
        x="VOLUMENES",
        y="LECTORES",
        title="Impacto de los volúmenes sobre la popularidad",
        labels={"VOLUMENES": "Volúmenes", "LECTORES": "Lectores"},
        template="plotly_white"
    )
    fig_dispersion.update_traces(marker=dict(color="#1f77b4"))

    # Gráfico por género y estado
    fig_genero_status = px.bar(
        df_genero_status,
        x="GENERO",
        y="TOTAL",
        color="STATUS",
        barmode="stack",
        title="Cantidad de mangas por género y publicación",
        template="plotly_white",
        color_discrete_sequence=px.colors.cmocean.dense
    )
    fig_genero_status.update_layout(xaxis_tickangle=-45)

    return dbc.Container([
        html.H2("📊 Estadísticas del contenido manga", className="text-center text-white fw-bold mb-4"),

        dbc.Row([
            dbc.Col(circle_card("📘 Publicados", f"{mangas_publicados}", "#007bff"), md=4),
            dbc.Col(circle_card("✅ Finalizados", f"{mangas_finalizados}", "#17a2b8"), md=4),
            dbc.Col(circle_card("📅 En emisión", f"{mangas_en_emision}", "#6f42c1"), md=4),
        ], className="mb-5"),

        dbc.Row([
            dbc.Col([
                html.H5("🎭 Top géneros más frecuentes", className="fw-bold mb-2 text-white"),
                dcc.Graph(figure=fig_genero)
            ], md=6),

            dbc.Col([
                html.H5("🎨 Temas más comunes en manga", className="fw-bold mb-2 text-white"),
                dcc.Graph(figure=fig_tema)
            ], md=6)
        ], className="mb-4"),

        dbc.Row([
            dbc.Col([
                html.H5("📈 Relación entre volúmenes y lectores", className="fw-bold mb-2 text-white"),
                dcc.Graph(figure=fig_dispersion)
            ])
        ], className="mb-4"),

        dbc.Row([
            dbc.Col([
                html.H5("📚 Cantidad de mangas por género y publicación", className="fw-bold mb-2 text-white"),
                dcc.Graph(figure=fig_genero_status)
            ])
        ])

    ], fluid=True, className="p-4 bg-info")