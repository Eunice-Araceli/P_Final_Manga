from dash import html, dcc, Input, Output, dash_table, callback
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

#CONEXION DE SQL
import Constantes_BD as c

# CONEXION AL SQL
cadena_con = f"mysql+mysqlconnector://{c.USER}:{c.PASSWORD}@{c.HOST}/{c.DATABASE}"
engine = create_engine(cadena_con)


#CARGA DE DATOS
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
except Exception as e:
    print("Error:", e)
    df_artistas = pd.DataFrame(columns=["ID_ARTISTA", "NOMBRE"])
    df_generos = pd.DataFrame(columns=["ID_ARTISTA", "ARTISTA", "GENERO"])


def get_layout():
    return html.Div([
        html.H1("Relación de Artista con Géneros", style={
            "fontSize": "2.5rem", "fontWeight": "bold", "color": "#333",
            "marginBottom": "20px", "textAlign": "center"
        }),
        html.P("Selecciona un artista para ver los géneros relacionados",
               style={"textAlign": "center", "color": "#555"}),

        html.Div([
            dcc.Dropdown(
                id="dd-artista",
                options=[{"label": row["NOMBRE"], "value": row["ID_ARTISTA"]} for _, row in df_artistas.iterrows()],
                placeholder="Selecciona un artista",
                style={"width": "300px", "margin": "0 auto", "fontSize": "1rem"}
            )
        ], style={"textAlign": "center", "marginBottom": "30px"}),

        html.Div(id="info-artista", style={
            "textAlign": "center", "color": "#fff", "backgroundColor": "#17a2b8",
            "padding": "20px", "margin": "20px auto", "maxWidth": "600px",
            "borderRadius": "10px", "fontSize": "1.2rem", "boxShadow": "0 4px 8px rgba(0,0,0,0.1)"
        }),

        html.Div([
            html.Div([
                dcc.Graph(id="grafica-artista", style={"height": "500px"})
            ], style={"flex": "1", "backgroundColor": "#fff", "padding": "20px", "borderRadius": "10px",
                      "boxShadow": "0 4px 8px rgba(0,0,0,0.1)", "margin": "10px"}),

            html.Div([
                html.H4("Géneros relacionados", style={"color": "#17a2b8", "marginBottom": "20px"}),
                dash_table.DataTable(
                    id="tabla-generos",
                    columns=[
                        {"name": "ID_ARTISTA", "id": "ID_ARTISTA"},
                        {"name": "GENERO", "id": "GENERO"}
                    ],
                    style_table={"overflowX": "auto", "height": "400px"},
                    style_cell={"textAlign": "left", "padding": "10px", "fontFamily": "Arial, sans-serif"},
                    style_header={"backgroundColor": "#17a2b8", "color": "white",
                                  "fontWeight": "bold", "textAlign": "center"},
                    style_data={"backgroundColor": "#f9f9f9", "color": "#333"},
                    page_size=10
                )
            ], style={"flex": "1", "backgroundColor": "#fff", "padding": "20px", "borderRadius": "10px",
                      "boxShadow": "0 4px 8px rgba(0,0,0,0.1)", "margin": "10px"}),
        ], style={"display": "flex", "flexWrap": "wrap", "justifyContent": "center",
                  "maxWidth": "1200px", "margin": "0 auto"})
    ], style={"backgroundColor": "#f0f2f5", "padding": "40px"})

# Callback
@callback(
    Output("info-artista", "children"),
    Output("grafica-artista", "figure"),
    Output("tabla-generos", "data"),
    Input("dd-artista", "value")
)
def actualizar_artista(id_artista):
    if id_artista is None or df_generos.empty:
        fig = px.pie(title="Selecciona un artista", template="plotly_white")
        return "Selecciona un artista para ver la información.", fig, []

    artista_info = df_artistas[df_artistas["ID_ARTISTA"] == id_artista]
    nombre_artista = artista_info.iloc[0]["NOMBRE"]

    df_filtrado = df_generos[df_generos["ID_ARTISTA"] == id_artista]

    if df_filtrado.empty:
        fig = px.pie(title="No hay géneros para este artista", template="plotly_white")
        return f"Artista seleccionado: {nombre_artista} | No hay géneros relacionados.", fig, []

    conteo_generos = df_filtrado["GENERO"].value_counts().reset_index()
    conteo_generos.columns = ["GENERO", "TOTAL"]

    fig = px.pie(
        conteo_generos,
        names="GENERO",
        values="TOTAL",
        title=f"Géneros relacionados con {nombre_artista}",
        template="plotly_white"
    )

    return (
        f"Artista seleccionado: {nombre_artista} | Total de géneros: {len(df_filtrado)}",
        fig,
        df_filtrado[["ID_ARTISTA", "GENERO"]].to_dict("records")
    )