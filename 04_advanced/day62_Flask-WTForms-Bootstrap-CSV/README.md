### Coffee & Wi-fi Project
#### Flask, Wtforms, Bootstrap and CSV
# Objective
The main goal of today is to ensure that you are fully comfortable with Flask-WTF, 
Bootstrap-Flask, Bootstrap classes and do a bit of revision on csv manipulation.

## Requirements

- The home page should use the css/styles.css file
- The /cafes route should render the cafes.html file.
  - This file should contain a Bootstrap table which displays all the data from the cafe-data.csv
- The location URL should be rendered as an anchor tag \<a> in the table instead of the full link. 
  - It should have the link text "Maps Link" and the href should be the actual link
- Clicking on the "Show Me!" button on the home page should take you to the cafes.html page
- There should be a secret route "/add" which doesn't have a button, but those in the know should be able to access it, and it should take you to the add.html file
- Use what you have learnt about WTForms and Bootstrap-Flask to use ```render_form``` in the add.html page that contains all the fields you can see in the demo
- Make sure that the location URL field has validation that check the data entered is a valid URL
- When the user successfully submits the form on add.html, make sure the data gets added to the cafe-data.csv. It needs to be appended to the end of the csv file. The data from each field need to be comma-separated like all the other lines of data in cafe-data.csv
- Make sure all the navigation links in the website work
