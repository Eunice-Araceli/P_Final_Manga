from dash import html, dcc, dash_table, Input, Output, callback
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
import Constantes_BD as c

# CONEXIÓN A BD
cadena_con = f"mysql+mysqlconnector://{c.USER}:{c.PASSWORD}@{c.HOST}/{c.DATABASE}"
engine = create_engine(cadena_con)

# CONSULTAS DE SQL
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

    df_estreno = pd.read_sql("""
        SELECT A.NOMBRE AS NOMBRE_ARTISTA, YEAR(M.ESTRENO) AS ESTRENO
        FROM MANGA_ARTISTA MA 
        JOIN MANGAS M ON M.ID_MANGA = MA.ID_MANGA
        JOIN ARTISTAS A ON MA.ID_ARTISTA = A.ID_ARTISTA
        WHERE M.ESTRENO IS NOT NULL;
    """, con=engine)

    df_estreno_agg = df_estreno.groupby(["NOMBRE_ARTISTA", "ESTRENO"]).size().reset_index(name="TOTAL")
    lista_anios = sorted(df_estreno_agg["ESTRENO"].unique())

    df_mejor_rank = pd.read_sql("""
        SELECT A.NOMBRE AS NOMBRE_ARTISTA, MIN(R.RANK) AS MEJOR_RANK
        FROM MANGA_ARTISTA MA 
        JOIN MANGAS M ON M.ID_MANGA = MA.ID_MANGA
        JOIN ARTISTAS A ON MA.ID_ARTISTA = A.ID_ARTISTA
        JOIN RANKS R ON M.ID_MANGA = R.ID_MANGA
        GROUP BY A.NOMBRE
    """, con=engine)

except Exception as e:
    print("Error:", e)
    df_artistas = pd.DataFrame(columns=["ID_ARTISTA", "NOMBRE"])
    df_generos = pd.DataFrame(columns=["ID_ARTISTA", "ARTISTA", "GENERO"])
    df_estreno_agg = pd.DataFrame(columns=["NOMBRE_ARTISTA", "ESTRENO", "TOTAL"])
    lista_anios = []
    df_mejor_rank = pd.DataFrame(columns=["NOMBRE_ARTISTA", "MEJOR_RANK"])

#GRAFICA DE RELACION DE ARTISTAS CON GENERO
def get_layout():
    return html.Div([
        html.H1("💻 Relacion de artista con generos 📌", style={"textAlign": "center", "color": "#333", "marginBottom": "20px"}),

        html.Div([
            dcc.Dropdown(
                id="dd-artista",
                options=[{"label": row["NOMBRE"], "value": row["ID_ARTISTA"]} for _, row in df_artistas.iterrows()],
                placeholder=" 📌 Selecciona un artista 📌",
                style={"width": "300px", "margin": "0 auto"}
            )
        ], style={"textAlign": "center", "marginBottom": "30px"}),

        html.Div(id="info-artista", style={
            "textAlign": "center", "color": "#fff", "backgroundColor": "#17a2b8",
            "padding": "20px", "margin": "20px auto", "maxWidth": "600px",
            "borderRadius": "10px", "fontSize": "1.2rem", "boxShadow": "0 4px 8px rgba(0,0,0,0.1)"
        }),

        dcc.Graph(id="grafica-artista"),

        html.H2("📈 Mangas por artista y año de estreno 📈", className="text-center text-primary mt-5 mb-3"),
        dcc.Graph(id="grafico-anio-artista"),

        html.H2("🌟 mejor ranking por artista 🌟", className="text-center text-primary mt-5 mb-3"),
        dcc.Graph(id="grafico-rank-artista")

    ], style={"backgroundColor": "#eaf6ff", "padding": "40px"})


@callback(
    Output("info-artista", "children"),
    Output("grafica-artista", "figure"),
    Output("grafico-anio-artista", "figure"),
    Output("grafico-rank-artista", "figure"),
    Input("dd-artista", "value")
)
def actualizar_todo(id_artista):
    if id_artista is None:
        fig_blank = px.bar(title="Selecciona un artista", template="plotly_white")
        fig_blank.update_layout(xaxis={'visible': False}, yaxis={'visible': False})
        return "🐉 Selecciona un artista para ver su informacion ⛩️", fig_blank, fig_blank, fig_blank

    #DATA FRAMES
    artista_info = df_artistas[df_artistas["ID_ARTISTA"] == id_artista]
    nombre_artista = artista_info.iloc[0]["NOMBRE"]


    df_gen = df_generos[df_generos["ID_ARTISTA"] == id_artista]
    conteo_generos = df_gen["GENERO"].value_counts().reset_index()
    conteo_generos.columns = ["GENERO", "TOTAL"]
    fig_pie = px.pie(
        conteo_generos,
        names="GENERO",
        values="TOTAL",
        title=f"🐉 Generos relacionados con {nombre_artista}",
        template="plotly_white"
    )

    #GRAFICA DE BARRAS Y DATA FRAME
    df_estreno_filtrado = df_estreno[df_estreno["NOMBRE_ARTISTA"] == nombre_artista]
    df_estreno_agg = df_estreno_filtrado.groupby("ESTRENO").size().reset_index(name="TOTAL")
    fig_estreno = px.bar(
        df_estreno_agg,
        x="ESTRENO",
        y="TOTAL",
        title=f"⛩️ Mangas por año de estreno de {nombre_artista}",
        template="plotly_white",
        color="TOTAL",
        color_continuous_scale="Blues"
    )

    #GRAFICA DE MEJOR RANKING
    df_rank = df_mejor_rank[df_mejor_rank["NOMBRE_ARTISTA"] == nombre_artista]
    fig_rank = px.bar(
        df_rank,
        x="MEJOR_RANK",
        y="NOMBRE_ARTISTA",
        orientation="h",
        title="🥇 Mejor ranking del artista 🥇",
        template="plotly_white",
        color="MEJOR_RANK",
        color_continuous_scale="Blues"
    )

    return (
        f"⛩️ Artista seleccionado: {nombre_artista} 📚 Total de generos: {len(df_gen)}",
        fig_pie,
        fig_estreno,
        fig_rank
    )


