## Data Entry Job Automation

# Objective

Webscrape data from a website (in our case from a 
[Zillow clone website](https://appbrewery.github.io/Zillow-Clone/)) 
then upload that data to a Google Form and finally 
get a spreadsheet about the web-scraped data.

## Steps
1) Initialize the environment (Python project, Google Form)
2) Webscrape data from the website with BeautifulSoup
   1) Create a list of links for all the listings
   2) Create a list of prices for all the listings
   3) Create a list of addresses for all the listings
   4) Clean the datasets
3) Open and fill up the Google Form with the data above
4) Open the Google Sheets from the responses

## Requirements
### External python modules
```commandline
bs4
selenium
```
### Environment variables
```commandline
GOOGLE_FORM_ID
GOOGLE_SHEETS_ID
```