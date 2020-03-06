import json

in_file = open("eq_data_30_day_m1.json","r")
out_file = open("readable_eq_data.json", "w")

eq_data = json.load(in_file) 


json.dump(eq_data, out_file, indent=4) 

list_of_eqs = eq_data["features"]


print(len(list_of_eqs))
mags, lons, lats = [],[],[]

for eq in list_of_eqs:
    mag = eq["properties"]["mag" ]
    lon = eq["geometry"]["coordinates"][0]
    lat = eq["geometry"]["coordinates"][1]
    hover_texts = eq["properties"]["title"] 
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10]) 
from plotly.graph_objs import Scattergeo, Layout 
from plotly import offline 
print(type(mags))

'''
data = [{ ### created dictionary to customize size of dots on map
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker':{
        'size':[5*mag for mag in mags],## magnifies size of each dot 5 times
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar' : {'title':'Magnitude'} ## gives the little color thing on the side 
        },
}]

my_layout = Layout(title = "Global Earthquakles")

fig = {"data": data, "layout":my_layout}

offline.plot(fig,filename="global_earthquakes.html")'''