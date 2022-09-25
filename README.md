# UNCC Parking Availabilty scraper
## Purpose
Scrapes the <a href="https://parkingavailability.charlotte.edu/">UNC Charlotte Parking Availability page</a> using <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/">Beautiful Soup</a>. The Python script is run every 30 minutes using <a href="https://en.wikipedia.org/wiki/Windows_Task_Scheduler">Windows Task Scheduler</a>, where it scrapes the website for a specific HTML tag, then parses the data and removes unnecessary components. Using the <a href="https://dev.mysql.com/doc/connector-python/en/">MySQL Connector/Python</a>, which is a self-contained Python driver for communicating with MySQL servers, it sends the current *unavalaible* capacity to a MySQL database for long term storage and to use to look at historical trends.

## What's next
The next step is to add additional code that will query the data for use in a github.io page, where historical trends can be plotted.

## Issues
I wrote this when I was first learning Python, had never used a database before, and had never used Beautiful Soup. The code needs to be refactored to clean up many redundant lines, but it works well enough that I do not have the means.
