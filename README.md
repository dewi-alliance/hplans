# hplans
hplans is a geojson representation of the LoRaWAN regional parameter channel plans. It is based off of [RP2-1.0.3 LoRaWAN Regional Parameters](https://lora-alliance.org/resource_hub/rp2-1-0-3-lorawan-regional-parameters/) from the LoRaWAN Alliance as well as [Helium Network's country definitions](https://github.com/helium/miner/blob/master/priv/countries_reg_domains.csv). 

The geojson does not contain the channel plan and spectrum definitions but only the geographic regions they apply to.

## what is needed for?
These regions are used to determine what channel plan hotspots should be using. When a hotspot's location is asserted the LoRaWAN region is looked up and set depending on its location. 

## how does it work?
These geojson regions are used by lorawan-h3 to generate binary lists of Uber h3 hex
https://github.com/helium/lorawan-h3

h3idx files are created which contain a binary list of user h3 hexes for each region. These files are used by the miner to determine which plan to use. 

## how was it created?
The dataset was originally download from https://osm-boundaries.com/ based off the regions.csv file using getgeojson.py(this code is no longer used but moved to archive). Each LoRaWAN region is captured in its own file by country.

regions.geojson contains all regions. It is created by running plans.py which takes each region file and runs unary_union function to merge all neighbouring polygons with the same region and combines them all into a single file. 


## how do i make an update?
### moving or updating a countries borders
The country/regions geographic borders are stored as stardard geojson. Each country is stored as a geojson polygon or multipolygon within their appropriate LoRaWAN region file. The geojson can be modified with GIS tools, online geojson editors, mapshaper, etc. The whole region file may be too large to work with so the country of interest's polygon can be put in its own file while being worked on and then merged back into its region file

### changing a country LoRaWAN region
The regions.csv should be updated even though it is only used as an index at this point and then simply move the polygon from its orginal LoRaWAN region to its new one.

Once the borders have been updated or country moved to a new region file plans.py should be run which will simplify with unary_union and combine all the regions into one file.
