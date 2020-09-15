# hiv_data_collection

This repository contains cleaning scripts for various data sources on HIV monitoring. Some notes for each of them
- Civicus: this is a scraper, and therefore depends on the structure of the website; if it changes, the scraper also needs to be changed
- Unaids: Unaids does not have an API for easy data collecting, making that you are required to download all the files manually. Make sure the names of the files are in similar format as in the repo, and then processing will be easy
- RIVM: this data was directly collected from the website
- Worldbank: has a nice API, script may be outdated
- Genderstats: may be outdated
