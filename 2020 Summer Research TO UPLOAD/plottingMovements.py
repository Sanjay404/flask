#https://plotly.com/python/lines-on-maps/#performance-improvement-put-many-lines-in-the-same-trace

import plotly.graph_objects as go
import pandas as pd
import os
 
# Reading in Data
directory = r'/Users/sanjay/Desktop/CODE/Python/2020 Summer Research/Data' #what does r do
for file in os.listdir(directory):
    if filename.endswith(".csv")
        ALL_DATA.append(pd.read_csv(str(directory)+str(file)))
    else:
        continue

print('Number of birds I am looking at: '+ str((len(ALL_DATA['LAT'].values)-1)))

df_airports = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_february_us_airport_traffic.csv')
df_airports.head()

df_flight_paths = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_february_aa_flight_paths.csv')
df_flight_paths.head()

fig = go.Figure()

fig.add_trace(go.Scattergeo(
    locationmode = 'Africa',
    lon = df_airports['LONG'],
    lat = df_airports['LAT'],
    hoverinfo = 'text',
    text = df_airports['airport'],
    mode = 'markers',
    marker = dict(
        size = 2,
        color = 'rgb(255, 0, 0)',
        line = dict(
            width = 3,
            color = 'rgba(68, 68, 68, 0)'
        )
    )))

flight_paths = []
lons = []
lats = []
import numpy as np
lons = np.empty(3 * len(df_flight_paths))
lons[::3] = df_flight_paths['start_lon']
lons[1::3] = df_flight_paths['end_lon']
lons[::3] = None
lats = np.empty(3 * len(df_flight_paths))
lats[::3] = df_flight_paths['start_lat']
lats[1::3] = df_flight_paths['end_lat']
lats[::3] = None

fig.add_trace(
    go.Scattergeo(
        locationmode = 'USA-states',
        lon = lons,
        lat = lats,
        mode = 'lines',
        line = dict(width = 1,color = 'red'),
        opacity = 0.5 
    )
)

fig.update_layout(
    title_text = 'Feb. 2011 American Airline flight paths<br>(Hover for airport names)',
    showlegend = False,
    geo = go.layout.Geo(
        scope = 'Africa',
        projection_type = 'azimuthal equal area',
        showland = True,
        landcolor = 'rgb(243, 243, 243)',
        countrycolor = 'rgb(204, 204, 204)',
    ),
    height=700,
)

fig.show()