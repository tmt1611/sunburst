import pandas as pd
import plotly.express as px
import datetime
import plotly.subplots as sp 

if __name__ == "__main__":
    url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTiwummYiOCTzagxsbho_ZAFxTpluojPuF6Ynaxjtato5r965ppSx0ST_XPQuwzxSpP_BcF51VMuprM/pub?output=xlsx'
    # Load the Excel file into a DataFrame
    df = pd.read_excel(url)
    df = df.fillna(method='ffill', limit=1).fillna('')


# Sunburst =======
fig = px.sunburst(
    df,
    names='ID',
    parents='parent',
    values='adjusted_popularity',
    color='value_num',
    hover_data='value',
    branchvalues='total',
    maxdepth = None,
)


# Icicle =========
fig2 = px.icicle(
    df,
    names='ID',
    parents='parent',
    values='adjusted_popularity',
    color='value_num',
    hover_data='value',
    branchvalues='total',
    maxdepth = None,
)

fig2.update_traces(tiling = dict(
            orientation='v'
))


# Create subplots =========
fig3 = sp.make_subplots(rows=1, cols=2, specs=[[{'type': 'domain'}, {'type': 'domain'}]])

# Add traces to subplots
fig3.add_trace(fig.data[0], row=1, col=1)
fig3.add_trace(fig2.data[0], row=1, col=2)

# Update layout
fig3.update_layout(
    margin=dict(t=30, l=10, r=10, b=10),
    annotations=[
        dict(
            x=0,
            y=0,
            xref='paper',
            yref='paper',
            text='Generated on ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            showarrow=False,
            font=dict(size=14),
            bgcolor='rgba(255, 255, 255, 1)',
            bordercolor='rgba(0, 0, 0, 0)',
            borderwidth=1,
            borderpad=4,
            align='left'
        )
    ]
)

fig3.write_html("index.html", include_plotlyjs="cdn")
