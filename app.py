# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

app = Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#7FDBFF',
}

font_family={
    'font': 'sans-serif'
}
# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Languajes": ["Javascript", "Java", "Python"],
    "Amount": [4, 2, 3],
    "Frameworks": ["Angular","Spring","Django"]
})

fig = px.bar(df, x="Languajes",y="Amount", color="Frameworks", barmode="group")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(style={'backgroundColor': colors['background'], 'fontFamily': font_family['font']}, children=[
    html.H1(
        children='My Stack',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='it is my stack', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-2',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
