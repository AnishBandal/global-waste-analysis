# Global plastics production - Data package

This data package contains the data that powers the chart ["Global plastics production"](https://ourworldindata.org/grapher/global-plastics-production?v=1&csvType=full&useColumnShortNames=false) on the Our World in Data website. It was downloaded on October 1, 2026.

### Active Filters

A filtered subset of the full data was downloaded. The following filters were applied:

## CSV structure

Each row is an observation for an entity (usually a country or region) at a timepoint.

- "Entity" — the name of the entity, e.g. "United States".
- "Code" — our internal entity code. For most countries this is the [ISO alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) code, e.g. "USA"; historical and other non-standard entities get a custom code.
- "Year" or "Day" — the timepoint. Annual data has a "Year" column holding an integer year; otherwise a "Day" column holds a date string in the form "YYYY-MM-DD".
- The final column is the data column — the time series that powers the chart. Downloaded with the "full data" option it corresponds to the time series below; with "only selected data visible in the chart" it is transformed depending on the chart type, so the correspondence may be less direct.


## Metadata.json structure

The .metadata.json file contains metadata about the data package. The "charts" key contains information to recreate the chart, like the title, subtitle etc. The "columns" key contains information about each of the columns in the csv, like the unit, timespan covered, citation for the data etc.

## How we process data at Our World in Data

Our World in Data is almost never the original producer of the data - almost all of the data we use has been compiled by others. If you want to re-use data, it is your responsibility to ensure that you adhere to the sources' license and to credit them correctly. Please note that a single time series may have more than one source - e.g. when we stitch together data from different time periods by different producers or when we calculate per capita metrics using population data from a second source.

Preparing this data involves several processing steps. Depending on the data, this can include standardizing country names and world region definitions, converting units, calculating derived indicators such as per capita measures, as well as adding or adapting metadata such as the name or the description given to an indicator.
[Read about our data pipeline](https://docs.owid.io/projects/etl/).

## Detailed information about the data


### Annual plastic production between 1950 and 2019
Annual production of polymer resin and fibers.
Last updated: September 26, 2023  
Date range: 1950–2019  
Unit: tonnes  
Source: Geyer et al. (2017); OECD (2022) – with major processing by Our World in Data  

#### How to cite this data

Geyer et al. (2017); OECD (2022) – with major processing by Our World in Data

#### How this data is described by its producers
Total annual plastic production is global annual pure polymer (resin) production data from 1950 to 2015, published by the Plastics Europe Market Research Group, and global annual fiber production data from 1970 to 2015 published by The Fiber Year and Tecnon OrbiChem (Geyer et al. 2017)

#### Notes on our processing step for this indicator
The data on plastic production from 1950 to 2015 are based on the research by Greyer et al., published in 2017. For the years 2016 to 2018, the figures were projected by applying a consistent annual growth rate of 5%, which aligns with the growth estimates provided by Geyer. The most recent data for the year 2019 has been directly sourced from the OECD Global Plastics Outlook, released in 2022.


## Sources

These are the sources behind the data in this package. Each time series above names the ones it draws on in its citation.

### Geyer et al. – Production, use, and fate of all plastics ever made

Plastics have outgrown most man-made materials and have long been under environmental scrutiny. However, robust global information, particularly about their end-of-life fate, is lacking. By identifying and synthesizing dispersed data on production, use, and end-of-life management of polymer resins, synthetic fibers, and additives, we present the first global analysis of all mass-produced plastics ever manufactured. We estimate that 8300 million metric tons (Mt) as of virgin plastics have been produced to date. As of 2015, approximately 6300 Mt of plastic waste had been generated, around 9% of which had been recycled, 12% was incinerated, and 79% was accumulated in landfills or the natural environment. If current production and waste management trends continue, roughly 12,000 Mt of plastic waste will be in landfills or in the natural environment by 2050.

Producer: Geyer et al.  
Published: 2017-07-19  
Retrieved on: 2023-09-26  
Retrieved from: https://www.science.org/doi/10.1126/sciadv.1700782  
License: CC BY 4.0 (https://www.science.org/doi/10.1126/sciadv.1700782)  

Citation: Geyer et al., Production, use, and fate of all plastics ever made. Sci. Adv.3,e1700782(2017).DOI:10.1126/sciadv.1700782

### OECD – Global Plastics Outlook – Plastics use by application

This dataset provides estimates of plastics use at the global level by application.

Primary plastics use is estimated using regional consumption by application data from Ryberg et al. (2019). An assumption of the split by polymer by application is made that it is homogeneous to the global values. Historical values (pre-2015 data) is extrapolated from 2015 data using the global evolution contained in Geyer, Jambeck and Law (2017). Secondary plastics use are derived using recycling rates and recycling loss rates, as described in the GPO annex. The plastics use data is associated with the economic flows in the OECD ENV-Linkages model to estimate changes over time. The total plastics use is equal to the sum of primary and secondary plastics use.

Producer: OECD  
Published: 2022-02-09  
Retrieved on: 2023-09-21  
Retrieved from: https://stats.oecd.org/viewhtml.aspx?datasetcode=PLASTIC_USE_10&lang=en  
License: CC BY 4.0 (https://www.oecd.org/termsandconditions)  

Citation: OECD (2022), Global Plastics Outlook, https://stats.oecd.org/viewhtml.aspx?datasetcode=PLASTIC_USE_10&lang=en, accessed on 21 September 2023

    