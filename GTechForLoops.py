#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 22:56:08 2018

@author: meganporter
"""




#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#In math, factorial is a mathematical operation where an
#integer is multipled by every number between itself and 1.
#For example, 5 factorial is 5 * 4 * 3 * 2 * 1, or 120.
#Factorial is represented by an exclamation point: 5!
#
#Use a for loop to calculate the factorial of the number
#given by mystery_int above. Then, print the result.
#
#Hint: Running a loop from 1 to mystery_int will give you
#all the integers you need to multiply together. You'll need
#to track the total product using a variable declared before
#starting the loop, though!


#Add your code here!
mystery_int = 5
factorial = 1
for i in range (1, mystery_int + 1):
    factorial *= i
print(factorial)  



#_____________________________________________________________________________
print("Third loop:")

#Write a loop here that prints the even numbers only from 1
#to 20, inclusive. Print each number on a separate line.
#
#Hint: There are two ways to do this. You can use the syntax
#for the range() function shown in the multiple-choice
#problem above, or you can use a conditional with a modulus
#operator to determine whether or not to print.

for k in range (2, 21, 2):
    print(k)
   
for l in range(1,21):
    if l % 2 == 0:
        print(l)







