import folium
import json
from shapely import geometry
#from shapely.ops import cascaded_union
from shapely.ops import unary_union
from geojson import Point, Feature, FeatureCollection, dump


'''
regions=['EU868','US915','CN779','AU915','AS923-1','AS923-2','AS923-3','KR920','IN865','RU864'] #'EU433','CN470'
colors={'EU868':'yellow',
        'US915':'blue',
        'CN779':'red',
        'AU915':'seagreen',
        'CN470':'green',
        'AS923-1':'lawngreen',
        'AS923-2':'lightgrey',
        'AS923-3':'lightskyblue',
        'KR920':'pink',
        'IN865':'purple',
        'RU864':'orange',
        'EU433':'brown'}
m = folium.Map([51,-102], tiles='stamentoner', zoom_start=5,control_scale=True,max_zoom=10)#,crs='EPSG4326')
polygons=[]
region=[]
for rfplan in regions:
    gjfile=open(rfplan+'.geojson', 'r', encoding="utf8")
    gjland = json.loads(gjfile.read())

    for area in gjland['features']:
        if (area['geometry']['type'] == 'MultiPolygon'):

            for poly in area['geometry']['coordinates']:
                poly=geometry.Polygon(poly[0])
                polygons.append(poly)
        else:
            poly=geometry.Polygon(area['geometry']['coordinates'][0])
            polygons.append(poly)
    combined=unary_union(polygons)
    style = {'color': colors[rfplan]}
    print(colors[rfplan])
    folium.GeoJson(combined, style_function=lambda x: style).add_to(m)
    region.append(Feature(geometry=combined, properties={'region':rfplan,'fill':colors[rfplan]}))


feature_collection = FeatureCollection(region)
with open('regions.geojson', 'w') as f:
   dump(feature_collection, f)
   
print('end')
m.save('regions.html')
'''


m = folium.Map([51,-102], tiles='stamentoner', zoom_start=5,control_scale=True,max_zoom=20)#,crs='EPSG4326')

gjfile=open('Unknown.geojson', 'r', encoding="utf8")
gjland = json.loads(gjfile.read())

style1 = {'color': 'white'}
polygons=[]
region=[]
for area in gjland['features']:
    if (area['geometry']['type'] == 'MultiPolygon'):

        for poly in area['geometry']['coordinates']:
            poly=geometry.Polygon(poly[0])
            polygons.append(poly)

    else:
        poly=geometry.Polygon(area['geometry']['coordinates'][0])
        polygons.append(poly)

combined=unary_union(polygons)
folium.GeoJson(combined, style_function=lambda x: style1).add_to(m)
region.append(Feature(geometry=combined, properties={'region':'Unknown','fill':'white'}))


gjfile=open('EU433.geojson', 'r', encoding="utf8")
gjland = json.loads(gjfile.read())
polygons=[]
style1 = {'color': 'brown'}
for area in gjland['features']:
    if (area['geometry']['type'] == 'MultiPolygon'):

        for poly in area['geometry']['coordinates']:
            poly=geometry.Polygon(poly[0])
            polygons.append(poly)

    else:
        poly=geometry.Polygon(area['geometry']['coordinates'][0])
        polygons.append(poly)

combined=unary_union(polygons)
folium.GeoJson(combined, style_function=lambda x: style1).add_to(m)
region.append(Feature(geometry=combined, properties={'region':'EU433','fill':'brown'}))


gjfile=open('AS923-1.geojson', 'r', encoding="utf8")
gjland = json.loads(gjfile.read())

style1 = {'color': 'seagreen'}
polygons=[]
for area in gjland['features']:
    if (area['geometry']['type'] == 'MultiPolygon'):

        for poly in area['geometry']['coordinates']:
            poly=geometry.Polygon(poly[0])
            polygons.append(poly)

    else:
        poly=geometry.Polygon(area['geometry']['coordinates'][0])
        polygons.append(poly)

combined=unary_union(polygons)
folium.GeoJson(combined, style_function=lambda x: style1).add_to(m)
region.append(Feature(geometry=combined, properties={'region':'AS923-1','fill':'green'}))


gjfile=open('AS923-2.geojson', 'r', encoding="utf8")
gjland = json.loads(gjfile.read())
polygons=[]
style2 = {'color': 'lawngreen'}
for area in gjland['features']:
    if (area['geometry']['type'] == 'MultiPolygon'):

        for poly in area['geometry']['coordinates']:
            poly=geometry.Polygon(poly[0])

            polygons.append(poly)
    else:
        poly=geometry.Polygon(area['geometry']['coordinates'][0])
        polygons.append(poly)

combined=unary_union(polygons)
folium.GeoJson(combined, style_function=lambda x: style2).add_to(m)
region.append(Feature(geometry=combined, properties={'region':'AS923-2','fill':'lawngreen'}))


gjfile=open('AU915.geojson', 'r', encoding="utf8")
gjland = json.loads(gjfile.read())
polygons=[]
style3 = {'color': 'orange'}
for area in gjland['features']:
    if (area['geometry']['type'] == 'MultiPolygon'):

        for poly in area['geometry']['coordinates']:
            poly=geometry.Polygon(poly[0])
            polygons.append(poly)

    else:
        poly=geometry.Polygon(area['geometry']['coordinates'][0])
        polygons.append(poly)

combined=unary_union(polygons)
folium.GeoJson(combined, style_function=lambda x: style3).add_to(m)
region.append(Feature(geometry=combined, properties={'region':'AU915','fill':'orange'}))

gjfile=open('CN779.geojson', 'r', encoding="utf8")
gjland = json.loads(gjfile.read())
polygons=[]
style4 = {'color': 'red'}
for area in gjland['features']:
    if (area['geometry']['type'] == 'MultiPolygon'):

        for poly in area['geometry']['coordinates']:
            poly=geometry.Polygon(poly[0])
            polygons.append(poly)

    else:
        poly=geometry.Polygon(area['geometry']['coordinates'][0])
        polygons.append(poly)

combined=unary_union(polygons)
folium.GeoJson(combined, style_function=lambda x: style4).add_to(m)
region.append(Feature(geometry=combined, properties={'region':'CN779','fill':'red'}))

    
gjfile=open('EU868.geojson', 'r', encoding="utf8")
gjland = json.loads(gjfile.read())
polygons=[]
style5 = {'color': 'yellow'}
for area in gjland['features']:
    if (area['geometry']['type'] == 'MultiPolygon'):

        for poly in area['geometry']['coordinates']:
            poly=geometry.Polygon(poly[0])
            polygons.append(poly)

    else:
        poly=geometry.Polygon(area['geometry']['coordinates'][0])
        polygons.append(poly)

combined=unary_union(polygons)
folium.GeoJson(combined, style_function=lambda x: style5).add_to(m)
region.append(Feature(geometry=combined, properties={'region':'EU868','fill':'yellow'}))
    
gjfile=open('IN865.geojson', 'r', encoding="utf8")
gjland = json.loads(gjfile.read())
polygons=[]
style5 = {'color': 'lightskyblue'}
for area in gjland['features']:
    if (area['geometry']['type'] == 'MultiPolygon'):

        for poly in area['geometry']['coordinates']:
            poly=geometry.Polygon(poly[0])
            polygons.append(poly)

    else:
        poly=geometry.Polygon(area['geometry']['coordinates'][0])
        polygons.append(poly)

combined=unary_union(polygons)
folium.GeoJson(combined, style_function=lambda x: style5).add_to(m)
region.append(Feature(geometry=combined, properties={'region':'IN865','fill':'lightskyblue'}))

gjfile=open('KR920.geojson', 'r', encoding="utf8")
gjland = json.loads(gjfile.read())
polygons=[]
style6 = {'color': 'lightgrey'}
for area in gjland['features']:
    if (area['geometry']['type'] == 'MultiPolygon'):

        for poly in area['geometry']['coordinates']:
            poly=geometry.Polygon(poly[0])
            polygons.append(poly)

    else:
        poly=geometry.Polygon(area['geometry']['coordinates'][0])
        polygons.append(poly)

combined=unary_union(polygons)
folium.GeoJson(combined, style_function=lambda x: style6).add_to(m)
region.append(Feature(geometry=combined, properties={'region':'KR920','fill':'lightgrey'}))


gjfile=open('RU864.geojson', 'r', encoding="utf8")
gjland = json.loads(gjfile.read())
polygons=[]
style6 = {'color': 'pink'}
for area in gjland['features']:
    if (area['geometry']['type'] == 'MultiPolygon'):

        for poly in area['geometry']['coordinates']:
            poly=geometry.Polygon(poly[0])
            polygons.append(poly)

    else:
        poly=geometry.Polygon(area['geometry']['coordinates'][0])
        polygons.append(poly)

combined=unary_union(polygons)
folium.GeoJson(combined, style_function=lambda x: style6).add_to(m)
region.append(Feature(geometry=combined, properties={'region':'RU864','fill':'pink'}))


gjfile=open('US915.geojson', 'r', encoding="utf8")
gjland = json.loads(gjfile.read())

#style7 = {'fillColor': 'blue', 'color': '#ffffbf'}
style7 = {'color': 'blue'}
polygons=[]
for area in gjland['features']:
    if (area['geometry']['type'] == 'MultiPolygon'):

        for poly in area['geometry']['coordinates']:
            poly=geometry.Polygon(poly[0])
            polygons.append(poly)
    else:
        poly=geometry.Polygon(area['geometry']['coordinates'][0])
        polygons.append(poly)

combined=unary_union(polygons)
folium.GeoJson(combined, style_function=lambda x: style7).add_to(m)
region.append(Feature(geometry=combined, properties={'region':'US915','fill':'blue'}))

feature_collection = FeatureCollection(region)
with open('regions.geojson', 'w') as f:
   dump(feature_collection, f)
   
print('end')
m.save('plans.html')
