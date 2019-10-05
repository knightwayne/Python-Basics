# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 23:29:06 2018

@author: Arnav Ishaan
"""

def power(x,y):
    if (y==0):
        return 1
    else:
        return x*power(x,y-1)
    
#print(power(5,2))

print("Input x")
x=int(input())
print("Input y")
y=int(input())

print("x^y is ",power(x,y))