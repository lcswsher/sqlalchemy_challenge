# SQL Alchemy Homework - Overview 



### Data files in repository:

- SQL Alchemy Homework, Climate  Analysis Files:
  - climate.ipynb file -  https://github.com/lcswsher/sqlalchemy_challenge/blob/main/climate.ipynb
  - app.py  file - https://github.com/lcswsher/sqlalchemy_challenge/blob/main/app.py
- PNG Files - https://github.com/lcswsher/sqlalchemy_challenge/tree/main/png_files

### Step 1 - Climate Analysis and Exploration

* Precipitation Analysis - 12 months of precipitation data  (08/24/2016 through 08/23/2017)
* Pandas plot chart of summary statistics for the precipitation data.
*  Station Analysis 
  * Query to calculate the total number of stations.
  * Query designed to identify the most active stations descending order.
* Histogram plot the results as a histogram with `bins=12`.

### Step 2 - Climate App

* Flask API design based on the queries for the following Available Routes:
* Precipitation data by date
* List of stations by name
* List of temperature observations for station USC00519281 for dates 08/24/2016 - 08/23/2017
* Min, Max, Avg Temperatures by Start Date
* Min, Max, Avg Temperatures by Start and End Dates.

### Bonus: Other Recommended Analyses

#### Temperature Analysis I & II

* Avg temperatures for June and December (all years)
* T-test calculation
* Min, avg and max temperatures for trip using prior year
* Plot the min, avg, and max temperature from your previous query as a bar chart.
  * Average temperature is the Bar Height
  * The peak to peak values is shown as an y error bar

#### Daily Rainfall Average

* Rainfall for each station (9 total)
* Create list of dates for vacation time period (06-01 through 06-15)
* Pandas used for area plot (`stacked=False`)  using daily historical normals.