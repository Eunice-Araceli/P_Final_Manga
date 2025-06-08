from dash import html, dcc, Input, Output, dash_table, callback
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

#CONEXION EN SQL
USER = 'root'
PASSWORD = '123456'
HOST = 'localhost'
DATABASE = 'manga'
cadena_conexion = f"mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}/{DATABASE}"
engine = create_engine(cadena_conexion)

#CARGA DE DATOS
try:
    df_generos = pd.read_sql("SELECT ID_GENERO, NOMBRE AS NOMBRE_GENERO FROM generos", con=engine)
    df_artistas = pd.read_sql("SELECT ID_ARTISTA, NOMBRE FROM artistas", con=engine)
except Exception as e:
    print("Error:", e)
    df_generos = pd.DataFrame(columns=["ID_GENERO", "NOMBRE_GENERO"])
    df_artistas = pd.DataFrame(columns=["ID_ARTISTA", "NOMBRE"])


#DISEÑO DEL CUADRO POR ARTISTA Y GENERO
def get_layout():
    return html.Div([
        html.Div([
            html.H1("RELACION DE GENERO CON ARTISTA", style={
                "fontSize": "2.5rem", "fontWeight": "bold", "color": "#333",
                "marginBottom": "20px", "textAlign": "center"
            }),
            html.P("Selecciona un género para ver los artistas relacionados",
                   style={"textAlign": "center", "color": "#555"})
        ], style={"marginBottom": "40px"}),

        html.Div([
            dcc.Dropdown(
                id="dd-genero",
                options=[{"label": row["NOMBRE_GENERO"], "value": row["ID_GENERO"]} for _, row in df_generos.iterrows()],
                placeholder="Selecciona un género",
                style={
                    "width": "300px", "margin": "0 auto", "fontSize": "1rem",
                    "padding": "8px", "borderRadius": "6px"
                }
            )
        ], style={"textAlign": "center", "marginBottom": "30px"}),

        html.Div(id="info-genero", style={
            "textAlign": "center", "color": "#fff", "backgroundColor": "#007bff",
            "padding": "20px", "margin": "20px auto", "maxWidth": "600px",
            "borderRadius": "10px", "fontSize": "1.2rem", "boxShadow": "0 4px 8px rgba(0,0,0,0.1)"
        }),

        html.Div([
            html.Div([
                dcc.Graph(id="grafica-genero", style={"height": "500px"})
            ], style={
                "flex": "1", "backgroundColor": "#fff", "padding": "20px", "borderRadius": "10px",
                "boxShadow": "0 4px 8px rgba(0,0,0,0.1)", "margin": "10px"
            }),

            html.Div([
                html.H4("artistas relacionados", style={"color": "#007bff", "marginBottom": "20px"}),
                dash_table.DataTable(
                    id="tabla-artistas",
                    columns=[
                        {"name": "ID_ARTISTA", "id": "ID_ARTISTA"},
                        {"name": "NOMBRE", "id": "NOMBRE"}
                    ],
                    style_table={"overflowX": "auto", "height": "400px"},
                    style_cell={
                        "textAlign": "left", "padding": "10px",
                        "fontFamily": "Arial, sans-serif"
                    },
                    style_header={
                        "backgroundColor": "#007bff", "color": "white",
                        "fontWeight": "bold", "textAlign": "center"
                    },
                    style_data={"backgroundColor": "#f9f9f9", "color": "#333"},
                    page_size=10
                )
            ], style={
                "flex": "1", "backgroundColor": "#fff", "padding": "20px", "borderRadius": "10px",
                "boxShadow": "0 4px 8px rgba(0,0,0,0.1)", "margin": "10px"
            }),
        ], style={
            "display": "flex", "flexWrap": "wrap", "justifyContent": "center",
            "maxWidth": "1200px", "margin": "0 auto"
        })
    ], style={"backgroundColor": "#f0f2f5", "padding": "40px"})


@callback(
    Output("info-genero", "children"),
    Output("grafica-genero", "figure"),
    Output("tabla-artistas", "data"),
    Input("dd-genero", "value")
)
def actualizar_genero(id_genero):
    if id_genero is None or df_generos.empty:
        fig = px.pie(title="Selecciona un género", template="plotly_white")
        return "Selecciona un género para ver la información.", fig, []

    nombre_genero = df_generos.loc[df_generos["ID_GENERO"] == id_genero, "NOMBRE_GENERO"].values[0]
    total_generos = len(df_generos)
    df_filtrado = df_artistas[df_artistas["ID_ARTISTA"] % total_generos == id_genero % total_generos]

    if df_filtrado.empty:
        fig = px.pie(title="No hay artistas para este género", template="plotly_white")
        return f"Género seleccionado: {nombre_genero} | No hay artistas relacionados.", fig, []

    fig = px.pie(
        names=df_filtrado["NOMBRE"],
        values=[1] * len(df_filtrado),
        title=f"Distribucion de artistas: {nombre_genero}",
        template="plotly_white"
    )

    return (
        f"Género seleccionado: {nombre_genero} | Total de artistas: {len(df_filtrado)}",
        fig,
        df_filtrado.to_dict("records")
    )
