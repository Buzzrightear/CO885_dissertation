import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

split_point = 365*144

df = pd.read_csv('wind_data_1.csv', parse_dates=['Date time',])

print(df.head())

df=df[['Date time', 'Power avg']].dropna()

print(df.head())


train_features = df.drop(['Power avg'], axis = 1).head(len(df)-split_point) #Get rid of the 'Power avg' columns inc. column heading and keep all rows up to split_point
print(train_features.head())

train_labels = df['Power avg'].head(len(df)-split_point) #Just show 'Power avg' column without col heading up to split-point
print(train_labels.head())

val_features = df.drop(['Power avg'], axis = 1).tail(split_point) #Get rid of the 'Power avg' columns inc. column heading and keep all rows after split_point
print(val_features.head())

val_labels = df['Power avg'].tail(split_point) #Just show 'Power avg' column without col heading ater split-point
print(val_labels.head())
