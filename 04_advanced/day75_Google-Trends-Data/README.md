## Google Trends Data

# Objective

- Making time-series data comparable by resampling and converting to the same periodicity (e.g., from daily data to monthly data)
- Fine-tuning the styling of Matplotlib charts by using limits, labels, linestyles, markers, colours, and the charts's resolution
- Using grid grids to help visually identify seasonality in a time series
- Finding the number of missing and NaN values and how to locate NaN values in a DataFrame
- Working with Locators to better style the time axis on a chart
- Review the concepts learned in the previous three days and apply them to new datasets

# Learning Points & Summary

- use ```.describe()``` to quickly see some descriptive statistics at a glance 
- use ```.resample()``` to make a time-series data comparable to another by changing the periodicity
- work with ```matplotlib.dates``` Locators to better style a timeline (e.g., an axis on a chart)
- find the number of NaN values with ```.isna().values.sum()```
- change the resolution of a chart using the figure's ```dpi``
- create dashed ```'--'``` and dotted ```'-.'``` lines using ```linestyles```
- use different kinds of markers (e.g., ```'o'``` or ```'^'```) on charts
- fine-tuning the styling of Matplotlib charts by using limits, labels, ```linewidth``` and colours (both in the form of named colours and HEX codes)
- using ```.grid()``` to help visually identify seasonality in a time series