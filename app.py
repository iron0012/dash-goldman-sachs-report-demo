
# coding: utf-8

# In[1]:

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from plotly import graph_objs as go
from datetime import datetime as dt
import pandas as pd
import json
from pandas_datareader import data as web


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

app = dash.Dash('GS Bond II Portfolio')

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
##################################################################################################
                html.Div([
                    html.H6(["Performance (Indexed)"],
                            className = "gs-header gs-table-header padded"),
                    dcc.Dropdown(
                        id='selected-dropdown',
                        options=[
                            {'label': 'Last Quarter', 'value': 'PAST'},  #################################
                            {'label': 'Current', 'value': 'PRESENT'},   ##################################
                            {'label': 'Projection', 'value': 'FUTURE'}  #################################
                        ],
                        value='PRESENT'
                    ),
                    dcc.Graph(id='tester')
                ], className = "eight columns" ),
######################################################################################
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
                    html.Iframe(src="https://plot.ly/~jackp/17560.embed?modebar=false&link=false&autosize=true", \
                        seamless="seamless", style=dict(border=0), width="100%", height="300"),

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


@app.callback(
    Output('tester', 'figure'),
    [Input('selected-dropdown', 'value')])
def redo_graph(selected_dropdown_value):
    # Get some new data from Yahoo finance with Pandas

    dateFirst = {
        'PAST': dt(2015, 1, 1),
        'PRESENT': dt(2016, 1, 1),
        'FUTURE': dt(2017, 1, 1)
    }[selected_dropdown_value]

    dateSecond = {
        'PAST': dt(2015, 12, 31),
        'PRESENT': dt(2016, 12, 31),
        'FUTURE': dt.now()
    }[selected_dropdown_value]


    df = web.DataReader(
        'GS', 'yahoo',
        dateFirst, dateSecond
    )

    # Construct a figure and return it to dash's front-end
    # This will end up updating the Graph's `figure` property
    # in the front-end of the application.
    return go.Figure(
        data=[{
            'x': df.index,
            'y': df.Close,
            "line": {
                "color": "rgb(140, 15, 7)",
                "width": 3
            },
        }],
        layout={'autosize': True,
                'margin': {"r": 0, "t": 10, "b": 30, "l": 35, "pad": 0},
                'width': '425',
                'height': '250',
                "plot_bgcolor": "rgb(217, 224, 236)",
                'xaxis': {'gridcolor': 'rgb(255, 255, 255)'},
                'yaxis': {'gridcolor': 'rgb(255, 255, 255)'}
               }
    )
# "https://plot.ly/~jackp/17553.embed?modebar=false&link=false&autosize=true", \
#                            seamless="seamless", style=dict(border=0), width="100%", height="250")


# In[ ]:

external_css = [ "https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
        "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
        "//fonts.googleapis.com/css?family=Raleway:400,300,600",
        "https://codepen.io/plotly/pen/KmyPZr.css",
        "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"]

for css in external_css:
    app.css.append_css({ "external_url": css })

external_js = [ "https://code.jquery.com/jquery-3.2.1.min.js",
        "https://codepen.io/plotly/pen/KmyPZr.js" ]

for js in external_js:
    app.scripts.append_script({ "external_url": js })


# In[ ]:

app.server.run()


# In[ ]:




# In[ ]:
