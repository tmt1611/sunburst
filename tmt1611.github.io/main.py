import pandas as pd

# Replace 'your_link_to_csv' with the actual URL of the CSV file
url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTiwummYiOCTzagxsbho_ZAFxTpluojPuF6Ynaxjtato5r965ppSx0ST_XPQuwzxSpP_BcF51VMuprM/pub?output=xlsx'

# Load the Excel file into a DataFrame
df = pd.read_excel(url)
df = df.fillna(method='ffill', limit=1).fillna('')

# Discribe the DataFrame
# df.head()

import plotly.express as px
fig = px.sunburst(
    df,
    names='ID',
    parents='parent',
    values='adjusted_popularity',
    color='value_num',
    hover_data='value',
    branchvalues='total',
    maxdepth = None
)
fig.update_layout(
    margin = dict(t=10, l=10, r=10, b=10)
)
# fig.update_traces(insidetextorientation='radial')
fig.show()