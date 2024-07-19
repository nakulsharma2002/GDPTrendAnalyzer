import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



# Function to filter GDP data
def filter_gdp_data(data,user_input):
    return data[data['Series Name'] == user_input]





# Function to get user input for countries
def get_country_input(data):
    # country_name = data['Country Name']
    # unique_names = country_name.unique()
    # count = 1
    # for i in unique_names:
    #     print(f'{count} - {i}')
    #     count +=1

    # countries = input("Enter country names in separated by commas: => (first letter of every country should be capital )").split(',')
    # return [country.strip() for country in countries]





    # countries = input("Enter country names separated by commas: ").split(',')
    # print(countries)
    # return [country.strip() for country in countries]

# Function to plot GDP data for the selected countries
    country_name = data['Country Name']
    unique_names = country_name.unique()
    
    # Create a dictionary with indices as keys and country names as values
    country_dict = {index + 1: name for index, name in enumerate(unique_names)}
    
    # Display the country dictionary to the user
    for k, v in sorted(country_dict.items()):
        print(f"{k} - {v}")
        
    # Prompt the user to enter country indices separated by commas
    indices = input("Enter country indices separated by commas: => ").split(',')
    
    # Validate and convert input indices to a list of corresponding country names
    selected_countries = []
    for index in indices:
        try:
            index = int(index.strip())
            if index in country_dict:
                selected_countries.append(country_dict[index])
            else:
                print(f"Index {index} is not valid")
        except ValueError:
            print(f"{index.strip()} is not a valid index")
    
    return selected_countries



def plot_gdp_data(GDP_Growth, countries ,type_of_data):
   
    GDP_Growth = GDP_Growth.set_index('Country Name')
    years = [col for col in GDP_Growth.columns if col.isdigit()]
    GDP_Growth = GDP_Growth[years].replace('..', np.nan).astype(float)
    
    # Transpose the data for plotting
    GDP_Growth = GDP_Growth.transpose()
    
    # Plotting the data
    plt.figure(figsize=(13, 6))
    
    for country in countries:
        if country in GDP_Growth.columns:
            plt.plot( GDP_Growth.index,GDP_Growth[country], label=country)
        else:
            print(f"Data for {country} not found")

    
    plt.title(f'{type_of_data} of Different Countries Over Years')
    plt.xlabel('year')
    plt.ylabel(f'{type_of_data}')
    plt.legend()
    plt.grid(True)
    plt.show()
