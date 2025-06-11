from dash import Dash, html

def lista():
    return html.Ul([
        html.Li(html.A("Información Adicional del proyecto", href="https://docs.google.com/document/d/1wCumUV3Mli_3TdIWVds-bghRgEb797WD0_NLUA_fd4E/edit?tab=t.0#heading=h.fjio3jaax9my", target="_blank")),
        html.Li(html.A("Top Manga", href="https://myanimelist.net/topmanga.php", target="_blank")),
        html.Li(html.A("Mangazenkan", href="https://www.mangazenkan.com/r/rekidai/total/?srsltid=AfmBOoo74zKqIrpmoGSOdfecYuZAZTvVMG3yoEL4uVR_YyfnT2hbbxqC", target="_blank"))
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
            html.Center(html.H2("Descripción del problema", style={"color": "#003366"})),
            html.P(
                "Gran número de mangas estrenados sin un previo análisis de mercado, lo que conlleva a varios en estado de Hiatus (Pausa indefinida), lo cual desencadena en editoriales con pérdidas monetarias por sus proyectos sin finalizar, generando repercusiones tanto monetarias como reputacionales."
            ),
            html.Div([
                html.Img(src=url, style=img_style) for url in [
                    "https://i.pinimg.com/736x/ff/d6/17/ffd61770cd671e42b4431b72b79eebd1.jpg",
                    "https://i.pinimg.com/736x/84/7a/5d/847a5d5d14ff7ab649b61c87a2939cdb.jpg",
                    "https://i.pinimg.com/736x/27/1a/b1/271ab14dbe8d65dc0b9d8888fc508a0f.jpg",
                    "https://i.pinimg.com/736x/e2/8c/12/e28c12d755fba575d11259b360ce9abd.jpg",
                    "https://i.pinimg.com/736x/fc/ca/95/fcca952c3fdfe05d16525315be99812c.jpg",
                    "https://i.pinimg.com/736x/72/15/2d/72152daeb4da1881068028c901ff3baf.jpg",
                    "https://i.pinimg.com/736x/93/7d/a0/937da03f79c7c1d33510522e7d3e24ba.jpg",
                    "https://i.pinimg.com/736x/77/f7/37/77f737027145dd755530f78a4fe276c1.jpg",
                    "https://i.pinimg.com/736x/a0/52/20/a05220170083fcbd50f49511edf6bc82.jpg"
                ]
            ], style={
                "display": "flex",
                "justifyContent": "center",
                "flexWrap": "wrap"
            })
        ], style=cuadro_style),

        html.Div([
            html.Center(html.H2("Objetivo General", style={"color": "#003366"})),
            html.P("Desarrollar un sistema que extraiga los datos de una página web, en el cual después llevará un proceso de limpiar y procesar los datos con el fin de que sea más fácil su interpretación, con la finalidad de poder analizar los datos que obtengamos para generar estadísticas y posteriormente visualizaciones.")
        ], style=cuadro_style),

        html.Div([
            html.Center(html.H2("Objetivos Específicos", style={"color": "#003366"})),
            html.Ul([
                html.Li("Verificar la calidad y confiabilidad de los datos."),
                html.Li("Documentar todo el proyecto de manera clara y ordenada."),
                html.Li("Elaborar dashboards reales y funcionales.")
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
