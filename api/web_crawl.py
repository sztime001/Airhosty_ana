# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 13:12:22 2018

@author: Sofei
"""
# Import required modules
import requests
from bs4 import BeautifulSoup

# Create a variable with the url
url = 'https://www.airbnb.com.au/s/Parramatta--New-South-Wales/all?place_id=ChIJT69n4RijEmsRAMYyFmh9AQU&guests=10&adults=10&query=Parramatta%2C%20New%20South%20Wales&refinement_paths%5B%5D=%2Ffor_you'

# Use requests to get the contents
r = requests.get(url)

# Get the text of the contents
html_content = r.text

# Convert the html content into a beautiful soup object
soup = BeautifulSoup(html_content, 'lxml')