# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 13:06:18 2020

@author: skyle
"""

import math

x = float(input("Enter an angle in degrees: "))
if x > 360:
    x = x % 360
x = x*math.pi/180

term = x
sum = x
error = 1E-8
n = 2

while abs (term/sum) > error:
    term = -term*x*x/((2*n-1)*(2*n-2)) 
    sum = sum + term
    n = n+1

print(sum)