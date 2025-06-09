from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sqlalchemy import create_engine

#CONEXION DE SQL
import Constantes_BD as c

# CONEXION AL SQL
cadena_con = f"mysql+mysqlconnector://{c.USER}:{c.PASSWORD}@{c.HOST}/{c.DATABASE}"
engine = create_engine(cadena_con)


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

# Función para aplicar fondo blanco manual en cada gráfico
def set_white_background(fig):
    fig.update_layout(
        paper_bgcolor='#cce8ff',
        plot_bgcolor='white'
    )
    return fig

# Layout principal
def layout_dashboard_japon():
    # Gráfico de barras: demografías
    fig_demografias = px.bar(
        df_demografias.sort_values("TOTAL", ascending=False),
        x="DEMOGRAFIA",
        y="TOTAL",
        title="Popularidad de Demografías Japonesas",
        template="plotly_white",
        color="TOTAL",
        color_continuous_scale="Blues"
    )
    set_white_background(fig_demografias)

    # Gráfico de barras horizontales: géneros
    fig_genero = px.bar(
        df_genero.sort_values("TOTAL", ascending=True).tail(15),
        x="TOTAL",
        y="GENERO",
        orientation="h",
        title="Top Géneros más Populares",
        template="plotly_white",
        color="TOTAL",
        color_continuous_scale="Blues"
    )
    set_white_background(fig_genero)

    # Gráfico de pastel: temas
    fig_tema = px.pie(
        df_tema.sort_values("TOTAL", ascending=False).head(10),
        values="TOTAL",
        names="TEMA",
        title="Temas Principales",
        template="plotly_white",
        hole=0.3,
        color_discrete_sequence=px.colors.sequential.Blues
    )
    set_white_background(fig_tema)

    return dbc.Container([
        html.H3("Dashboard global de manga", className="text-center fw-bold mb-4 text-white"),

        dbc.Row([
            dbc.Col(circular_card("📚 Mangas", f"{len(df_manga):,}", "#17a2b8"), md=4),
            dbc.Col(circular_card("🎭 Géneros", f"{df_genero.shape[0]:,}", "#007bff"), md=4),
            dbc.Col(circular_card("🎨 Temas", f"{df_tema.shape[0]:,}", "#0056b3"), md=4)
        ], className="mb-5"),

        dbc.Row([
            dbc.Col(dcc.Graph(figure=fig_demografias), md=12)
        ], className="mb-5"),

        dbc.Row([
            dbc.Col(dcc.Graph(figure=fig_genero), md=6),
            dbc.Col(dcc.Graph(figure=fig_tema), md=6)
        ])
    ], fluid=True, className="p-4 bg-dark text-white")