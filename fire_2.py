import csv

open_file = open("MODIS_C6_Australia_NewZealand_MCD14DL_NRT_2020026.txt","r") 
readFile = csv.reader(open_file, delimiter =",")
JanuaryData = [row for row in readFile]

brigs, lons, lats = [],[],[] 
headers = JanuaryData[0]

JanuaryData_noheaders = JanuaryData[1:868]   

lats = [x[0] for x in JanuaryData_noheaders]
lons = [x[1] for x in JanuaryData_noheaders]
brigs = [x[2] for x in JanuaryData_noheaders]


from plotly.graph_objs import Scattergeo, Layout 
from plotly import offline


'''scl = [300,"rgb(0, 152, 255)"],[320,"rgb(44, 255, 150)"],[340,"rgb(151, 255, 0)"],\
[380,"rgb(255, 234, 0)"],[400,"rgb(255, 111, 0)"],[440,"rgb(255, 0, 0)"]'''

brigs = [float(x) for x in brigs]


data = [{ 
    'type': 'scattergeo',
    'lat': lats,
    'lon': lons,
    'marker':{
        'size':[.05*brig for brig in brigs],
        'color': brigs,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar' : {'title':'Brightness'} 
        },
}]

my_layout = Layout(title = "Australian Fires - January 2020", \
    geo = dict( 
        showland = True,
        lataxis = dict(range=[-37,-13]),
        lonaxis = dict(range=[111,160])
    ))

fig = {"data": data, "layout":my_layout}

offline.plot(fig,filename="january_fires.html")