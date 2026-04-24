# import libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#change the directory to where the file is stored
os.chdir("/Users/j/Desktop/IBI Practical/IBI1_2025-26/Practical10")
#test the dictionary
print(os.getcwd())
print(os.listdir())

#read the file using pandas
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

#read the head 5 lines
print(dalys_data.head(5))
#look at the bsic information
print(dalys_data.info())

#use describe to get the statistic information
print(dalys_data.describe())
# Maximum DALYs = 693367.49
# Minimum DALYs = 15045.11
# First recorded year = 1990
# Most recent year = 2019

#extract specific data using iloc and loc
print(dalys_data.iloc[0:10,2:4])#show the third and fourth columns for the first 10 raws
first10=dalys_data.iloc[0:10,2:4]
max_row=first10.loc[first10.DALYs.idxmax()]
print("The maximum DALYs across the first 10 years in Afghanistan was recorded in 1998")
# The maximum DALYs across the first 10 years in Afghanistan was recorded in 1998.

#use a Boolean to show all years that DALYs were recorded in Zimbabwe
entity_list=[]
for i in dalys_data["Entity"]:
    if i=="Zimbabwe":
        entity_list.append(True)
    else:
        entity_list.append(False)
zimbabwe=dalys_data.loc[dalys_data.Entity=="Zimbabwe",["Year"]]
first_year=zimbabwe["Year"].iloc[0]
last_year=zimbabwe["Year"].iloc[-1]
print(zimbabwe)
print("The first year:",first_year)
print("The last year:",last_year)
print("Zimbabwe data were recorded from 1990 to 2019.")
#Zimbabwe data were recorded from 1990 to 2019.

#compute the countries with the maximum and minumum DALYs in 2019
recent_data = dalys_data.loc[dalys_data.Year == 2019, ["Entity", "DALYs"]]#put the 2019 data into a new object
print(recent_data)
max_row=recent_data.loc[recent_data.DALYs.idxmax()]#find the maximum DALYs in 2019
min_row=recent_data.loc[recent_data.DALYs.idxmin()]#find the minimum DALYs in 2019
print(max_row)
print(min_row)
print("In 2019, the country with the highest DALYs was Lesotho.")
print("In 2019, the country with the lowest DALYs was Singapore.")
# In 2019, the country with the highest DALYs was Lesotho.
# In 2019, the country with the lowest DALYs was Singapore.

#draw the plot
lesotho = dalys_data.loc[dalys_data.Entity == "Lesotho", :]#choose Lesotho as the country
plt.plot(lesotho.Year, lesotho.DALYs, 'bo-')# set the x, y axis and tuxing yang shi 
#- :means connection between each dot
plt.title("DALYs in Lesotho Over Time")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.xticks(rotation=90)
plt.grid(True, alpha=0.3)# tou ming du is 0.3
plt.show()

# Question analysis starts here

recent_data = dalys_data.loc[dalys_data.Year == 2019, ["Entity", "DALYs"]]
plt.figure(figsize=(10,5))
plt.hist(recent_data.DALYs, bins=20, edgecolor="black")#bins:20个区间，edgecolor：the edge of the column is black

plt.title("Distribution of DALYs Across Countries in 2019")
plt.xlabel("DALYs")
plt.ylabel("Number of Countries")

plt.grid(True, alpha=0.3)

plt.show()