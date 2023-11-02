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


# Read csv and add new column Year from the ACTIVITY_START_DATE
df = pd.read_csv('./datasets/data.csv')
df['ACTIVITY_START_DATE'] = pd.to_datetime(df['ACTIVITY_START_DATE'])
df['Year'] = df['ACTIVITY_START_DATE'].dt.year

# filter based on treatment
fertilized = df[df['TREATMENT'] == 'fertilized']
non_fertilized = df[df['TREATMENT'] == 'none (reference/control)']


columns =[]
for column in df.columns[6:len(df.columns) -1]:
    columns.append(column)


non_fertilized_year = non_fertilized
y1 = non_fertilized_year['K']
y2 = non_fertilized_year['MG']
y3 = non_fertilized_year['CL']
x = non_fertilized_year['Year']


#average Chemical value by year
year = np.array(non_fertilized['Year'].unique())
avg_chem =  np.array(non_fertilized.groupby('Year')['PH'].mean())

#site = non_fertilized.sort_values(by=['SITE'], ascending=[True])['SITE'].unique()
site = non_fertilized['SITE']
site_chem =  np.array(non_fertilized['PH'].value_counts(dropna=True))



from app import app
df = px.data
#print(df)

fig1 = go.Figure(
    data = [go.Bar(x=[1,4,3,2,5,6,3,5,6,7], y=[3,5,6,7,6,8,1,5,6,8])],
    layout= go.Layout(
        title= {
            'text': "Histogram Distribution Plot",
            'x': 0.3,
            'y': 0.95,
            'xanchor': 'center',
            'yanchor': 'top'
            },
        titlefont={
            'color':'#54643e',
            'size': 18
        },
        legend = {
            'orientation': 'h',
            'bgcolor': '#54f43e',
            'xanchor': 'center', 'x': 0.5, 'y':-0.07
        },
        font= dict(
            family="sans-serif",
            size=12,
            color='white'
        ),
        height=350,
        width=525,
        plot_bgcolor="#FFFFFF",
        paper_bgcolor="#ffffff",
        hovermode="closest",
        margin=go.layout.Margin(l=15, r=15, b=15, t=15, pad=4),


    )
)



fig2 = go.Figure(
    data = [go.Histogram(x=site, y=site_chem)],
    layout= go.Layout(
        barmode='stack',
        title= {
            'text': "A sample go Plot",
            'x': 0.3,
            'y': 1,
            'xanchor': 'center',
            'yanchor': 'top'
            },
        titlefont={
            'color':'#ffffff',
            'size': 18
        },
        legend = {
            'orientation': 'h',
            'bgcolor': '#1f2c56',
            'xanchor': 'center', 'x': 0.5, 'y':-0.07
        },
        font= dict(
            family="sans-serif",
            size=12,
            color='white'
        ),
            height=350,
            width=325,
            plot_bgcolor="#1A2E62",
            paper_bgcolor="#1A2E62",
            hovermode="closest",
            margin=go.layout.Margin(l=15, r=15, b=15, t=15, pad=4),


    )

)


fig3 = go.Figure(
    data = [go.Scatter(
            x=df.tips().tail(300),  # x-coordinates of trace
            y=df.tips().head(300),  # y-coordinates of trace
            mode="markers +text ",  # scatter mode (more in UG section 1)
            text="scatter plot",
            opacity=1,
            textposition="top center",
            marker=dict(size=25, color='red', line=dict(width=0.5)),
            textfont=dict(
                color="black",
                size=18,  # can change the size of font here
                family="Times New Roman",
            ),
        )],
   layout = go.Layout(
    autosize=False,
    width=725,
    height=350,
    xaxis=go.layout.XAxis(linecolor="black", linewidth=1, mirror=True),
    yaxis=go.layout.YAxis(linecolor="black", linewidth=1, mirror=True),
    margin=go.layout.Margin(l=50, r=50, b=15, t=20, pad=4),
    #plot_bgcolor="#1A2E62",
    #paper_bgcolor="#1A2E62",
)
)






layout = html.Div([
    #row 1
    html.Div([
        html.Div([
            html.P("Freshwater Health Assessment Dashboard", className="heading"),
            ], className="col-12 flex-display")
    ],className="row", style={'margin-top': '10px'}),
    #row2
    html.Div([
        html.Div([
            html.P("Exploratory Data Analysis", className="heading2")
        ], className="col-9"),
        html.Div([
                dcc.Link('Back Home', href='/home', className='sBtn topNav'),
                dcc.Link('Prediction', href='/prediction', className='sBtn topNav')
        ], className="col-3 topNavCol flex-display"),
], className="row flex-display"),
    #row 2
    html.Div([
        #container Column
        html.Div([
            dbc.Label("Data Source:", style={'width': '12%'}),
            dbc.Input(placeholder="select CSV", ),
            dbc.Button("Load CSV", style={'margin-left': '10px'})
        ], className="col-9 flex-display" ),

    ], className="row", style={'margin': '20px 22px 10px 22px', 'border': '1px solid white',
                               'border-radius': '5px', 'padding': '15px'}),

    #row 4
    html.Div([
        html.Div([
        #box 1
            html.Div([
               # html.P("Chart Title 1"),
               #  html.P("Names: "),
               #  dcc.Dropdown(id='names',
               #               options=['smoker', 'day', 'time', 'sex'],
               #               value='day', clearable=False
               #               ),
                 html.Div([
                            dcc.Dropdown(id='treatment_type1',
                              options=['Fertilized', 'Non-Fertilized'],
                              value='Non-Fertilized', clearable=False
                              ),
                 ], style={'width':'100%'}),
                html.Span("", style={'height': '15px'}),
                dcc.Graph(id="graph1", )

            ], className="card_container flex-display", style={'align-items': 'center', 'justify-content': 'center',
                                                               'flex-direction': 'column'}),
        ], className="col-4"),
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
                dcc.Graph(id="graph2", figure=charts.createGoPieChart(values=site_chem, labels=site,
                                                                      title="Results By Site",
                                                                      colors=['gold', 'mediumturquoise', 'darkorange',
                                                                              'lightgreen','blue'])),
            ], className="card_container flex-display", style={'align-items': 'center', 'justify-content': 'center',
                                                               'flex-direction': 'column'}),
        ], className="col-4"),
        html.Div([
        #box 1
            html.Div([
               #html.P("Chart Title 1"),
                html.Div([
                    dcc.Dropdown(id='chemical_type3',
                      options=columns,
                      value=columns[0], clearable=False
                      ),
                 ], style={'width':'100%'}),
                html.Span("", style={'height': '15px'}),
                dcc.Graph(id="graph3", figure=charts.createGoHistogramChart(year=year, chem=avg_chem, title="Average Result By Year")),
            ], className="card_container flex-display", style={'align-items': 'center', 'justify-content': 'center',
                                                               'flex-direction': 'column'}),
        ], className="col-4"),

    ], className="row"),

    #row 5
    html.Div([
        html.Div([
            #box 1
            html.Div([
               #html.P("Chart Title 5"),
                dcc.Graph(id="graph5", figure=charts.createGOScatterPlot(x, y1,y2,y3)),
            ], className="card_container flex-display", style={'align-items': 'center', 'justify-content': 'center', 'background-color': 'white'}),
        ], className="col-8"),

        html.Div([
            # box 2
            html.Div([
                #html.P("Chart Title 6"),
                dcc.Graph(id="graph6", figure=fig2),
            ], className="card_container flex-display", style={'align-items': 'center', 'justify-content':'center'}),

        ], className="col-4"),
    ], className="row"),

    # row 5
    html.Div([
        html.Div([
            # box 1
            html.Div([
                dcc.Graph(id="graph7", figure=charts.createGoViolinPlot()),
            ], className="card_container", style={'backgroundColor': '#ffffff'}),
        ], className="col-6"),

        html.Div([
            # box 2
            html.Div([
                html.P("Chart Title 8"),
                dcc.Graph(id="graph8", figure=fig1),
            ], className="card_container", style={'backgroundColor': '#ffffff'}),

        ], className="col-6"),
    ], className="row"),


    html.Div([
        html.Div([
            # box 2
            html.Div([
                html.Div([
                    html.Div([
                        html.P("*** Advance Exploratory Analysis ***"),
                        html.Div(id='advAnalysisBtn', children='Generate Analysis', className='sBtn primaryBtn',
                             style={'margin-left': '30px'})
                    ], className="col-12 flex-display", style={'justify-content': 'space-between'}),

                ], className="row "),

                 #Advance chart
                    #chats here

                    # row 5
                    html.Div([
                        html.Div([
                            # box 1
                            html.Div([
                                #html.P("Chart Title 7"),
                                dcc.Graph(id="graph7", figure=charts.createGOLinePlot()),
                            ], className="card_container", style={'backgroundColor': '#ffffff'}),
                        ], className="col-6", ),

                        html.Div([
                            # box 2
                            html.Div([
                                html.P("Chart Title 8"),
                                dcc.Graph(id="graph8", figure=charts.createGoBoxPlot()),
                            ], className="card_container", style={'backgroundColor': '#ffffff'}),

                        ], className="col-6"),
                    ], className="row"),

                    #row 2 advance char
                    html.Div([
                        html.Div([
                            # box 2
                            html.Div([
                                html.P("Chart Title 8"),
                                dcc.Graph(id="graph8", figure=fig3),
                            ], className="card_container", style={'align-items': 'center', 'justify-content': 'center', 'background-color': 'white'}),

                        ], className="col-12"),


                    ], className="row")


            ], className="card_container"),

        ], className="col-12", style={'margin-top': '20px'}),



    ], className="row"),

], className="dashboardPage")


@app.callback(
     Output("graph1","figure"),
     Input("treatment_type1", "value")
 )
def generate_chart(values):
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

    fig = charts.createGoPieChart(values=research_count, labels=water_type,
                                  title="Results For " + values + " Water", colors=[], pull=[0.2, 0, 0.0, 0])
    #fig.show()
    return fig

