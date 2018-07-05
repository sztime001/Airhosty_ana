#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 15:05:37 2018

@author: Sofei1
"""
#1. import 
import pandas as pd
import numpy as np
import time
import datetime
import matplotlib
import matplotlib.pyplot as plt
import requests

def read_file(address):
    listings_file = address
    listing = pd.read_csv(listings_file, usecols)
    return listing
address = '/Users/Sofei1/Dropbox/A Sofei/CS/Airhosty/aus_postcode/aus_postcode.csv'
listing = read_file(address)

def check_type(df):
    for item in df.columns:
        print(type(df[item][0]))
        print(df[item][0])

check_type(listing)

listing[['latitude','longitude']] = listing[['latitude','longitude']].apply(pd.to_numeric)

listing.to_csv(address)
