#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 15:41:20 2018

@author: kathytan
"""
#Day01
import pandas as pd
data = pd.read_csv("/Users/kathytan/Desktop/Advent of Code/Advent of Code day 1.csv", header=None,names="d")

#Puzzle 1 
result=data.sum()
print(result)

#Puzzle 2
data['result'] = 0

#data.iloc[result][row]
seen=set()
value = 0
found = False
while(not found):
    for i in range(len(data)):
        value = value + data['d'][i]
        if value in seen: 
            found=True
            print(value)
            break
        else:
            seen.add(value)
            
#Day02
#Puzzle 1
twoletters=0
threeletters=0
file = open('day02.txt','r')
for line in file:
    counts={}
    for letter in line:
        if letter in counts:
            counts[letter]+=1
        else:
            counts[letter]=1
    if 2 in counts.values():
        twoletters+=1
    if 3 in counts.values():
        threeletters+=1
ans=threeletters*twoletters
print(ans)

#Puzzle 2
#checklist=list()
#file=open('day02.txt','r')
#for line in file:
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    