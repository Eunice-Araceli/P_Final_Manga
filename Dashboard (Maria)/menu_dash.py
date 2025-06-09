
import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, callback
import welcome_dash as wd
import dashboard_dos as ds
import dashboard_uno as du
import dashboard_cuatro as d4
import dashboard_cinco as dc
import dashboard_seis as dss
import Constantes_BD as c

#app es para darle un estilo a la pagina
#BOOTSTRAP es para cambiar el tema de la pagina




#ESTO ES LA PARTE IZQUIERDA
#Display-4 se le puede cambiar es el tipo de letra
#GadMinder  es el nombre que le estamos poniendo  en el titulo
#ClassName es para cambiar el tipo de letra
#
sidebar = html.Div(
    [
        html.H2("📜 Menú", className="menu-title"),
        html.Hr(),
        html.P("🎆 Dashboard de Comic 🏮", className="menu-lead"),
        dbc.Nav(
            [
                dbc.NavLink("🏠 Inicio", href="/", active="exact"),
                dbc.NavLink("🧮 Dashboard 1", href="/dash1", active="exact"),
                dbc.NavLink("📝 Dashboard 2", href="/dash2", active="exact"),
                dbc.NavLink("📈 Dashboard 3", href="/dash3", active="exact"),
                dbc.NavLink("👩🏻‍💻 Dashboard 4", href="/dash4", active="exact"),
                dbc.NavLink("🖥️ Dashboard 5", href="/dash5", active="exact"),
                dbc.NavLink("👨🏻‍💻 Documento final", href="https://docs.google.com/document/d/1wCumUV3Mli_3TdIWVds-bghRgEb797WD0_NLUA_fd4E/edit?tab=t.0", active="exact", target="_blank"),
                dbc.NavLink("💻 GitHub", href="https://github.com/", active="exact", target="_blank"),
            ],
            vertical=True,
            pills=True,
            className="nav-comic"
        ),
    ],
    className="SIDEBAR_STYLE comic-box",
)


#ESTO ES LA PARTE DERECHA
content = html.Div(id="page-content", className="CONTENT_STYLE")



#en esta parte es importante lo del href para que pueda navejar entre las paginas
@callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return wd.welcome()
    elif pathname == "/dash1":
        return du.layout_dashboard_japon()
    elif pathname == "/dash2":
        return ds.get_dashboard()
    elif pathname == "/dash3":
        return d4.get_layout()
    elif pathname == "/dash4":
        return dc.layout_editorial_por_rango_multiples()
    elif pathname == "/dash5":
        return dss.layout_dashboard_final()
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )


if __name__ == "__main__":
    app = dash.Dash(external_stylesheets=[dbc.themes.SOLAR],suppress_callback_exceptions=True)
    app.layout = html.Div([dcc.Location(id="url"), sidebar, content])
    app.run(debug=True)

