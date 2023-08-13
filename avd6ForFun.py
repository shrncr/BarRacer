# -*- coding: utf-8 -*-
"""
Sara Hrnciar
CSC 101
Lori

A bar chart racer displaying the top 10 most popular girls names in the US from the 1800s to now
"""
import matplotlib.pyplot as plt
import pandas as pd
from time import sleep # found on google to add a delay between each bar chart

#import the data
dataVibes = pd.read_csv(r"C:\Users\lovey\Downloads\baby-names.csv")

dataVibes = dataVibes[dataVibes.date != "100"]
diction = {}

#fill the dictionary with what will be the individual time periods for the racer
for i in range(99, 165348, 100):
    #key becomes the time period
    key = dataVibes.iloc[i, 0]
    #value is the 100 most popular names
    value = dataVibes.iloc[i-100:i,:]
    diction[key] = value

for key in diction:
    #sort the vals from greatest to least, narrow it down to female names only, and narrow the female names down to the top 10 most popular
    diction[key] = diction[key].sort_values(by =['numBirths'], ascending = True)
    #diction[key] = diction[key][diction[key].sex == "Female"]
    diction[key] = diction[key].iloc[0:10,:]
    colors = []
    for i in diction[key].sex:
        if i == "Female":
            colors.append("pink")
        else:
            colors.append("purple")
    #make the plot
    plt.figure(figsize=(23, 15))
    #eaach iteration will create a different bar chart!
    plt.barh(diction[key].name, diction[key].numBirths, color = colors, label = key)
    plt.xlabel("Number of Females Born w Name", size = 40)
    plt.ylabel("Name", size = 40)
    plt.title("Top 10 Most Popular Names in the U.S. Through Time", size = 55)
    plt.legend(loc ="lower right", prop = {'size' : 60}, frameon = False)
    plt.yticks(size = 30)
    plt.xticks(size = 30)
    plt.show()
    sleep(.0000000000000000000000000000000000000000001)
    plt.clf()
