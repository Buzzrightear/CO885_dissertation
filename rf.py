# Taken from https://colab.research.google.com/drive/1WJjty6Q87WZeqBZVy6--cgrnuW4p50PP#scrollTo=1iEXEPxRNNUX 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv('wind_data_1.csv', parse_dates=['Date time',])
df=df[['Date time', 'Power avg']].dropna()

#print(df.head())

def train_forest(df, split_point):
  train_features = df.drop(['Power avg'], axis = 1).head(len(df)-split_point)
  train_labels = df['Power avg'].head(len(df)-split_point)
  val_features = df.drop(['Power avg'], axis = 1).tail(split_point)
  val_labels = df['Power avg'].tail(split_point)

  rf = RandomForestRegressor(n_estimators = 50, random_state = 42)
  rf.fit(train_features, train_labels)

  return [rf, train_features, train_labels, val_features, val_labels]

def check_predictions(rf, train_features, train_labels, val_features, val_labels):
  fig,axes  = plt.subplots(nrows=2, ncols=2, figsize=(10,10))
  fig.tight_layout(pad=6.0)
  predictions_plot(rf, train_features, train_labels, axes[0,0])
  predictions_plot(rf, val_features, val_labels, axes[0,1])
  predictions_plot(rf, train_features.tail(7*48), train_labels.tail(7*48), axes[1,0])
  predictions_plot(rf, val_features.head(7*48), val_labels.head(7*48), axes[1,1])

def predictions_plot(rf, features, labels, ax):
  predictions = rf.predict(features)
  errors = abs(predictions - labels)
  title='MAE:' + str(round(np.mean(errors), 2)) + \
        ' MAX_AE:' + str(round(np.max(abs(errors)), 2)) + \
        ' RMSE:' + str(round(np.sqrt(np.mean(np.square(errors))), 2))
  pd.DataFrame({'labels': labels, 
                'predictions': predictions, 
                'Date / time': features['Date time']}).plot(title=title, ax=ax, x='Date time')
                
[rf, train_features, train_labels, val_features, val_labels] = train_forest(df, 365*144) #Attempting to train on last year' worth of entries (144 entries per day)
#check_predictions(rf, train_features, train_labels, val_features, val_labels)