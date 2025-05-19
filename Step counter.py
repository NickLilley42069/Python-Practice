"""I want to make a step counter that works out roughly how many calories
you lose with how many steps you have walked that day

Based on a chart I found from verywellfit.com, there are charts based on height
and weight and even the steps that show how many calories are burnt.

For the sake of simplicity and a quiet life, i will use the 5"6 - 5"11
converter table.
"""

"""
For this, I will be making a csv file for the lookup directory
"""
#Weight - IN KG
weight = float(input("Please enter your weight in kg: "))

#Steps - IN THOUSANDS
steps = float(input("Please enter your steps in thousands: "))

#Calories

calories = round(0.0005 * weight * steps, 2)

print(calories)