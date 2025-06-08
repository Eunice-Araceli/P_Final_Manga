from dash import dcc, html
import dash_bootstrap_components as dbc
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

#CONEXION DE SQL
import Constantes_BD as c

# CONEXION AL SQL
cadena_con = f"mysql+mysqlconnector://{c.USER}:{c.PASSWORD}@{c.HOST}/{c.DATABASE}"
engine = create_engine(cadena_con)


#EVOLUCION DE MANGAS POR AÑO
df_mangas_anio = pd.read_sql("""
    SELECT YEAR(ESTRENO) AS ANIO, COUNT(*) AS TOTAL
    FROM mangas
    WHERE ESTRENO IS NOT NULL
    GROUP BY ANIO
    ORDER BY ANIO;
""", con=engine)

#GRAFICO DE BURBUJAS
df_burbujas = pd.read_sql("""
    SELECT m.EDITORIAL, COUNT(*) AS TOTAL_MANGAS,
           ROUND(AVG(r.CALIFICACION), 2) AS PROMEDIO_CALIFICACION,
           SUM(m.LECTORES) AS TOTAL_LECTORES
    FROM mangas m
    JOIN ranks r ON m.ID_MANGA = r.ID_MANGA
    WHERE m.EDITORIAL IS NOT NULL AND m.LECTORES IS NOT NULL
    GROUP BY m.EDITORIAL
    HAVING TOTAL_LECTORES IS NOT NULL
    ORDER BY TOTAL_MANGAS DESC
    LIMIT 15;
""", con=engine)

# Eliminar None (por seguridad extra)
df_burbujas.dropna(inplace=True)

# Datos: género vs estado
df_genero_estado = pd.read_sql("""
    SELECT g.NOMBRE AS GENERO, m.STATUS, COUNT(*) AS TOTAL
    FROM mangas m
    JOIN manga_genero mg ON m.ID_MANGA = mg.ID_MANGA
    JOIN generos g ON mg.ID_GENERO = g.ID_GENERO
    WHERE m.STATUS IS NOT NULL
    GROUP BY g.NOMBRE, m.STATUS
    ORDER BY TOTAL DESC
    LIMIT 100;
""", con=engine)

# Gráfico de línea: cambio de fondo a blanco, línea azul
fig_linea = px.line(
    df_mangas_anio,
    x="ANIO",
    y="TOTAL",
    markers=True,
    title="Mangas publicados por año",
    labels={"ANIO": "Año", "TOTAL": "Cantidad"},
    template="plotly_white"
)
fig_linea.update_traces(line=dict(color='blue'))

# Gráfico de burbujas
fig_burbujas = px.scatter(
    df_burbujas,
    x="TOTAL_MANGAS",
    y="TOTAL_LECTORES",
    size="PROMEDIO_CALIFICACION",
    color="EDITORIAL",
    title="Relación de mangas con lectores",
    labels={"TOTAL_MANGAS": "Cantidad de Mangas", "TOTAL_LECTORES": "Lectores Totales"},
    template="plotly_white"
)

# Gráfico de barras apiladas (tamaño grande)
fig_barras_apiladas = px.bar(
    df_genero_estado,
    x="GENERO",
    y="TOTAL",
    color="STATUS",
    title="Cantidad de mangas por género y publicación",
    template="plotly_white"
)
fig_barras_apiladas.update_layout(xaxis_tickangle=-45)

# Layout final
def layout_dashboard_final():
    return dbc.Container([
        html.H2("Exploración Completa del Universo Manga", className="text-center text-primary fw-bold mb-4"),

        dbc.Row([
            dbc.Col(dcc.Graph(figure=fig_linea), md=12)
        ], className="mb-4"),

        dbc.Row([
            dbc.Col(dcc.Graph(figure=fig_burbujas), md=8, lg=6, className="mx-auto")  # 👈 CENTRADA
        ], className="mb-4"),

        dbc.Row([
            dbc.Col(dcc.Graph(figure=fig_barras_apiladas), md=12)
        ])
    ], fluid=True, className="p-4 bg-light")