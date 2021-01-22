import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

#read data from a file 'tweets'
def read_data(file_name = 'NSE-Tata.csv'):
    data = pd.read_csv(file_name)
    return data

def figure_data(data):
    data["Date"]=pd.to_datetime(data.Date,format="%Y-%m-%d")
    data.index=data['Date']
    plt.figure(figsize=(16,8))
    plt.plot(data["Close"],label='Close Price history')

def sorting_result_by_date(data):
    new_data = data.sort_index(ascending=True,axis=0)
    new_dataset = pd.DataFrame(index=range(0,len(data)),columns=['Date','Close'])    
    for i in range(0,len(new_dataset)):
        new_dataset["Date"][i]=new_data['Date'][i]
        new_dataset["Close"][i]=new_data["Close"][i]
    return new_dataset

def data_normalization(new_dataSet):
    scaler=MinMaxScaler(feature_range=(0,1))
    final_dataset=new_dataset.values
    return final_dataset
    
    
data = read_data()
new_dataset = sorting_result_by_date(data)
normalized_dataSet = data_normalization(new_dataset)
print(normalized_dataSet)