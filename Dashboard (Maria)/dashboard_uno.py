from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sqlalchemy import create_engine

#CONEXION DE SQL
engine = create_engine("mysql+mysqlconnector://root:123456@localhost/manga")

#CONSULTAS
df_manga = pd.read_sql("SELECT ID_MANGA FROM mangas", con=engine)
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

df_demografias = pd.read_sql("""
    SELECT d.NOMBRE AS DEMOGRAFIA, COUNT(*) AS TOTAL
    FROM manga_demografia md
    JOIN demografias d ON md.ID_DEMOGRAFIA = d.ID_DEMOGRAFIA
    GROUP BY d.NOMBRE
""", con=engine)

#GRAFICO RADAR
def radar_demografias(df):
    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=df["TOTAL"],
        theta=df["DEMOGRAFIA"],
        fill='toself',
        name="Popularidad"
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, df["TOTAL"].max()])
        ),
        title="Popularidad de demografias Japonesas",
        showlegend=False,
        template="plotly_dark"
    )
    return fig

# Estilo para círculos informativos
def circular_card(title, value, color):
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

# Layout principal
def layout_dashboard_japon():
    return dbc.Container([
        html.H3("Dashboard global de manga", className="text-center fw-bold mb-4"),

        dbc.Row([
            dbc.Col(circular_card("📚 Mangas", f"{len(df_manga):,}", "#17a2b8"), md=4),
            dbc.Col(circular_card("🎭 Géneros", f"{df_genero.shape[0]:,}", "#007bff"), md=4),
            dbc.Col(circular_card("🎨 Temas", f"{df_tema.shape[0]:,}", "#ffc107"), md=4)
        ], className="mb-5"),

        dbc.Row([
            dbc.Col(dcc.Graph(
                id="grafico-demografias",
                figure=radar_demografias(df_demografias)
            ), md=12)
        ], className="mb-5"),

        dbc.Row([
            dbc.Col(dcc.Graph(
                figure=px.bar(
                    df_genero.sort_values("TOTAL", ascending=True).tail(15),
                    x="TOTAL",
                    y="GENERO",
                    orientation="h",
                    title="Top Generos mas Populares",
                    template="plotly_white",
                    color="TOTAL",
                    color_continuous_scale="Tealgrn"
                )
            ), md=6),

            dbc.Col(dcc.Graph(
                figure=px.bar_polar(
                    df_tema.sort_values("TOTAL", ascending=False).head(15),
                    r="TOTAL",
                    theta="TEMA",
                    color="TOTAL",
                    title="Temas Principales",
                    color_continuous_scale="Purples",
                    template="plotly_dark"
                )
            ), md=6)
        ])
    ], fluid=True, className="p-4 bg-dark text-white")
