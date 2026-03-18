'''
1st, create a list for the 11 heart rate s
2nd, print the len(L) of the list and calculate the average
3rd, sort every heart rate to its category and find which category have most patients
    print a sentense to tell the amount of each category and category have most patients
4th, create a pie chart, show the number of patients in each category
'''

# import the libraby
import matplotlib.pyplot as plt
import numpy as np

# 1st, create the list
heart_rates = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]

total_patients = len(heart_rates)
mean = sum(heart_rates) / total_patients
mean = round(mean, 2)

# 2nd, print
print(f"there are {total_patients} patients in this survey, the average of their heart rate is {mean} bpm.")

# 3rd, sort
low = 0
normal = 0
high = 0

for i in heart_rates:
    if i < 60:
        low += 1
    elif i > 120:
        high += 1
    else:
        normal += 1
print(f"There are {low} people have a low heart rate,"
      f" {normal} people have normal heart rate,"
      f" and {high} people have high heart rate")

# 3rd, judge
max_count = max(low, normal, high)
if max_count == low:
    max_category = "low"
elif max_count == normal:
    max_category = "normal"
else:
    max_category = "high"
print(f"The largest category is {max_category}, which have {max_count} people.")

# 4th, draw the pie graph
# set the variable for the x-axis and y-axis
labels = ['low', 'normal', 'high']
sizes = [low, normal, high]
colors = ['#ff9999', '#66b3ff', '#99ff99']  # make a nice color, light blue, light red, and light green

# wmphasize the portion that have most people
explode = (0.1 if max_count == low else 0, 
           0.1 if max_count == normal else 0, 
           0.1 if max_count == high else 0)

# create the pie chart
plt.pie(sizes, explode=explode,  # set the size of each sector (value), emphasize a sector (the value is the length that extend the circle)
        labels=labels, colors=colors,  # set English name for each sector, dye color for each section
        autopct='%1.0f%%', shadow=True, startangle=90)  # keep 0 decimal place, set the shadow, set the starting drawing angle
# 标注完整
plt.title('the pie chart of the heart rate', fontsize=14)
# plt.axis('equal') # ensure the pie chart is a circle
plt.show()