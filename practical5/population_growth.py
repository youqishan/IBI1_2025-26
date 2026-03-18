'''
1st, create a list / dictionary for the 5 countries' name and two population, I prefer later
2nd, calculate the percentage and add it to the new dictionary!!!
3rd, list the percentage (value) from big to small (in the new dictionary)
4th, print a sentense of the highst and lowest growth rate of population
5th, create a variable gene_find, and judge whether it is in the dictionary
'''

# import the libraby
import matplotlib.pyplot as plt
import numpy as np

# 1st, create a dictionary
pop_data = {
    'UK': [66.7, 69.2],
    'China': [1426, 1410],
    'Italy': [59.4, 58.9],
    'Brazil': [208.6, 212.0],
    'USA': [331.6, 340.1]
}

# 2nd, create a new dictionary to record the percentage
pop_change = {}

# using for-loop to calculate every growth rate
# for key, value in dictionary_name.items():
for country, pops in pop_data.items():
    pop_20 = pops[0]
    pop_24 = pops[1]
    change = (pop_24 - pop_20) / pop_20 * 100
    pop_change[country] = round(change, 2)

# 2nd, test the type-in in the new dictionary
print(pop_change)

'''
# using list to record the change
countries = ['UK', 'China', 'Italy', 'Brazil', 'USA']
pop2020 = [66.7, 1426, 59.4, 208.6, 331.6]
pop2024 = [69.2, 1410, 58.9, 212.0, 340.1]

pop_change = {}

for i in range(len(countries)):
    country = countries[i]
    p20 = pop2020[i]
    p24 = pop2024[i]
    change = (p24 - p20) / p20 * 100
    pop_change[country] = round(change, 2)
# Sorry but I prefer list now (laughing), it might be easier!!!
'''

# sort by rate of change: 
# sorted(a, b, reverse=True(from big to small) / False) means to sort a, in the rule of b
# xx.items() means change the (key, value) as a group
# key = lambda x: x[1], x means a group of (key, value), 
# key and lamda: format, x[1] means take the second element to rank
sorted_change = sorted(pop_change.items(), key=lambda x: x[1], reverse=True)

'''
It can also be divided as follows:

# define: sort by rate of change
def fun_sort(item):
    return item[1]

sorted_change = sorted(pop_change.items(), key=fun_sort, reverse=True)

'''

# test the print out
print("\nSort the population change rates from the largest increase to the largest decrease:")
for country, ch in sorted_change:
    print(f"{country}: {ch}%")

max_increase = sorted_change[0]
max_decrease = sorted_change[-1]  # Negative indexing starts from -1 and counts from right to left.
print(f"\nThe country with the largest population growth: {max_increase[0]} ({max_increase[1]}%)")
print(f"The countries with the largest population decline: {max_decrease[0]} ({max_decrease[1]}%)")

# 4th, draw the pie graph
# set the variable for the x-axis and y-axis
sorted_countries = [x[0] for x in sorted_change]
sorted_vals = [x[1] for x in sorted_change]

# Draw a bar chart, with positive and negative values colored red and blue.
colors = ['red' if x > 0 else 'blue' for x in sorted_vals]
plt.bar(sorted_countries, sorted_vals, color=colors, width=0.6)

# add the title and discription of x-axis and y-axis
plt.title('2020-2024 Percentage Change in Population of Various Countries', fontsize=14)
plt.xlabel('Countries', fontsize=12)
plt.ylabel('Percentage change in population (%)', fontsize=12)
# Add a horizontal zero line to more clearly distinguish between increases and decreases
plt.axhline(y=0, color='black', linestyle='-', alpha=0.8)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()