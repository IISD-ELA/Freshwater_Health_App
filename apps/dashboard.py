# freshwater health assessment Exploratory Data Analysis Page

from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px


layout = html.Div([
    #row 1
    html.Div([
        html.Div([
            html.H1("Freshwater Health Assessment Dashboard"),
            dcc.Link('Back Home', href='/home', className='btn secondary'),
            dcc.Link('Prediction', href='/prediction', className='btn primary'),
            ], className="container")
    ],className="row"),

    #row 2
    html.Div([
        #box 1
        html.Div([
           html.P("Chart Title 1"),
        ], className="container"),
        #Box 2
        html.Div([
            html.P("Chart Title 2"),
        ], className="container"),
        #Box 3
        html.Div([
            html.P("Chart Title 3"),
        ], className="container"),
        #Box 4
        html.Div([
            html.P("Chart Title 4"),
        ], className="container"),
    ], className="row flex-display"),



], className="container")