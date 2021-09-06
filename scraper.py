# import libraries
from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
import re

# Scrape website
session = HTMLSession()
resp = session.get("https://parkingavailability.uncc.edu/")
resp.html.render()
soup = BeautifulSoup(resp.html.html, "lxml")

# Get required info
allInfo = soup.find_all("mat-list-item")
allInfoArray = [tag.text for tag in allInfo]

# Clean up info
for parkingDecks in allInfoArray:
    parkingDecks = parkingDecks.replace('\n',' ').replace('place','').replace('star_border','')
    print(parkingDecks)
