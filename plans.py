import folium
import json
from shapely import geometry
#from shapely.ops import cascaded_union
from shapely.ops import unary_union
from geojson import Point, Feature, FeatureCollection, dump

regions=['Unknown','EU868','US915','CN779','AU915','AS923-1','AS923-1B','AS923-2','AS923-3','AS923-4','KR920','IN865','RU864','EU433','CN470']

colors={'Unknown':'white',
        'EU868':'yellow',
        'US915':'blue',
        'CN779':'red',
        'AU915':'seagreen',
        'CN470':'red',
        'AS923-1':'lawngreen',
        'AS923-1B':'mistyrose',
        'AS923-2':'lightgrey',
        'AS923-3':'lightskyblue',
        'AS923-4':'darkblue',
        'KR920':'pink',
        'IN865':'purple',
        'RU864':'orange',
        'EU433':'brown' }

m = folium.Map([51,-102], tiles='stamentoner', zoom_start=5,control_scale=True,max_zoom=10)#,crs='EPSG4326')
region=[]
style={}
for rfplan in regions:
    try:
        print(rfplan)
        gjfile=open(rfplan+'.geojson', 'r', encoding="utf8")
        gjland = json.loads(gjfile.read())
    except FileNotFoundError as ex:
        print('File not Found', rfplan)
        continue
    polygons=[]
    for area in gjland['features']:
        if (area['geometry']['type'] == 'MultiPolygon'):
            for poly in area['geometry']['coordinates']:
                poly=geometry.Polygon(poly[0])
                polygons.append(poly)
        else:
            poly=geometry.Polygon(area['geometry']['coordinates'][0])
            polygons.append(poly)
    # take the list of polygons for a region and combine them into one polygon
    combined=unary_union(polygons)
    style_function = lambda color : (lambda feature: dict(color=color))# weight=2, opacity=0.6))
    folium.GeoJson(combined, style_function=style_function(colors[rfplan])).add_to(m)
    region.append(Feature(geometry=combined, properties={'region':rfplan,'fill':colors[rfplan]}))

feature_collection = FeatureCollection(region)
with open('regions.geojson', 'w') as f:
   dump(feature_collection, f)
   
m.save('plans.html')

