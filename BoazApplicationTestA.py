# This is the overall application with some basic layouts and a really rough idea of what I am thinking
# Still WIP
#
# Install the packaging
# pip install pyinstaller
#
# build exe - pyinstaller --onefile BoazApplicationTestA.py
#
#

import time
import dash
import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd
import plotly.graph_objs as go
from dash import Input, Output, dcc, html
import plotly.express as px

#
# Major issues with installing this, not sure what its problem is. Also looking for other libraries
#
# import prophet
#


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

input1 = input()
df = pd.read_csv(input1)
fig1 = px.scatter(df, x='Data_value', y='Period')
df.info()

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# The style for the sidebar.
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Boaz Project", className="display-4"),
        html.Hr(),
        html.P(
            "Select a Graph", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Bar", href="/Bar", active="exact"),
                dbc.NavLink("Page 2", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.P("This is the content of the home page!")
    elif pathname == "/Bar":

        return dcc.Graph(figure=fig1)
    elif pathname == "/page-2":
        return html.P("Oh cool, this is page 2!")
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )
#
# Running on local host
#
if __name__ == "__main__":
    app.run_server(port=8888)

# time.sleep(10000000)
