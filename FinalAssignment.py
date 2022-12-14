# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 03:13:56 2022

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 22:12:26 2022

@author: user
"""
"""Importing Libraries"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def get_data(filename):
    """ 
    This function takes filename as argument and
    read the data file into dataframes 
    
    """
    data=pd.read_csv(filename)
    datatranspose=data.set_index('Country Name').transpose()
    return data,datatranspose
country_list1=['Brazil', 'China', 'Canada', 'Denmark', 'Finland', 'Italy']
country_list2=['Brazil', 'France', 'Germany', 'India', 'Spain', 'United States']


def filter_bar_data(data):
    
    """
    Defining function for filtering years and 
    countries for plotting bar chart and returning the data
    
    """
    data=data[['Country Name', 'Indicator Name', '1990', '2000', '1994', '2013', '2019', '2020']]
    data=data[(data["Country Name"]=="Brazil")|
              (data["Country Name"]=="China")|
              (data["Country Name"]=="Canada")|
              (data["Country Name"]=="Denmark")|
              (data["Country Name"]=="Finland")|
              (data["Country Name"]=="Italy")]
    return data


def filter_line_plot(data):
    """
    Defining function for filtering years and 
    countries for plotting line plot and returning the data
    
    """
    data=data[['Country Name','Indicator Name', '1991', '1997', '2004', '2010', '2016', '2019']]
    data=data[(data["Country Name"]=="Brazil")|
              (data["Country Name"]=="France")|
              (data["Country Name"]=="Germany")|
              (data["Country Name"]=="India")|
              (data["Country Name"]=="Spain")|
              (data["Country Name"]=="United States")]
    return data


#Function for plotting bar graph
def barplot(data, label1, label2):
    plt.figure(figsize=(28, 20))
    sp=plt.subplot(1, 1, 1)
    x=np.arange(6)
    width=0.2
    
    bar_plt1=sp.bar(x, data["1990"], width, label=1990, color="red")
    bar_plt2=sp.bar(x+width, data["1994"], width, label=1994, color="yellow")
    bar_plt3=sp.bar(x+width*2, data["2000"], width, label=2000, color="green")
    
    sp.set_xlabel("Country", fontsize=40)
    sp.set_ylabel(label1, fontsize=40)
    sp.set_title(label2, fontsize=40)
    sp.set_xticks(x, country_list1, fontsize=30, rotation=90)
    sp.legend(fontsize=30)
   
    sp.bar_label(bar_plt1, padding=2, rotation=90, fontsize=18)
    sp.bar_label(bar_plt2, padding=2, rotation=90, fontsize=18)
    sp.bar_label(bar_plt3, padding=2, rotation=90, fontsize=18)
    plt.savefig("barplot.png")#Saving Barplot
    plt.show()
    
    
#Function for plotting Line plot   
def line_plot(data, label1, label2):
    plt.figure(figsize=(26, 10))
    data_index=data.set_index('Country Name')
    transpose_data=data_index.transpose()
    transpose_data=transpose_data.drop(index=['Indicator Name'])
    for i in range(len(country_list2)):
        plt.plot(transpose_data.index, transpose_data[country_list2[i]], label=country_list2[i])
    plt.title(label2, size=18)
    plt.xlabel("Years", size=12)
    plt.ylabel(label1, size=12)
    plt.xticks(rotation=90)
    plt.legend(fontsize=10)
    plt.savefig("lineplot.png")#Saving Lineplot
    plt.show() 
    
    
def pop_growth_mean():   
  """
  
  Function to calculate the mean of population growth for 5 countries

  """
  dataf1,dataf2 =get_data("C:/Users/user/Desktop/Assignment2/Population_growth.csv")
  data=dataf1.set_index('Country Name')
  transpose=data.transpose()
  #Droping unneccessary columns
  transpose=transpose.drop(index='Indicator Code')
  transpose=transpose.drop(index='Indicator Name')  
  transpose=transpose.drop(index='Country Code')
  clean_data=transpose.fillna(0)
  mean=clean_data[["Brazil", "China", "Canada", "Denmark", "Finland", "Italy"]].mean()
  return mean
    
  
#Reading data from csv file to data frames using the function get_data 
population_data, population_data1=get_data("C:/Users/user/Desktop/Assignment2/Population_growth.csv")
population_data=filter_bar_data(population_data)
Arable_data, Arable_data1=get_data("C:/Users/user/Desktop/Assignment2/Arable land.csv")
Arable_data=filter_bar_data(Arable_data)    
CO2_data, CO2_data1=get_data("C:/Users/user/Desktop/Assignment2/CO2_emission.csv")
CO2_data=filter_line_plot(CO2_data)
Cereal_data, Cereal_data1=get_data("C:/Users/user/Desktop/Assignment2/cereal.csv")
Cereal_data=filter_line_plot(Cereal_data)

#Plotting barplot for Population growth and Arable land
barplot(population_data, "Total population Growth",  "Population Growth")
barplot(Arable_data, "Total Land", " Arable land")
#Plotting line plot for CO2 Emission and Cereal Yield
line_plot(CO2_data, "CO2 Emission ", "CO2 Emission")
line_plot(Cereal_data, "Cereal yield", " Cereal Yield")

#Statistical function for returning mean for population growth data
pop_mean=pop_growth_mean()
print(pop_mean)  
##Writing data to csv file
pop_mean=pop_mean.to_csv("mean_of_population_growth.csv")
    
    