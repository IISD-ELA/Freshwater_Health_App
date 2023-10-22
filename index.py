from dash import  dcc
from dash import html
from dash.dependencies import Input, Output

# get dash app and server from app
from app import app
from app import server

# get web pages
from apps import home
from apps import dashboard
from apps import prediction

app.layout = html.Div([
    # access the browser url, this component has the pathname child
    dcc.Location(id='url', refresh=False),
    #some page links
    # html.Div([
    #     dcc.Link('Home', href='/home'),
    #     dcc.Link('Dashboard', href='/dashboard'),
    #     dcc.Link('Prediction', href='/prediction')
    # ], className="row"),
    #container where other pages will be rendered
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
    else:
        return home.layout

if __name__ == '__main__':
    app.run_server(debug=True)