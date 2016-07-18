from django.shortcuts import render
from plotly.graph_objs import Bar, Scatter, Figure, Layout
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from django.http import HttpResponse
from django.template import Context, loader, Template
from django.template.loader import get_template
from django.shortcuts import render

""" Create a plotly graph locally as an HTML document or string.
    Example:
    ```
    from plotly.offline import plot
    import plotly.graph_objs as go
    plot([go.Scatter(x=[1, 2, 3], y=[3, 2, 6])], filename='my-graph.html')
    # We can also download an image of the plot by setting the image parameter
    # to the image format we want
    plot([go.Scatter(x=[1, 2, 3], y=[3, 2, 6])], filename='my-graph.html'
         image='jpeg')
    ```
    More examples below.
    figure_or_data -- a plotly.graph_objs.Figure or plotly.graph_objs.Data or
                      dict or list that describes a Plotly graph.
                      See https://plot.ly/python/ for examples of
                      graph descriptions.
    Keyword arguments:
    show_link (default=True) -- display a link in the bottom-right corner of
        of the chart that will export the chart to Plotly Cloud or
        Plotly Enterprise
    link_text (default='Export to plot.ly') -- the text of export link
    validate (default=True) -- validate that all of the keys in the figure
        are valid? omit if your version of plotly.js has become outdated
        with your version of graph_reference.json or if you need to include
        extra, unnecessary keys in your figure.
    output_type ('file' | 'div' - default 'file') -- if 'file', then
        the graph is saved as a standalone HTML file and `plot`
        returns None.
        If 'div', then `plot` returns a string that just contains the
        HTML <div> that contains the graph and the script to generate the
        graph.
        Use 'file' if you want to save and view a single graph at a time
        in a standalone HTML file.
        Use 'div' if you are embedding these graphs in an HTML file with
        other graphs or HTML markup, like a HTML report or an website.
    include_plotlyjs (default=True) -- If True, include the plotly.js
        source code in the output file or string.
        Set as False if your HTML file already contains a copy of the plotly.js
        library.
    filename (default='temp-plot.html') -- The local filename to save the
        outputted chart to. If the filename already exists, it will be
        overwritten. This argument only applies if `output_type` is 'file'.
    auto_open (default=True) -- If True, open the saved file in a
        web browser after saving.
        This argument only applies if `output_type` is 'file'.
    image (default=None |'png' |'jpeg' |'svg' |'webp') -- This parameter sets
        the format of the image to be downloaded, if we choose to download an
        image. This parameter has a default value of None indicating that no
        image should be downloaded.
    image_filename (default='plot_image') -- Sets the name of the file your image
        will be saved to. The extension should not be included.
    image_height (default=600) -- Specifies the height of the image in `px`.
    image_width (default=800) -- Specifies the width of the image in `px`.
    """

def plot_p(request):
    scatter_diag = plot([Scatter(x=[1, 2, 3], y=[3, 1, 6])], filename='my-graph.html', auto_open=False, output_type='div')
    bar_diag = plot([Bar(x=['1', '2', '3'], y=[13, 10, 50])], filename='my-bar.html', auto_open=False, output_type='div')
    fig = {
		'data': [{'labels': ['Residential', 'Non-Residential', 'Utility'],
		'values': [19, 26, 55],
		'type': 'pie'}],
		'layout': {'title': 'Event Comparison'}
		}
    pie_chart = plot(fig, filename='my-pie.html', auto_open=False, output_type='div')
    utf8 = [scatter_diag, u'<br>', bar_diag, u'<br>', pie_chart]
    html = ''.join(utf8) #str(scatter_diag) + u'<br>' + str(bar_diag) + u'<br>' + str(pie_chart)
    return HttpResponse(html)