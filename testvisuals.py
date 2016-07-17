import pandas
import numpy
import plotly.plotly as py
import plotly.graph_objs as go

# Import data from csv
data = pandas.read_csv('data2.csv')
print data

trace1 = go.Scatter(
                    x=data['x'], y=data['logx'], # Data
                    mode='lines', name='logx' # Additional options
                   )
trace2 = go.Scatter(x=data['x'], y=data['sin'], mode='lines', name='sin' )
trace3 = go.Scatter(x=data['x'], y=data['cosx'], mode='lines', name='cosx')

layout = go.Layout(title='Simple Plot from csv data',
                   plot_bgcolor='rgb(230, 230,230)')

fig = go.Figure(data=[trace1, trace2, trace3], layout=layout)

# Plot data in the notebook
py.plot(fig, filename='simple-plot-from-csv')

