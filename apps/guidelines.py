# ML Prediction Model page

import pandas as pd
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import csv
from tabulate import tabulate

guideline = pd.read_csv('./datasets/guidelines.csv')

heading = guideline.columns
rows = guideline.iterrows()


layout = html.Div([
    # row 1
    html.Div([
        html.Div([
            html.P("Freshwater Health Assessment ", className="heading"),
        ], className="col-md-12 flex-display")
    ], className="row", style={'margin-top': '10px'}),
    # row2
    html.Div([
        html.Div([
            html.P("Freshwater Assessment Guidelines ", className="heading2")
        ], className="col-md-9"),
        html.Div([
            dcc.Link('Back Home', href='/home', className='sBtn topNav'),
            dcc.Link('Dashboard', href='/dashboard', className='sBtn topNav'),
            dcc.Link('Prediction', href='/prediction', className='sBtn topNav')
        ], className="col-md-3 topNavCol flex-display"),
    ], className="row flex-display"),

# Form Guidelines
    html.Div([
        html.Div([
            html.H5("*** Guidelines ***"),
            html.P("Explanation and application of this guidelines given here... ")
        ], className="container")
    ], className="row", style={'margin': '20px 22px 10px 22px', 'border': '1px solid white',
                               'border-radius': '5px', 'padding': '15px'}),

#Form Row
    html.Div([
        # Prediction Form Area
        html.Div([
            html.Div([
                html.P("Freshwater Health Assessment Guidelines"),
                html.Div([

                    # row1
                    html.Div([
                        html.Div([
                            html.Table(
                                    # Header
                                    [html.Tr([html.Th(col) for col in guideline.columns])] +
                                    # Body
                                    [html.Tr([html.Td(guideline.iloc[i][col]) for col in guideline.columns]) for i in range(len(guideline))]
                                )


                            #print(to_html('./datasets/data.csv'))

                        ], className="col-md-12")
                    ], className="row flex-display",style={'padding-top': '25px'}),
                ], className="container-fluid", style={'width': '100%'}),

            ], className="card_container"),
        ], className="col-md-12"),
    ], className="row "),
], className="dashboardPage")