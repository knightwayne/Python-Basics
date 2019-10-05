# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 23:36:33 2018

@author: Arnav Ishaan

Hackerrank Py Practice Runner Up Score
"""

n = int(input())
#arr = map(int, input().split())
arr=[]
while(n>0):
    a=int(input())
    arr.append(a)
    n=n-1
arr.sort()
arr.reverse()

print(arr)

x=arr[0]
for i in range(1,len(arr)):
    if(x!=arr[i]):
        print("runner up score is ",arr[i])
        break
    else:
        continue