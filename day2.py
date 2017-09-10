"""
# Task
# Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.
"""

meal = float(input())
tipPercent = float(input())
taxPercent  = float(input())

tip = meal*(tipPercent/100)
tax = meal*(taxPercent/100)

totalCost = int(round(meal + tax + tip))

print("The total meal cost is %i dollars." % totalCost)
