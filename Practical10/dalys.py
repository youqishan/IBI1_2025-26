'''
(√) 1. read csv file of DALYs 
(√) 2. show the first 10 rows and 3&4 columns of the data frame
    2.1 add comments to show Afghanistan's first 10 years' maximum DALYs in which year
(√) 3. used a Boolean to show all years for which DALYs were about Zimbabwe
    3.1 add comments to show the first and last years in which DALYs were about Zimbabwe
(√) 4. computed the countries with the maximum and mimumum DALYs in 2019
    4.1 add comments to show these countries' names
(√) 5. plotted the DALYs of the contry with the maximum DALYs in 2019
    5.1 show the DALYS over time
(x) 6.1 find out whether the global DALYs have increased or decreased in 1999-2019, plotting a line graph
(x) 6.2 contract five great permanent members of security council, plotting a line graph
(√) 6.3 find out The regions with the most stable / most volatile changes in DALYs over 30 years
'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Set working directory and test
os.chdir('/Users/youqishan/Desktop/IBI1/IBI1_2025-26/Practical10')
# print("current directory", os.getcwd())
# print("files in the current directory", os.listdir())

# =====================  1. read csv file of DALYs into a data frame  ====================
dalys_data = pd.read_csv('dalys-rate-from-all-causes.csv')
# dalys_data.info()

# =====================  2. show the first 10 rows and 3&4 columns of the data frame  ====================
print(dalys_data.iloc[:10, 2:4])
# the maximum DALYs for Afghanistan in the first 10 years is in 1998, with a value of 86656.29
print(f"The maximum DALYs for Afghanistan in the first 10 years is in 1998, with a value of 86656.29.")

# =====================  3. used a Boolean to show all years for which DALYs were about Zimbabwe  ====================
zimbabwe_dalys = dalys_data[dalys_data['Entity'] == 'Zimbabwe']
print(zimbabwe_dalys)
# just output the years for Zimbabwe
print(zimbabwe_dalys['Year'])
# the first year in which DALYs were about Zimbabwe is 1990, and the last year is 2019
print(f"The first year in which DALYs were about Zimbabwe is {zimbabwe_dalys['Year'].min()}, and the last year is {zimbabwe_dalys['Year'].max()}.")

# =====================  4. computed the countries with the maximum and mimumum DALYs in 2019  ====================
dalys_2019 = dalys_data[dalys_data['Year'] == 2019]
# dalys_2019.info()
max_dalys_2019 = dalys_2019['DALYs'].max()
min_dalys_2019 = dalys_2019['DALYs'].min()
max_country_2019 = dalys_2019[dalys_2019['DALYs'] == max_dalys_2019]['Entity'].values[0]
min_country_2019 = dalys_2019[dalys_2019['DALYs'] == min_dalys_2019]['Entity'].values[0]
# .values is to get the list, and [0] is to get the first element, counrey name
# The country with the maximum DALYs in 2019 is Lesotho with a value of 90771.64.
# The country with the minimum DALYs in 2019 is Singapore with a value of 15045.11.
print(f"The country with the maximum DALYs in 2019 is {max_country_2019} with a value of {max_dalys_2019}.")
print(f"The country with the minimum DALYs in 2019 is {min_country_2019} with a value of {min_dalys_2019}.")

# =====================  5. plotted the DALYs of the country with the maximum DALYs in 2019  ====================
plt.figure(figsize=(10, 6))
max_country_dalys = dalys_data[dalys_data['Entity'] == max_country_2019]
plt.plot(max_country_dalys['Year'], max_country_dalys['DALYs'], label=max_country_2019)
# # plot the DALYs of the country with the minimum DALYs in 2019
# min_country_dalys = dalys_data[dalys_data['Entity'] == min_country_2019]
# plt.plot(min_country_dalys['Year'], min_country_dalys['DALYs'], label=min_country_2019)
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.title('DALYs over time for the countries with max DALYs in 2019 (Lesotho)')
plt.xticks(rotation=45)
plt.grid(alpha=0.3)
plt.legend()

plt.savefig('dalys_plot_for_max_dalys(2019)_Lesotho.png')  # Save the plot as a PNG file
plt.show()

'''

# =====================  6.1 find out whether the global DALYs have increased or decreased in 1999-2019, plotting a line graph  ====================
global_dalys = dalys_data.groupby('Year')['DALYs'].sum().reset_index()
plt.figure(figsize=(10, 6))
plt.plot(global_dalys['Year'], global_dalys['DALYs'], label='Global DALYs')
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.title('Global DALYs over time (1990-2019)')
plt.xticks(rotation=45)
plt.grid(alpha=0.3)
plt.legend()
plt.savefig('global_dalys_over_time.png')  # Save the plot as a PNG file
plt.show()

# =====================  6.2 contract five great permanent members of security council, plotting a line graph  ====================
region1 = "China"
region2 = "United States"
region3 = "Russia"
region4 = "United Kingdom"
region5 = "France"

# colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
colors = ['#4E79A7', '#F28E2B', '#E15759', '#76B7B2', '#59A14F']
i = 0
plt.figure(figsize=(10, 6))

df_compare = dalys_data[dalys_data['Entity'].isin([region1, region2, region3, region4, region5])]
for region, group in df_compare.groupby('Entity'):
    plt.plot(group['Year'], group['DALYs'], label=region, linewidth=2, color=colors[i])
    i = i + 1

plt.xlabel('Year')
plt.ylabel('DALYs')
plt.title('Five great permanent members of security council')
plt.xticks(rotation=45)
plt.grid(alpha=0.3)
plt.legend()
plt.savefig('five_great_permanent_members_of_security_council.png')  # Save the plot as a PNG file
plt.show()

'''

# =====================  6.3 find out The regions with the most stable / most volatile changes in DALYs over 30 years  ====================
volatility = dalys_data.groupby('Entity')['DALYs'].std().sort_values(ascending=False).reset_index()
volatility.columns = ['region', 'Standard deviation of DALY fluctuations']

print("The 10 regions with the greatest fluctuations: ")
print(volatility.head(10))
print("\nThe 10 regions with the smallest fluctuations:")
print(volatility.tail(10))

# find out why Rwanda had such a strange data
plt.figure(figsize=(10, 6))
max_country_dalys = dalys_data[dalys_data['Entity'] == 'Rwanda']
plt.plot(max_country_dalys['Year'], max_country_dalys['DALYs'], label='Rwanda')
# # plot the DALYs of the country with the minimum DALYs in 2019
# min_country_dalys = dalys_data[dalys_data['Entity'] == min_country_2019]
# plt.plot(min_country_dalys['Year'], min_country_dalys['DALYs'], label=min_country_2019)
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.title('DALYs over time for Rwanda')
plt.xticks(rotation=45)
plt.grid(alpha=0.3)
plt.legend()

plt.savefig('dalys_plot_for_Rwanda.png')  # Save the plot as a PNG file
plt.show()

# In 1994, a major ethnic massacre occurred in Rwanda.
# Resulting in the DALYs data for that year being more than five times that of the previous year and the following year.
# Making Rwanda the country with the largest standard deviation in DALYs data.