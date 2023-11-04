# home page - Landing Page implementation here

from dash import dcc
from dash import html
from dash.dependencies import Input, Output


layout = html.Div([
    html.Div([
        html.Div([
            html.H1('Freshwater Health\n'
                    'Assessment Application ', style={'color': 'white'}),
            html.P('A freshwater health assessment application is a digital '
                   'tool designed to evaluate and monitor the overall health '
                   'and quality of freshwater ecosystems such as lakes, rivers, '
                   'and streams. This application utilizes various data sets, '
                   'in assessing water quality \n', className="hero-desc", style={'color': 'white'}),
            html.Span(['(Dataset Source: IISD-ELA, 2023)'],className="hero-desc"),
            html.Div([
                dcc.Link('View Dashboard', href='/dashboard', className='sBtn secondaryBtn', style={'margin-left': '10px'}),

                dcc.Link('Predict Now', href='/prediction', className='sBtn primaryBtn', style={'margin-left': '30px'})
            ], className="row", style={'margin-top': '30px'})
        ],className="col-6"),

        html.Div(className="col-6")
    ], className="row")
], className="container homePage")