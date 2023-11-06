# freshwater health assessment Exploratory Data Analysis Page
import pandas as pd
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objs as go_obj
import plotly.graph_objects as go
from visuals import charts
import numpy as np
from app import app

graph_style ={"flex":1, "min-width":700}

# Read csv and add new column Year from the ACTIVITY_START_DATE
df = pd.read_csv('./datasets/data.csv')
df['ACTIVITY_START_DATE'] = pd.to_datetime(df['ACTIVITY_START_DATE'])
df['Year'] = df['ACTIVITY_START_DATE'].dt.year
df['Month'] = df['ACTIVITY_START_DATE'].dt.month
df['Day'] = df['ACTIVITY_START_DATE'].dt.day



# filter based on treatment
fertilized = df[df['TREATMENT'] == 'fertilized']
non_fertilized = df[df['TREATMENT'] == 'none (reference/control)']


columns =[]
for column in df.columns[6:len(df.columns) -3]:
    columns.append(column)

unique_treatment = df.sort_values(by=['TREATMENT'], ascending=[True])['TREATMENT'].unique()
unique_site = df.sort_values(by=['SITE'], ascending=[True])['SITE'].unique()
unique_media_name = df.sort_values(by=['ACTIVITY_MEDIA_NAME'], ascending=[True])['ACTIVITY_MEDIA_NAME'].unique()

year = df.sort_values(by=['Year'], ascending=[True])['Year'].unique()
month = df.sort_values(by=['Month'], ascending=[True])['Month'].unique()
first = str(year[0]) + "-" + str(year[len(year)-1])
years = []
years.append(first)
for x in year:
    years.append(x)

months =[]
months.append('All Months')
for x in month:
    months.append(x)


treatments =[]
treatments.append('All Record')
for x in unique_treatment:
    treatments.append(x)

sites =[]
sites.append('All Sites')
for x in unique_site:
    sites.append(x)

media_names =[]
media_names.append('All Sources')
for x in unique_media_name:
    media_names.append(x)




site_chem = np.array(non_fertilized['ACTIVITY_MEDIA_NAME'].value_counts(dropna=True))
# site = non_fertilized.sort_values(by=['SITE'], ascending=[True])['SITE'].unique()
site = np.array(non_fertilized['ACTIVITY_MEDIA_NAME'].unique())


dataF = df[df['Year'] >= 2015]
chemValue1 = 'PH'
chemValue2 = 'ALK'
bin=10

# Dashboard layout starts here

layout = html.Div([
    # row 1
    html.Div([
        html.Div([
            html.P("Freshwater Health Assessment Dashboard", className="heading"),
            ], className="col-md-12 flex-display")
    ],className="row", style={'margin-top': '10px'}),
    #row2
    html.Div([
        html.Div([
            html.P("Exploratory Data Analysis", className="heading2")
        ], className="col-md-9"),
        html.Div([
                dcc.Link('Back Home', href='/home', className='sBtn topNav'),
                dcc.Link('Guidelines', href='/guidelines', className='sBtn topNav'),
                dcc.Link('Prediction', href='/prediction', className='sBtn topNav')
        ], className="col-md-3 topNavCol flex-display"),
], className="row flex-display"),
    #row 2
    html.Div([
        #container Column
        html.Div([
            dbc.Label("Data Source:", style={'width': '12%'}),
            dbc.Input(placeholder="select CSV [ * This module is not functional yet its just a proof of concept ]",
                      style={'font-size': '16px'}),
            dbc.Button("Load CSV", style={'margin-left': '10px'})
        ], className="col-md-9 flex-display" ),

    ], className="row loadcsv"),

    #row 4
    html.Div([
html.Div([
        #box 1
            html.Div([
              # html.P("Chart Title 1"),
                html.Div([
                        dcc.Dropdown(id='treatment_type1',
                          options=['Fertilized', 'Non-Fertilized'],
                          value='Non-Fertilized', clearable=False
                          ),
                ], style={'width':'100%', 'height': '100%'}),
                html.Span("", style={'height': '15px'}),
                dcc.Graph(id="graph1",  responsive=True, style={'width':'100%','height': '350px'}),
            ], className="card_container flex-display topChart", style={}),
        ], className="col-md-4"),

        html.Div([
        #box 1
            html.Div([
              # html.P("Chart Title 1"),
                html.Div([
                        dcc.Dropdown(id='treatment_type2',
                          options=['Fertilized', 'Non-Fertilized'],
                          value='Non-Fertilized', clearable=False
                          ),
                ], style={'width':'100%'}),
                html.Span("", style={'height': '15px'}),
                dcc.Graph(id="graph2",  responsive=True, style={'width':'100%', 'height': '350px'} ),
            ], className="card_container flex-display topChart", style={}),
        ], className="col-md-4"),
        html.Div([
        #box 1
            html.Div([

                html.Div([
                    dcc.Dropdown(id='chemical_type3',
                      options=columns,
                      value=columns[0], clearable=False
                      ),
                 ], style={'width':'100%'}),
                html.Span("", style={'height': '5px'}),
                html.P("FOR NON FERTILIZED"),
                html.Span("", style={'height': '5px'}),
                dcc.Graph(id="graph3",  responsive=True,
                          style={'width':'100%', 'height': '330px'}),
            ], className="card_container flex-display topChart", style={}),
        ], className="col-md-4"),

    ], className="row"),

    #row 5
    html.Div([
        html.Div([
            #box 1
            html.Div([
               #html.P("Chart Title 5"),

                html.Div([
                    html.Div([
                        html.Div([
                            dcc.Dropdown(
                                id='treatment_type_5',
                                options=['Fertilized', 'Non-Fertilized'],
                                value='Non-Fertilized', clearable=False
                            )
                        ], className="col-md-4"),
                        html.Div([
                            dcc.Dropdown(
                                id='year_5',
                                options=years,
                                value=years[0], clearable=False
                            )
                        ], className="col-md-4"),
                        html.Div([
                            dcc.Dropdown(
                                id='month_5',
                                options=months,
                                value=months[0], clearable=False
                            )
                        ], className="col-md-4")
                    ], className="row"),
                ], className="container-fluid"),

                html.Span("", style={'height': '10px'}),


                html.Div([
                    html.Div([
                        html.Div([
                            dcc.Dropdown(
                                id='chem_5_1',
                                options=columns,
                                value=columns[0], clearable=False
                            )
                        ],className="col-md-4"),
                        html.Div([
                            dcc.Dropdown(
                                id='chem_5_2',
                                options=columns,
                                value=columns[1], clearable=False
                            )
                        ], className="col-md-4"),
                        html.Div([
                            dcc.Dropdown(
                                id='chem_5_3',
                                options=columns,
                                value=columns[6], clearable=False
                            )
                        ], className="col-md-4")
                    ],className="row"),
                ], className="container-fluid"),
                html.Span("", style={'height': '15px'}),
                dcc.Graph(id="graph5", responsive=True, style={'width': '100%', 'height': '450px'}),
            ], className="card_container flex-display full-length",
                style={'background-color': 'white'}),
        ], className="col-md-8"),

        html.Div([
            # box 2
            html.Div([

                html.Div([
                    dcc.Dropdown(id='chemical_type6',
                      options=columns,
                      value=columns[0], clearable=False
                      ),
                 ], style={'width':'100%'}),
                html.Span("", style={'height': '15px'}),
                html.P("FOR FERTILIZED"),
                html.Span("", style={'height': '10px'}),
                dcc.Graph(id="graph6",  responsive=True, style={'width':'100%'})
            ], className="card_container flex-display topChart", style={}),

        ], className="col-md-4"),
    ], className="row"),

    # row 5
    html.Div([


        html.Div([
            # box 2
            html.Div([

                html.Div([
                    html.Div([
                        html.Div([
                            dcc.Dropdown(
                                id='category_7',
                                options=['TREATMENT', 'SITE','ACTIVITY_MEDIA_NAME'],
                                value='TREATMENT', clearable=False
                            )
                        ], className="col-md-4"),
                        html.Div([
                            dcc.Dropdown(
                                id='chem_7_2',
                                options=columns,
                                value=columns[0], clearable=False
                            )
                        ], className="col-md-4"),
                        html.Div([
                            dcc.Dropdown(
                                id='chem_7_3',
                                options=columns,
                                value=columns[1], clearable=False
                            )
                        ], className="col-md-4")
                    ], className="row"),
                ], className="container-fluid"),
                html.Span("", style={'height': '15px'}),

                dcc.Graph(id="graph7", responsive=True, style={'width':'100%', 'height': '450px'})
            ], className="card_container", style={'backgroundColor': '#ffffff'}),

        ], className="col-md-12"),
        html.Div([
            # box 2
            html.Div([

                html.Div([
                    html.Div([
                        html.Div([
                            dcc.Dropdown(
                                id='treatments_8',
                                options=treatments,
                                value=treatments[0], clearable=False
                            )
                        ], className="col-md-4"),
                        html.Div([
                            dcc.Dropdown(
                                id='sites_8',
                                options=sites,
                                value=sites[0], clearable=False
                            )
                        ], className="col-md-2"),
                        html.Div([
                            dcc.Dropdown(
                                id='media_names_8',
                                options=media_names,
                                value=media_names[0], clearable=False
                            )
                        ], className="col-md-4"),
                        html.Div([
                            dcc.Dropdown(
                                id='chem_8',
                                options=columns,
                                value=columns[0], clearable=False
                            )
                        ], className="col-md-2")
                    ], className="row"),
                ], className="container-fluid"),
                html.Span("", style={'height': '15px'}),

                dcc.Graph(id="graph8", responsive=True, style={'width': '100%', 'height': '450px'} ),
            ], className="card_container", style={'backgroundColor': '#ffffff'}),

        ], className="col-md-12"),
        # html.Div([
        #     # box 1
        #     html.Div([
        #         dcc.Graph(id="graph8_1",  responsive=True, style={'width':'100%'},
        #                   figure=charts.createGoViolinPlot()),
        #     ], className="card_container", style={'backgroundColor': '#ffffff'}),
        # ], className="col-md-6"),
        # html.Div([
        #     # box 1
        #     html.Div([
        #         dcc.Graph(id="graph9",  responsive=True, style={'width':'100%'},  figure=charts.createGoViolinPlot()),
        #     ], className="card_container", style={'backgroundColor': '#ffffff'}),
        # ], className="col-md-6"),
    ], className="row"),


    # html.Div([
    #     html.Div([
    #         # box 2
    #         html.Div([
    #             html.Div([
    #                 html.Div([
    #                     html.P("*** Advance Exploratory Analysis ***"),
    #                     html.Div(id='advAnalysisBtn', children='Generate Analysis', className='sBtn primaryBtn',
    #                          style={'margin-left': '30px'})
    #                 ], className="col-md-12 flex-display", style={'justify-content': 'space-between'}),
    #
    #             ], className="row "),
    #
    #              #Advance chart
    #                 #chats here
    #
    #                 # row 5
    #                 html.Div([
    #                     html.Div([
    #                         # box 1
    #                         html.Div([
    #                             #html.P("Chart Title 10"),
    #                             dcc.Graph(id="graph10", style={'width':'100%'}, figure=fig2),
    #                         ], className="card_container", style={'backgroundColor': '#ffffff'}),
    #                     ], className="col-md-6", ),
    #
    #                     html.Div([
    #                         # box 2
    #                         html.Div([
    #                             html.P("Chart Title 11"),
    #                             dcc.Graph(id="graph11", style={'width':'100%'}, figure=charts.createGoBoxPlot()),
    #                         ], className="card_container", style={'backgroundColor': '#ffffff'}),
    #
    #                     ], className="col-md-6"),
    #                 ], className="row"),
    #
    #                 #row 2 advance char
    #                 html.Div([
    #                     html.Div([
    #                         # box 2
    #                         html.Div([
    #                             html.P("Chart Title 12"),
    #                             dcc.Graph(id="graph12", style={'width':'100%'}, figure=fig3),
    #                         ], className="card_container", style={'align-items': 'center', 'justify-content': 'center', 'background-color': 'white'}),
    #
    #                     ], className="col-md-12"),
    #
    #
    #                 ], className="row")
    #
    #
    #         ], className="card_container"),
    #
    #     ], className="col-md-12", style={'margin-top': '20px'}),
    #
    #
    #
    # ], className="row"),

], className="dashboardPage")



# Callback for Chart 1
@app.callback(
     Output("graph1","figure"),
     Input("treatment_type1", "value")
 )
def generate_chart_1(values):
    #print('callback fired')
    #print(values)
    research_count=[]
    water_type = []
    if values == 'Non-Fertilized':
        research_count = np.array(non_fertilized['ACTIVITY_MEDIA_NAME'].value_counts())
        water_type = np.array(non_fertilized['ACTIVITY_MEDIA_NAME'].unique())
    elif values == 'Fertilized':
        research_count = np.array(fertilized['ACTIVITY_MEDIA_NAME'].value_counts())
        water_type = np.array(fertilized['ACTIVITY_MEDIA_NAME'].unique())

    fig1 = charts.createGoPieChart(values=research_count, labels=water_type,
                                  title="Results For " + values + " Water", colors=[],
                                  pull=[0.2, 0, 0.0, 0])
    #fig.show()
    return fig1


# Callback for chart_2
@app.callback(
     Output("graph2","figure"),
     Input("treatment_type2", "value")
 )
def generate_chart_2(values):
    # #print('callback2 fired')
    site_chem = np.array(non_fertilized['SITE'].value_counts(dropna=True))
    # site = non_fertilized.sort_values(by=['SITE'], ascending=[True])['SITE'].unique()
    site = np.array(non_fertilized['SITE'].unique())

    if values == 'Non-Fertilized':
        site_chem = np.array(non_fertilized['SITE'].value_counts(dropna=True))
        site = np.array(non_fertilized.sort_values(by=['SITE'], ascending=[True])['SITE'].unique())
    elif values == 'Fertilized':
        site_chem = np.array(fertilized['SITE'].value_counts(dropna=True))
        site = np.array(fertilized.sort_values(by=['SITE'], ascending=[True])['SITE'].unique())

    fig2 = charts.createGoPieChart(values=site_chem, labels=site,
                                   title="Total " + values + " values by SITE",
                                   colors=['gold', 'mediumturquoise', 'darkorange',
                                           'lightgreen', 'blue'])

    return fig2


# Callback for Chart 3
@app.callback(
     Output("graph3","figure"),
     Input("chemical_type3", "value")
 )
def generate_chart_3(values):
    # average Chemical value by year
    year = np.array(non_fertilized['Year'].unique())
    avg_chem = np.array(non_fertilized.groupby('Year')[values].mean())

    fig3 = charts.createGoHistogramChart(year=year, chem=avg_chem,
                                           title="Average Result for " + values + " By Year",
                                           height=300)
    #fig.show()
    return fig3



# Callback for Chart 6
@app.callback(
     Output("graph6","figure"),
     Input("chemical_type6", "value")
 )
def generate_chart_6(values):
    # average Chemical value by year
    year = np.array(fertilized['Year'].unique())
    avg_chem = np.array(fertilized.groupby('Year')[values].mean())

    fig6 = charts.createGoHistogramChart(year=year, chem=avg_chem,
                                           title="Average Result for " + values + " By Year",
                                           height=300)
    return fig6




# Line chart callback
@app.callback(
    Output("graph5", 'figure'),
    Input("treatment_type_5",'value'),
    Input("year_5",'value'),
    Input("month_5", "value"),
    Input("chem_5_1", "value"),
    Input("chem_5_2", "value"),
    Input("chem_5_3", "value")
)
def create_scatter(treatment_type, year, month, chem1, chem2, chem3):
    table = df
    mean_values = []
    view='Year'
    aggregate = True

    if treatment_type == 'Non-Fertilized':
        table = non_fertilized
    elif treatment_type == 'Fertilized':
        table= fertilized

    if not year == first:
        table = table[table['Year'] == year]
        view='Month'
        if not month == 'All Months':
            table = table[table['Month'] == month]
            view='Day'
            aggregate = False

    if aggregate:
        mean_values = table.groupby(['Year', 'Month'])[['Year', 'Month', chem1, chem2, chem3]].mean()
    else:
        mean_values = table[['Year', 'Month', 'Day', chem1, chem2, chem3]]

    title= "Results for 3 " + treatment_type + "Water Compositions Seen over " + str(year)
    y1 = np.array(mean_values[chem1])
    y2 = np.array(mean_values[chem2])
    y3 = np.array(mean_values[chem3])

    x = np.array(mean_values[view])

    figure = charts.createGOScatterPlot(x, y1, y2, y3, name1=chem1, name2=chem2, name3=chem3, title=title)
    return figure


# Callback for Chart 7
@app.callback(
     Output("graph7","figure"),
     Input("category_7", "value"),
     Input("chem_7_2", "value"),
     Input("chem_7_3", "value"),
 )
def generate_chart_7(category, chem1, chem2):
    # average Chemical value by year

    fig7 = charts.createPxScatterPlot(dataFrame=dataF,
                                      x=chem1,
                                      y=chem2,
                                      color=category,
                                      title=chem1 + " and " + chem2 + " RESULTS FOR " + category)

    return fig7




# Callback for Chart 8
@app.callback(
     Output("graph8","figure"),
     Input("treatments_8", "value"),
     Input("sites_8", "value"),
     Input("media_names_8", "value"),
     Input("chem_8", "value"),
 )
def generate_chart_8(treatment, site, media_name, chem):
    data_f = pd.DataFrame(dataF)
    if not treatment == "All Record":
        data_f = data_f[data_f['TREATMENT'] == treatment]

    if not site == "All Sites":
        data_f = data_f[data_f['SITE'] == site]

    if not media_name == "All Sources":
        data_f = data_f[data_f['ACTIVITY_MEDIA_NAME'] == media_name]


    x = np.array(data_f['ACTIVITY_START_DATE'])
    chemical = np.array(data_f[chem])
        # title=chem1 + " and " + chem2 + " RESULTS FOR " + category)

    #fig8 = charts.createPxLinePlot(dataFrame=data_f, x='ACTIVITY_START_DATE', y=chem)

    # fig8 = charts.createPxScatterPlot(dataFrame=data_f,
    #                                   x='ALK', y=chem,
    #                                color='ACTIVITY_START_DATE', title="Chat"
    #                                    )
    fig8 = charts.createGOLinePlot(x=x, y=chemical, name=chem)

    return fig8


