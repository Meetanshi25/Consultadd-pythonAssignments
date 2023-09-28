# 1. Write a program that calculates and prints the value according to the given formula:
# Q= Square root of [(2*C*D)/H]
# Following are the fixed values of C and H:
# C is 50.
# H is 30.
# D is a variable whose values should be input to your program in a comma-separated sequence.

from math import sqrt

class solution():
    def __init__(self):
        self.C = 50
        self.H = 30

    def calculate(self,D):
        Q = sqrt((2*self.C*D)/self.H)
        return Q

resultObj = solution()

input_val = float(input("Enter Value of D "))
result = resultObj.calculate(input_val)
print(result)