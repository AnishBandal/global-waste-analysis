# Share of plastic waste that is recycled, landfilled, incinerated and mismanaged - Data package

This data package contains the data that powers the chart ["Share of plastic waste that is recycled, landfilled, incinerated and mismanaged"](https://ourworldindata.org/grapher/share-plastic-fate?v=1&csvType=full&useColumnShortNames=false) on the Our World in Data website.

### Active Filters

A filtered subset of the full data was downloaded. The following filters were applied:

## CSV structure

Each row is an observation for an entity (usually a country or region) at a timepoint.

- "Entity" — the name of the entity, e.g. "United States".
- "Code" — our internal entity code. For most countries this is the [ISO alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) code, e.g. "USA"; historical and other non-standard entities get a custom code.
- "Year" or "Day" — the timepoint. Annual data has a "Year" column holding an integer year; otherwise a "Day" column holds a date string in the form "YYYY-MM-DD".
- Every remaining column is a data column, each one a time series. Downloaded with the "full data" option each corresponds to one time series below; with "only selected data visible in the chart" they are transformed depending on the chart type, so the correspondence may be less direct.


## Metadata.json structure

The .metadata.json file contains metadata about the data package. The "charts" key contains information to recreate the chart, like the title, subtitle etc. The "columns" key contains information about each of the columns in the csv, like the unit, timespan covered, citation for the data etc.

## How we process data at Our World in Data

Our World in Data is almost never the original producer of the data - almost all of the data we use has been compiled by others. If you want to re-use data, it is your responsibility to ensure that you adhere to the sources' license and to credit them correctly. Please note that a single time series may have more than one source - e.g. when we stitch together data from different time periods by different producers or when we calculate per capita metrics using population data from a second source.

Preparing this data involves several processing steps. Depending on the data, this can include standardizing country names and world region definitions, converting units, calculating derived indicators such as per capita measures, as well as adding or adapting metadata such as the name or the description given to an indicator.
[Read about our data pipeline](https://docs.owid.io/projects/etl/).

## Detailed information about each time series


### Recycled
Last updated: September 21, 2023  
Date range: 2000–2019  
Unit: %  
Source: OECD (2023) – processed by Our World in Data  

#### How to cite this data

OECD (2023) – processed by Our World in Data


### Incinerated
Last updated: September 21, 2023  
Date range: 2000–2019  
Unit: %  
Source: OECD (2023) – processed by Our World in Data  

#### How to cite this data

OECD (2023) – processed by Our World in Data


### Mismanaged
Last updated: September 21, 2023  
Date range: 2000–2019  
Unit: %  
Source: OECD (2023) – processed by Our World in Data  

#### How to cite this data

OECD (2023) – processed by Our World in Data


### Landfilled
Last updated: September 21, 2023  
Date range: 2000–2019  
Unit: %  
Source: OECD (2023) – processed by Our World in Data  

#### How to cite this data

OECD (2023) – processed by Our World in Data


## Sources

These are the sources behind the data in this package. Each time series above names the ones it draws on in its citation.

### OECD – Global Plastics Outlook – Plastics waste by region and end-of-life fate

This dataset provides estimates of plastics waste for the 15 global regions of the OECD ENV-Linkages model, detailed in the Annex of the OECD Global Plastics Outlook.

This dataset provides estimates of plastics waste per end-of-life fate after accounting for recycling losses and collected littering.

Plastic waste is calculated as a function of plastics use (in volumes), following Geyer, Jambeck and Law (2017), using a methodology based on lifespan distributions. Plastic waste is divided into different waste management streams (end-of-life fates) by applying end-of-life shares that vary across countries and that account for account for recycling losses and collected litter. The methodology to derive the end-of-life shares is explained in the Annex to the OECD Global Plastics Outlook.

Producer: OECD  
Published: 2023-02-22  
Retrieved on: 2023-09-21  
Retrieved from: https://stats.oecd.org/viewhtml.aspx?datasetcode=PLASTIC_WASTE_5&lang=en  
License: CC BY 4.0 (https://www.oecd.org/termsandconditions)  

Citation: OECD (2022), Global Plastics Outlook, https://stats.oecd.org/viewhtml.aspx?datasetcode=PLASTIC_WASTE_5&lang=en, accessed on 21 September 2023

    