
# coding: utf-8

# In[1]:

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from plotly import graph_objs as go
import pandas as pd
from flask import Flask


# In[2]:

df_fund_data = pd.read_csv('https://plot.ly/~jackp/17534.csv')
df_fund_data.head()


# In[3]:

df_perf_summary = pd.read_csv('https://plot.ly/~jackp/17530.csv')
df_perf_summary.head()


# In[4]:

df_cal_year = pd.read_csv('https://plot.ly/~jackp/17528.csv')
df_cal_year.head()


# In[5]:

df_perf_pc = pd.read_csv('https://plot.ly/~jackp/17532.csv')


# In[6]:

def make_dash_table( df ):
    ''' Return a dash definitio of an HTML table for a Pandas dataframe '''
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append( html.Td([ row[i] ]) )
        table.append( html.Tr( html_row ) )
    return table


# In[7]:

modifed_perf_table = make_dash_table( df_perf_summary )


# In[8]:

modifed_perf_table.insert(
    0, html.Tr( [
            html.Td([]),
            html.Td(['Cumulative'], colSpan=4, style=dict(textAlign="center")),
            html.Td(['Annualised'], colSpan=4, style=dict(textAlign="center"))
        ], style = dict( background='white', fontWeight=600 )
    )
)


# In[9]:

df_fund_info = pd.read_csv('https://plot.ly/~jackp/17544.csv')
df_fund_characteristics = pd.read_csv('https://plot.ly/~jackp/17542.csv')
df_fund_facts = pd.read_csv('https://plot.ly/~jackp/17540.csv')
df_bond_allocation = pd.read_csv('https://plot.ly/~jackp/17538.csv')


# In[10]:

dash.__version__


# In[178]:
server = Flask('my app')
server.secret_key = 'secret'

app = dash.Dash('GS Bond II Portfolio', server=server)

# Describe the layout, or the UI, of the app
app.layout = html.Div([

    html.Div([ # page 1

        html.A([ 'Print PDF' ],
           className="button no-print",
           style=dict(position="absolute", top=-40, right=0)),

        html.Div([ # subpage 1

            # Row 1 (Header)

            html.Div([

                html.Div([
                    html.H5('Goldman Sachs Strategic Absolute Return Bond II Portfolio'),
                    html.H6('A sub-fund of Goldman Sachs Funds, SICAV', style=dict(color='#7F90AC')),
                    ], className = "nine columns padded" ),

                html.Div([
                    html.H1([html.Span('03', style=dict(opacity=0.5)), html.Span('17')]),
                    html.H6('Monthly Fund Update')
                ], className = "three columns gs-header gs-accent-header padded", style=dict(float='right') ),

            ], className = "row gs-header gs-text-header"),

            html.Br([]),

            # Row 2

            html.Div([

                html.Div([
                    html.H6('Investor Profile', className = "gs-header gs-text-header padded"),

                    html.Strong('Investor objective'),
                    html.P('Capital appreciation and income.', className = 'blue-text'),

                    html.Strong('Position in your overall investment portfolio*'),
                    html.P('The fund can complement your portfolio.', className = 'blue-text'),

                    html.Strong('The fund is designed for:'),
                    html.P('The fund is designed for investors who are looking for a flexible \
                            global investment and sub-investment grade fixed income portfolio \
                            that has the ability to alter its exposure with an emphasis on interest \
                            rates, currencies and credit markets and that seeks to generate returns \
                            through different market conditions with a riskier investment strategy \
                            than GS Strategic Absolute Return Bond I Portfolio.', className = 'blue-text' ),

                ], className = "four columns" ),

                html.Div([
                    html.H6(["Performance (Indexed)"],
                            className = "gs-header gs-table-header padded"),
                    dcc.Dropdown(
                        id='selected-dropdown',
                        className="dropdown",
                        options=[
                            {'label': 'GS', 'value': 'GS'},
                            {'label': 'Moving Average (50 day)', 'value': 'MovingAverage50'},
                            {'label': 'Moving Average (200 day)', 'value': 'MovingAverage200'},
                            {'label': 'Volume', 'value': 'Volume'}
                        ],
                        multi=True,
                        value='GS'
                    ),
                    dcc.Graph(id='tester')
                ], className = "eight columns"),
            ], className = "row "),

            # Row 2.5

            html.Div([

                html.Div([
                    html.H6('Performance (%)', className = "gs-header gs-text-header padded"),
                    html.Table( make_dash_table( df_perf_pc ), className = 'tiny-header' )
                ], className = "four columns" ),

                html.Div([
                    html.P("This is an actively managed fund that is not designed to track its reference benchmark. \
                        Therefore the performance of the fund and the performance of its reference benchmark \
                        may diverge. In addition stated reference benchmark returns do not reflect any management \
                        or other charges to the fund, whereas stated returns of the fund do."),
                    html.Strong("Past performance does not guarantee future results, which may vary. \
                        The value of investments and the income derived from investments will fluctuate and \
                        can go down as well as up. A loss of capital may occur.")
                ], className = "eight columns" ),

            ], className = "row "),

            # Row 3

            html.Div([

                html.Div([
                    html.H6('Fund Data', className = "gs-header gs-text-header padded"),
                    html.Table( make_dash_table( df_fund_data ) )
                ], className = "four columns" ),

                html.Div([
                    html.H6("Performance Summary (%)", className = "gs-header gs-table-header padded"),
                    html.Table( modifed_perf_table, className = "reversed" ),

                    html.H6("Calendar Year Performance (%)", className = "gs-header gs-table-header padded"),
                    html.Table( make_dash_table( df_cal_year ) )
                ], className = "eight columns" ),

            ], className = "row "),

        ], className = "subpage" ),

    ], className = "page" ),

    html.Div([ # page 2

        html.A([ 'Print PDF' ],
           className="button no-print",
           style=dict(position="absolute", top=-40, right=0)),

        html.Div([ # subpage 2

            # Row 1 (Header)

            html.Div([

                html.Div([
                    html.H5('Goldman Sachs Strategic  Absolute Return Bond II Portfolio'),
                    html.H6('A sub-fund of Goldman Sachs Funds, SICAV', style=dict(color='#7F90AC')),
                    ], className = "nine columns padded" ),

                html.Div([
                    html.H1([html.Span('03', style=dict(opacity=0.5)), html.Span('17')]),
                    html.H6('Monthly Fund Update')
                ], className = "three columns gs-header gs-accent-header padded", style=dict(float='right') ),

            ], className = "row gs-header gs-text-header"),

            # Row 2

            html.Div([

                # Data tables on this page:
                # ---
                # df_fund_info = pd.read_csv('https://plot.ly/~jackp/17544/.csv')
                # df_fund_characteristics = pd.read_csv('https://plot.ly/~jackp/17542/.csv')
                # df_fund_facts = pd.read_csv('https://plot.ly/~jackp/17540/.csv')
                # df_bond_allocation = pd.read_csv('https://plot.ly/~jackp/17538/')

                # Column 1

                html.Div([
                    html.H6('Financial Information', className = "gs-header gs-text-header padded"),
                    html.Table( make_dash_table( df_fund_info ) ),

                    html.H6('Fund Characteristics', className = "gs-header gs-text-header padded"),
                    html.Table( make_dash_table( df_fund_characteristics ) ),

                    html.H6('Fund Facts', className = "gs-header gs-text-header padded"),
                    html.Table( make_dash_table( df_fund_facts ) ),

                ], className = "four columns" ),

                # Column 2

                html.Div([
                    html.H6('Sector Allocation (%)', className = "gs-header gs-table-header padded"),
                    dcc.Dropdown(
                        id='second-dropdown',
                        className="dropdown",
                        options=[
                            {'label': 'Bar Graph', 'value': 'Graph'},
                            {'label': 'Pie Chart', 'value': 'PieChart'}
                        ],
                        value='Graph'
                    ),
                    dcc.Graph(id="select_viz_graph", style={"padding-top": "60px"}),
                    html.H6('Country Bond Allocation (%)', className = "gs-header gs-table-header padded"),
                    html.Table( make_dash_table( df_bond_allocation ) ),

                ], className = "four columns" ),

                # Column 3

                html.Div([
                    html.H6('Top 10 Currency Weights (%)', className = "gs-header gs-table-header padded"),
                    html.Iframe(src="https://plot.ly/~jackp/17555.embed?modebar=false&link=false&autosize=true", \
                        seamless="seamless", style=dict(border=0), width="100%", height="300"),

                    html.H6('Credit Allocation (%)', className = "gs-header gs-table-header padded"),
                    html.Iframe(src="https://plot.ly/~jackp/17557.embed?modebar=false&link=false&autosize=true", \
                        seamless="seamless", style=dict(border=0), width="100%", height="300"),

                ], className = "four columns" ),

            ], className = "row"),

        ], className = "subpage" ),

    ], className = "page" ),

])


@app.callback(Output('select_viz_graph', 'figure'),
              [Input('second-dropdown', 'value')])
def select_viz_graph(value):
    if(value=="PieChart"):
        print("WE HERE")
        trace1 = {
          "labels": ["Governments", "Asset-Back Securities (ABS)", "Residential Mortgages (RMBS)", "Emerging Market Debt", "Corporates - High Yield", "Municipal", "Commercial Mortgages (CMBS)", "Corporates - Inv. Grade", "Covered Bonds", "Quasi-Governments", "Derivatives", "N/A"],
          "labelssrc": "alishobeiri:661:71ae57",
          "name": "B",
          "type": "pie",
          "uid": "353874",
          "values": ["46.5", "18.7", "10.6", "4.7", "2.7", "1.4", "1.4", "0.8", "0.4", "0.3", "0.0", "12.5"],
          "valuessrc": "alishobeiri:661:2b5e75"
        }
        data = go.Data([trace1])
        layout = {
          "annotations": [
            {
              "x": 0.9583,
              "y": 0.569230769231,
              "font": {"size": 12},
              "showarrow": False,
              "text": "Governments",
              "xref": "x",
              "yref": "y"
            },
            {
              "x": 0.1533,
              "y": 0.8446,
              "font": {"size": 9},
              "showarrow": False,
              "text": "Asset-Backed<br>Securities",
              "textangle": -11,
              "xref": "x",
              "yref": "y"
            },
            {
              "x": 0.07,
              "y": 0.5475,
              "font": {"size": 10},
              "showarrow": False,
              "text": "N/A",
              "xref": "x",
              "yref": "y"
            },
            {
              "x": 0.18,
              "y": 0.39,
              "showarrow": False,
              "text": "Residential <br>Mortages",
              "textangle": -35,
              "xref": "x",
              "yref": "y"
            },
            {
              "x": 0.4167,
              "y": 0.195,
              "font": {"size": 8},
              "showarrow": False,
              "text": "Emerging Mkt Debt",
              "textangle": -68,
              "xref": "x",
              "yref": "y"
            }
          ],
          "autosize": True,
          "bargroupgap": 0.2,
          "font": {
            "family": "Raleway",
            "size": 9
          },
          "height": 300,
          "hiddenlabels": ["Derivatives"],
          "hovermode": "closest",
          "legend": {
            "x": 2.46333333333,
            "y": 0.810153846154,
            "bgcolor": "rgba(255, 255, 255, 0)",
            "font": {"color": "rgb(68, 68, 68)"},
            "orientation": "v",
            "xanchor": "left"
          },
          "margin": {
            "r": 0,
            "t": 0,
            "b": 40,
            "l": 0,
            "pad": 6
          },
          "showlegend": False,
          "titlefont": {
            "family": "Raleway",
            "size": 9
          },
          "width": 200
        }
        return go.Figure(data=data, layout=layout)
    else:
        trace1 = {
          "x": ["Governments", "Asset-Back Securities (ABS)", "Residential Mortgages (RMBS)", "Emerging Market Debt", "Corporates - High Yield", "Municipal", "Commercial Mortgages (CMBS)", "Corporates - Inv. Grade", "Covered Bonds", "Quasi-Governments", "Derivatives", "N/A"],
          "y": ["46.5", "18.7", "10.6", "4.7", "2.7", "1.4", "1.4", "0.8", "0.4", "0.3", "0.0", "12.5"],
          "marker": {"color": "rgb(101, 32, 31)"},
          "name": "B",
          "type": "bar",
          "uid": "353874"
        }
        data = go.Data([trace1])
        layout = {
          "autosize": False,
          "bargroupgap": 0.2,
          "font": {
            "family": "Raleway",
            "size": 9
          },
          "height": 300,
          "hovermode": "closest",
          "margin": {
            "r": 10,
            "t": 0,
            "b": 140,
            "l": 20,
            "pad": 0
          },
          "titlefont": {
            "family": "Raleway",
            "size": 9
          },
          "width": 300,
          "xaxis": {
            "autorange": True,
            "range": [-0.5, 11.5],
            "title": "",
            "type": "category"
          },
          "yaxis": {
            "autorange": True,
            "range": [0, 48.9473684211],
            "title": "",
            "type": "linear"
          },
          "width": 200
        }
        return go.Figure(data=data, layout=layout)



@app.callback(
    Output('tester', 'figure'),
    [Input('selected-dropdown', 'value')])
def redo_graph(selected_dropdown_value):
    # Get some new data from Yahoo finance with Pandas
    df = pd.read_csv("GS.csv")
    mf = pd.read_csv("JPMorgan.csv")
    cf = pd.read_csv("MS.csv")
    print(selected_dropdown_value)
    print(len(selected_dropdown_value))
    # Construct a figure and return it to dash's front-end
    # This will end up updating the Graph's `figure` property
    # in the front-end of the application.
    traces = []
    stockTicker = {
        'x': df['date'],
        'y': df['close'],
        "line": {
            "color": "rgb(140, 15, 7)",
            "width": 3
        },
        "name": "GS",
        "type": "scatter",
        "uid": "0fac46",
        "xsrc": "alishobeiri:661:796f86",
        "ysrc": "alishobeiri:661:56eff0"
    }
    movingAverage50 = {
        'x': df['date'],
        'y': df['close'].rolling(50).mean(),
        "line": {
            "width": 2,
            "color": '#b8f441'
        },
        "name": "Moving Average"
    }
    movingAverage200 = {
        'x': df['date'],
        'y': df['close'].rolling(200).mean(),
        "line": {
            "width": 2,
            "color": '#f4c441'
        },
        "name": "Moving Average"
    }
    volume = {
        'x': df['date'],
        'y': df['volume'],
        'name': 'Moving Average',
        'line': {
            "width": 1,
            'color': '#418cf4'
        },
        'yaxis': 'y2'
        }
    if "GS" in selected_dropdown_value:
        traces.append(stockTicker)
    if "MovingAverage50" in selected_dropdown_value:
        traces.append(movingAverage50)
    if "MovingAverage200" in selected_dropdown_value:
        traces.append(movingAverage200)
    if "Volume" in selected_dropdown_value and len(selected_dropdown_value) == 1:
        traces.append({
                'x': df['date'],
                'y': df['volume'],
                'name': 'Moving Average',
                'line': {
                    "width": 1,
                    'color': '#418cf4'
                }
                })
        layout = {
                'autosize': True,
                'margin': {"r": 35, "t": 10, "b": 30, "l": 35, "pad": 0},
                'width': '425',
                'height': '250',
                "plot_bgcolor": "rgb(217, 224, 236)",
                'xaxis': {'gridcolor': 'rgb(255, 255, 255)', "range": ["2008-01-01 00:00:00", "2018-12-31 00:00:00.00"]},
                'yaxis': {'gridcolor': 'rgb(255, 255, 255)', "rangemode": "nonnegative"},
                'showlegend': False
               }
    elif "Volume" in selected_dropdown_value:
        traces.append(volume)
        layout = {
                'autosize': True,
                'margin': {"r": 30, "t": 10, "b": 30, "l": 35, "pad": 0},
                'width': '425',
                'height': '250',
                "plot_bgcolor": "rgb(217, 224, 236)",
                'xaxis': {'gridcolor': 'rgb(255, 255, 255)', "range": ["2008-01-01 00:00:00", "2018-12-31 00:00:00.00"]},
                'yaxis': {'gridcolor': 'rgb(255, 255, 255)'},
                "yaxis2": {
                    "anchor": "x",
                    "autorange": True,
                    "overlaying": "y",
                    "side": "right",
                    "type": "linear",
                    'showgrid': False,
                    'zeroline': False,
                    'showline': False
                },
                'showlegend': False
               }
    else:
        layout = {
                'autosize': True,
                'margin': {"r": 30, "t": 10, "b": 30, "l": 35, "pad": 0},
                'width': '425',
                'height': '250',
                "plot_bgcolor": "rgb(217, 224, 236)",
                'xaxis': {'gridcolor': 'rgb(255, 255, 255)', "range": ["2008-01-01 00:00:00", "2018-12-31 00:00:00.00"]},
                'yaxis': {'gridcolor': 'rgb(255, 255, 255)'},
                'showlegend': False
               }
    data = go.Data(traces)

    return go.Figure(data=data, layout=layout)
    #
    # if(selected_dropdown_value=="PRESENT"):

    # elif(selected_dropdown_value=="FUTURE"):
    #     return go.Figure(
    #         data=[
    #             {
    #                 'name': "Goldman Sachs",
    #                 'x': df['date'],
    #                 'y': df['close'],
    #                 "line": {
    #                     "color": "rgb(140, 15, 7)",
    #                     "width": 3
    #                     },
    #             },
    #             {
    #                 'name': "Morgan Stanley",
    #                 'x': mf['date'],
    #                 'y': mf['close'],
    #                 "line": {
    #                     "color": "#4286f4",
    #                     "width": 3
    #                     },
    #             },
    #             {
    #                 'name': "JP Morgan Chase",
    #                 'x': cf['date'],
    #                 'y': cf['close'],
    #                 "line": {
    #                     "color": "rgb(244, 220, 65)",
    #                     "width": 3
    #                     },
    #             },
    #         ],
    #         layout={
    #                 'autosize': True,
    #                 'margin': {"r": 0, "t": 10, "b": 30, "l": 35, "pad": 0},
    #                 'width': '425',
    #                 "legend": {
    #                     "x": 0.233000718248,
    #                     "y": -0.0950524188455,
    #                     "bgcolor": "rgb(255, 255, 255)",
    #                     "borderwidth": -1,
    #                     "font": {
    #                       "family": "Arial",
    #                       "size": 10
    #                     },
    #                     "orientation": "h"
    #                 },
    #                 'height': '250',
    #                 "plot_bgcolor": "rgb(217, 224, 236)",
    #                 'xaxis': {'gridcolor': 'rgb(255, 255, 255)', "range": ["2008-01-01 00:00:00", "2018-12-31 00:00:00.00"],
    #                           "type": "date"},
    #                 'yaxis': {'gridcolor': 'rgb(255, 255, 255)', "rangemode": "nonnegative"}
    #                }
    #     )
    # else:
    #     print("made teh else")
    #     trace = go.Candlestick(
    #                 x=df['date'][2000:],
    #                 high=df['high'][2000:],
    #                 open=df['open'][2000:],
    #                 close=df['close'][2000:],
    #                 low=df['low'][2000:]
    #             )
    #     data = [trace]
    #     layout={
    #         'autosize': True,
    #         'margin': {"r": 0, "t": 10, "b": 30, "l": 35, "pad": 0},
    #         'showlegend': False,
    #         'width': '425',
    #         'height': '250',
    #         "plot_bgcolor": "rgb(217, 224, 236)",
    #         'xaxis': {'gridcolor': 'rgb(255, 255, 255)', 'fixedrange': True},
    #         'yaxis': {'gridcolor': 'rgb(255, 255, 255)', 'fixedrange': True}
    #        }
    #     return go.Figure(data=data, layout=layout)

# "https://plot.ly/~jackp/17553.embed?modebar=false&link=false&autosize=true", \
#                            seamless="seamless", style=dict(border=0), width="100%", height="250")


# In[ ]:

external_css = [ "https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
        "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
        "//fonts.googleapis.com/css?family=Raleway:400,300,600",
        "https://codepen.io/alishobeiri/pen/XgpXaq.css",
        "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"]

for css in external_css:
    app.css.append_css({ "external_url": css })

external_js = [ "https://code.jquery.com/jquery-3.2.1.min.js",
        "https://codepen.io/plotly/pen/KmyPZr.js" ]

for js in external_js:
    app.scripts.append_script({ "external_url": js })


# In[ ]:
if __name__ == "__main__":
    app.server.run(debug=True)


# In[ ]:




# In[ ]:
