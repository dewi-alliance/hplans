import folium
import json
from shapely import geometry
#from shapely.ops import cascaded_union
from shapely.ops import unary_union
from geojson import Point, Feature, FeatureCollection, dump



m = folium.Map([51,-102], tiles='stamentoner', zoom_start=5,control_scale=True,max_zoom=20)#,crs='EPSG4326')

gjfile=open('AS920-923-AS1.geojson', 'r')
gjland = json.loads(gjfile.read())


style1 = {'color': 'seagreen'}
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
region.append(Feature(geometry=combined, properties={'region':'AS1','fill':'green'}))


gjfile=open('AS923-925-AS2.geojson', 'r')
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
region.append(Feature(geometry=combined, properties={'region':'AS2','fill':'lawngreen'}))


gjfile=open('AU915-928.geojson', 'r')
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

gjfile=open('CN779-787.geojson', 'r')
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

    
gjfile=open('EU863-870.geojson', 'r')
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
region.append(Feature(geometry=combined, properties={'region':'EU863','fill':'yellow'}))
    
gjfile=open('IN865-867.geojson', 'r')
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

gjfile=open('KR920-923.geojson', 'r')
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

gjfile=open('US902-930.geojson', 'r')
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
region.append(Feature(geometry=combined, properties={'region':'US902','fill':'blue'}))

feature_collection = FeatureCollection(region)
with open('regions.geojson', 'w') as f:
   dump(feature_collection, f)
   
print('end')
m.save('plans.html')
