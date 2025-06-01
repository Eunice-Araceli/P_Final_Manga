# Jazmin Alejandra Soriano Garcia
# 952
# 15/05/2025
# Dashboard menu principal
import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, callback
import welcome_dash as wd
import dashboard_uno as kd
import dashboard_dos as dd

SIDEBAR_STYLE = {
   "position": "fixed",
   "top": 0,
   "left": 0,
   "bottom": 0,
   "width": "16rem",
   "padding": "2rem 1rem",
   "background-color": "#skyblue",
}

CONTENT_STYLE = {
   "margin-left": "18rem",
   "margin-right": "2rem",
   "padding": "2rem 1rem",
}

sidebar = html.Div(
   [
       html.H2("Mangas", className="display-5", style={"color": "white"}),
       html.Hr(),
       html.P("Menú principal", className="lead", style={"color": "white"}),
       dbc.Nav(
           [
               dbc.NavLink("Home", href="/", active="exact"),
               dbc.NavLink("Ranking vs Calificación", href="/dash1", active="exact"),
               dbc.NavLink("Lectores por manga", href="/dash2", active="exact"),
               dbc.NavLink("Dashboard 3", href="/dash3", active="exact"),

           ],
           vertical=True,
           pills=True,
       ),
   ],
   style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

@callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
   if pathname == "/":
       return wd.welcome()
   elif pathname == "/dash1":
       return kd.kpi()
   elif pathname == "/dash2":
       return dd.kpi_tres()
   elif pathname == "/dash3":
       return

   return html.Div(
       [
           html.H1("404: Not found", className="text-danger"),
           html.Hr(),
           html.P(f"The pathname {pathname} was not recognised..."),
       ],
       className="p-3 bg-light rounded-3",
   )

if __name__ == "__main__":
    app = dash.Dash(external_stylesheets=[dbc.themes.SOLAR],
                   suppress_callback_exceptions=True)
    app.layout = html.Div([dcc.Location(id="url"), sidebar, content])
    app.run(debug=True)
