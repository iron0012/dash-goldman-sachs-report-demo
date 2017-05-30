import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from plotly import graph_objs as go
from flask import Flask
server = Flask('my app')

app = dash.Dash('The New Oil Order', server=server)

app.layout = html.Div([

        # Page 1
        html.Div([
            html.A(['Print PDF'],
                   className="button no-print",
                   style=dict(position="absolute", top=-35, right=0)),
            # Letterhead Title
            html.Div([
                html.Div([
                        html.H6("September 11, 2015",
                        style={'position': 'relative', 'top': '25px', 'font-size': '0.9rem'}),
                        html.H4("The New Oil Order",
                        style={'font-weight': 'bold', 'position': 'relative', 'top': '25px', 'font-size': '2.1rem'}),
                        html.Br([]),
                        html.Img(src="http://i.imgur.com/6FHYhuO.png", \
                                 style={
                                        'height': '95',
                                        'float': 'right',
                                        'margin-right': '50',
                                        'position': 'relative',
                                        'bottom': '55px',
                                        'background': 'black'
                                 }),
                        html.H1('Lower for even longer',
                                style={'font-weight': 'bold',
                                       'font-size': '3.45rem',
                                       'position': 'relative',
                                       'top': '10',
                                       'padding-bottom': '15px',
                                       }),
                        html.H6('Commodities Research',
                                style={
                                        'position': 'absolute',
                                        'background': '#5F3890',
                                        'right': '50',
                                        'top': '165'
                                        }),
                        html.Br([]),
                        html.Br([])
                ], className = 'letterhead'),

                #Page 1 Text
                html.Div([
                    html.Div([
                        html.Strong("Lower oil prices warranted by fundamentals", className='strongPurple'),
                        html.P('Oil prices have declined sharply over the past month to our $45/bbl WTI \
                               Fall forecast. While this decline was precipitated by macro concerns, it was \
                               warranted in our view by weak fundamentals. In fact, the oil market is even \
                               more oversupplied than we had expected and we now forecast this surplus \
                               to persist in 2016 on further OPEC production growth, resilient non-OPEC \
                               supply and slowing demand growth, with risks skewed to even weaker \
                               demand given China\'s slowdown and its negative EM feedback loop'),
                       html.Strong('Persistent surplus requires lower prices for even longer', className='strongPurple'),
                       html.P('Given our updated forecast for a more oversupplied oil market in 2016, we \
                                are lowering our oil price forecast once again. Our new 1-, 3-, 6- and 12-mo \
                                WTI oil price forecast are $38/bbl, $42/bbl, $40/bbl and $45/bbl. Our 2016 \
                                forecast is $45/bbl vs. $57/bbl previously and forwards at $51/bbl. As we \
                                continue to view US shale as the likely near-term source of supply \
                                adjustment given the short cycle nature of shale production, we forecast \
                                that US Lower 48 crude & NGL production will decline by 585 kb/d in 2016 \
                                with other non-OPEC supply down 220 kb/d to end the oversupply by 4Q16.'),
                       html.Strong('Less US shale is one path to rebalancing the oil market', className='strongPurple'),
                       html.P('As the market now requires non-OPEC production to shift from growth to \
                                large declines in 2016, especially in the US, the uncertainty on how and \
                                where that adjustment will take place has increased significantly. In the US, \
                                capital allocation by Investment Grade E&Ps is now critical to rebalancing \
                                the market despite (1) less binding financial levers for IG than HY E&Ps and \
                                (2) deeply entrenched expectations that shale production growth will be \
                                required within the next couple years. This potential access to capital and \
                                the uncertainty it creates means that elevated financial stress needs to be \
                                maintained given the need for such large supply adjustments.'),
                       html.Strong('Operational stress is a growing downside risk to our forecast', className='strongPurple'),
                       html.P('This further creates the risk that a slowdown in production takes place too \
                                gradually forcing oil markets to clear as they historically have, through a \
                                collapse to production costs once the surplus breaches logistical and \
                                storage capacity. While not our base case, the potential for oil prices to fall \
                                to such levels, which we estimate near $20/bbl, is becoming greater as \
                                storage continues to fill.'),
                                ], className="firstLeft seven columns", style={'padding-top': '10px'}),

                        html.Div([
                            html.Strong("Damien Courvallin"),
                            html.P("(212) 902-3307 damien.courvallin@gs.com"),
                            html.P("Goldman, Sachs & Co"),
                            html.Strong("Jeffrey Currie"),
                            html.P("(212) 357-6801 jeffrey.currie@gs.com"),
                            html.P("Goldman, Sachs & Co"),
                            html.Strong("Abhisek Banerjee"),
                            html.P("+44(20)7774-3470 raquel.ohana@gs.com"),
                            html.P("Goldman, Sachs International"),
                            html.Strong("Raquel Ohana"),
                            html.P("(212) 902-3307 damien.courvallin@gs.com"),
                            html.P("Goldman, Sachs International"),
                            html.Strong("Michael Hinds"),
                            html.P("(212) 357-7528 michael.hinds@gs.com"),
                            html.P("Goldman, Sachs & Co"),
                        ], className = "contact five columns")
                ], className = "firstPage row", style={"margin-top": "20px"}),
            ], className = "subpage"),

        ], className = "page"),


        #Page 2
        html.Div([
            html.Div([
                #Page 2 Text
                html.Div([
                    html.H1("Executive Summary", style={'font-weight': 'bold'}),
                ], className = "header-text"),
                html.Div([
                    html.P("Oil prices have declined sharply over the past month, along with other asset classes. \
                            Importantly, we view this pull back to our Fall WTI forecast of $45/bbl as warranted by \
                            weak oil fundamentals with concerns for a slowdown in EM/China activity creating \
                            additional downside risk to current prices. In fact, even before potential further deceleration \
                            in global growth, the oil market is more oversupplied than we had forecast in May.", style={"padding-bottom": "5px", "padding-top": "10px"}),
                    html.P("We expect the drivers of this 2015 oversupply to persist through 2016 given: (1) further \
                            OPEC production growth as this remains the optimal strategy to raising long-term \
                            revenues in our view, (2) resilient non-OPEC ex. US production as broadly determined by \
                            investments already made, and (3) slowing demand growth on sequentially stable prices \
                            and lackluster global growth with risks clearly skewed to the downside given China\'s recent \
                            slowdown and the negative feedback loop of lower commodity prices on EM exporters \
                            facing large imbalances and debt. Finally, while the EIA recently reported a decline in US \
                            production, it is important to note that it also increased the stock build and \"balancing \
                            term\", leaving uncertainty around the reported decline. Our own modeling of US \
                            production - consistent with company guidance and high frequency pipeline data-points \
                            to an only moderate 2Q vs. 4Q15 production decline of 245 kb/d.", style={"padding-bottom": "5px"}),
                    html.P("Given our updated forecast for a more oversupplied oil market in 2016, we are lowering \
                            our oil price forecast once again. As previously, we continue to view US shale as the likely \
                            near-term source of supply adjustment given both the short cycle nature of shale \
                            production and the importance of capital as the new margin of adjustment. Our new 1-, 3, \
                            6- and 12-mo WTI oil price forecast are $38/bbl, $42/bbl, $40/bbl and $45/bbl from $45/bbl, \
                            $49/bbl, $54/bbl and $60/bbl previously. Our 2016 average price forecast is now $45/bbl vs. \
                            $57/bbl previously and the forward curve at $51/bbl. On our updated forecast, we expect \
                            the sharp deterioration in producer financial conditions that has occurred recently to \
                            persist on the recognition that the rebalancing of supply and demand is proving to be far \
                            more difficult than previously expected and that such stress is needed until evidence that \
                            US shale production growth is required. As a result, we now forecast that US Lower 48 \
                            crude and NGL production will decline by 585 kb/d in 2016 with other non-OPEC production \
                            down 220 kb/d to end the global oil market oversupply by 4Q16.", style={"padding-bottom": "5px"}),
                    html.P("It is important to emphasize that as we now believe the market requires non-OPEC \
                            production to shift from our prior expectation of modest growth to large declines in 2016, \
                            the uncertainty on how and where that adjustment will take place has increased. While \
                            until now market focus was on the need to see High Yield US E&Ps potentially be forced \
                            close to bankruptcy, the required magnitude of the US production decline in 2016 now \
                            needs to include reductions by Investment Grade E&Ps, whose production is three times \
                            larger than HY E&Ps. This is an important shift, as ultimately the levers to force HY \
                            producers into lower production such as borrowing basis redeterminations, debt maturities \
                            and hedge coverage, are significantly less binding for IG E&Ps. This near-term adjustment \
                            mechanism is further put at risk by the deeply entrenched expectation - ours included - \
                            that the global oil market will require shale production growth within the next couple years.", style={"padding-bottom": "5px"}),
                    html.P("This creates the risk that a slowdown in US production takes place too late or not at all, \
                            forcing oil markets to balance elsewhere or as they have historically cleared, through a \
                            collapse to production costs once the surplus breaches logistical and storage capacity. Net, \
                            while we are increasingly convinced that the market needs to see lower oil prices for longer \
                            to achieve a production cut, the source of this production decline and its forcing \
                            mechanism is growing more uncertain, raising the possibility that we may ultimately clear \
                            at a sharply lower price with cash costs around $20/bbl Brent prices, on our estimates. \
                            While such a drop would prove transient and help to immediately rebalance the supply and \
                            demand for barrels, it would likely do little for the longer-term capital imbalance in the \
                            market with only lower prices for longer rebalancing the capital markets for energy.", style={"padding-bottom": "5px"}),
                ], className = "written-text eight columns"),
            ], className = "subpage"),
            html.A([ 'Print PDF' ],
                   className="button no-print",
                   style=dict(position="absolute", top=-35, right=0)),
        ], className = "page"),


        #Page 3
        html.Div([
            html.Div([
                html.Div([
                    html.H1("Lower for even longer"),
                ], className = "header-text"),
                html.Div([
                    #Page 3 Text
                    html.H6("Oil sell-off precipitated by macro concerns, but warranted by oil fundamentals"),
                    html.P("Oil prices have declined sharply over the past month, along with other asset classes, to \
                            retrace their lows of last winter. Importantly, we view this pull back in prices to our Fall WTI \
                            forecast of $45/bbl as warranted by weak oil fundamentals with concerns over a slowdown \
                            in EM/China activity creating additional downside risk to current oil prices. In fact, even \
                            before a potential further deceleration in global growth, the global oil market is more \
                            oversupplied than we had forecast in May, still driven by excess supply (Exhibit 1) due to:", style={"padding-bottom": "5px"}),
                    html.Ul([
                            html.Li("OPEC production has continued to rise sharply, up 1.0 mb/d yoy, with Iraq and Saudi \
                                    production setting new record highs. Non-OPEC production outside the US Lower 48 \
                                    has also surprised to the upside, with production reaching 47.3 mb/d in 2Q15 vs. our \
                                    46.9 forecast. In particular, Russia and North Sea production are currently up 235 kb/d \
                                    yoy in 1H16."),
                            html.Li("Higher production outside of the US has more than offset a decline in the US Lower 48, \
                                    with the updated EIA measure showing production down 316 kb/d since its April peak. \
                                    Given that the EIA also increased the June stock build and its \"balancing term\", \
                                    uncertainty around the reported decline remains high. Further, this decline is likely to \
                                    have been exacerbated by a sharp rise in in the backlog of drilled, but uncompleted \
                                    wells. Our own modeling of US production - consistent with company guidance and \
                                    high frequency pipeline data-pointing to an only moderate 2Q to 4Q15 production \
                                    decline of 245 kb/d"),
                            html.Li("While oil demand growth has been strong relative to recent years, this looks \
                                    increasingly price induced (with a cold winter helping too) as global economic growth \
                                    has in fact weakened since our last forecast revision in May. We currently estimate that \
                                    yoy oil demand growth is 1.75 mb/d YTD, with our 2015 forecast now of 1.62 mb/d vs. \
                                    1.40 mb/d previously. Our modeling suggests that prices alone have contributed to 530 \
                                    kb/d of oil demand growth this year."),
                            html.Li("Net, demand growth remains well shy of the year-to-date supply growth of 2.9 mb/d \
                                    with only 2004 briefly posting such demand growth as China and EM kicked off the \
                                    previous decade's commodity boom. Not only is emerging market growth slowing, but \
                                    the benefits from lower prices are most likely behind us, as our demand impulse \
                                    modeling shows that they typically last 9-12 months (Exhibit 3)."),
                    ], className = "twelve columns row"),
                    html.P("We estimate that the third quarter global market imbalance will be c.1.9 mb/d vs. c.2.2 \
                            mb/d in 1H15, with weekly stock data in the US, Europe, Singapore and Japan pointing to \
                            counter-seasonally large stock builds in July-August (Exhibit 2).")
                ], className = "written-text eight columns"),
            ], className = "subpage"),
                        html.A([ 'Print PDF' ],
                               className="button no-print",
                               style=dict(position="absolute", top=-35, right=0)),
        ], className = "page"),

        #Page 4
        html.Div([
            html.Div([
                #Page 4 Exhibits (1)
                html.Div([
                        html.Div([
                            html.Strong("Exhibit 1: The global oil market is oversupplied as production remains 3.0 mb/d higher than last year"),
                            html.P("Year over year growth, million barrels per day", style={"font-size": "11"}),
                        ], className="title six columns"),
                        html.Div([
                            html.Strong("Exhibit 2: High frequency stocks point to a counter-seasonally large build in July-August"),
                            html.P("Weekly stocks (US, Japan, Singapore, ARA). Crude only for US & Singapore. Month-on-month change (kb/d) vs. seasonal", style={"font-size": "11"}),
                        ], className="title six columns"),
                    ], className="thirdPage first row", style={'position': 'relative', 'top': '20px'}),
                html.Div([
                        html.Iframe(src="https://plot.ly/~alishobeiri/55.embed?modebar=false&link=false&autosize=true",
                                    className="exhibit six columns", seamless="seamless", style={}, height="250"),
                        html.Iframe(src="https://plot.ly/~alishobeiri/204.embed?modebar=false&link=false&autosize=true",
                                    className="exhibit six columns", seamless="seamless", style={}, height="250"),
                ], className="thirdPage row"),
                #Page 4 Text
                html.Div([
                    html.P("Going forward we expect this oversupply to persist until late 2016. Specifically: ",
                            style={'padding-top': '20px', "padding-bottom": "5px"}),
                    html.Ul([
                        html.Li("We expect demand growth to sequentially weaken to 1.275 mb/d in 2016 vs. our 1.5 \
                                mb/d previous forecast. Driving this forecast is our assumption that 2016 global growth \
                                will remain at 2015\'s 3.25% pace vs. our prior 3.75% assumption and our updated \
                                forecast for roughly sequentially stable oil prices in 2016. Importantly we view the risks \
                                to this demand growth forecast as clearly skewed to the downside, given China\'s \
                                recent slowdown, its potential impact on EM growth and the negative feedback loop of \
                                lower commodity prices on EM exporters facing large macro imbalances and debt. We \
                                illustrate our demand sensitivity to various growth and price outcomes in Exhibit 4."
                                , style={"padding-bottom": "10px"}),
                    ], className="twelve columns row"),
                ], className = "written-text eight columns"),
                #Page 4 Exhibits (2)
                html.Div([
                        html.Div([
                            html.Strong("Exhibit 3: Our VAR analysis shows that demand \
                                         responses occur within 9 to12 months..."),
                            html.P("Estimated oil demand response (in %) to +1% shock to prices \
                                    or industrial production", style={"font-size": "11"}),
                        ], className="title six columns"),
                        html.Div([
                            html.Strong("Exhibit 4: ... with potentially weaker global growth a key \
                                        downside risk to 2016 demand"),
                            html.P("2016 vs. 2015 global oil demand growth sensitivity (kb/d). \
                                    2015 Brent prices assumed at $54/bbl", style={"font-size": "11"}),
                        ], className="title six columns"),
                    ], className="thirdPage first row"),
                html.Div([
                        html.Iframe(src="https://plot.ly/~alishobeiri/513.embed?modebar=false&link=false&autosize=true",
                                    className="exhibit six columns", seamless="seamless",
                                    height="250", style={"padding-bottom": "10px", 'position': 'relative', 'bottom': '25px'}),
                        html.Img(src="http://i.imgur.com/IJsVT9P.png",
                                    className="exhibit six columns", style={"padding-bottom": "100px", "padding-top": "20px", "padding-left": "5px", "padding-right": "5px"}, height="225"),
                ], className="thirdPage row"),
            ], className = "subpage"),
            html.A([ 'Print PDF' ],
                   className="button no-print",
                   style=dict(position="absolute", top=-35, right=0)),
        ], className = "page"),

        #Page 5
        html.Div([
            html.Div([
                #Page 5 Text
                html.Div([
                    html.Ul([
                            html.Li("Our supply outlook is similar to what occurred in 2015. We forecast more production \
                                    growth from OPEC, up 615 kb/d yoy vs. 2015, driven by Saudi, Iraq and Iran. For Iran, \
                                    we assume that production will grow by 260 kb/d on average. We only assume that the \
                                    Neutral zone output will recover to reach 200 kb/d by end-2016 up from zero currently \
                                    and 520 kb/d in 2014, leaving risk to our OPEC forecast skewed to the upside."),
                            html.Li("This forecast reflects our view that OPEC\'s resolve in growing market share has likely \
                                    strengthened following the pick-up in US activity that occurred this summer once WTI \
                                    prices returned to $60/bbl. Despite the fiscal challenges that low oil prices create for \
                                    OPEC producers, the alternative of reducing production would similarly undermine \
                                    long-term revenues. As a result we continue to view production growth and the \
                                    associated investment stimulus to the wider economy as the optimal strategy to help \
                                    offset these lower revenues, with low-cost OPEC producers likely to expand capacity \
                                    now that they have pushed output to near max utilization. Even Venezuela has \
                                    accepted further Chinese financing to produce oil from older fields. Ultimately, the one \
                                    scenario where we could see OPEC pursuing a cartel strategy and cutting output is one \
                                    where fundamentals push prices down to the steep part of the cash-cost curve 3 , a likely \
                                    outcome should oil demand growth weaken sharply, as we discuss later. However this \
                                    production cut would occur at much lower oil prices."),
                            html.Li("We continue to expect that non-OPEC production outside of the US Lower 48 and NGL \
                                    will remain resilient, declining only by 220 kb/d in 2016 with growth in the GoM, \
                                    Canada, Argentina, Brazil and Russia. This reflects our view that the production outlook \
                                    to 2017 remains broadly determined by investments already made. Importantly, the \
                                    well-publicized shale cost reduction is occurring globally as well, driven by productivity \
                                    gains, a substantially stronger dollar and sharp declines in other commodity prices."),
                    ], className="twelve columns row"),
                    dcc.Markdown("Given this slower expected demand growth in the face of growing OPEC production and \
                            resilient non-OPEC ex. US production, **we now forecast that US Lower 48 crude and \
                            NGL production will need to decline by 585 kb/d in 2016 with other non-OPEC \
                            production down 220 kb/d to end the global oil market oversupply by 4Q16**, a \
                            similar time frame to what we laid out in our May forecast."),
                ], className="written-text eight columns no-header row"),
                #Page 5 Exhibits
                        html.Div([
                                html.Div([
                                    html.Strong("Exhibit 5: We continue to expect that the global oil \
                                                market will remain in surplus until 4Q16..."),
                                    html.P("Global supply minus demand (mb/d)", style={"font-size": "11"}),
                                ], className="title six columns"),
                                html.Div([
                                    html.Strong("Exhibit 6: ... with OECD ex. US NGL stocks building more \
                                                than the seasonal average over the next 4 quarters"),
                                    html.P("Thousand barrels per day", style={"font-size": "11"}),
                                ], className="title six columns"),
                            ], className="thirdPage first row"),
                    html.Div([
                            html.Iframe(src="https://plot.ly/~alishobeiri/516.embed?modebar=false&link=false&autosize=true",
                                        className="exhibit six columns", seamless="seamless",
                                        height="250", style={"padding-bottom": "10px", 'position': 'relative', 'bottom': '25px'}),
                            html.Iframe(src="https://plot.ly/~alishobeiri/519.embed?modebar=false&link=false&autosize=true",
                                        className="exhibit six columns", seamless="seamless",
                                        height="250", style={"padding-bottom": "10px", 'position': 'relative', 'bottom': '25px'}),
                    ], className="thirdPage row"),
            ], className = "subpage"),
            html.A([ 'Print PDF' ],
                   className="button no-print",
                   style=dict(position="absolute", top=-35, right=0)),
        ], className = "page"),

        #Page 6
        html.Div([
            html.Div([
                #Page 6 Text
                html.Div([
                    html.P("Consistent with our prior forecasts, we continue to view US shale as the likely near-term \
                            source of supply adjustment given both the short-cycle nature of shale production and \
                            capital as the new margin of adjustment. This is exacerbated by high-quality assets on \
                            average owned by weak balance sheets and strong balance sheets owning lower-quality \
                            producing assets. This runs opposite to history when weak balance sheets typically owned \
                            high-cost assets, creating a linear relationship between lower prices and financial stress \
                            which led to more financially motivated supply cuts as prices dropped.", style={"padding-bottom": "5px"}),
                    dcc.Markdown("As a result, our updated price forecast requires oil prices to stay lower for longer to achieve \
                            a sufficient US and non-OPEC production decline. We now forecast that WTI oil prices need \
                            to remain near current levels and below the forward curve through 4Q16, with most \
                            downside during shoulder months. Specifically, we are lowering our 1-, 3-, 6- and 12-mo \
                            WTI oil price forecast to $38/bbl, $42/bbl, $40/bbl and $45/bbl from $45/bbl, $49/bbl, $54/bbl \
                            and $60/bbl previously. Our 2016 average price forecast is now $45/bbl vs. $57/bbl \
                            previously and the forward curve at $51/bbl. Our WTI-Brent spread forecast remains $5/bbl \
                            except in 2H16 when declining US production in the face of US demand growth, US spare \
                            storage capacity and elevated refinery runs lead to rising US crude oil imports and a $4/bbl \
                            differential.")
                ], className="written-text eight columns no-header row", style={"padding-bottom": "10px"}),
                #Page 6 Exhibits
                    html.Div([
                            html.Div([
                                html.Strong("Exhibit 7: We lower our 2015-16 oil price forecasts..."),
                                html.P("$/bbl", style={"font-size": "11"}),
                            ], className="title six columns"),
                            html.Div([
                                html.Strong("Exhibit 8: ... and expect prices to remain below current \
                                forwards until 2017"),
                                html.P("$/bbl", style={"font-size": "11"}),
                            ], className="title six columns"),
                        ], className="thirdPage first row", style={"margin-top": "100px"}),
                    html.Div([
                            html.Img(src="http://i.imgur.com/DBkxRT2.png",
                                        className="exhibit six columns", style={"padding-bottom": "40px", "padding-top": "0px"}, height="225"),
                            html.Iframe(src="https://plot.ly/~alishobeiri/539.embed?modebar=false&link=false&autosize=true",
                                        className="exhibit six columns", seamless="seamless",
                                        height="250", style={"padding-bottom": "10px", 'position': 'relative', 'bottom': '25px'}),
                    ], className="thirdPage row"),
                    #Page 6 Text
                     html.Div([
                                html.H6("Declining US production is but one path to rebalancing the oil market"),
                                html.P("It is important to emphasize that as we now believe the market requires non-OPEC \
                                        production to shift from our prior expectation of modest growth to large declines in 2016, \
                                        the uncertainty on how that adjustment will take place has increased. In particular, while \
                                        until now market focus has been on the need to see high yield US E&Ps be forced into \
                                        maintenance and restructuring- which our US energy credit research team led by Jason \
                                        Gilbert views as likely with WTI prices remaining at $35/bbl for six months - the required \
                                        magnitude of the US production decline in 2016 now needs to include reductions by \
                                        Investment Grade E&Ps whose production is three times larger than HY E&Ps (Exhibit 9). In \
                                        other words capital allocation decisions by IG are more likely to drive market rebalancing \
                                        than HY bankruptcies."),
                            ], className = "written-text eight columns"),
            ], className = "subpage"),
            html.A([ 'Print PDF' ],
                   className="button no-print",
                   style=dict(position="absolute", top=-35, right=0)),
        ], className = "page"),

        #Page 7
        html.Div([
            html.Div([
                #Page 7 Text
                    html.Div([
                        html.P("This is important, as ultimately the levers to force HY producers into lower production, \
                                such as borrowing basis redeterminations, debt maturities and hedge coverage, are \
                                significantly less binding for IG E&Ps. It is instead management\'s focus on balancing capex \
                                and cash flow and investors\' willingness to finance funding gaps that are the levers of \
                                adjustments for this cohort of companies. And while HY debt markets may be once again \
                                shutting, tentative signs of greater discipline by US IG E&Ps have so far only translated in \
                                stabilizing production guidance rather than pointing to the decline that our global oil \
                                balance requires.", style={"padding-bottom": "5px"}),
                        html.P("As a result, the sharp intensification in producer financial stress observed recently - with \
                                forward oil prices and energy equity share prices at multi-year lows (and credit spreads at \
                                highs) - is unlikely to yield sufficient financial stress in the short-term. So while this \
                                deterioration in financial conditions is finally reflecting the markets\' decreasing confidence \
                                in a quick rebound in prices and a recognition that the rebalancing of supply and demand \
                                will likely prove to be far more difficult than previously expected, we now believe that such \
                                stress needs to remain in place well into 2016 and up until evidence emerges that US shale \
                                production growth is actually required.", style={"padding-bottom": "5px"}),
                        html.P("This short-term adjustment mechanism is further put at risk by the deeply entrenched \
                                expectation - ours included - that the global oil market will require shale production \
                                growth within the next couple years. This creates the risk that if investor capital is available \
                                to accommodate producers continuing to outspend cash flow, the slowdown in US \
                                production will take place too late or not at all, forcing oil markets to clear as they \
                                historically have, through a collapse to production costs once the surplus breaches \
                                logistical and storage capacity.", style={"padding-bottom": "5px"}),
                        html.P("Net, while we are increasingly convinced that we need to see lower prices for longer to \
                                achieve a production cut, the origin of this production decline and its forcing mechanism is \
                                growing uncertain, raising the possibility that we may ultimately clear at a sharply lower \
                                price."),
                    ], className="written-text eight columns no-header row", style={"padding-bottom": "40px"}),
                #Page 7 Exhibits
                        html.Div([
                                html.Div([
                                    html.Strong("Exhibit 9: Rebalancing depends now more on IG behavior \
                                                given 3x more production than HY"),
                                    html.P("Total US E&P production by credit rating category", style={"font-size": "11"}),
                                ], className="title six columns"),
                                html.Div([
                                    html.Strong("Exhibit 10: Financial stress on producers needs to remain \
                                                elevated to force US production declines"),
                                    html.P("EPX equity sector (indexed to 90 as or Sep-14, lhs); WTI 2-\
                                            year swap ($/bbl, lhs); HY Energy spread as a ratio to HY \
                                            Index spread (rhs, inverted)", style={"font-size": "11"}),
                                ], className="title six columns"),
                            ], className="thirdPage first row", style={"margin-top": "100px"}),
                    html.Div([
                            html.Iframe(src="https://plot.ly/~alishobeiri/551.embed?modebar=false&link=false&autosize=true",
                                        className="exhibit six columns", seamless="seamless",
                                        height="250", style={"padding-bottom": "10px", 'position': 'relative', 'bottom': '25px'}),
                            html.Iframe(src="https://plot.ly/~alishobeiri/569.embed?modebar=false&link=false&autosize=true",
                                        className="exhibit six columns", seamless="seamless",
                                        height="250", style={'position': 'relative', 'bottom': '25px'}),
                    ], className="thirdPage row"),
            ], className = "subpage"),
            html.A([ 'Print PDF' ],
                   className="button no-print",
                   style=dict(position="absolute", top=-35, right=0)),
        ], className = "page"),

        #Page 8
        html.Div([
            html.Div([
                #Page 8 Text
                html.Div([
                    html.H6("Operational stress key downside risk to our forecast in coming months"),
                    html.P("With storage continuing to fill globally and uncertainty on the market\'s balancing \
                            mechanism, the odds of resolving the global balance through a fall to cash costs has \
                            increased, although our base case supply-demand forecast doesn\'t call for it yet.", style={"padding-bottom": "5px"}),
                    html.P("Although perceptions this past April were that the market was near operational stress, with \
                            the floating storage arbitrage briefly open, it is now far closer. We estimate that the \
                            industry has added c.240 million barrels of petroleum to crude and product storage tanks \
                            from January to August, with 180 mb in OECD stocks exc. NGLs. In addition, 40 million \
                            barrels were added to clean and dirty floating storage while OGP stock data implies that \
                            China commercial crude and product inventories increased by 40 mb with the Chinese SPR \
                            absorbing an additional 110 mb between January and July.", style={"padding-bottom": "5px"}),
                    dcc.Markdown("With increased operational stress in the system vs. six months ago, we now attach a \
                            substantially higher probability to this being the margin of adjustment than we did in \
                            January. Specifically, **we estimate that available identified storage capacity outside \
                            China is currently 375 mb, with our balance pointing to a 240 mb ex. China \
                            inventory build in between September 2015 and year-end 2016** (Exhibits 11 and \
                            12):"),
                    html.Ul([
                        html.Li("We estimate OECD available storage capacity at 220 mb as of the end of August. This \
                                is comprised of 80 mb of crude oil storage capacity in the US\' PADDs 1, 2 and 3, based \
                                on historical peak utilization of EIA\'s assessment of US working storage capacity. US \
                                clean product spare capacity (vs. peak stocks) is an additional 30 mb. We also assume \
                                that OECD ex.-US storage has similar capacity than when storage peaked in 1999, \
                                leaving 110 mb of available storage capacity."),
                        html.Li("We proxy non-OECD storage capacity as follows: we identify commercial storage \
                                capacity of 290 mb and refinery storage of 600 mb (assuming 7 days of crude and \
                                product storage cover on 42 mb/d of runs). Combined this represents almost 900 mb of \
                                total storage capacity and assuming that non-OECD storage capacity is as full as OECD \
                                ex. US (92%) implies that remaining spare capacity is 70 mb."),
                        html.Li("While we have data on total clean and dirty vessel capacity, information on actual \
                                loadings is more limited. Based on Argus reported oil in transit and estimated floating \
                                storage since 2009, we estimate an additional 85 mb of crude oil can be stored in \
                                floating storage before vessel utilization reaches its recent peak of April 2010."),
                    ], className="twelve columns row", style={"marginBottom": "0px"}),
                        html.P("In the case of China, we estimate that the SPR ramp up has absorbed 550 kb/d through July, \
                                following a 350 kb/d build out in 2014. Going forward we assume an additional 300 kb/d \
                                increase in SPR capacity in 2016, with an additional 100 kb/d build in commercial crude and \
                                product stocks."),
                ], className = "written-text no-header eight columns row"),
            ], className = "subpage"),
            html.A([ 'Print PDF' ],
                   className="button no-print",
                   style=dict(position="absolute", top=-35, right=0)),
        ], className = "page"),

        #Page 9
        html.Div([

            html.Div([
                #Page 9 Exhibits
                html.Div([
                        html.Div([
                            html.Strong("Exhibit 11: We estimate that remaining identifiable \
                                        storage capacity is 375 million barrels outside of China..."),
                            html.P("Million barrels", style={"font-size": "11"}),
                        ], className="title six columns"),
                        html.Div([
                            html.Strong("Exhibit 12: ... with our projected OECD vs. non-OECD ex. \
                                        China stock build through 2016 of 240 million barrels"),
                            html.P("Quarterly changes in stock (thousand barrels per day)", style={"font-size": "11"}),
                        ], className="title six columns"),
                    ], className="thirdPage first row", style={'position': 'relative', 'top': '20px'}),
                html.Div([
                        html.Img(src="http://i.imgur.com/wX5mQYn.png",
                                    className="exhibit six columns", style={"padding-bottom": "40px", "margin-top": "25px",
                                                                            "padding-right": "5px", "padding-left": "5px"}, height="225"),
                        html.Iframe(src="https://plot.ly/~alishobeiri/584.embed?modebar=false&link=false&autosize=true",
                                    className="exhibit six columns", seamless="seamless", style={}, height="250"),
                ], className="thirdPage row"),
                #Page 9 Text
                html.Div([
                    html.P("Importantly, we acknowledge that the uncertainty around this estimated spare storage \
                            capacity is significant. First, there is uncertainty on the starting point of storage utilization \
                            with our end-of-August OECD stocks based on our balance and high frequency stock data. \
                            Second, while our own implied miscellaneous to balance is lower than the IEA\'s given our \
                            accounting of non-OECD storage builds (where data is available) and China stocks, it has \
                            nonetheless averaged 200 kb/d over the last twelve months, with some of these missing \
                            barrels likely ending in non-OECD inventories as we believe was the case in 1998-99 \
                            (Exhibit 13). The backlog of drilled but uncompleted shale wells, another feature of the New \
                            Oil Order, complicates this margin of adjustment even further, as the \"fracklog\" is just \
                            another form of storage.", style={'padding-top': '5px'}),
                    html.P("Finally, even if our assessed storage capacity estimate is roughly correct, a combined error \
                            on our 2016 production (higher) and demand (lower) forecasts of 370 kb/d would ultimately \
                            fill our assessed spare storage capacity. This could be achieved for example with global \
                            growth of 2.75% (Exhibit 4) or more resilient US production than we model.", style={'padding-top': '5px'}),
                    html.P("Given our forecast for rising inventories through 4Q16, the probability of breaching storage \
                            capacity constraints will be highest this autumn and during next spring\'s refinery \
                            turnarounds. The first step would be the opening of the floating storage arbitrage which on \
                            our calculations is nearly open, requiring little further steepening of the Brent forward \
                            curve at current freight rates. In the event that storage fills faster than we forecast or \
                            capacity is lower than we model, the potential downside to our oil price forecast from \
                            hitting storage capacity is significant as it requires forcing production lower and back in \
                            line with demand, as occurred in 1998 (Exhibit 14).", style={'padding-top': '5px'}),
                ], className="written-text eight columns", style={'padding-top': '25px'}),
            ], className = "subpage"),
            html.A([ 'Print PDF' ],
                   className="button no-print",
                   style=dict(position="absolute", top=-35, right=0)),
        ], className = "page"),

        #Page 10
        html.Div([
            html.Div([
                #Page 10 Exhibits (1)
                html.Div([
                        html.Div([
                            html.Strong("Exhibit 13: We believe that most of the miscellaneous to \
                                        balance represents non-OECD stock builds, like in 1998"),
                            html.P("Quarterly stock changes, thousand barrels per day", style={"font-size": "11"}),
                        ], className="title six columns"),
                        html.Div([
                            html.Strong("Exhibit 14: Operational stress ultimately brings spot and \
                                        forward prices down to cash costs"),
                            html.P("2015 $/bbl", style={"font-size": "11"}),
                        ], className="title six columns"),
                    ], className="thirdPage first row", style={'position': 'relative', 'top': '20px'}),
                html.Div([
                        html.Iframe(src="https://plot.ly/~alishobeiri/588.embed?modebar=false&link=false&autosize=true",
                                    className="exhibit six columns", seamless="seamless", style={}, height="250"),
                        html.Iframe(src="https://plot.ly/~alishobeiri/590.embed?modebar=false&link=false&autosize=true",
                                    className="exhibit six columns", seamless="seamless", style={}, height="250"),
                ], className="thirdPage row"),
                #Page 10 Text
                html.P("From a level perspective, we estimate high cost producers have operating breakevens in \
                        the $30/bbl Brent prices. However these producers, typically Canadian oil sands producers, \
                        have also limited leverage and elevated fixed costs to shutting down production. As a \
                        result, a fall to cash costs could likely take prices instead to the highly levered high-cost US \
                        shale producers, whose cash breakevens are closer to $20/bbl, on our estimates (Brent \
                        equivalent).", className="thirdPage written-text row eight columns", style={'padding-top': '25px'}),
                html.Div([
                #Page 10 Exhibits (2)
                        html.Div([
                            html.Strong("Exhibit 15: The highest cash costs are near $30/bbl..."),
                            html.P("Oil cash cost (in Brent equivalent $/bbl)", style={"font-size": "11"}),
                        ], className="title six columns"),
                        html.Div([
                            html.Strong("Exhibit 16: ... but are for low levered producers"),
                            html.P("2015 production costs ($/bbl) vs. net debt/capital employed", style={"font-size": "11"}),
                        ], className="title six columns"),
                    ], className="thirdPage first row", style={'position': 'relative', 'top': '20px'}),
                html.Div([
                        html.Iframe(src="https://plot.ly/~alishobeiri/592.embed?modebar=false&link=false&autosize=true",
                                    className="exhibit six columns", seamless="seamless", style={}, height="250"),
                        html.Iframe(src="https://plot.ly/~alishobeiri/596.embed?modebar=false&link=false&autosize=true",
                                    className="exhibit six columns", seamless="seamless", style={}, height="250"),
                ], className="thirdPage row"),
            ], className = "subpage"),
            html.A([ 'Print PDF' ],
                   className="button no-print",
                   style=dict(position="absolute", top=-35, right=0)),
        ], className = "page"),

        #Page 11
        html.Div([
            html.Div([
                html.Div([
                    #Page 11 Text
                    html.H6("US shale growth not required until 2017"),
                    html.P("Under our updated oil supply and demand forecast, we believe the market only requires \
                            US production growth in 2017 (of 300 kb/d), and as a result maintain our 2017 $60/bbl WTI \
                            price forecast, with prices trading by then above our US shale $55/bbl breakeven forecast. \
                            Our longer-term forecast is unchanged as well with continued productivity gains bringing \
                            these numbers lower by $10/bbl by 2020.", style={"padding-bottom": "5px"}),
                    html.P("Although our 2017 WTI forecast now sits above the forward curve given the recent sell off, \
                            we would not interpret that as a signal to buy long-dated oil. Historically, once the storage \
                            arbitrage that connects spot to forward prices is no longer needed, bear markets typically \
                            end with a sharp sell-off in long-dated prices that creates a shift in producer and investor \
                            behavior.", style={"padding-bottom": "5px"}),
                    html.P("A sharper decline in US production than we expect or a more limited increase in OPEC \
                            production could require an earlier recovery in US production. However we see several \
                            potential catalysts for an even later required increase in US production such as weaker \
                            global demand and more resilient non-OPEC ex. US production (as long as storage \
                            capacity isn\'t breached). Further, the consequence of this New Oil Order is that any \
                            sustainable price rally can quickly impact forward fundamentals. This spring\'s rally did \
                            prove to be self-defeating as reopened capital markets lead to producers redeploying rigs \
                            (Exhibit 17) 5 . This reinforces our conviction that sustainability low spot and forward prices \
                            are required until there is greater confidence that US shale growth is indeed required.", style={"padding-bottom": "15px"}),
                    html.Div([
                        #Page 11 Exhibits
                        html.Div([
                            html.Strong("Exhibit 17: US producers ramped up activity once funding markets reopened"),
                            html.P("Energy share of HY US debt issuance (rhs), monthly change in the US oil rig count (lhs)", style={"font-size": "11"}),
                        ], className="title twelve columns"),
                        html.Iframe(src="https://plot.ly/~alishobeiri/650.embed?modebar=false&link=false&autosize=true",
                                    className="exhibit twelve columns", style={'padding-right':'150px', 'position': 'relative', 'bottom': '15px'}, seamless="seamless", height="300"),
                    ], className="twelve columns", style={'margin-right':'25px'}),
                    #Page 11 Text
                    html.H6("A later and shallow recovery", style={"padding-bottom": "5px"}),
                    html.P("While we forecast that the supply and demand for the barrels of oil will likely find a balance \
                            by the end of 2016, this doesn\'t mean a sharp rebound in prices will occur quickly as many", style={"padding-bottom": "5px"}),
                ], className = "written-text no-header eight columns"),
            ], className = "subpage"),
            html.A([ 'Print PDF' ],
                   className="button no-print",
                   style=dict(position="absolute", top=-35, right=0)),
        ], className = "page"),

        #Page 12
        html.Div([
            html.Div([
                html.Div([
                    #Page 12 Text
                    html.Ul([
                        dcc.Markdown("other factors will likely weigh on prices, as we argued in *A lost decade reinforces lower for \
                                    longer*, August 6, 2015."),
                    ], style={"margin": "0px", "padding": "0px"}),
                    html.P("As we have noted before, it is important to emphasize that markets have never seen such a \
                            large appreciation in the US dollar at the same time they have seen such a large surplus in \
                            the oil market, exacerbating both the downward pressure on EM commodity importers and \
                            EM commodity production costs. This not only impacts emerging market demand for oil, \
                            Latin American demand in particular, but also lowers the costs to produce oil in these \
                            countries. We find for example that a 10% move in BRL or CAD shifts cash costs by 3% and \
                            5% respectively. The BRL and CAD have weakened year-to-date by 45% and 14%, \
                            respectively, and it is no surprise that 2015 supply growth in regions facing sharp currency \
                            depreciation such as Brazil and Russia have been persistently revised higher by the IEA, by \
                            a cumulative 350 kb/d since March.", style={"padding-bottom": "5px"}),
                    html.P("Further, if operational stress is required with a decline in prices to near $20/bbl, such a drop \
                            would prove transient and help to immediately rebalance the supply and demand for \
                            barrels. However, it would likely do little for the longer-term capital imbalance in the \
                            market. New capital would likely take ownership of higher quality assets and capex would \
                            actually rise again in places like the US. Only expectations for lower prices for longer will \
                            rebalance the capital markets for energy, which creates downside risks to our 2017 price \
                            forecasts as well.", style={"padding-bottom": "5px"}),
                    html.P("Not only will the macro forces such as US dollar appreciation and weaker EM economic \
                            growth keep prices under pressure, but historically markets trade near cash costs until new \
                            incremental higher-cost capacity is needed. In addition, low-cost OPEC producers are likely \
                            to expand capacity now that they have pushed output to capacity. Ultimately, the capital \
                            markets for energy need to be rebalanced through consolidation and capital restructuring."),
                ], className = "written-text no-header eight columns"),
            ], className = "subpage"),
            html.A([ 'Print PDF' ],
                   className="button no-print",
                   style=dict(position="absolute", top=-35, right=0)),
        ], className = "page"),

        #Page 13
        html.Div([
            #Page 13 Exhibits
            html.Div([
                html.Div([
                    html.H1("Balance table breakdown"),
                ], className = "header-text", style={"padding-top": "40px"}),
                html.Div([
                    #html.Br([]),
                    html.Div([
                        html.Strong("Exhibit 18: Global supply-demand balance (thousand barrels per day)"),
                        html.Img(src="http://i.imgur.com/c7PM25P.png",
                                    className="exhibit", style={"padding-bottom": "10px", "margin-top": "15px", "margin-right": "0px"}, width="675"),
                    ], className="row title", style={"padding-left": "0px", "margin-left": "50px", "margin-top": "35px", "font-size": "1.4rem"}),

                ], className = "twelve columns"),
                    html.Div([
                        #html.Br([]),
                        html.Div([
                            html.Strong("Exhibit 19: Global demand estimates (thousand barrels per day)"),
                            html.Img(src="http://i.imgur.com/Pizq3rk.png",
                                        className="exhibit", style={"padding-bottom": "10px", "margin-top": "15px", "margin-right": "0px"}, height="250", width="675"),
                        ], className="row title", style={"padding-left": "0px", "margin-left": "50px", "margin-top": "35px", "font-size": "1.4rem"}),
                ], className = "twelve columns"),
            ], className = "subpage"),
            html.A([ 'Print PDF' ],
                   className="button no-print",
                   style=dict(position="absolute", top=-35, right=0)),
        ], className = "page"),

        #Page 14
        html.Div([
            html.Div([
                html.Div([
                    #Page 14 Exhibits
                    html.Div([
                        html.Strong("Exhibit 20: Global supply estimates (thousand barrels per day)", className="no-header"),
                        html.Img(src="http://i.imgur.com/zdXONlc.png",
                                    className="exhibit", style={"padding-bottom": "10px", "margin-top": "15px", "margin-right": "0px"}, width="675"),
                    ], className="row title no-header", style={"padding-left": "0px", "margin-left": "50px", "margin-top": "35px",
                                                     "font-size": "1.4rem", "margin-top": "45px"}),

                ], className = "twelve columns no-header"),
            ], className = "subpage"),
            html.A([ 'Print PDF' ],
                   className="button no-print",
                   style=dict(position="absolute", top=-35, right=0)),
        ], className = "page"),

])

external_css = ["https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
                "//fonts.googleapis.com/css?family=Raleway:400,300,600",
                "https://codepen.io/alishobeiri/pen/wdXNjV.css?v=plotly",
                "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"]

for css in external_css:
    app.css.append_css({"external_url": css})

external_js = [ "https://code.jquery.com/jquery-3.2.1.min.js",
        "https://codepen.io/plotly/pen/KmyPZr.js" ]

for js in external_js:
    app.scripts.append_script({ "external_url": js })

if __name__ == '__main__':
    app.server.run()
