from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
from BD import Constantes_BD as c

# Conexión al SQL
cadena_con = f"mysql+mysqlconnector://{c.USER}:{c.PASSWORD}@{c.HOST}/{c.DATABASE}"
engine = create_engine(cadena_con)

# Consultas
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

#LAS TARJETITAS CIRCULARES
def circular_card(title, value, color):
    return html.Div([
        html.H6(title, className="fw-bold mb-2"),
        html.H3(value, className="fw-bold")
    ], style={
        "background": color,
        "color": "white",
        "borderRadius": "80%",
        "width": "160px",
        "height": "160px",
        "display": "flex",
        "flexDirection": "column",
        "alignItems": "center",
        "justifyContent": "center",
        "textAlign": "center",
        "margin": "0 auto"
    })

#EN ESTA PARTE SE PONE QUE TIPO DE GRAFICOS ES EL QUE QUIERES Y LAS X Y Y
def layout_dashboard_japon():
    #GRAFICOS DE LA DEMOGRFIA CON GRAFICO EN BLANCO
    fig_demografias = px.bar(
        df_demografias.sort_values("TOTAL", ascending=False),
        x="DEMOGRAFIA",
        y="TOTAL",
        title="Popularidad de demografias Japonesas 🐉",
        template="plotly_white",
        color="TOTAL",
        color_continuous_scale="ice"
    )
    fig_demografias.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        font=dict(color="black"),
        xaxis=dict(color="black"),
        yaxis=dict(color="black")
    )

    # GRAFICOS DE GENERO CON EL FONDO OSCURO
    fig_genero = px.bar(
        df_genero.sort_values("TOTAL", ascending=True).tail(15),
        x="TOTAL",
        y="GENERO",
        orientation="h",
        title="Top Géneros más Populares",
        template="plotly_dark",
        color="TOTAL",
        color_continuous_scale="ice"  # Azul-gris suave
    )
    fig_genero.update_layout(
        paper_bgcolor="#121212",
        plot_bgcolor="#1e1e1e",
        font=dict(color="white"),
        xaxis=dict(color="white"),
        yaxis=dict(color="white")
    )

#GRAFICO DE TEMAS CON TEMA OBSUCURO
    fig_tema = px.pie(
        df_tema.sort_values("TOTAL", ascending=False).head(10),
        values="TOTAL",
        names="TEMA",
        title="Temas Principales",
        template="plotly_dark",
        hole=0.3,
        color_discrete_sequence=px.colors.sequential.ice
    )
    fig_tema.update_layout(
        paper_bgcolor="#121212",
        font=dict(color="white")
    )

    return dbc.Container([
        html.H3("📊 Dashboard global de manga 🌎", className="text-center fw-bold mb-4 text-white"),

        dbc.Row([
            dbc.Col(circular_card("📚 Mangas", f"{len(df_manga):,}", "#3399cc"), md=4),
            dbc.Col(circular_card("🎭 Géneros", f"{df_genero.shape[0]:,}", "#5dade2"), md=4),
            dbc.Col(circular_card("🎨 Temas", f"{df_tema.shape[0]:,}", "#2874a6"), md=4)
        ], className="mb-5"),

        dbc.Row([
            dbc.Col(dcc.Graph(figure=fig_demografias), md=12)
        ], className="mb-5"),

        dbc.Row([
            dbc.Col(dcc.Graph(figure=fig_genero), md=6),
            dbc.Col(dcc.Graph(figure=fig_tema), md=6)
        ])
    ], fluid=True, className="p-4", style={"backgroundColor": "#1c1c1c"})
