[Project Report](report.html)

# Methodology

This study adopts a quantitative, data-driven approach to examine migration from Nigeria to the United Kingdom as a multi-dimensional process. The methodology is structured into three analytical sections: (1) economic push factors and policy influences, (2) labour market outcomes and occupational integration, and (3) economic returns through remittance flows. This structure allows for a comprehensive and integrated analysis of migration dynamics.

---

## Section 1: Policy and Flow Analysis

### Section 1a: Inflation and Unemployment as Economic Push Factors in Nigeria

#### Datasets and Preprocessing

The dataset used in this study was obtained from the World Bank World Development Indicators (WDI), which provides reliable, standardised, and internationally comparable macroeconomic data. The analysis focuses on Nigeria and incorporates three key indicators: inflation (consumer prices, annual percentage), unemployment rate (percentage of the labour force), and total labour force.

The study covers the period from 2000 to 2025, enabling both long-term trend analysis and the examination of recent economic developments. The raw dataset was initially structured in wide format, with each year represented as a separate column. To facilitate analysis, the data was transformed into long format using Python’s `melt()` function, ensuring that each observation corresponds to a single year-value pair.

Data preprocessing involved several steps to ensure quality and consistency. The dataset was filtered to include only Nigeria, and unnecessary metadata columns were removed. Year values were converted into numeric format, while inflation and unemployment variables were standardised into numeric types. Missing and invalid values were removed, and the dataset was sorted chronologically.

To improve interpretability, labour force data was combined with unemployment rates to estimate population-level indicators:

\[
\text{Unemployed} = \frac{\text{Unemployment Rate}}{100} \times \text{Total Labour Force}
\]

The number of employed individuals was then derived by subtracting the unemployed population from the total labour force. This transformation allows for a more meaningful representation of labour market dynamics.

#### Analytical Approach

A descriptive time-series approach was adopted to examine how inflation and unemployment function as economic push factors. The analysis focuses on identifying patterns, trends, and relationships over time.

Two main visualisation techniques were employed:

- A dual-axis line graph to compare inflation and unemployment trends  
- A stacked area chart to analyse labour force composition  

The dual-axis graph enables simultaneous comparison despite differing scales, while the area chart provides insight into structural changes within the labour market. This combined approach enhances interpretability and real-world relevance.

---

### Section 1b: UK Immigration Policy and Migration of Nigerian Healthcare Workers

#### Datasets and Preprocessing

Two datasets were used to examine the relationship between UK immigration policy and Nigerian healthcare migration. The first dataset captured immigration policy changes and was used to construct a cumulative Policy Index, where lower values indicate more restrictive conditions. The second dataset contained migration totals for selected years (2000–2024).

Both datasets were merged using year as a common variable, resulting in a dataset with three variables: year, Policy Index, and healthcare migration.

#### Analytical Approach

A quantitative approach was used to assess the relationship between policy and migration.

The analysis proceeded in four stages:

1. Visualisation of policy trends over time  
2. Comparison of migration trends alongside policy changes  
3. Pearson correlation analysis to measure relationship strength  
4. Ordinary Least Squares (OLS) regression to estimate the relationship  

The regression model is specified as:

\[
\text{Healthcare Migration} = \beta_0 + \beta_1(\text{Policy Index}) + \epsilon
\]

This approach enables the estimation of how changes in policy are associated with migration levels.

---

## Section 2: Brain Waste and Spatial Distribution

#### Datasets and Preprocessing

This section uses UK Census data (2001, 2011, 2021) at Lower Tier Local Authority (LTLA) level, alongside geospatial shapefiles.

Six datasets were used: a country-of-birth file and an occupation file for each census year. Due to differences in data structures, bespoke cleaning procedures were applied. The 2001 and 2021 datasets used standardised geo-codes, while the 2011 dataset required matching based on area names.

The datasets were merged to create a longitudinal dataset. Key variables included total occupation counts, professional healthcare roles (Major Group 2), and caring occupations (Major Group 6).

A Brain Waste Index (BWI) was constructed:

\[
\text{BWI} = \frac{\text{Caring Occupations}}{\text{Professional + Caring Occupations}}
\]

Values close to 1 indicate high brain waste, while values close to 0 indicate strong professional integration.

#### Analytical Approach

A mixed descriptive and spatial approach was used:

1. Longitudinal trend analysis using bar-line charts  
2. Regional ranking of best and worst performing areas  
3. Regression analysis between population size and BWI  
4. Choropleth mapping using GeoPandas  

This approach enables both temporal and spatial analysis of labour market outcomes.

---

## Section 3: Migration and Remittance Analysis

#### Datasets and Preprocessing

Two datasets were used:

- UN DESA migration stock data  
- World Bank remittance data  

Data was cleaned using pandas, with metadata removed and variables standardised. Migration stock was aggregated across gender, and datasets were merged by year (2000–2024).

#### Analytical Approach

The analysis combined:

- Time-series visualisation  
- Pearson correlation analysis  
- Construction of a Policy Efficiency Index  

The correlation coefficient (~0.22) indicates a weak positive relationship between migration and remittances.

A weighted index was constructed:

\[
\text{Policy Index} = 0.7 \times \text{Remittances}_{scaled} - 0.3 \times \text{Migrants}_{scaled}
\]

This index captures the net economic outcome of migration.

---

## Methodological Justification

The multi-dimensional approach is justified by the complexity of migration as a socio-economic process. By integrating economic, policy, labour market, and financial perspectives, the study provides a more comprehensive understanding than single-factor analyses.

---

## Limitations

The study is subject to limitations, including reliance on secondary data, small sample sizes in regression analysis, and simplified policy indicators. These factors limit generalisability and should be considered when interpreting results.

---



[Previous: Significance of the Study](significance.html) | [Next: Results and Discussion](results-discussion.html)
