## Asthma Disparities in New York City


**Purpose:**


This project was the capstone of the Correlation One Data Science for All program.
The purpose of this project was to analyze New York City data on asthma contributors and Social Determinants of Health to uncover what potentially drives asthma disparity in this city. Although there are a wide variety of potential asthma contributors, for this project focused on indoor and outdoor air quality because they are widely believed to be the main contributors. 


![Team45_projectBoard](https://github.com/Hevander27/Correlation-One/assets/45948489/f3a0638b-edc8-41c6-914c-b7658fb140c5)
**Full Report:** [What Contributes to Asthma Disparity 
in New York City](https://docs.google.com/document/d/1PZRT_0nhVFE29YuoBeKd6435zLIpL_2vErgc3j9Iu_4/edit)

**Power Point:** [Team 45 Presentation](https://docs.google.com/presentation/d/1TyA2HsA6o0-gvV_tjdVr-jMRYL1DyoXaqumnDSX84uw/edit#slide=id.ge6b119a546_0_24)



## Data Table Schema Team 45

`Dataset:airq\_34\_all`


Contains data about the average amounts of toxins: Fine particulate matter, nitrogen
dioxide, and ozone. The data is categorized by UHF34 neighborhood for years 2009 to
2018.


There are 330 rows and 6 columns.


https://data.cityofnewyork.us/Environment/Air-Quality/c3uy-2p5r



|**Field**|**Type** |**Description**|
| - | - | - |
|**name\_of\_column**|The python consumable format|Brief description of the field. If the field follows a specific format (e.g. a specific date format) include that here too.|
|**year**|STRING|Year|
|**Borough**|STRING|NYC Borough Name associated with UHF 34 neighborhood|
|**geo\_place\_name**|STRING|UHF 34 Neighborhood name|
|**mean\_fpm**|Float|Average yearly amount of fine particulate matter|
|**mean\_no**|Float|Average yearly amount of nitrogen dioxide|
|**Ozone mean (ppb)**|Float|Average yearly amount of ozone|

`Dataset:airq\_42\_all`


Contains data about the average amounts of toxins: ?ine particulate matter, nitrogen
dioxide, and ozone. The data is categorized by UHF42 neighborhood for years 2009 to
2018. 


There are 420 rows and 6 columns.


https://data.cityofnewyork.us/Environment/Air-Quality/c3uy-2p5r



|**Field**|**Type** |**Description**|
| - | - | - |
|**name\_of\_column**|The python consumable format|Brief description of the field. If the field follows a specific format (e.g. a specific date format) include that here too.|
|**year**|STRING|Year|
|**Borough**|STRING|NYC Borough Name associated with UHF 42 neighborhood|
|**geo\_place\_name**|STRING|UHF 42 Neighborhood name|
|**mean\_fpm**|Float|Average yearly amount of fine particulate matter|
|**mean\_no**|Float|Average yearly amount of nitrogen dioxide|
|**Ozone mean (ppb)**|Float|Average yearly amount of ozone|

`Dataset:benzene\_42`

Contains data about the average concentration of benzene in the air.The data is categorized by UHF42 neighborhood for years 2005 and 2011.


There are 84 rows and 3 columns. 


https://data.cityofnewyork.us/Environment/Air-Quality/fyf4-hrcu



|**Field**|**Type** |**Description**|
| - | - | - |
|**name\_of\_column**|The python consumable format|Brief description of the field. If the field follows a specific format (e.g. a specific date format) include that here too.|
|**year**|STRING|Year|
|**geo\_place\_name**|STRING|UHF 34 Neighborhood name|
|**mean\_benzene**|Float|Average yearly concentration of benzene in the air|

`Dataset:formaldehyde\_42`


Contains data about the average concentration of formal dehyde in the air.The data is categorized by UHF42 neighborhood for years 2005 and 2011.


There are 84 rows and 3 columns.


https://data.cityofnewyork.us/Environment/Air-Quality/fyf4-hrcu



|**Field**|**Type** |**Description**|
| - | - | - |
|**name\_of\_column**|The python consumable format|Brief description of the field. If the field follows a specific format (e.g. a specific date format) include that here too.|
|**year**|STRING|Year|
|**geo\_place\_name**|STRING|UHF 34 Neighborhood name|
|**mean\_formaldehyde**|Float|Average yearly concentration of benzene in the air|

`Dataset:boiler\_emissions`

Contains data about the average boiler emissions of toxins nitrogen dioxide,sulfurdioxide and ine particulate matter.The data is categorized by UHF42 neighborhood for years 2013 and 2015.


There are 84 rows and 5 columns. 


https://data.cityofnewyork.us/Environment/Air-Quality/fyf4-hrcu



|**Field**|**Type** |**Description**|
| - | - | - |
|**name\_of\_column**|The python consumable format|Brief description of the field. If the field follows a specific format (e.g. a specific date format) include that here too.|
|**year**|STRING|Year|
|**geo\_place\_name**|STRING|UHF 42 Neighborhood name|
|**nox\_num\_per\_km2**|Float|Number of emissions per kilometer squared|
|**so2\_num\_per\_km2**|Float|Number of emissions per kilometer squared|
|**pm2\_num\_per\_km2**|Float|Number of emissions per kilometer squared|

`Dataset:sulfur\_34` 


Contains data about the average amount of sulfurdioxide in the air.The data is categorized by UHF34 neighborhood for years 2008-2015.


There are 272 rows and 3 columns. 



https://data.cityofnewyork.us/Environment/Air-Quality/fyf4-hrcu



|**Field**|**Type** |**Description**|
| - | - | - |
|**name\_of\_column**|The python consumable format|Brief description of the field. If the field follows a specific format (e.g. a specific date format) include that here too.|
|**year**|STRING|Year|
|**geo\_place\_name**|STRING|UHF 34 Neighborhood name|
|**mean\_so2**|Float|Average yearly amount of sulfur|

Dataset:sulfur\_42


Contains data about the average amount of sulfurdioxide in the air.
The data is categorized by UHF42 neighborhood for years 2008 and 2015. There are 336 rows and 3 columns. 


https://data.cityofnewyork.us/Environment/Air-Quality/fyf4-hrcu



|**Field**|**Type** |**Description**|
| - | - | - |
|**name\_of\_column**|The python consumable format|Brief description of the field. If the field follows a specific format (e.g. a specific date format) include that here too.|
|**year**|STRING|Year|
|**geo\_place\_name**|STRING|UHF 42 Neighborhood name|
|**mean\_so2**|Float|Average yearly amount of sulfur|

Dataset:o3\_pm2\_attributable\_hospital\_visits



Contains data about the number of emergency department visits and hospitalizations for
asthma attributed to ?ine particulate matter and ozone toxins. The data is categorized by
UHF 42 neighborhood. The data is categorized in the following time periods: 2005-2007,
2009 - 2011, 2012-2014, 2015-2017. There are 168 rows and 9 columns.



https://data.cityofnewyork.us/Environment/Air-Quality/fyf4-hrcu



|**Field**|**Type** |**Description**|
| - | - | - |
|**name\_of\_column**|The python consumable format|Brief description of the field. If the field follows a specific format (e.g. a specific date format) include that here too.|
|**Time Period**|STRING|Two year range|
|**Start\_Date**|STRING|Start date for time period|
|**geo\_place\_name**|STRING|UHF 42 Neighborhood name|
|**child\_o3\_asthma\_hos pital\_per\_100k**|Float|Rate of hospitalizations for asthma in children attributed to ozone out of 100,000|
|**adult\_o3\_asthma\_ho spital\_per\_100k**|Float|Rate of hospitalizations for asthma in adults attributed to ozone out of 100,000|
|**adult\_pm2\_asthma\_e d\_visits\_per\_100k**|Float|Rate of emergency department visits for asthma in adults attributed to fine particulate matter out of 100,000|
|**child\_pm2\_asthma\_e d\_visits\_per\_100k**|Float|Rate of emergency department visits for asthma in children attributed to fine particulate matter out of 100,000|
|**adult\_o3\_asthma\_ed\_ visits\_per\_100k**|Float|Rate of emergency department visits for asthma in adults attributed to ozone out of 100,000|
|**child\_o3\_asthma\_ed\_ visits\_per\_100k** |Float|Rate of emergency department visits for asthma in children attributed to ozone out of 100,001|

Dataset:traf ic\_merged ContainsdataaboutthenumberofmilesdrivenbycarsandtrucksinUHF42 neighborhoods.Thedatacoversyears2005and2016.Thereare84rowsand5columns.

https://data.cityofnewyork.us/Environment/Air-Quality/fyf4-hrcu



|**Field**|**Type** |**Description**|
| - | - | - |
|**name\_of\_column**|The python consumable format|Brief description of the field. If the field follows a specific format (e.g. a specific date format) include that here too.|
|**year**|STRING|Year|
|**geo\_place\_name**|STRING|UHF 42 Neighborhood name|
|**cars\_million\_miles**|Float|Number of miles traveled by cars in millions|
|**trucks\_million\_miles**|Float|Number of miles traveled by trucks in millions|
|**total\_million\_miles**|Float|Sum of miles traveled by cars and trucks in millions|

**Dataset: adult\_smoking\_joined\_UHF34\_CLEAN**


This is data related to adults smoking and being in smoking environments. Additional meta data was dropped.
Data was converted to numeric values to allow for appropriate usage.


[https://a816-dohbesp.nyc.gov/ IndicatorPublic/Subtopic.aspx?theme_code=2,3&subtopic_id=3](https://a816-dohbesp.nyc.gov/IndicatorPublic/Subtopic.aspx?theme_code=2,3&subtopic_id=3)

|Field|Type |Description|
| - | - | - |
|**Year**|Category|Year of data, in format yyyy|
|**geo\_type\_name**|Category|Granularity level of geography category|
|**borough**|Category|Borough for data|
|**secondhand\_smoke\_home \_adult\_count**|FLOAT|Count of adults reporting secondhand smoke at home|
|**secondhand\_smoke\_home \_adult\_percent**|FLOAT|Percent of adults reporting secondhand smoke at home|
|**smoking\_adults\_count**|FLOAT|Count of adults reporting smoking|
|**smoking\_adults\_percent**|FLOAT|Percent of adults reporting smoking|
|**secondhand\_smoke\_work\_ adult\_count**|FLOAT|Count of adults reporting secondhand smoke at work|
|secondhand\_smoke\_wor k\_adult\_percent|FLOAT|Percent of adults reporting secondhand smoke at work|


Dataset:NYC\_SDOH


The social determinants of health (SDH) are the non-medical factors that in?luence health
outcomes. They are the conditions in which people are born, grow, work, live, and age, and
the wider set of forces and systems shaping the conditions of daily life. Variables in the
SDOH database correspond to the 5 key domains identi?ied by AHRQ: social context, economic
context, education, physical infrastructure, and healthcare context. In addition to these
domains, there is a category for Geography, which includes ID variables (County, FIPS code,
ZCTA, State, and Year) as well as 14 county adjacency variables and urban/rural codes.
Data was cleaned based on the values available for the 5 ?ive counties of New York City for
2009-2018. Counties: Brooklyn County - The Bronx, Kings County - Brooklyn, New York
County - Manhattan, Queens County - Queens, Richmond County - Staten Island.



*51 rows & 231 columns.* Size:69.7KBSource: [AgencyofHealthcareResearchandQuality](https://www.ahrq.gov/sdoh/data-analytics/sdoh-data.html)



|Field|Type |Description|
| - | - | - |
|**COUNTY**|STRING|County name|
|**FIPSCODE**|INTEGER|State-county FIPS code, 5 digits (County only)|
|**YEAR**|DATE|The year the data is from|
|**ACS\_PCT\_AGE\_65UP**|FLOAT|Percentage of population age 65 and over|
|**ACS\_PCT\_AGE\_0\_17**|FLOAT|Percentage of population age 0-17|
|**ACS\_PCT\_AGE\_15\_17**|FLOAT|Percentage of population age 15-17|
|**ACS\_PCT\_AGE\_0\_4**|FLOAT|Percentage of population age 0-4|
|**etc. - full descrip on in NYC\_SDOH\_dic onary**|||
**NYC\_SDOH\_dictionary**

Detaileddescriptionofeachofthe ields.

*236 rows & 4 columns.* Size:29.5KBSource: [AgencyofHealthcareResearchandQuality](https://www.ahrq.gov/sdoh/data-analytics/sdoh-data.html)

**Asthma\_ED\_Visits**


Asthma emergency room visits for NYC residents. Data cleaned based on “lowest common
denominator” or based on the least detailed data set which was the SDOH data set that
contained more general data gathered based on county rather than individual UHF 42
neighbourhood. The average of the total ED visits from all neighborhoods in each county was taken and
organized by year. The age-adjusted rate (for adults only, per 10000 residents) and
estimated annual rate (per 10000 residents) from all counties was taken and organized by
year. Asthma ED Visit data was only taken/available for the years 2009-2016 with no data
available per county for the year 2015.


*106 rows & 6 columns.* Size:approximatesizeasappearsonyour ileexplorer.Source: [NYC Environment&HealthDataPortal](https://a816-dohbesp.nyc.gov/IndicatorPublic/VisualizationData.aspx?id=2380,4466a0,11,Summarize)



|Field|Type |Description|
| - | - | - |
|**COUNTY**|STRING|County name|
|**YEAR**|DATE|Year of data collection|
|**INDICATOR\_NAME**|STRING|Population name by age. i.e. Adults (18+), Children (0-4), Children (5-17)|
|**NUMBER**|INTEGER|Average  of  the  total  ED  visits  from  all neighborhoods in each county.|
|**AGE\_ADJUSTED\_RA TE**|FLOAT|Number of ED visits per country adjusted for population older than 18 years (adults), per 10,000 residents.|
|**ESTIMATED\_ANNUA L\_RATE**|FLOAT|Number of ED visits per country adjusted for population older than 18 years, per 10,000 residents for that year.|

**Dataset: Indoor\_air\_quality\_all** 


Dataset contains resident reported complaints on indoor air quality.
Complaints are tabulated individually per report; report dates range from 2010 to 2021.
The included columns: Borough, geo_place_name, zip code, longitude and latitude, are used
to identify location.


*Rows: 65050*
*Columns: 7*

Size:3,601KB

Source: https://data.cityofnewyork.us/Health/DOHMH-Indoor-Environmental-Complaints/9jgj- bmct/data



|Field|Type |Description|
| - | - | - |
|name\_of\_column|The python consumable format|Brief description of the field. If the field follows a specific format (e.g. a specific date format) include that here too.|
|Year|STRING|Year|
|Borough|STRING|NYC Borough Name associated with UHF 42 neighborhood|
|geo\_place\_name|STRING|UHF 42 Neighborhood name|



|Zip code|STRING|Zip code of complaint address|
| - | - | - |
|Complaint type|STRING|Type of complaint reported by residents|
|Longitude|FLOAT|Longitude of complaint location|
|Latitude |FLOAT|Latitude of complaint location|

**Dataset: Adultswith Asthma in the Past 12 Months.csv** 

Description: Prevelance of adults with asthma in the past 12 months. Listed by NYC UHF
Neighborhoods and year. I removed metadata, removed commas, changed column names,
made everything lowercase, and changed the datatypes to the appropriate datatypes for
each column.


Rows:521

Columns:8

Size:140kb

Source:NYCEnvironment&HealthDataPortal [https://a816dohbesp.nyc.gov/IndicatorPublic/Subtopic.aspx? theme_code=2,3&subtopic_id=11](https://a816dohbesp.nyc.gov/IndicatorPublic/Subtopic.aspx?theme_code=2,3&subtopic_id=11)



|Field|**Type** |Description|
| - | - | - |
|**year** |category|The year of that data point|
|**geo\_type\_name** |cateogry|The type of geography for that data point (ex. Citywide, Neighborhood, Borough)|
|**borough** |category|Name of borough in NYC |
|**geography** |category|The most specific geographical location |
|**geography\_id** |category|Unique geographical ID for every geographical location|
|**adults\_12mo\_asthma\_ag e\_adjusted\_percent** |float|Percentage of adults with asthma adjusted for age|
|**adults\_12mo\_asthma\_nu mber** |float|Number of adults with asthma|
|**adults\_12mo\_asthma\_pe rcent** |float|Percentage of adults with asthma|

**Dataset: Public School Children (5-14 YrsOld) with Asthma.csv** 


Description: Prevelance of public school children from ages 5-14 with asthma. Listed by
NYC UHF Neighborhoods and year. I removed metadata, removed commas, changed column
names, made everything lowercase, and changed the datatypes to the appropriate
datatypes for each column


Rows:193

Columns:7

Size:25kb

Source:NYCEnvironment&HealthDataPortal [https://a816dohbesp.nyc.gov/IndicatorPublic/Subtopic.aspx? theme_code=2,3&subtopic_id=11](https://a816dohbesp.nyc.gov/IndicatorPublic/Subtopic.aspx?theme_code=2,3&subtopic_id=11)



|**Field**|**Type** |**Description**|
| - | - | - |
|**year** |category|The year of that data point|
|**geo\_type\_name** |cateogry|The type of geography for that data point (ex. Citywide, Neighborhood, Borough)|
|**borough** |category|Name of borough in NYC |
|**geography** |category|The most specific geographical location |
|**geography\_id** |category|Unique geographical ID for every geographical location|
|**children\_5\_14\_estimated \_annual\_rate\_per\_1000**|float|Rate of children age 5-14 with asthma (per 1000)|
|**children\_5\_14\_number**|float|Number of children age 5-14 with asthma|
||||
**Dataset: Asthma Emergency Department Visits(Adults).csv** Description:Asthmarelatedemergencydepartmentvisitsforadults.ListedbyNYCUHF Neighborhoodsandyear.Iremovedmetadata,removedcommas,changedcolumnnames, madeeverythinglowercase,andchangedthedatatypestotheappropriatedatatypesfor eachcolumn.

Rows:530

Columns:8

Size:65kb

Source:NYCEnvironment&HealthDataPortal [https://a816dohbesp.nyc.gov/IndicatorPublic/Subtopic.aspx? theme_code=2,3&subtopic_id=11](https://a816dohbesp.nyc.gov/IndicatorPublic/Subtopic.aspx?theme_code=2,3&subtopic_id=11)



|**Field** |**Type**|**Description**|
| - | - | - |
|**geo\_type\_name** |cateogry|The type of geography for that data point (ex. Citywide, Neighborhood, Borough)|
|**borough** |category|Name of borough in NYC |
|**geography** |category|The most specific geographical location |
|**geography\_id** |category|Unique geographical ID for every geographical location|
|**ed\_annual\_adult\_estima ted\_age\_adjusted\_rate\_ per10k**|float|Age adjusted rate of adults (per10,000) that visited the emergency department for asthma|
|**ed\_annual\_adult\_rate\_p er10k**|float|Rate of adults (per10,000) that visited the emergency department for asthma|
|**ed\_annual\_adult\_numbe r**|float|Number of adults that visited the emergency department for asthma|
|**year** |category|The year of that data point|

**Dataset: Asthma Emergency Department Visits(Children 5 to 17 YrsOld) .csv** Description:Description:Asthmarelatedemergencydepartmentvisitsforchildren5-17 yearsold.ListedbyNYCUHFNeighborhoodsandyear.Iremovedmetadata,removed commas,changedcolumnnames,madeeverythinglowercase,andchangedthedatatypesto theappropriatedatatypesforeachcolumn.

Rows:577

Columns:7

Size:78kb

Source:NYCEnvironment&HealthDataPortal [https://a816dohbesp.nyc.gov/IndicatorPublic/Subtopic.aspx? theme_code=2,3&subtopic_id=11](https://a816dohbesp.nyc.gov/IndicatorPublic/Subtopic.aspx?theme_code=2,3&subtopic_id=11)



|**Field** |**Type**|**Description**|
| - | - | - |
|**geo\_type\_name** |cateogry|The type of geography for that data point (ex. Citywide, Neighborhood, Borough)|
|**borough** |category|Name of borough in NYC |
|**geography** |category|The most specific geographical location |
|**geography\_id** |category|Unique geographical ID for every geographical location|
|**ed\_annual\_5\_17\_rate\_pe r10k**|float|Rate of children 5-17 years old (per10,000) that visited the emergency department for asthma|
|**ed\_5\_17\_number**|float|Number of children 5-17 years old that visited the emergency department for asthma|
|**year** |category|The year of that data point|

**Dataset: Asthma Hospitalizations(Adults).csv** Description:Numberofadultshospitalizedforasthma.ListedbyNYCUHFNeighborhoods andyear.Iremovedmetadata,removedcommas,changedcolumnnames,madeeverything lowercase,andchangedthedatatypestotheappropriatedatatypesforeachcolumn. Rows:530

Columns:8

Size:59kb

Source:NYCEnvironment&HealthDataPortal [https://a816dohbesp.nyc.gov/IndicatorPublic/Subtopic.aspx? theme_code=2,3&subtopic_id=11](https://a816dohbesp.nyc.gov/IndicatorPublic/Subtopic.aspx?theme_code=2,3&subtopic_id=11)



|**Field** |**Type**|**Description**|
| - | - | - |
|**geo\_type\_name** |cateogry|The type of geography for that data point (ex. Citywide, Neighborhood, Borough)|
|**borough** |category|Name of borough in NYC |
|**geography** |category|The most specific geographical location |
|**geography\_id** |category|Unique geographical ID for every geographical location|
|**asthma\_hosp\_adult\_esti mated\_\_age\_adjusted\_r ate\_per10k**|float|Age adjusted rate of adults (per10,000) that were hospitalized for asthma|
|**asthma\_hosp\_adult\_esti mated\_\_rate\_per10k**|float|Rate of adults (per10,000) that were hospitalized for asthma|
|**asthma\_hosp\_adult\_nu mber**|float|Number of adults that were hospitalized for asthma|
|**year** |category|The year of that data point|

Dataset:AsthmaHospitalizations(Children5to17YrsOld).csv Description:Numberofchildren5-17yearsoldhospitalizedforasthma.ListedbyNYCUHF Neighborhoodsandyear.Iremovedmetadata,removedcommas,changedcolumnnames, madeeverythinglowercase,andchangedthedatatypestotheappropriatedatatypesfor eachcolumn.

Rows:577

Columns:7

Size:71kb

Source:NYCEnvironment&HealthDataPortal [https://a816dohbesp.nyc.gov/IndicatorPublic/Subtopic.aspx? theme_code=2,3&subtopic_id=11](https://a816dohbesp.nyc.gov/IndicatorPublic/Subtopic.aspx?theme_code=2,3&subtopic_id=11)



|**Field** |**Type**|**Description**|
| - | - | - |
|**geo\_type\_name** |cateogry|The type of geography for that data point (ex. Citywide, Neighborhood, Borough)|
|**borough** |category|Name of borough in NYC |
|**geography** |category|The most specific geographical location |
|**geography\_id** |category|Unique geographical ID for every geographical location|
|**asthma\_hosp\_5\_17\_esti mated\_annual\_rate\_per \_10000**|float|Rate of children 5-17 years old (per10,000) that were hospitalized for asthma|
|**asthma\_hosp\_5\_17\_num ber**|float|Number of children 5-17 years old hospitalized for asthma|
|**year** |category|The year of that data point|

MedianHouseholdIncomeByRacebyTract,2012-2016 Containsdataabouttheaveragehouseholdincomeorganizedbyraceindifferentstateand

regionallevelsthedataisorganizebyyearfrom2012to2016

Having over 30 ields I will be organizing and cleaning up including below what seems morerelevanttoourresearch

*Rounded number of rows:*72730 *& speci ic number of columns: 33.* Size:72728records [Source: https://racialequity.maps.arcgis.com/apps/mapviewer/index.html? webmap=7ea542ec16364bd58c7d073443a35967](https://racialequity.maps.arcgis.com/apps/mapviewer/index.html?webmap=7ea542ec16364bd58c7d073443a35967)



|**Field**|**Type** |**Description**|
| - | - | - |
|**name\_of\_column**|The python consumable format|Brief description of the field. If the field follows a specific format (e.g. a specific date format) include that here too.|
|**STATE\_NAME** |STRING|Ex: Maryland or New York|
|**ST\_ABBREV** |STRING|EX: MD or NY|
|**Median Household Income in Past 12 Months, Some Other Race Householder - Estimate** |FLOAT|Calculates the median income over a year for a specific group – these are estimates from public census data|
|**Median Household Income in Past 12 Months - Estimate** |FLOAT|Calculates the median income over a year for a specific group – these are estimates from public census data|
|**Median Household Income in Past 12 Months, 2 or More Races Householder - Estimate** |FLOAT|Calculates the median income over a year for a specific group – these are estimates from public census data|



|**Median Household Income in Past 12 Months, American Indian and Alaska Native Householder - Estimate** |FLOAT|Calculates the median income over a year for a specific group – these are estimates from public census data|
| :- | - | :- |
|**Median Household Income in Past 12 Months, Asian Householder - Estimate** |FLOAT|Calculates the median income over a year for a specific group – these are estimates from public census data|
|**Median Household Income in Past 12 Months, Black or African American Householder - Estimate** |FLOAT|Calculates the median income over a year for a specific group – these are estimates from public census data|
|**Median Household Income in Past 12 Months, Hispanic or Latino Householder - Estimate** |FLOAT|Calculates the median income over a year for a specific group – these are estimates from public census data|
|**Median Household Income in Past 12 Months, Native Hawaiian and Other Pacific Islander Householder - Estimate** |FLOAT|Calculates the median income over a year for a specific group – these are estimates from public census data|
|**Median Household Income in Past 12 Months, Non-Hispanic White Householder – Estimate** |FLOAT|Calculates the median income over a year for a specific group – these are estimates from public census data|

