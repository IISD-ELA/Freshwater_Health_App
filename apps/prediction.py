# ML Prediction Model page

from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pickle

#pickled_model = pickle.load(open('../mLModels/model.pkl', 'rb'))
# to use the model

#pickled_model.predict(X_test)


layout = html.Div([
    # row 1
    html.Div([
        html.Div([
            html.P("Freshwater Health Assessment ", className="heading"),
        ], className="col-12 flex-display")
    ], className="row", style={'margin-top': '10px'}),
    # row2
    html.Div([
        html.Div([
            html.P("Freshwater Prediction Model", className="heading2")
        ], className="col-9"),
        html.Div([
            dcc.Link('Back Home', href='/home', className='sBtn topNav'),
            dcc.Link('Guidelines', href='/guidelines', className='sBtn topNav'),
            dcc.Link('Dashboard', href='/dashboard', className='sBtn topNav')
        ], className="col-3 topNavCol flex-display"),
    ], className="row flex-display"),

# Form Guidelines
    html.Div([
        html.Div([
            html.H5("*** Guidelines ***"),
            html.P("In using our machine learning prediction form, it's essential to provide "
                   "accurate and complete data relevant to the prediction task. Please ensure "
                   "that all information is up-to-date and devoid of errors. "
                   "Follow the instructions carefully when inputting data, providing specific "
                   "details where required. The form is designed to make predictions based on "
                   "the provided information, so accuracy in data entry significantly impacts the results. ")
        ], className="container")
    ], className="row", style={'margin': '20px 22px 10px 22px', 'border': '1px solid white', 'border-radius': '5px', 'padding': '15px'}),

#Form Row
    html.Div([
        #Prediction Form Area
        html.Div([
            html.Div([
                html.P("*** Prediction Form ***"),
                html.Div([

                    #row1
                    html.Div([
                        html.Div([
                            html.Div([
                                html.Label("Variable 1")
                            ]),
                                html.Div([
                                dbc.Input("Variable 1", placeholder="Enter Variable 1", type='text')
                            ])
                        ], className="col-4"),
                        html.Div([
                            html.Div([
                                html.Label("Variable 1")
                            ]),
                                html.Div([
                                dbc.Input("Variable 1", placeholder="Enter Variable 1", type='text')
                            ])
                        ], className="col-4"),
                        html.Div([
                            html.Div([
                                html.Label("Variable 1")
                            ]),
                                html.Div([
                                dbc.Input("Variable 1", placeholder="Enter Variable 1", type='text')
                            ])
                        ], className="col-4")

                    ], className="row flex-display",style={'padding-top': '25px'}),

                    #row 2
                    html.Div([
                        html.Div([
                            html.Div([
                                html.Label("Variable 1")
                            ]),
                            html.Div([
                                dbc.Input("Variable 1", placeholder="Enter Variable 1", type='text')
                            ])
                        ], className="col-4"),
                        html.Div([
                            html.Div([
                                html.Label("Variable 1")
                            ]),
                            html.Div([
                                dbc.Input("Variable 1", placeholder="Enter Variable 1", type='text')
                            ])
                        ], className="col-4"),
                        html.Div([
                            html.Div([
                                html.Label("Variable 1")
                            ]),
                            html.Div([
                                dbc.Input("Variable 1", placeholder="Enter Variable 1", type='text')
                            ])
                        ], className="col-4")

                    ], className="row flex-display",style={'padding-top': '25px'}),

#row 3
                    html.Div([
                        html.Div([
                            html.Div([
                                html.Label("Variable 1")
                            ]),
                            html.Div([
                                dbc.Input("Variable 1", placeholder="Enter Variable 1", type='text')
                            ])
                        ], className="col-4"),
                        html.Div([
                            html.Div([
                                html.Label("Variable 1")
                            ]),
                            html.Div([
                                dbc.Input("Variable 1", placeholder="Enter Variable 1", type='text')
                            ])
                        ], className="col-4"),
                        html.Div([
                            html.Div([
                                html.Label("Variable 1")
                            ]),
                            html.Div([
                                dbc.Input("Variable 1", placeholder="Enter Variable 1", type='text')
                            ])
                        ], className="col-4")

                    ], className="row flex-display", style={'padding-top': '25px'}),

                    #row 4
                    html.Div([
                        html.Div([
                            html.Div([
                                html.Label("Variable 1")
                            ]),
                            html.Div([
                                dbc.Input("Variable 1", placeholder="Enter Variable 1", type='text')
                            ])
                        ], className="col-4"),
                        html.Div([
                            html.Div([
                                html.Label("Variable 1")
                            ]),
                            html.Div([
                                dbc.Input("Variable 1", placeholder="Enter Variable 1", type='text')
                            ])
                        ], className="col-4"),
                        html.Div([
                            html.Div([
                                html.Label("Variable 1")
                            ]),
                            html.Div([
                                dbc.Input("Variable 1", placeholder="Enter Variable 1", type='text')
                            ])
                        ], className="col-4", )

                    ], className="row flex-display",style={'padding-top': '25px'}),

                    #form buttons
                    html.Div([
                        html.Div([
                            html.Div(id='clearBtn', children='Clear Form', className='sBtn secondaryBtn',
                                     style={'margin-left': '10px'}),

                            html.Div(id='predictBtn', children='Predict', className='sBtn primaryBtn',
                                     style={'margin-left': '30px'})
                        ], className="col-12 flex-display",
                            style={'margin-top': '30px', 'margin-bottom': '30px', 'align-items': 'center',
                                   'justify-content': 'center'})

                    ], className="row")
                ], className="container", style={'width': '100%'}),

            ], className="card_container"),
        ], className="col-8"),
        # Prediction Result Area
        html.Div([
            html.Div([
                html.P("*** Prediction Results ***"),
            ], className="card_container"),
        ], className="col-4"),
    ], className="row "),
    #bottom Info center
    html.Div([
        html.Div([
            html.Div([
                html.P("*** Details on the Variables/ Outcomes ***"),
            ], className="card_container"),
        ], className="col-12")
    ], className="row")
], className="dashboardPage")