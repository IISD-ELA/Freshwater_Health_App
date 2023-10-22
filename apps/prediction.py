# ML Prediction Model page

from dash import html
from dash import dcc
from dash.dependencies import Input, Output

layout = html.Div([
    # Form Heading
    html.Div([
        html.H1("Freshwater Prediction Page"),

        dcc.Link('Back Home', href='/home', className='btn secondary'),
        dcc.Link('View Dashboard', href='/dashboard', className='btn primary'),

    ], className="row"),

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
    ], className="row"),

#Form Row
    html.Div([
        #Prediction Form Area
        html.Div([
            html.Div([
                html.P("*** Prediction Form ***"),
            ], className="row"),
        ], className="container"),
        # Prediction Result Area
        html.Div([
            html.Div([
                html.P("*** Prediction Results ***"),
            ], className="row"),
        ], className="container"),
    ], className="row"),
], className="container")