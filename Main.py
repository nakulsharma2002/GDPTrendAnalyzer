import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Show import filter_gdp_data
from Show import get_country_input
from Show import plot_gdp_data


class Collect_data:
    def __init__(self):
        self.data = 'C:\\Users\\snaku\\OneDrive\\Desktop\\python\\pandas\\world.csv'



class Clean_data:
    def __init__(self):
        self.collect = Collect_data()
    def data_clean(self):
        print("Data collect")
        df = pd.read_csv(self.collect.data)
        print("data cleaning ")
        df.dropna(inplace=True)
        return df



class Analysis_Data:
    def __init__(self):
        pass
    def what_show_you(self,data):
        # Extract the 'Series Name' column
        series_names = data['Series Name']

        # Get the unique series names
        unique_series_names = series_names.unique()

        # Create a dictionary with index numbers as keys and unique series names as values
        series_dict = {index + 1: name for index, name in enumerate(unique_series_names)}
        for k,v in sorted(series_dict.items()):
            print(f"{k} - {v}")

        return series_dict
    

    def user_input(self,title):
        user_input = int(input("\n\nEnter which detail you want (you can  enter the index number)\t=> "))
        if user_input not in  title.keys():
            print('Sir you enter the wrong number')
        else: 
            return title[user_input]


    def filter_data(self,reading_data,user_input):
        return filter_gdp_data(reading_data,user_input)


    def country(self,data):
        return get_country_input(data)
    

    def graph(self,filter_data,country_name,user_input):
        plot_gdp_data(filter_data,country_name,user_input)



if __name__=='__main__':
    clean = Clean_data()
    cleaning = clean.data_clean()


    Data = Analysis_Data()
    title = Data.what_show_you(cleaning)
    user_input = Data.user_input(title)
    filter = Data.filter_data(cleaning,user_input)
    country_name = Data.country(cleaning)
    show_graph = Data.graph(filter,country_name,user_input)



    

