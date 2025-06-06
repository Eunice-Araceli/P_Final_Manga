# Jazmin Alejandra Soriano Garcia
# 952
# 28/05/2025
# Home
from dash import Dash, html

def lista():
    return html.Ul([
        html.Li(html.A("Mangazenkan", href="https://www.mangazenkan.com/r/yearly/book/2024/", target="_blank", style={'color': 'blue'})),
        html.Li(html.A("Myanimelist", href="https://myanimelist.net/topmanga.php?type=manga&limit=50", target="_blank", style={'color': 'blue'})),
        html.Li(html.A("Hulu", href="https://www.hulu.com/welcome", target="_blank", style={'color': 'blue'})),
    ])

def welcome():
    return html.Div([
        html.Img(
            src="https://logodix.com/logo/1859046.png",
            style={
                "width": "100px",
                "height": "100px",
                "position": "absolute",
                "top": "10px",
                "right": "10px",
                "zIndex": "1"
            }
        ),

        html.H1("Proyecto Final"),
        html.P("Programación para la extracción de datos"),
        html.Hr(),

        lista(),

        html.Div([
            html.Img(
                src="https://tse4.mm.bing.net/th/id/OIP.jjS8joxSbrPeV39oOs2-uwHaEK?rs=1&pid=ImgDetMain.png",
                style={
                    "width": "300px",
                    "height": "120px",
                    "objectFit": "cover",
                    "marginRight": "20px",
                }
            ),

            html.Div([
                html.H3("Descripción"),
                html.P("Esta página web fue desarrollada en la materia de programación para la extracción de datos, impartida por el profesor Josue Miguel Flores Parra, su propósito principal es proporcionar una interfaz sencilla y clara que permita al usuario acceder rápidamente información referente a sus mangas favoritos.")
            ],
            style={"maxWidth": "400px",
                   "color": "black",
                   "marginLeft": "60px"})
        ],
        style={
            "display": "flex",
            "alignItems": "center",
            "marginTop": "20px"
        }),

        html.Div([
            html.P("Integrantes:"),
            html.Ul([
                html.Li("Eunice Reyes Archuleta"),
                html.Li("Maria Guadalupe Gonzalez Gonzalez"),
                html.Li("Jazmin Alejandra Soriano Garcia")
            ])
        ], style={"marginTop": "30px"}),
    ],
    style={
        "backgroundColor": "skyblue",
        "color": "black",
        "padding": "20px",
        "fontFamily": "Arial",
        "position": "relative"
    })

if __name__ == "__main__":
    app = Dash(__name__)
    app.layout = welcome()
    app.run(debug=True)