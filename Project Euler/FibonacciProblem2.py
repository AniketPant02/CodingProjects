# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 20:46:27 2017

@author: Aniket Pant
"""

sum = 0 # This is the total sum

#Change second range limit to 1 after number you want to sum till (n-1)
for current in range(1, 10):
    toAdd = 1
    lastFib = 1
    secondLastFib = 0
    
    for fib in range(2, current + 1):
        next = lastFib + secondLastFib
        
        toAdd = int(str(toAdd) + str(next))
        
        secondLastFib = lastFib
        lastFib = next
        
    sum += toAdd
    
print(sum)