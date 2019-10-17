from nbconvert import HTMLExporter
from bs4 import BeautifulSoup

# Reading

# this can be use to read from github
# from urllib.request import urlopen
# url = 'http://jakevdp.github.com/downloads/notebooks/XKCD_plots.ipynb'
# response = urlopen(url).read().decode()


import nbformat

notebook = None
with open('notebook.ipynb', 'r') as f:
    data = f.read()
    notebook = nbformat.reads(data, as_version=4)

# Instantiate the exporter. We use the `basic` template for now; we'll get into more details
# later about how to customize the exporter further.
html_exporter = HTMLExporter()
html_exporter.template_file = 'basic'

# Process the notebook we loaded earlier
(body, resources) = html_exporter.from_notebook_node(notebook)

# print(body)  # HTML basic

soup = BeautifulSoup(body, 'html.parser')

pres = soup.find_all('pre')

# soup.find("div")['class'] = "green_titles"
# replace class 'cell' to class 'w3cell'
# cell class: w3-row w3-white w3-padding-small
for cell in soup.find_all('div', class_='cell'):
    #print(cell)
    pos = cell.attrs['class'].index('cell')
    cell.attrs['class'][pos] = 'w3cell'
    #input('Press Enter...')

# mydivs = soup.findAll("div", {"class": "w3cell"})
# print(mydivs)

mydivs = soup.findAll("div", {"class": "highlight"})
print(mydivs)

