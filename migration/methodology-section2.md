[Methodology](methodology.html)

# Section 2: Brain Waste and Spatial Distribution

## Datasets and Preprocessing 

This section draws on three primary data sources to examine the geographic settlement patterns and professional integration of Nigerian healthcare workers across the UK. UK Census data was used across three census years — 2001, 2011, and 2021 — covering Lower Tier Local Authority (LTLA) level records for country of birth and occupation by industry. In addition, geospatial shapefiles of UK administrative boundaries were incorporated to map the density of the Nigerian-born population against local labour market conditions. 

Six raw datasets were used in total: a country of birth file and an occupation file for each of the three census years. Because each census adopted a different data structure and geographic coding convention, bespoke cleaning functions were developed for each year. The 2001 and 2021 datasets used standardised LTLA geo-codes, enabling records to be matched directly. The 2011 dataset did not share a consistent code system and required matching on area name instead, introducing an additional harmonisation step to bridge the gap between census periods. 

For each census year, the birth-country file was filtered to retain only the Nigerian-born population count per Local Authority. The occupation file was then processed to extract three key variables: total occupational count, professional healthcare occupations (Major Group 2), and caring and personal service occupations (Major Group 6). These two files were merged at the Local Authority level, assigned a census year identifier, and concatenated into a single longitudinal master dataset spanning 2001 to 2021. All numeric columns were standardised to consistent data types, and missing values were replaced with zero to preserve Local Authority coverage. 

A core derived variable — the Brain Waste Index (BWI) — was then calculated for each Local Authority and census year using the following formula: 

BWI= Caring Occupations / Professional Occupations+Caring Occupations  

A BWI value approaching 1.0 indicates high brain waste, where Nigerian-born workers are disproportionately concentrated in lower-skilled caring roles relative to professional ones. A value approaching 0.0 indicates strong professional integration into high-skilled medical roles. Local Authorities with zero total occupational records were excluded from the analysis to avoid distortion from data-deficient areas. Migration counts were further normalised relative to the total local healthcare workforce to identify regions with a disproportionate reliance on Nigerian labour. 

## Analytical Approach 

This section adopts a mixed descriptive and spatial analytical approach structured across four stages to examine brain waste and the geographic distribution of Nigerian healthcare workers over time. 

In the first stage, a longitudinal overview was produced using a combined bar and line chart. The bar component displays the total Nigerian-born population per census year on the primary axis, while the line component overlays the mean Brain Waste Index on the secondary axis. This dual-axis design enables simultaneous examination of population growth and shifts in occupational integration across 2001, 2011, and 2021. 

In the second stage, a regional ranking analysis was conducted using the 2021 dataset. Local Authorities were ranked by their BWI to identify the ten strongest integration hubs — areas where Nigerian workers most successfully accessed professional roles — and the ten worst-performing brain waste hotspots, where workers were disproportionately concentrated in caring roles. This LTLA validation step cross-referenced local authority data with regional healthcare infrastructure to confirm that high concentrations of Nigerian residents coincided with areas of high healthcare demand. 

In the third stage, a regression scatter plot was produced to examine the relationship between the size of the Nigerian-born population and the BWI at Local Authority level. A linear regression line with a 95% confidence interval was overlaid to visualise the direction and strength of this association. The top ten hotspots and integration hubs were individually annotated to contextualise the distributional pattern, with the national mean BWI included as a benchmark reference line. 

In the fourth and final stage, a choropleth map was generated using GeoPandas by merging the processed BWI dataset with UK Local Authority boundary geometries. UK regions were categorised into integration hubs, where residency aligns with high-skilled professional placement, and occupational immobility zones, where residency is high but professional placement is low. Integration hubs were shaded green and brain waste hotspots in red, providing a spatial representation of where professional integration succeeds and where occupational downgrading persists across England and Wales. 

[Previous: Section 1](methodology-section1.html) | [Next: Section 3](methodology-section3.html)
