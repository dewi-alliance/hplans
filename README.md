# hplans
hplans is a geojson representation of the LoRaWAN regional parameter channel plans. It is based on the LoRaWAN Alliance's [RP2-1.0.4 LoRaWAN Regional Parameters](https://resources.lora-alliance.org/technical-specifications/rp002-1-0-4-regional-parameters), as well as the [Helium Network's country definitions](https://github.com/helium/miner/blob/master/priv/countries_reg_domains.csv). 

The geojson does not contain the channel plan and spectrum definitions; it only contains the geographic regions they apply to.

## Why is this data needed?
These regions are used to determine what channel plan hotspots should be using. When a hotspot's location is asserted, the LoRaWAN region is looked up and set depending on its location. 

## How does it work?
These geojson regions are used by [lorawan-h3](https://github.com/helium/lorawan-h3) to generate binary lists of Uber h3 hex areas with associated regions.

h3idx files are created, which contain a binary list of user h3 hexes for each region. These files are used by the miner to determine which plan to use. 

## How was it created?
The dataset was originally download from https://osm-boundaries.com/, and based off the `regions.csv` file using `getgeojson.py`. This code is no longer used, and was moved to the repo's `archive` folder. Each LoRaWAN region is captured in its own file by country.

`regions.geojson` contains all regions. It is created by running `plans.py`, which takes each region file, runs the `unary_union` function to merge all neighbouring polygons with the same region, and combines them all into a single file. 


## How do I make an update?
### Moving or Updating a Country's Borders
The country/region geographic borders are stored as stardard geojson. Each country is stored as a geojson polygon or multipolygon within their appropriate LoRaWAN region file. The geojson can be modified with GIS tools, online geojson editors, mapshaper, etc. The whole region file may be too large to work with so the country of interest's polygon can be put in its own file while being worked on and then merged back into its region file.

### Changing a Country's LoRaWAN Region
The `regions.csv` should be updated, even though it is only used as an index at this point. Then, simply move the polygon from its orginal LoRaWAN region to its new one.

Once the borders have been updated or a country moved to a new region file, `plans.py` should be run, which will simplify with `unary_union` and combine all the regions into one file.
