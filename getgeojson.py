import csv
import requests
import gzip

#openstreetmaps api key
apikey='xxxxxxxxxxxxxxxxxxxxxxxxxxxx'
osmids={}

with open('regions.csv', newline='') as f:
    reader = csv.reader(f)
    regions = list(reader)
f.close()
regions=regions[1:]
#print(regions)


for region in regions:
    code,lat,lng,country,region,region2,region3,zone,osmindex=region
    try:
        if osmindex=='':
            continue
        else:
            osmids[region]=osmids[region]+osmindex+','
    except KeyError:
        print('keyerror')
        osmids[region]=osmindex+','
#print(osmids)

for region in osmids:
    url = "https://osm-boundaries.com/Download/Submit?apiKey="+apikey+"&db=osm20210104&osmIds="+osmids[region]
    #print(url)
    data=requests.get(url=url)

    # save the gzip to disk
    open(region+'.geojson.gz', 'wb').write(data.content)

    # open it and unzip it
    f=gzip.open(region+'.geojson.gz','rb')
    file_content=f.read()
    f.close()

    # write it back to disk
    open(region+'.geojson', 'wb').write(file_content)



