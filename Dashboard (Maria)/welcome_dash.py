from dash import Dash, html

def lista():
    return html.Ul([
        html.Li(html.A("Información Adicional del proyecto", href="https://docs.google.com/document/d/1wCumUV3Mli_3TdIWVds-bghRgEb797WD0_NLUA_fd4E/edit?tab=t.0#heading=h.fjio3jaax9my", target="_blank")),
        html.Li(html.A("mangazenkan", href="https://www.mangazenkan.com/ranking/products/?mode=monthly&type=comic", target="_blank")),
        html.Li(html.A("mangazenkan-2", href="https://www.mangazenkan.com/r/rekidai/total/?srsltid=AfmBOoo74zKqIrpmoGSOdfecYuZAZTvVMG3yoEL4uVR_YyfnT2hbbxqC", target="_blank"))
    ], style={"color": "#333", "fontSize": "18px", "paddingLeft": "20px"})

cuadro_style = {
    "border": "2px solid #007BFF",
    "borderRadius": "20px",
    "padding": "25px",
    "margin": "30px 0",
    "background": "linear-gradient(135deg, #f0f8ff, #e0f7fa)",
    "boxShadow": "0 8px 20px rgba(0, 0, 0, 0.15)",
    "transition": "all 0.3s ease"
}

img_style = {
    "width": "140px",
    "height": "auto",
    "margin": "10px",
    "borderRadius": "12px",
    "boxShadow": "0 6px 12px rgba(0, 0, 0, 0.2)",
    "transition": "transform 0.2s",
    ":hover": {"transform": "scale(1.05)"}
}

def welcome():
    return html.Div([
        html.Center(html.H1("Universidad Autónoma de Baja California", style={"color": "#004085", "marginTop": "20px"})),
        html.Img(
            src="https://comunicacioninstitucional.uabc.mx/wp-content/uploads/2024/03/Escudo_0_0-e1709986753738-768x1042.png",
            style={
                "width": "90px",
                "height": "90px",
                "position": "absolute",
                "top": "30px",
                "right": "30px"
            }
        ),
        html.Center(html.H4("Facultad de Contaduría y Administración", style={"color": "#155724"})),

        html.Div([
            html.Center(html.H2("Integrantes", style={"color": "#003366"})),
            html.Ul([
                html.Li("Maria Guadalupe Gonzalez Gonzalez"),
                html.Li("Eunice Araceli Reyes Archuleta")
            ], style={"fontSize": "18px", "paddingLeft": "20px"})
        ], style=cuadro_style),

        html.Div([
            html.Center(html.H2("Introducción", style={"color": "#003366"})),
            html.P(
                "En este proyecto lo que realizamos es la extracción de datos de varias páginas de manga utilizando Python y varias bibliotecas como pandas, Beautiful Soup, etc. con el propósito de crear un archivo CSV con información relevante. Se realiza limpieza de datos para eliminar valores nulos, espacios innecesarios y errores de formato."
            ),
            html.Div([
                html.Img(src=url, style=img_style) for url in [
                    "https://redbookediciones.com/wp-content/uploads/2020/11/978-84-122311-5-1-410x528.jpg",
                    "https://m.media-amazon.com/images/I/91AOnFyU6cL._AC_UF1000,1000_QL80_.jpg",
                    "https://d28hgpri8am2if.cloudfront.net/book_images/onix/cvr9781647229146/a-history-of-modern-manga-9781647229146_lg.jpg",
                    "https://m.media-amazon.com/images/I/91jahq5PI2L._AC_UF894,1000_QL80_.jpg",
                    "https://i.ebayimg.com/images/g/9koAAOSwSXtnSdH4/s-l400.jpg",
                    "https://i.ebayimg.com/images/g/t-cAAOSwYTllaGIG/s-l400.jpg",
                    "https://images.cdn3.buscalibre.com/fit-in/360x360/a7/f8/a7f8de0c0ea08ed476c2a9f906285899.jpg",
                    "https://imagenesal.bros.me/9788491456803.jpg",
                    "https://m.media-amazon.com/images/I/712cKmJuchL._AC_UF894,1000_QL80_.jpg"
                ]
            ], style={
                "display": "flex",
                "justifyContent": "center",
                "flexWrap": "wrap"
            })
        ], style=cuadro_style),

        html.Div([
            html.Center(html.H2("Objetivo General", style={"color": "#003366"})),
            html.P("Desarrollar un sistema para extraer, limpiar y analizar datos de páginas web de manga y generar visualizaciones significativas para la toma de decisiones.")
        ], style=cuadro_style),

        html.Div([
            html.Center(html.H2("Objetivos Específicos", style={"color": "#003366"})),
            html.Ul([
                html.Li("Utilizar herramientas como BeautifulSoup, Scrapy o Selenium."),
                html.Li("Verificar la calidad y confiabilidad de los datos."),
                html.Li("Documentar todo el proyecto de manera clara y ordenada.")
            ], style={"fontSize": "18px", "paddingLeft": "20px"})
        ], style=cuadro_style),

        html.Div([
            html.Center(html.H2("Conclusión", style={"color": "#003366"})),
            html.P("A través de este trabajo, se comprendió la importancia de la limpieza de datos como parte esencial del análisis, permitiendo construir visualizaciones significativas para comprender patrones en los datos extraídos."),
            html.P("El proyecto permitió desarrollar habilidades de administración de proyectos, documentación técnica y uso de herramientas modernas de extracción de datos."),
            lista()
        ], style=cuadro_style)

    ], style={
        "padding": "30px",
        "maxWidth": "1000px",
        "margin": "auto",
        "background": "#ffffff",
        "borderRadius": "20px",
        "boxShadow": "0 10px 25px rgba(0,0,0,0.1)"
    })

if __name__ == "__main__":
    app = Dash(__name__)
    app.layout = welcome()
    app.run_server(debug=True)
