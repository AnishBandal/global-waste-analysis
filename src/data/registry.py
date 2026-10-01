from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data"

DATASET_REGISTRY = {
    "production": {
        "label": "Global plastics production",
        "directory": "global-plastics-production",
        "file": "global-plastics-production.csv",
        "value_columns": ["Annual plastic production between 1950 and 2019"],
        "unit": "tonnes",
        "description": "Annual global production of polymer resin and fibers.",
    },
    "waste_gdp": {
        "label": "Per capita plastic waste vs GDP per capita",
        "directory": "per-capita-plastic-waste-vs-gdp-per-capita",
        "file": "per-capita-plastic-waste-vs-gdp-per-capita.csv",
        "value_columns": ["Per capita plastic waste", "GDP per capita"],
        "unit": "kg per person per day; international-$ in 2021 prices",
        "description": "Plastic waste generation and GDP per capita with population and region.",
    },
    "ocean_gdp": {
        "label": "Ocean plastic waste per capita vs GDP",
        "directory": "ocean-plastic-waste-per-capita-vs-gdp",
        "file": "ocean-plastic-waste-per-capita-vs-gdp.csv",
        "value_columns": ["Per capita plastic waste emitted to the ocean", "GDP per capita"],
        "unit": "kg per person; international-$ in 2021 prices",
        "description": "Estimated ocean plastic emissions per capita and GDP per capita.",
    },
    "waste_per_capita": {
        "label": "Plastic waste generation per capita",
        "directory": "plastic-waste-per-capita",
        "file": "plastic-waste-per-capita.csv",
        "value_columns": ["Per capita plastic waste"],
        "unit": "kg per person per day",
        "description": "Plastic waste generation before management, recycling, or incineration.",
    },
    "mismanaged_per_capita": {
        "label": "Mismanaged plastic waste per capita",
        "directory": "mismanaged-plastic-waste-per-capita",
        "file": "mismanaged-plastic-waste-per-capita.csv",
        "value_columns": ["Mismanaged plastic waste per capita"],
        "unit": "kg per person",
        "description": "Plastic waste that is not recycled, incinerated, or kept in sealed landfills.",
    },
    "fate": {
        "label": "Annual plastic waste by disposal method",
        "directory": "plastic-fate",
        "file": "plastic-fate.csv",
        "value_columns": ["Recycled", "Incinerated", "Mismanaged", "Landfilled"],
        "unit": "tonnes",
        "description": "Plastic waste by end-of-life fate for regions and selected countries.",
    },
    "fate_share": {
        "label": "Share of plastic waste by disposal method",
        "directory": "share-plastic-fate",
        "file": "share-plastic-fate.csv",
        "value_columns": ["Recycled", "Incinerated", "Mismanaged", "Landfilled"],
        "unit": "%",
        "description": "Percentage distribution of plastic waste by end-of-life fate.",
    },
    "sector": {
        "label": "Plastic waste generation by industrial sector",
        "directory": "plastic-waste-generation-by-industrial-sector",
        "file": "plastic-waste-generation-by-industrial-sector.csv",
        "value_columns": ["China", "United States", "Europe", "India", "Oceania", "World", "Sub-Saharan Africa", "Middle East & North Africa", "Asia (excl. China and India)"],
        "unit": "tonnes",
        "description": "Plastic waste by application and region in 2019.",
    },
    "ocean_share": {
        "label": "Share of global plastic waste emitted to the ocean",
        "directory": "share-of-global-plastic-waste-emitted-to-the-ocean",
        "file": "share-of-global-plastic-waste-emitted-to-the-ocean.csv",
        "value_columns": ["Share of global plastic waste emitted to the ocean"],
        "unit": "%",
        "description": "Country and regional shares of estimated plastic waste emitted to the ocean.",
    },
    "rivers": {
        "label": "Top rivers contributing to ocean plastic pollution",
        "directory": "plastics-top-rivers",
        "file": "plastics-top-rivers.csv",
        "value_columns": ["Share of global plastics emitted to the ocean"],
        "unit": "%",
        "description": "Estimated share of global ocean plastic pollution from major rivers.",
    },
    "exports": {
        "label": "Share of cumulative plastic exports",
        "directory": "share-of-cumulative-plastic-exports",
        "file": "share-of-cumulative-plastic-exports.csv",
        "value_columns": ["Share of global exports (%)"],
        "unit": "%",
        "description": "Share of cumulative plastic exports for the top ten exporters.",
    },
}


def dataset_path(key):
    spec = DATASET_REGISTRY[key]
    return DATA_DIR / spec["directory"] / spec["file"]
