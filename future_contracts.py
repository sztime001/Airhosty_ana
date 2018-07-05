#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 21:11:30 2018

@author: Sofei1
"""

import pandas as pd
from urllib.request import urlopen

def construct_futures_symbols(symbol, start_year=2010, end_year=2014):

    futures = []
    months = 'HMUZ'  # March, June, September and December delivery codes
    for y in range(start_year, end_year+1):
        for m in months:
            futures.append("%s%s%s" % (symbol, m, y))
    return futures

def download_contract_from_quandl(contract, auth_token, dl_dir):

    # Construct the API call from the contract and auth_token    
    api_call_head = "http://www.quandl.com/api/v1/datasets/OFDP/FUTURE_%s.csv" % contract
    params = "?&auth_token=%s&sort_order=asc" % auth_token
    
    # Download the data from Quandl
    data = urlopen("%s%s" % (api_call_head, params)).read()
    
    # Store the data to disk
    fc = open('%s/%s.csv' % (dl_dir, contract), 'w')
    fc.write(data)
    fc.close()

def download_historical_contracts(symbol, auth_token, dl_dir, start_year=2010, end_year=2014):

    contracts = construct_futures_symbols(symbol, start_year, end_year)
    for c in contracts:
        download_contract_from_quandl(c, auth_token, dl_dir)
        
if __name__ == "__main__":
    symbol = 'ES'
    dl_dir = 'data/quandl/futures/ES'  # Make sure you've created this relative directory beforehand
    auth_token = 'yYgJde-mLawURfw9eyuo'  # Replace this with your authorisation token
    start_year = 2010
    end_year = 2014

    # Download the contracts into the directory
    download_historical_contracts(symbol, auth_token, dl_dir, start_year, end_year)

    # Open up a single contract via read_csv and plot the closing price
    es = pd.io.parsers.read_csv("%s/ESZ2014.csv" % dl_dir)