#Program to format date time data of wind farm records

import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

row_list = []
temp_string = ""

with open('Data_2011_15.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        row_list.append(row)
print(row_list[0])
print(row_list[1])
print(row_list[2])
print(row_list[3])


with open('wind_data_1.csv', mode='w') as wind_data_file:
    wind_data_file = csv.writer(wind_data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    wind_data_file.writerow(['Date time', 'Wind min', 'Wind avg', 'Wind max', 'Power min', 'Power avg', 'Power max', 'Wind dir',])    
    for i in range(1,len(row_list)):
        temp_string = row_list[i][0] + " " + row_list[i][1]
        wind_data_file.writerow([temp_string, row_list[i][2],row_list[i][3],row_list[i][4],row_list[i][5],row_list[i][6],row_list[i][7], row_list[i][8],])    

