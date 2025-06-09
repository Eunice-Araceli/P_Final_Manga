from dash import html, dcc, dash_table, Input, Output, callback
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
import Constantes_BD as c

# CONEXIÓN A LA BD
cadena_con = f"mysql+mysqlconnector://{c.USER}:{c.PASSWORD}@{c.HOST}/{c.DATABASE}"
engine = create_engine(cadena_con)

# CONSULTAS
try:
    df_artistas = pd.read_sql("SELECT ID_ARTISTA, NOMBRE FROM artistas", con=engine)
    df_generos = pd.read_sql("""
        SELECT a.ID_ARTISTA, a.NOMBRE AS ARTISTA, g.NOMBRE AS GENERO
        FROM artistas a
        JOIN manga_artista ma ON a.ID_ARTISTA = ma.ID_ARTISTA
        JOIN mangas m ON ma.ID_MANGA = m.ID_MANGA
        JOIN manga_genero mg ON m.ID_MANGA = mg.ID_MANGA
        JOIN generos g ON mg.ID_GENERO = g.ID_GENERO
    """, con=engine)

    df_evolucion = pd.read_sql("""
        SELECT YEAR(ESTRENO) AS ANIO, COUNT(*) AS TOTAL
        FROM mangas
        WHERE ESTRENO IS NOT NULL
        GROUP BY ANIO
        ORDER BY ANIO;
    """, con=engine)

    df_top = pd.read_sql("""
        SELECT r.TITULO, m.LECTORES, r.RANK
        FROM mangas m
        JOIN ranks r ON m.ID_MANGA = r.ID_MANGA
        WHERE m.LECTORES IS NOT NULL AND r.RANK IS NOT NULL
        ORDER BY m.LECTORES DESC
        LIMIT 1;
    """, con=engine)

    top_manga = df_top.iloc[0]["TITULO"]
    top_lectores = int(df_top.iloc[0]["LECTORES"])
    top_rank = int(df_top.iloc[0]["RANK"])

except Exception as e:
    print("Error:", e)
    df_artistas = pd.DataFrame(columns=["ID_ARTISTA", "NOMBRE"])
    df_generos = pd.DataFrame(columns=["ID_ARTISTA", "ARTISTA", "GENERO"])
    df_evolucion = pd.DataFrame(columns=["ANIO", "TOTAL"])
    top_manga = ""
    top_lectores = 0
    top_rank = 0

def get_layout():
    return html.Div([
        html.H1("Relación de Artista con Géneros", style={"textAlign": "center", "color": "#333", "marginBottom": "20px"}),

        html.Div([
            dcc.Dropdown(
                id="dd-artista",
                options=[{"label": row["NOMBRE"], "value": row["ID_ARTISTA"]} for _, row in df_artistas.iterrows()],
                placeholder="Selecciona un artista",
                style={"width": "300px", "margin": "0 auto"}
            )
        ], style={"textAlign": "center", "marginBottom": "30px"}),

        html.Div(id="info-artista", style={
            "textAlign": "center", "color": "#fff", "backgroundColor": "#17a2b8",
            "padding": "20px", "margin": "20px auto", "maxWidth": "600px",
            "borderRadius": "10px", "fontSize": "1.2rem", "boxShadow": "0 4px 8px rgba(0,0,0,0.1)"
        }),

        dcc.Graph(id="grafica-artista"),

        html.H2("\ud83d\udcca Evolución de mangas publicados", className="text-center text-primary mt-5 mb-3"),
        dcc.Graph(
            figure=px.line(
                df_evolucion,
                x="ANIO",
                y="TOTAL",
                markers=True,
                title="\ud83d\udcca Evolución anual de mangas",
                labels={"ANIO": "Año", "TOTAL": "Cantidad"},
                template="plotly_white"
            ).update_traces(line=dict(color="#0077b6"))
        ),

        html.H2("\ud83c\udfc6 Manga más leído", className="text-center text-info mt-5"),
        html.Div([
            html.H3(top_manga, style={"color": "#fff", "marginBottom": "10px"}),
            html.P(f"\ud83d\udc41\ufe0f Lectores: {top_lectores:,}", style={"color": "#fff"}),
            html.P(f"\u2b50 Rank: {top_rank}", style={"color": "#fff"})
        ], style={
            "backgroundColor": "#6a0572", "padding": "20px", "borderRadius": "10px",
            "boxShadow": "0 4px 12px rgba(0,0,0,0.3)", "textAlign": "center",
            "maxWidth": "400px", "margin": "auto"
        })

    ], style={"backgroundColor": "#eaf6ff", "padding": "40px"})

# Callback
@callback(
    Output("info-artista", "children"),
    Output("grafica-artista", "figure"),
    Input("dd-artista", "value")
)
def actualizar_artista(id_artista):
    if id_artista is None or df_generos.empty:
        fig = px.pie(title="Selecciona un artista", template="plotly_white")
        return "Selecciona un artista para ver la información.", fig

    artista_info = df_artistas[df_artistas["ID_ARTISTA"] == id_artista]
    nombre_artista = artista_info.iloc[0]["NOMBRE"]

    df_filtrado = df_generos[df_generos["ID_ARTISTA"] == id_artista]

    if df_filtrado.empty:
        fig = px.pie(title="No hay géneros para este artista", template="plotly_white")
        return f"Artista seleccionado: {nombre_artista} | No hay géneros relacionados.", fig

    conteo_generos = df_filtrado["GENERO"].value_counts().reset_index()
    conteo_generos.columns = ["GENERO", "TOTAL"]

    fig = px.pie(
        conteo_generos,
        names="GENERO",
        values="TOTAL",
        title=f"Géneros relacionados con {nombre_artista}",
        template="plotly_white"
    )

    return f"Artista seleccionado: {nombre_artista} | Total de géneros: {len(df_filtrado)}", fig
