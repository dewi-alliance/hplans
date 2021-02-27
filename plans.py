import folium
import json
from shapely import geometry
import h3

m = folium.Map([51,-102], tiles='stamentoner', zoom_start=5,control_scale=True,max_zoom=20)#,crs='EPSG4326')

gjfile=open('AS920-923-AS1.geojson', 'r')
gjland = json.loads(gjfile.read())


style1 = {'color': 'seagreen'}

for area in gjland['features']:
    if (area['geometry']['type'] == 'MultiPolygon'):

        for poly in area['geometry']['coordinates']:
            poly=geometry.Polygon(poly[0])
            folium.GeoJson(poly, style_function=lambda x: style1).add_to(m)
    else:
        poly=geometry.Polygon(area['geometry']['coordinates'][0])
        folium.GeoJson(poly, style_function=lambda x: style1).add_to(m)
         
m.save('AS920-923-AS1.html')


gjfile=open('AS923-925-AS2.geojson', 'r')
gjland = json.loads(gjfile.read())

style2 = {'color': 'lawngreen'}
for area in gjland['features']:
    if (area['geometry']['type'] == 'MultiPolygon'):

        for poly in area['geometry']['coordinates']:
            poly=geometry.Polygon(poly[0])
            folium.GeoJson(poly, style_function=lambda x: style2).add_to(m)
    else:
        poly=geometry.Polygon(area['geometry']['coordinates'][0])
        folium.GeoJson(poly, style_function=lambda x: style2).add_to(m)


gjfile=open('AU915-928.geojson', 'r')
gjland = json.loads(gjfile.read())

style3 = {'color': 'orange'}
for area in gjland['features']:
    if (area['geometry']['type'] == 'MultiPolygon'):

        for poly in area['geometry']['coordinates']:
            poly=geometry.Polygon(poly[0])
            folium.GeoJson(poly, style_function=lambda x: style3).add_to(m)
    else:
        poly=geometry.Polygon(area['geometry']['coordinates'][0])
        folium.GeoJson(poly, style_function=lambda x: style3).add_to(m)


gjfile=open('CN779-787.geojson', 'r')
gjland = json.loads(gjfile.read())

style4 = {'color': 'red'}
for area in gjland['features']:
    if (area['geometry']['type'] == 'MultiPolygon'):

        for poly in area['geometry']['coordinates']:
            poly=geometry.Polygon(poly[0])
            folium.GeoJson(poly, style_function=lambda x: style4).add_to(m)
    else:
        poly=geometry.Polygon(area['geometry']['coordinates'][0])
        folium.GeoJson(poly, style_function=lambda x: style4).add_to(m)

    
gjfile=open('EU863-870.geojson', 'r')
gjland = json.loads(gjfile.read())

style5 = {'color': 'yellow'}
for area in gjland['features']:
    if (area['geometry']['type'] == 'MultiPolygon'):

        for poly in area['geometry']['coordinates']:
            poly=geometry.Polygon(poly[0])
            folium.GeoJson(poly, style_function=lambda x: style5).add_to(m)
    else:
        poly=geometry.Polygon(area['geometry']['coordinates'][0])
        folium.GeoJson(poly, style_function=lambda x: style5).add_to(m)

    
gjfile=open('IN865-867.geojson', 'r')
gjland = json.loads(gjfile.read())

style5 = {'color': 'lightskyblue'}
for area in gjland['features']:
    if (area['geometry']['type'] == 'MultiPolygon'):

        for poly in area['geometry']['coordinates']:
            poly=geometry.Polygon(poly[0])
            folium.GeoJson(poly, style_function=lambda x: style5).add_to(m)
    else:
        poly=geometry.Polygon(area['geometry']['coordinates'][0])
        folium.GeoJson(poly, style_function=lambda x: style5).add_to(m)

gjfile=open('KR920-923.geojson', 'r')
gjland = json.loads(gjfile.read())

style6 = {'color': 'lightgrey'}
for area in gjland['features']:
    if (area['geometry']['type'] == 'MultiPolygon'):

        for poly in area['geometry']['coordinates']:
            poly=geometry.Polygon(poly[0])
            folium.GeoJson(poly, style_function=lambda x: style6).add_to(m)
    else:
        poly=geometry.Polygon(area['geometry']['coordinates'][0])
        folium.GeoJson(poly, style_function=lambda x: style6).add_to(m)   


gjfile=open('US902-930.geojson', 'r')
gjland = json.loads(gjfile.read())

#style7 = {'fillColor': 'blue', 'color': '#ffffbf'}
style7 = {'color': 'blue'}
for area in gjland['features']:
    if (area['geometry']['type'] == 'MultiPolygon'):

        for poly in area['geometry']['coordinates']:
            poly=geometry.Polygon(poly[0])
            folium.GeoJson(poly, style_function=lambda x: style7).add_to(m)
    else:
        poly=geometry.Polygon(area['geometry']['coordinates'][0])
        folium.GeoJson(poly, style_function=lambda x: style7).add_to(m)

print('end')
m.save('map.html')
