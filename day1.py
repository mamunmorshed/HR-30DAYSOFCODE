"""
# Task
# Complete the code in the editor below. The variables , , and  are already declared and initialized for you. You must:
#
# Declare  variables: one of type int, one of type double, and one of type String.
# Read  lines of input from stdin (according to the sequence given in the Input Format section below) and initialize your  variables.
# Use the  operator to perform the following operations:
# Print the sum of  plus your int variable on a new line.
# Print the sum of  plus your double variable to a scale of one decimal place on a new line.
# Concatenate  with the string you read as input and print the result on a new line.
"""

i = 4
d = 4.0
s = 'HackerRank '

i_in = int(input())
d_in = float(input())
s_in = input()

d_t = d + d_in

print(i+i_in)
print("%.1f" % d_t)
print(s+s_in)