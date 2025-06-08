from dash import Dash, html

def lista():
    return html.Ul([
        html.Li(html.A("Informacion Adicional del proyecto", href="https://docs.google.com/document/d/1wCumUV3Mli_3TdIWVds-bghRgEb797WD0_NLUA_fd4E/edit?tab=t.0#heading=h.fjio3jaax9my", target="_blank")),
        html.Li(html.A("mangazenkan", href="https://www.mangazenkan.com/ranking/products/?mode=monthly&type=comic", target="_blank")),
        html.Li(html.A("mangazenkan-2", href="https://www.mangazenkan.com/r/rekidai/total/?srsltid=AfmBOoo74zKqIrpmoGSOdfecYuZAZTvVMG3yoEL4uVR_YyfnT2hbbxqC", target="_blank"))
    ], style={"color": "black"})

# Estilo común para cada cuadro
cuadro_style = {
    "border": "2px solid #007BFF",
    "borderRadius": "15px",
    "padding": "20px",
    "margin": "20px 0",
    "backgroundColor": "#f0f8ff",
    "boxShadow": "3px 3px 8px rgba(0, 0, 0, 0.1)"
}

img_style = {
    "width": "150px",
    "height": "auto",
    "margin": "10px",
    "borderRadius": "10px",
    "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.2)"
}

def welcome():
    return html.Div([
        html.Center(html.H2("Universidad Autónoma de Baja California")),
        html.Img(
            src="https://comunicacioninstitucional.uabc.mx/wp-content/uploads/2024/03/Escudo_0_0-e1709986753738-768x1042.png",
            style={
                "width": "100px",
                "height": "100px",
                "position": "absolute",
                "top": "30px",
                "right": "30px"
            }
        ),
        html.Center(html.P("Facultad de Contaduría y Administración")),

        # Integrantes
        html.Div([
            html.Center(html.H2("Integrantes")),
            html.Ul([
                html.Li("Maria Guadalupe Gonzalez Gonzalez"),
                html.Li("Eunice Araceli Reyes Archuleta"),
                html.Li("Jazmin Alejandra Soriano Garcia"),
                html.Li("Valeria Monserrat Camacho Perez"),
                html.Li("Juan Ricardo Garfias Arellanes")
            ]),
        ], style=cuadro_style),

        # Roles
        html.Div([
            html.Center(html.H2("Roles")),
            html.Ul([
                html.Li([
                    html.Strong("Scrum Master: "),
                    "Eunice Araceli Reyes Archuleta"
                ]),
                html.Li([
                    html.Strong("Product Owner: "),
                    "Maria Guadalupe Gonzalez Gozalez"
                ]),
                html.Li([
                    html.Strong("Developers: "),
                    html.Ul([
                        html.Li("Jazmin Alejandra Soriano Garcia"),
                        html.Li("Juan Ricardo Garfias Arellanes"),
                        html.Li("Valeria Monserrat Camacho Perez")
                    ])
                ]),
                html.Li([
                    html.Strong("Cliente: "),
                    "Josue Miguel Flores Parra"
                ])
            ]),
        ], style=cuadro_style),

        html.Div([
            html.Center(html.H2("Roles")),
            html.Ul([
                html.Li([html.Strong("Scrum Master: "), "Eunice Araceli Reyes Archuleta"]),
                html.Li([html.Strong("Product Owner: "), "Maria Guadalupe Gonzalez Gozalez"]),
                html.Li([html.Strong("Developers: "),
                         html.Ul([
                            html.Li("Jazmin Alejandra Soriano Garcia"),
                            html.Li("Juan Ricardo Garfias Arellanes"),
                            html.Li("Valeria Monserrat Camacho Perez")
                         ])]),
                html.Li([html.Strong("Cliente: "), "Josue Miguel Flores Parra"])
            ]),
        ], style=cuadro_style),

        # Introducción + Imágenes Juntas
        html.Div([
            html.Center(html.H2("Introducción")),
            html.P(
                "En este proyecto lo que realizamos es la extracción de datos de varias páginas de manga "
                "utilizando Python y varias bibliotecas entre ellas pandas, Beautiful Soup, etc., con el propósito de crear un archivo CSV "
                "que contiene información de mangas. Aplicaremos un análisis y tratamiento de datos, ya que los datos extraídos presentan problemas con "
                "valores nulos, espacios, filas extras o errores de lectura de formato."
            ),
            html.Div([
                html.Img(src="https://redbookediciones.com/wp-content/uploads/2020/11/978-84-122311-5-1-410x528.jpg", style=img_style),
                html.Img(src="https://m.media-amazon.com/images/I/91AOnFyU6cL._AC_UF1000,1000_QL80_.jpg", style=img_style),
                html.Img(src="https://d28hgpri8am2if.cloudfront.net/book_images/onix/cvr9781647229146/a-history-of-modern-manga-9781647229146_lg.jpg", style=img_style),
                html.Img(src="https://m.media-amazon.com/images/I/91jahq5PI2L._AC_UF894,1000_QL80_.jpg", style=img_style),
                html.Img(src="https://i.ebayimg.com/images/g/9koAAOSwSXtnSdH4/s-l400.jpg", style=img_style),
                html.Img(src="https://i.ebayimg.com/images/g/t-cAAOSwYTllaGIG/s-l400.jpg", style=img_style),
                html.Img(src="https://images.cdn3.buscalibre.com/fit-in/360x360/a7/f8/a7f8de0c0ea08ed476c2a9f906285899.jpg", style=img_style),
                html.Img(src="https://imagenesal.bros.me/9788491456803.jpg", style=img_style),
                html.Img(src="https://m.media-amazon.com/images/I/712cKmJuchL._AC_UF894,1000_QL80_.jpg", style=img_style)
            ], style={
                "display": "flex",
                "justifyContent": "center",
                "flexWrap": "wrap"
            }),
        ], style=cuadro_style),

        # Objetivo General
        html.Div([
            html.Center(html.H2("Objetivo General")),
            html.P("Desarrollar un sistema que extraiga los datos de una página web, en el cual después llevará un proceso de limpiar y procesar los datos "
                   "con el fin de que sea más fácil su interpretación, con la finalidad de poder analizar los datos que obtengamos para generar estadísticas y posteriormente visualizaciones."),
        ], style=cuadro_style),

        # Objetivos Específicos
        html.Div([
            html.Center(html.H2("Objetivos Específicos")),
            html.Ul([
                html.Li("Utilizar herramientas como BeautifulSoup, Scrapy o Selenium."),
                html.Li("Verificar la calidad y confiabilidad de los datos."),
                html.Li("Documentar todo el proyecto.")
            ]),
        ], style=cuadro_style),

        # Tareas
        html.Div([
            html.Center(html.H2("Tareas")),
            html.Ul([
                html.Li([
                    html.Strong("Establecer datos a recabar (Eunice): "),
                    "Definir qué información se necesita (autores, calificaciones, géneros, editoriales, etc.) para asegurar que los datos sean útiles y relevantes."
                ]),
                html.Li([
                    html.Strong("Seleccionar páginas web (Eunice): "),
                    "Buscar en internet las páginas que son necesarias para recabar todos los datos establecidos anteriormente."
                ]),
                html.Li([
                    html.Strong("Crear código para ingresar a la web (Garfias): "),
                    "Crear el código correspondiente para poder recabar la información en base a la página web que seleccionamos."
                ]),
                html.Li([
                    html.Strong("Comprobar código (Garfias): "),
                    "Poner a prueba el código realizado y verificar si cumple con el punto de recabar los datos correctos."
                ]),
                html.Li([
                    html.Strong("Extraer los datos (Garfias): "),
                    "Ejecutar el código de extracción para obtener la información de las páginas seleccionadas y almacenarlas temporalmente así como solucionar posibles fallos."
                ]),
                html.Li([
                    html.Strong("Identificar y corregir errores en los datos (Eunice): "),
                    "Revisar los datos extraídos en busca de valores duplicados, datos incompletos o inconsistencias y corregirlos."
                ]),
                html.Li([
                    html.Strong("Almacenar los datos (Maria): "),
                    "Los datos serán almacenados en una Base de Datos."
                ]),
                html.Li([
                    html.Strong("Transformar los datos (Maria): "),
                    "Verificar con qué información se podrá trabajar desde el DataFrame para realizar un análisis."
                ]),
                html.Li([
                    html.Strong("Limpiar los datos (Maria): "),
                    "Revisar duplicados, corregir valores nulos, eliminar outliers y limpiar el DataFrame para mayor accesibilidad y claridad."
                ]),
                html.Li([
                    html.Strong("Elaborar estadísticas en base a los datos (Valeria): "),
                    "Crear estadísticos relevantes y gráficas para interpretar mejor la información."
                ]),
                html.Li([
                    html.Strong("Verificar que los datos sean correctos (Valeria): "),
                    "Validar que los datos procesados sean precisos y coherentes."
                ]),
                html.Li([
                    html.Strong("Establecer los datos a utilizar en cada dashboard (Valeria): "),
                    "Seleccionar los datos más importantes para presentarlos en dashboards comprensibles y organizados por categoría."
                ]),
                html.Li([
                    html.Strong("Seleccionar la gama de colores a utilizar (Jazmin): "),
                    "Elegir colores principales y secundarios para el diseño visual del proyecto."
                ]),
                html.Li([
                    html.Strong("Diseñar los dashboards (Jazmin): "),
                    "Planificar la estructura visual, tipo de gráficos, tablas e indicadores."
                ]),
                html.Li([
                    html.Strong("Crear los dashboards (Jazmin): "),
                    "Construir los dashboards con herramientas de desarrollo, integrar los datos y asegurar que funcionen correctamente y de forma interactiva."
                ])
            ]),
        ], style=cuadro_style),

        # Conclusión
        html.Div([
            html.Center(html.H2("Conclusión")),
            html.P(
                "A través del desarrollo de este trabajo, fue posible entender la importancia de una limpieza de datos como parte principal del análisis de información, "
                "se realizaron varias correcciones en este trabajo tanto en el código como en el documento de esta materia con el fin de que se utilizarán al mismo tiempo, "
                "se subió evidencia y hubo en distintas ocasiones decisiones de proyecto con el fin de cumplir con las condiciones de ambos profesores, "
                "también en este trabajo se hizo documentación clara del código."
            ),
            html.Br(),
            html.P(
                "Aprendimos a realizar la administración de un proyecto, definiendo claramente cada una de las tareas a realizar así como el tiempo en que deberían estar completadas, "
                "apoyándonos de herramientas que nos van a ayudar a que la planeación del proyecto sea más fácil de cumplir. "
                "Definitivamente lo aprendido en la materia lo podemos aprovechar no solo en el ámbito escolar, sino también en el personal y próximamente en el ámbito laboral."
            ),
            lista(),
        ], style=cuadro_style),

    ], style={"padding": "20px", "maxWidth": "900px", "margin": "auto", "backgroundColor": "#fff8f8", "borderRadius": "20px", "boxShadow": "6px 6px 20px rgba(0,0,0,0.1)"})

if __name__ == "__main__":
    app = Dash(__name__)
    app.layout = welcome()
    app.run_server(debug=True)
