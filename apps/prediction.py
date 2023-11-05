# ML Prediction Model page
import dash
import pandas as pd
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import pickle


from app import app

with open('./mLModels/model_2.pkl', 'rb') as file:
    model = pickle.load(file)
# to use the model

def convert_to_dataset(input):
    data = {
        'CHLA': input['chla'],
        'ALK': input['alk'],
        'TDP': input['tdp'],
        'TDN': input['tdn'],
        'K': input['k'],
        'MG': input['mg'],
        'SRSI': input['srsi'],
        'MN': input['mn'],
        'CL': input['cl'],
        'FE': input['fe'],
        'SO4': input['so_4'],
        'DOC': input['doc'],
        'NO3': input['no_3'],
        'PARTN': input['partn'],
        'NA': input['na'],
        'COND': input['cond'],
        'NH3': input['nh_3'],
        'DIC': input['dic'],
        'PARTP': input['partp'],
        'PH': input['ph'],
        'CA': input['ca'],
        'NO2': input['no_2'],
        'PARTC': input['partc'],
        'SECCHI_DEPTHS': input['secchi_depths'],
        'MEAN_DAILY_DISCHARGE': input['mean_daily_discharge']
    }
    single_data = pd.DataFrame(data, index=[0])
    return single_data



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

html.Div([
            html.Div([
                html.P("*** Prediction Results ***"),
                html.Div([
                    html.H2(id="result", children="Very Good")
                ]),
                html.Div([
                    html.P(children="", id="error_text", style={'color':'#ff0000','font-size':'16px', 'font-weight':'300'})
                ]),
            ], className="card_container", style={'color':'white','text-align':'center'}),
        ], className="col-12"),
        #Prediction Form Area
        html.Div([
            html.Div([
                html.P("*** Prediction Form ***"),
                html.Div([

                    #row1
                    html.Div([
                        html.Div([
                            html.Div([
                                html.Label("Chlorophyll-a [ CHLA ] ")
                            ]),
                                html.Div([
                                dbc.Input("chla", placeholder="Enter value for CHLA in mg/L", type='number')
                            ])
                        ], className="col-3"),
                        html.Div([
                            html.Div([
                                html.Label("Alkalinity [ ALK ]")
                            ]),
                                html.Div([
                                dbc.Input("alk", placeholder="Enter value for ALK in ueq/L", type='number')
                            ])
                        ], className="col-3"),
                        html.Div([
                            html.Div([
                                html.Label("Total Phosphorus, mixed form) [ TDP ] ")
                            ]),
                                html.Div([
                                dbc.Input("tdp", placeholder="Enter value for TDP in ug/L", type='number')
                            ])
                        ], className="col-3"),
                        html.Div([
                            html.Div([
                                html.Label("Total Nitrogen, mixed form [ TDN ]")
                            ]),
                            html.Div([
                                dbc.Input("tdn", placeholder="Enter value for TDN in ug/L", type='number')
                            ])
                        ], className="col-3"),

                    ], className="row flex-display",style={'padding-top': '35px'}),

                    #row 2
                    html.Div([

                        html.Div([
                            html.Div([
                                html.Label("Potassium [ K ] ")
                            ]),
                            html.Div([
                                dbc.Input("k", placeholder="Enter value for K in mg/L", type='number')
                            ])
                        ], className="col-3"),
                        html.Div([
                            html.Div([
                                html.Label("Magnesium[ MG ] ")
                            ]),
                            html.Div([
                                dbc.Input("mg", placeholder="Enter value for MG in mg/L", type='number')
                            ])
                        ], className="col-3"),


                        html.Div([
                            html.Div([
                                html.Label("Silica, reactive [ SRSI ]")
                            ]),
                            html.Div([
                                dbc.Input("srsi", placeholder="Enter value for SRSI in mg/L", type='number')
                            ])
                        ], className="col-3"),
                        html.Div([
                            html.Div([
                                html.Label("Manganese [ MN ] ")
                            ]),
                            html.Div([
                                dbc.Input("mn", placeholder="Enter value for MN in mg/L", type='number')
                            ])
                        ], className="col-3")
], className="row flex-display",style={'padding-top': '50px'}),

#row 3
                    html.Div([
                        html.Div([
                            html.Div([
                                html.Label("Chloride [ CL ]  1")
                            ]),
                            html.Div([
                                dbc.Input("cl", placeholder="Enter value for CL in mg/L", type='number')
                            ])
                        ], className="col-3"),


                        html.Div([
                            html.Div([
                                html.Label("[ FE ] Iron")
                            ]),
                            html.Div([
                                dbc.Input("fe", placeholder="Enter value for FE in mg/L", type='number')
                            ])
                        ], className="col-3"),
                        html.Div([
                            html.Div([
                                html.Label("Sulfate [ SO4 ]")
                            ]),
                            html.Div([
                                dbc.Input("so_4", placeholder="Enter value for SO4 in mg/L", type='number')
                            ])
                        ], className="col-3"),
                        html.Div([
                            html.Div([
                                html.Label("Organic Carbon [ DOC ]")
                            ]),
                            html.Div([
                                dbc.Input("doc", placeholder="Enter value for DOC in umol/L", type='number')
                            ])
                        ], className="col-3", )

                    ], className="row flex-display",style={'padding-top': '50px'}),

                    # row 4
                    html.Div([

                        html.Div([
                            html.Div([
                                html.Label("Nitrate [ NO3 ]")
                            ]),
                            html.Div([
                                dbc.Input("no_3", placeholder="Enter value for NO3 in ug/L", type='number')
                            ])
                        ], className="col-3"),

                        html.Div([
                            html.Div([
                                html.Label("Nitrogen [ PARTN ]")
                            ]),
                            html.Div([
                                dbc.Input("partn", placeholder="Enter value for PARTN in ug/L", type='number')
                            ])
                        ], className="col-3"),
                        html.Div([
                            html.Div([
                                html.Label("Sodium [ NA ]")
                            ]),
                            html.Div([
                                dbc.Input("na", placeholder="Enter value for NA in ug/L", type='number')
                            ])
                        ], className="col-3", ),
                        html.Div([
                            html.Div([
                                html.Label("Conductivity [ COND ]")
                            ]),
                            html.Div([
                                dbc.Input("cond", placeholder="Enter value for COND in uS/cm", type='number')
                            ])
                        ], className="col-3", )
                    ], className="row flex-display", style={'padding-top': '50px'}),

                    # row 5
                    html.Div([
                        html.Div([
                            html.Div([
                                html.Label("Ammonia [ NH3 ]")
                            ]),
                            html.Div([
                                dbc.Input("nh_3", placeholder="Enter value for NH3 in ug/L", type='number')
                            ])
                        ], className="col-3", ),


                        html.Div([
                            html.Div([
                                html.Label("Inorganic Carbon [ DIC ]")
                            ]),
                            html.Div([
                                dbc.Input("dic", placeholder="Enter value for DIC in umol/L", type='number')
                            ])
                        ], className="col-3"),
                        html.Div([
                            html.Div([
                                html.Label("Phosphorus [ PARTP ]")
                            ]),
                            html.Div([
                                dbc.Input("partp", placeholder="Enter value for PARTP in ug/L", type='number')
                            ])
                        ], className="col-3", ),
                        html.Div([
                            html.Div([
                                html.Label("pH [ PH ]")
                            ]),
                            html.Div([
                                dbc.Input("ph", placeholder="Enter value for PH in SU", type='number')
                            ])
                        ], className="col-3", ),
                    ], className="row flex-display", style={'padding-top': '50px'}),

                    # row 6
                    html.Div([
                        html.Div([
                            html.Div([
                                html.Label("Calcium [ CA ]")
                            ]),
                            html.Div([
                                dbc.Input("ca", placeholder="Enter value for CA in mg/L", type='number')
                            ])
                        ], className="col-3", ),


                        html.Div([
                            html.Div([
                                html.Label("Nitrite [ NO2 ]")
                            ]),
                            html.Div([
                                dbc.Input("no_2", placeholder="Enter value for NO2 in ug/L", type='number')
                            ])
                        ], className="col-3"),
                        html.Div([
                            html.Div([
                                html.Label("Carbon [ PARTC ]")
                            ]),
                            html.Div([
                                dbc.Input("partc", placeholder="Enter value for PARTC in ug/L", type='number')
                            ])
                        ], className="col-3", ),
html.Div([
                            html.Div([
                                html.Label("Luminology [ SECCHI_DEPTHS ]")
                            ]),
                            html.Div([
                                dbc.Input("secchi_depths", placeholder="Enter value for SECCHI_DEPTHS in meters ", type='number')
                            ])
                        ], className="col-3", )
                        ], className="row flex-display", style={'padding-top': '50px'}),

                    # row 7
                    html.Div([


                        html.Div([
                            html.Div([
                                html.Label("Hydrology [ MEAN_DAILY_DISCHARGE ]")
                            ]),
                            html.Div([
                                dbc.Input("mean_daily_discharge", placeholder="Enter value for MEAN_DAILY_DISCHARGE in m**3/s", type='number')
                            ])
                        ], className="col-3", ),

                    ], className="row flex-display", style={'padding-top': '25px'}),

html.Div([
                html.P("*** Prediction Results ***"),
                html.Div([
                    html.H2(id="result2", children="Very Good")
                ]),
                html.Div([
                    html.P(children="", id="error_text2", style={'color':'#ff0000','font-size':'16px', 'font-weight':'300'})
                ]),
            ], className="card_container", style={'color':'white','text-align':'center'}),


                    #form buttons
                    html.Div([
                        html.Div([
                            html.Button(id='clearBtn', children='Clear Form', className='sbtn secondaryBtn',
                                     style={'margin-left': '10px'}, n_clicks=0),

                            html.Button(id='predictBtn', children='Predict', className='sbtn primaryBtn',
                                     style={'margin-left': '30px'}, n_clicks=0)
                        ], className="col-12 flex-display",
                            style={'margin-top': '30px', 'margin-bottom': '30px', 'align-items': 'center',
                                   'justify-content': 'center'})

                    ], className="row")
                ], className="container-fluid", style={'width': '100%'}),

            ], className="card_container"),
        ], className="col-12"),
        # Prediction Result Area

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





# Callback for Form
@app.callback(
    Output("result", "children"),
    Output("error_text", "children"),
    Output("result2", "children"),
    Output("error_text2", "children"),
    Output("chla", "value"),
    Output("alk", "value"),
    Output("tdp", "value"),
    Output("tdn", "value"),
    Output("k", "value"),
    Output("mg", "value"),
    Output("srsi", "value"),
    Output("mn", "value"),
    Output("cl", "value"),
    Output("fe", "value"),
    Output("so_4", "value"),
    Output("doc", "value"),
    Output("no_3", "value"),
    Output("partn", "value"),
    Output("na", "value"),
    Output("cond", "value"),
    Output("nh_3", "value"),
    Output("dic", "value"),
    Output("partp", "value"),
    Output("ph", "value"),
    Output("ca", "value"),
    Output("no_2", "value"),
    Output("partc", "value"),
    Output("secchi_depths", "value"),
    Output("mean_daily_discharge", "value"),
    Input("predictBtn", "n_clicks"),
    Input("clearBtn", "n_clicks"),
    Input("chla", "value"),
    Input("alk", "value"),
    Input("tdp", "value"),
    Input("tdn", "value"),
    Input("k", "value"),
    Input("mg", "value"),
    Input("srsi", "value"),
    Input("mn", "value"),
    Input("cl", "value"),
    Input("fe", "value"),
    Input("so_4", "value"),
    Input("doc", "value"),
    Input("no_3", "value"),
    Input("partn", "value"),
    Input("na", "value"),
    Input("cond", "value"),
    Input("nh_3", "value"),
    Input("dic", "value"),
    Input("partp", "value"),
    Input("ph", "value"),
    Input("ca", "value"),
    Input("no_2", "value"),
    Input("partc", "value"),
    Input("secchi_depths", "value"),
    Input("mean_daily_discharge", "value")

)
def process_prediction(pred_n_clicks, clear_n_clicks, *input_values):
    ctx = dash.callback_context
    input_names =[]
    result_description ={
        4: 'Very Healthy',
        2: 'Healthy',
        0: 'Somewhat healthy',
        3: 'Not Quite Healthy',
        1: 'Something is not right Based on the Data'
    }


    button_id = ctx.triggered_id
    result = ""
    error = ""

    if button_id == "predictBtn" and pred_n_clicks>0:
        # Read the inputs
        for r in ctx.inputs_list:
            input_names.append(str(r['id']))
        input_names.remove('predictBtn')
        input_names.remove('clearBtn')
        input_dict = dict(zip(input_names, input_values))
        # Perform validation
        for chem,value in input_dict.items():
            error += " ***** Enter a value for " + str(chem).upper() if value is None else ""

        # check if all validation passed
        if error == "":
            # print('validation passed')
            # call prediction
            dataset = convert_to_dataset(input_dict)
            # print(dataset)
            result = model.predict(dataset)
            print(result)
            if 0 <= result <= 4:
                result = result_description[result[0]]
            #print(result[0])
    elif button_id == "clearBtn" and clear_n_clicks>0:
        #print("clear form fired")
        return "", "","","", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""

    return result, error, result, error, *input_values



