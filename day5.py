"""
# Task
# Given an integer, n,
# print its firs 10 multiples.
# Each multiple  (where ) should be printed on a new line
# in the form: n x i = result.
"""

n = int(input().strip())

for i in range(10):
    print("%i x %i = %i" %(n,i+1, n*(i+1)))
