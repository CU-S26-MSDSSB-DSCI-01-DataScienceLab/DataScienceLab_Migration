[Section 1](methodology-section1.html)

# Section 1A: Inflation and Unemployment as Economic Push Factors

## Datasets and Preprocessing 

The dataset used in this study was obtained from the World Bank World Development Indicators (WDI) database, which provides reliable, standardised, and internationally comparable macroeconomic data. The analysis focuses specifically on Nigeria and incorporates three key indicators: inflation (consumer prices, annual percentage), unemployment rate (total percentage of the labour force), and total labour force (population). The study covers the period from 2000 to 2025, depending on data availability, allowing for the observation of both long-term trends and more recent economic developments. 

The raw data was initially structured in a wide format, with each year represented as a separate column. In order to facilitate effective analysis, the dataset was transformed into a long format using Python's melt() function so that each observation corresponds to a single year and value. Several preprocessing steps were undertaken to ensure data quality and consistency. The dataset was first filtered to include only observations relating to Nigeria, after which unnecessary metadata columns, such as country codes and indicator descriptions, were removed. Year values were converted into numeric format to allow chronological ordering, while inflation and unemployment variables were also converted into numeric types to enable accurate computation. Missing or invalid values were subsequently removed, and the dataset was sorted chronologically. 

In addition to these steps, labour force data was combined with unemployment rates to estimate population-level indicators. This transformation allows for a more meaningful interpretation of the data by quantifying the number of individuals affected rather than relying solely on percentage values. 

Unemployed= Unemployment Rate /100 ×Total Labour Force 

The number of employed individuals was then derived by subtracting the unemployed population from the total labour force. This approach provides a clearer representation of labour market dynamics and enhances the real-world relevance of the analysis. 

## Analytical Approach 

This study adopts a descriptive time-series approach to examine how inflation and unemployment function as economic push factors in Nigeria. The analysis focuses on identifying patterns, trends, and relationships between the selected variables over time, without applying complex statistical modelling techniques. 

Two principal visualisation methods were employed. First, a dual-axis line graph was used to compare inflation and unemployment trends over the study period. Inflation was plotted on the primary axis, while unemployment was plotted on the secondary axis. This approach enables the simultaneous visualisation of both variables despite their differing scales, allowing for the identification of long-term trends, periods of economic instability, and potential divergence between rising living costs and employment conditions. 

Second, a stacked area chart was used to analyse the structure of the labour force by separating employed and unemployed populations over time. This method provides insight into the growth of the total labour force, the relative proportions of employed and unemployed individuals, and structural changes within the labour market. 

The selection of these methods is justified by their ability to combine trend analysis with structural analysis. While the line graph captures how macroeconomic conditions evolve over time, the area chart illustrates the scale of their impact on the population. This integrated approach prioritises clarity, interpretability, and practical relevance, making it well suited for analysing economic push factors. 

---

[Previous: Section 1](methodology-section1.html) | [Next: Section 1B](methodology-section1b.html)
