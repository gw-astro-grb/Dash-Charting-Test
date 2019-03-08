from astropy.io import fits
import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np

RSP_FILE_PATH = './glg_tte_n9_bn160625945_v00.fit'

app = dash.Dash(__name__)

def main():
    hdu_n9 = fits.open(RSP_FILE_PATH)

    # Show all tables in fits file

    # print(len(time))
    time = hdu_n9[2].data['TIME']
    pha = hdu_n9[2].data['PHA']

    # >>> len(hdu_n9[2].data['TIME'])
    # 923894
    # >>> len(hdu_n9[2].data['PHA'])
    
    colors = {
        'background': '#111111',
        'text': '#7FDBFF'
    }
    app.layout = html.Div(style={
        'backgroundColor': colors['background']
        }, 
        children=[
            html.H1(
                children='Counts by Time',
                style={
                    'textAlign': 'center',
                    'color': colors['text']
                }
            ),
            dcc.Graph(
                id='Graph1',
                figure={
                    'data': [
                        {
                            'x': time,
                            'type': 'histogram'
                        }
                    ],
                    'layout': {
                        'xaxis': {
                            'title': 'Time'
                        },
                        'yaxis': {
                            'title': 'Hits'
                        },
                        'plot_bgcolor': colors['background'],
                        'paper_bgcolor': colors['background'],
                        'font':{
                            'color': colors['text']
                        }
                    }
                }
            ),
            html.H1(
                children='Counts by Energy Bin',
                style={
                    'textAlign': 'center',
                    'color': colors['text']
                }
            ),
            dcc.Graph(
                id='Graph2',
                figure={
                    'data': [
                        {
                            'x': pha,
                            'type': 'histogram'
                        }
                    ],
                    'layout': {
                        'xaxis': {
                            'title': 'Energy Bins'
                        },
                        'yaxis': {
                            'title': 'Hits'
                        },
                        'plot_bgcolor': colors['background'],
                        'paper_bgcolor': colors['background'],
                        'font':{
                            'color': colors['text']
                        }
                    }
                }
            )
        ]
    )
    app.run_server(debug=True)

if __name__ == "__main__":
    main()
