# Section 3: Migration and Remittance Analysis

## Datasets and Preprocessing 

Two secondary datasets formed the basis of the analysis. The first was the International Migrant Stock dataset (UN DESA, 2024), which reports bilateral migrant stocks by origin, destination and sex at five-year intervals from 2000 to 2020 plus a 2024 estimate. The second was the Personal Remittances, Received (current US$) indicator from the World Bank World Development Indicators (World Bank, 2024), which records annual remittance inflows in US dollars. A supplementary IAB brain-drain indicator was retained as background context but was not used in the formal correlation analysis. 

Preprocessing was performed in pandas. Metadata rows at the top of each workbook were skipped on import, and column names were stripped of whitespace. To avoid label-matching errors in the UN file, Nigeria was identified by its M49 location code 566 and the United Kingdom by code 826; the migration table was filtered to the Nigeria-to-UK corridor on this basis, and the Nigeria row of the World Bank file was extracted by case-insensitive name match. Only the overlapping window 2000 to 2024 was retained. 

UN DESA reports male and female stocks separately, so the two were summed by reference year to give a single annual stock; the 2024 value (152,015 male plus 171,992 female migrants, totalling 324,007) was added manually because it appeared in a separate column block. The remittance series was transposed from wide to long format and merged with the migration series on the year key, using an inner join. The final dataset contains six observation years (2000, 2005, 2010, 2015, 2020 and 2024) and three variables: year, Nigerian migrant stock in the United Kingdom, and Nigerian remittance inflows in current US dollars. No missing values remained after the merge. 

## Analytical Approach 

The analysis combined trend description, bivariate correlation and a normalised composite index. The migration and remittance series were first plotted as time series to inspect their trajectories. The migrant stock rose almost monotonically from about 84,000 in 2000 to 324,000 in 2024, while remittances were markedly more volatile, with a pronounced spike in 2015 attributable to the 2014 to 2016 oil-price collapse and the associated naira depreciation (IMF, 2016); this value was retained in the series rather than treated as an outlier. 

The strength of the linear association between the two series was measured using the Pearson product-moment correlation coefficient, computed in pandas. The estimated coefficient was approximately 0.22, indicating a weak positive relationship, and was visualised with a Seaborn regression plot showing the fitted line and a 95 per cent confidence band. Because the two variables are measured on very different scales, each was rescaled to the unit interval using the scikit-learn MinMaxScaler before being combined. 

A weighted Policy Efficiency Index was then constructed to summarise, for each year, the net economic outcome of out-migration: 

Policy Index = 0.7 × Remittances<sub>scaled</sub> − 0.3 × Migrants<sub>scaled</sub> 

The 70/30 weighting reflects the assumption that remittance receipts are the dominant economic gain from out-migration, while the loss of human capital is treated as a cost the negative sign on the migration term operationalises that cost. The index is therefore highest when remittances are large relative to diaspora size, and lowest when the migrant stock grows without a matching financial return.  

---

[Previous: Section 2](methodology-section2.html) | [Next: Results and Discussion](results-discussion.html)
