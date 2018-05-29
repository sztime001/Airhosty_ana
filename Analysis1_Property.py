#1. import 
import pandas as pd
import numpy as np
import time
import datetime

listings_file = 'C:\\Users\\sofei\\Dropbox\\A Sofei\\CS\\Airhosty\\Data\\data.csv'

#import columns we want to extract
columns = ['Reservation Code',
           'Listing ID',
           'Full Address',
           'Booking User ID',
           'Checkin Date',
           'Checkout Date',
           'Nights',
           'Guests',
           'Guest Phones',
           'Base Price',
           'Extrac',
           'Fee',
           'Tax',
           'Total']
listing = pd.read_csv(listings_file, usecols=columns)

#rename columns
listing.columns = ['Reservation_Code',
           'Listing_ID',
           'Full_Address',
           'Booking_User_ID',
           'Checkin_Date',
           'Checkout_Date',
           'Nights',
           'Guests',
           'Guest—_Phones',
           'Base_Price',
           'Extrac',
           'Fee',
           'Tax',
           'Total']

#2. cleaning up the data
# replacing NaN values with 0
listing.fillna(0, inplace=True)

#separating date column into day month and year
listing['Checkin_Year'],listing['Checkin_Month'],listing['Checkin_Day']=listing['Checkin_Date'].str.split('-',2).str
listing['Checkout_Year'],listing['Checkout_Month'],listing['Checkout_Day']=listing['Checkout_Date'].str.split('-',2).str

#sort data by Listing ID and Checkin Date
listing = listing.sort_values(by = ['Listing_ID','Checkin_Date'])

#group data by Listing ID
property_info = listing.groupby(['Listing_ID', 'Full_Address']).agg({'Checkin_Date': 'min','Checkout_Date': 'max'})
property_info = property_info.rename(columns = {'Checkin_Date':'Come_into_Market','Checkout_Date':'End_of_Sta'})

#3. analysis of occupancy
#start of sta: come into market
#end of sta:2018-3-31 
end_of_sta = '2018-04-01'
listing1 = listing[(listing.Checkout_Date <= end_of_sta)]
data1 = listing1.groupby(['Listing_ID', 'Full_Address']).agg({'Checkin_Date':'min','Nights': 'sum'})
data1 = data1.rename(columns = {'Checkin_Date':'Come_into_Market'})
# calculate days bwtween start and end
data1['Total_Nights'] =  [(datetime.datetime.strptime(end_of_sta, '%Y-%m-%d') - datetime.datetime.strptime(x, '%Y-%m-%d')).days for x in data1.Come_into_Market]
data1['Occupancy'] = data1.Nights/data1.Total_Nights

#start of sta: start of each year
#end of sta: end of each year
data_y = listing1.groupby(['Listing_ID', 'Full_Address','Checkout_Year']).agg({'Checkin_Date':'min','Nights': 'sum'})
data_y = data_y.rename(columns = {'Checkin_Date':'Start_of_Sta'})
data_y['Total_Nights'] = 0
for i in range(len(data_y.index)):
    if data_y.index[i][2] == '2017':
        data_y.Total_Nights[i] =  (datetime.datetime.strptime("2018-01-01", '%Y-%m-%d') - datetime.datetime.strptime(data_y.Start_of_Sta[i], '%Y-%m-%d')).days
    elif data_y.index[i][2] == '2018':
        data_y.Total_Nights[i] =  (datetime.datetime.strptime("2018-04-01", '%Y-%m-%d') - datetime.datetime.strptime(data_y.Start_of_Sta[i], '%Y-%m-%d')).days
data_y['Occupancy'] = data_y.Nights/data_y.Total_Nights      

#start of sta: start of each year
#end of sta: end of each year
data_m = listing1.groupby(['Listing_ID', 'Full_Address','Checkout_Year','Checkout_Month']).agg({'Checkin_Date':'min','Nights': 'sum'})
data_m = data_m.rename(columns = {'Checkin_Date':'Start_of_Sta'})
  


