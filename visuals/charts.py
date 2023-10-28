
import numpy as np
import plotly.express as px
import plotly.graph_objs as go_obj
import plotly.graph_objects as go







#********************************** Plotly GO Bar Plot **********************************#
def createGoBarChart(x_data,y_data, title, title_x_position, title_y_position, title_font_color, title_font_size,
                   legend_bg_color, legend_position, legend_x_axis, legend_y_axis, font_color, chart_height,
                   chart_width, plot_bg_color, paper_bg_color,
                   ml, mr, mb, mt, padding
                   ):
    fig = go.Figure(
        data=[go.Bar(x=x_data, y=y_data)],
        layout=go.Layout(
            title={
                'text': title,
                'x': title_x_position,
                'y': title_y_position,
                'xanchor': 'center',
                'yanchor': 'top'
            },
            titlefont={
                'color': title_font_color,
                'size': title_font_size
            },
            legend={
                'orientation': 'h',
                'bgcolor': legend_bg_color,
                'xanchor': legend_position, 'x': legend_x_axis, 'y': legend_y_axis
            },
            font=dict(
                family="sans-serif",
                size=12,
                color=font_color
            ),
            height=chart_height,
            width=chart_width ,
            plot_bgcolor=plot_bg_color,
            paper_bgcolor=paper_bg_color,
            hovermode="closest",
            margin=go.layout.Margin(l=ml, r=mr, b=mb, t=mt, pad=padding),

        )

    )
    return fig


#********************************** Plotly GO Pie Chart **********************************#
def createGoPieChart():
    labels = ['Oxygen', 'Hydrogen', 'Carbon_Dioxide', 'Nitrogen']
    values = [4500, 2500, 1053, 500]
    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen']

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0, pull=[0, 0, 0.2, 0])],
                    layout=go.Layout(
                        title= {
                            'text': "Histogram Distribution Plot",
                            'x': 0.5,
                            'y': 0.98,
                            'xanchor': 'center',
                            'yanchor': 'top'
                            },
                        titlefont={
                            'color':'#FFFFFF',
                            'size': 16,
                        },
                        legend = {
                            'orientation': 'h',
                            'bgcolor': '#54643e',
                            'xanchor': 'center', 'x': 0.5, 'y':-0.07
                        },
                        font= dict(
                            family="sans-serif",
                            size=12,
                            color='white'
                        ),
                        height=350,
                        width=320,
                        plot_bgcolor="#1A2E62",
                        paper_bgcolor="#1A2E62",
                        hovermode="closest",
                        margin=go.layout.Margin(l=25, r=25, b=15, t=25, pad=9)

                    )
                    )
    fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=14,
                      marker=dict(colors=colors, line=dict(color='#000000', width=0)))
    fig.update(layout_title_text='Sample Pie Chart',
               layout_showlegend=True)
    return fig



#********************************** Plotly Go Scatter Plot **********************************#
def createGOScatterPlot():
    np.random.seed(1)

    N = 100
    random_x = np.linspace(0, 1, N)
    random_y0 = np.random.randn(N) + 5
    random_y1 = np.random.randn(N)
    random_y2 = np.random.randn(N) - 5
    fig = go.Figure(
                data=[go.Scatter(x=random_x, y=random_y0,
                            mode='markers',
                            name='markers',
                            opacity=0.75,
                            text="scatter plot",
                            textposition="top center",
                            marker=dict(showscale=False,size=7, color='#acace6', line=dict(width=0.1), ),
                            textfont=dict(
                                color="black",
                                size=16,  # can change the size of font here
                                family="Times New Roman",
                            ),
                )],
                layout=go.Layout(
                            autosize=True,
                            width=725,
                            height=350,
                            xaxis=go.layout.XAxis(linecolor="#d9d9d9", linewidth=0.5, mirror=False),
                            yaxis=go.layout.YAxis(linecolor="#d9d9d9", linewidth=0.5, mirror=False),
                            margin=go.layout.Margin(l=0, r=50, b=25, t=55, pad=8),
                            # plot_bgcolor="#1A2E62",
                            # paper_bgcolor="#1A2E62",
                )
            )
    fig.update_layout(title='Population of USA States')
    fig.add_trace(go.Scatter(x=random_x, y=random_y1,
                             mode='lines+markers',
                             name='lines+markers'))
    fig.add_trace(go.Scatter(x=random_x, y=random_y2,
                             mode='lines',
                             name='lines'))

    return fig

'''
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
'''



#********************************** Plotly Go Line Plot **********************************#
def createGOLinePlot():
    month = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
             'August', 'September', 'October', 'November', 'December']
    high_2000 = [32.5, 37.6, 49.9, 53.0, 69.1, 75.4, 76.5, 76.6, 70.7, 60.6, 45.1, 29.3]
    low_2000 = [13.8, 22.3, 32.5, 37.2, 49.9, 56.1, 57.7, 58.3, 51.2, 42.8, 31.6, 15.9]
    high_2007 = [36.5, 26.6, 43.6, 52.3, 71.5, 81.4, 80.5, 82.2, 76.0, 67.3, 46.1, 35.0]
    low_2007 = [23.6, 14.0, 27.0, 36.8, 47.6, 57.7, 58.9, 61.2, 53.3, 48.5, 31.0, 23.6]
    high_2014 = [28.8, 28.5, 37.0, 56.8, 69.7, 79.7, 78.5, 77.8, 74.1, 62.6, 45.3, 39.9]
    low_2014 = [12.7, 14.3, 18.6, 35.5, 49.9, 58.0, 60.0, 58.6, 51.7, 45.2, 32.2, 29.1]
    fig = go.Figure(
        data= [go.Scatter(x=month, y=high_2014, name='High 2014',
                         line=dict(color='firebrick', width=0.5))],
        layout=go.Layout(
            autosize=True,
            width=500,
            height=370,
            xaxis=go.layout.XAxis(linecolor="#d9d9d9", linewidth=0.5, mirror=False),
            yaxis=go.layout.YAxis(linecolor="#d9d9d9", linewidth=0.5, mirror=False),
            margin=go.layout.Margin(l=50, r=25, b=50, t=55, pad=8),
            # plot_bgcolor="#1A2E62",
            # paper_bgcolor="#1A2E62",
        )

    )

    fig.update_layout(title='PH range over the years')

    return fig




#********************************** Plotly Go Box Plot **********************************#

def createGoBoxPlot():
    df = px.data.tips()
    df.head()

    fig = go.Figure(
            data = [go.Box(x=df["sex"], y=df["total_bill"], marker=dict(color="violet"))],
            layout = go.Layout(
                autosize=True,
                width=500,
                height=345,
                xaxis=go.layout.XAxis(linecolor="#d9d9d9", linewidth=0.5, mirror=False),
                yaxis=go.layout.YAxis(linecolor="#d9d9d9", linewidth=0.5, mirror=False),
                margin=go.layout.Margin(l=50, r=15, b=20, t=25, pad=8),
                # plot_bgcolor="#1A2E62",
                # paper_bgcolor="#1A2E62",
            )
        )
    fig.update_layout(title='Finding Outliers')
    return fig






#********************************** Plotly Go Box Plot **********************************#

def createGoViolinPlot():
    df = px.data.tips()
    df.head()

    fig = go.Figure(
            data = [go.Violin(x=df["sex"], y=df["total_bill"], marker=dict(color="violet"))],
            layout = go.Layout(
                autosize=True,
                width=500,
                height=375,
                xaxis=go.layout.XAxis(linecolor="#d9d9d9", linewidth=0.5, mirror=False),
                yaxis=go.layout.YAxis(linecolor="#d9d9d9", linewidth=0.5, mirror=False),
                margin=go.layout.Margin(l=50, r=15, b=20, t=45, pad=8),
                # plot_bgcolor="#1A2E62",
                # paper_bgcolor="#1A2E62",
            )
        )
    fig.update_layout(title='Finding Violin Outliers')
    return fig






def createGoHistogramChart():
    month = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
             'August', 'September', 'October', 'November', 'December']

    high_2000 = [32.5, 37.6, 49.9, 53.0, 69.1, 75.4,
                 76.5, 76.6, 70.7, 60.6, 45.1, 29.3]

    fig= go.Figure(
        data=[go.Bar(x=month,y=high_2000, marker=dict(color='#E232D1'), opacity=0.75)],
        layout = go.Layout(
            title={
                'text': "A sample go Plot",
                'x': 0.3,
                'y': 1,
                'xanchor': 'center',
                'yanchor': 'top'
            },
            titlefont={
                'color': '#ffffff',
                'size': 18
            },
            legend={
                'orientation': 'h',
                'bgcolor': '#1f2c56',
                'xanchor': 'center', 'x': 0.5, 'y': -0.07
            },
            font=dict(
                family="sans-serif",
                size=12,
                color='white'
            ),
            height=350,
            width=325,
            plot_bgcolor="#1A2E62",
            paper_bgcolor="#1A2E62",
            hovermode="closest",
            margin=go.layout.Margin(l=15, r=15, b=5, t=45, pad=4),

        )

    )

    return fig






#********************************** Plotly Express Bar Plot **********************************#
def createPxBarChart(dataFrame, x, y, height, width, color, labels, title, hover_data, orientation):
    fig = px.bar(dataFrame, x=x, y=y, color=color, width=width, height=height,
                labels=labels, title=title, hover_data=hover_data, orientation=orientation,opacity=[0,0.8])
    return fig


#********************************** Plotly Express Lint Plot **********************************#
def createPxLinePlot(dataFrame, x, y, height, width, color, label, title):
    fig = px.line(dataFrame, x=x, y=y, height=height, width=width, color=color, labels=label, title=title)
    return fig


def createPxPieChart(data_frame,
        names, values, color, hover_name=[], hover_data=[],
        custom_data=None, category_orders=None, labels=None, title=None, template=None,
        width=None, height=None, opacity=None, hole =None):
    fig = px.pie(data_frame,names, values, color, hover_name, hover_data,
                 custom_data, category_orders, labels, title, template, width, height,
                 opacity,hole)
    return fig
def createPxScatterPlot(dataFrame, x, y, color):
    fig = px.scatter(dataFrame, x=x, y=y, color=color)
    #fig.show()
    #fig = go.Figure()
    return fig


