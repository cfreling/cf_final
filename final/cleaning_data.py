#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 18:21:34 2022

@author: cocofreling
"""


import os
import pandas as pd
# import geopandas
# from geopandas import GeoDataFrame
# from shapely.geometry import Point
# import matplotlib.pyplot as plt

PATH = r'/Users/cocofreling/Documents/W22_Data Visualization/final'
os.chdir(PATH)

def upload_file(fname):
    file_path = os.path.join(PATH, fname)
    file = pd.read_csv(file_path)
    return file 

us_lfg_raw = upload_file("us_lfg.csv")

# For Jupiter landfill and methane charts
us_lfg = us_lfg_raw.drop(['GHGRP ID', 
                          'Landfill Name',
                          'Physical Address',
                          'City',
                          'Zip Code',
                          'Ownership Type',
                          'Landfill Owner Organization(s)',
                          'Year Landfill Opened',
                          'Landfill Closure Year',
                          'Waste in Place Year',
                          'LFG Collection System In Place?',
                          'LFG Flared (mmscfd)',
                          'Project ID',
                          'Project Name',
                          'Project Start Date',
                          'Project Shutdown Date',
                          'RNG Delivery Method',
                          'Actual MW Generation',
                          'Rated MW Capacity',
                          'LFG Flow to Project (mmscfd)',
                          'Current Year Emission Reductions (MMTCO2e/yr) - Direct',
                          'Current Year Emission Reductions (MMTCO2e/yr) - Avoided'], axis=1)



us_lfg = us_lfg.rename(columns={'Landfill ID':'Landfill_ID',
                           'Current Landfill Status':'Current_Status',
                           'Waste in Place (tons)':'Current_Waste_Tons',
                           'LFG Collected (mmscfd)':'LFG_Collected',
                           'Current Project Status':'Project_Status',
                           'Project Type Category':'Project_Type',
                           'LFG Energy Project Type':'LFG_Energy_Type'}, errors='raise')
us_lfg = us_lfg.drop_duplicates()
us_lfg['Current_Waste_Tons'] = us_lfg['Current_Waste_Tons'].astype(float, errors = 'raise')

us_grouped = us_lfg.groupby('State')['Current_Waste_Tons','LFG_Collected'].sum()


filepath = file_path = os.path.join(PATH, 'us_waste.csv')
us_grouped.to_csv(filepath)