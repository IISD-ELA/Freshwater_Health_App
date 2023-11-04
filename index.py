from dash import  dcc
from dash import html
from dash.dependencies import Input, Output

# get dash app and server from app
from app import app
from app import server

# get web pages
from apps import home, dashboard, prediction, guidelines


app.layout = html.Div([
    # access the browser url, this component has the pathname child
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-container', children=[], className="bgImg")
], className="main-container")


@app.callback(
    Output('page-container', 'children'),
    [Input('url', 'pathname')]
)
def render_page(pathname):
    if pathname == '/':
        return home.layout
    if pathname == '/home':
        return home.layout
    if pathname == '/dashboard':
        return dashboard.layout
    if pathname == '/prediction':
        return prediction.layout
    if pathname == '/guidelines':
        return guidelines.layout
    else:
        return home.layout


if __name__ == '__main__':
    app.run_server(debug=True)