#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 19:02:54 2018

@author: meganporter
"""


#Imagine you're writing the software for an inventory system for
#a store. Part of the software needs to check to see if inputted
#product codes are valid.
#
#A product code is valid if all of the following conditions are
#true:
#
# - The length of the product code is a multiple of 4. It could
#   be 4, 8, 12, 16, 20, etc. characters long.
# - Every character in the product code is either an uppercase
#   character or a numeral. No lowercase letters or punctuation
#   marks are permitted.
# - The character sequence "A1" appears somewhere in the
#   product code.
#
#Write a function called valid_product_code. valid_product_code
#should have one parameter, a string. It should return True if
#the string is a valid product code, and False if it is not.


#Add your code here!
def valid_product_code(string):
    
    if "A1" in string and len(string) % 4 ==0 and string.isupper():
        return True
    else:
        return False
       
        
      
          
                        
            



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, True, False, False, False
print(valid_product_code("A12B44BP"))
print(valid_product_code("BFDSAUSA98932RWEFOEWA9FEAA1DSFSF"))
print(valid_product_code("A1BBD5"))
print(valid_product_code("BDD5664S"))
print(valid_product_code("66aBSaA1fdsv"))
print()
##############################################################################
#Write a function called remove_capitals. remove_capitals
#should accept one parameter, a string. It should return a
#string containing the original string with all the capital
#letters removed. Everything else should be in the same
#place and order as before.
#
#For example:
#
# remove_capitals("A1B2C3D") -> "123"
# remove_capitals("WHAT") -> ""
# remove_capitals("what") -> "what"
#
#Remember, capital letters have ordinal numbers between 65
#("A") and 90 ("Z"). You may use the ord() function to get
#a letter's ordinal number.
#
#Your function should be able to handle strings with no
#capitals (return the original string) and strings with all
#capitals (return an empty string). You may assume we'll
#only use regular characters (no emojis, formatting
#characters, etc.).


#Write your function here!
#def remove_capitals(a_string):
    
def remove_capitals(a_string):
    string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    string2 = ""
    for i in a_string:
        #if (i.islower() or i.isdigit() or i == " "):
        if not i.isupper():
           
            string2 += i
            
    return string2
            
        
            
              
    
            
    
    


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#123
#eorgia nstitute of echnology
print(remove_capitals("A1B2C3D"))
print(remove_capitals("Georgia Institute of Technology"))
#############################################################################

##############################################################################
#Write a function called valid_release_date. The function
#should have two parameters: a date and a string. The
#string will represent a type of media release: "Game",
#"Movie", "Album", "Show", and "Play".
#
#valid_release_date should check to see if the date is
#a valid date to release that type of media according to
#the following rules:
#
# - Albums should be released on Mondays.
# - Games should be released on Tuesdays.
# - Shows should be released on Wednesdays or Sundays.
# - Movies should be released on Fridays.
# - Plays should be released on Saturdays.
#
#valid_release_date should return True if the date is
#valid, False if it's not.
#
#The date will be an instance of Python's date class. If
#you have an instance of date called a_date, you can
#access an integer representing the day of the week with
#a_date.weekday(). a_date.weekday() will return 0 if the
#day is Monday, 1 if it's Tuesday, 2 if it's Wednesday,
#up to 6 if it's Sunday.
#
#If the type of release is not one of these strings,
#the release date is automatically invalid, so return
#False.

from datetime import date

#Write your function here!
def valid_release_date(a_date, string):
    if string == "Album":
        if  a_date.weekday() == 0:
            return True
        else:
            return False
    elif string == "Game":
        if a_date.weekday() == 1:
            return True
        else:
            return False
    elif string == "Show":
        if a_date.weekday() == 2 or a_date.weekday() == 6:
            return True
        else:
            return False
    elif string == "Movie":
        if a_date.weekday() == 4:
            return True
        else:
            return False
    elif string == "Play":
        if a_date.weekday() == 5:
            return True
        else:
            return False
    else:
        return False


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, False, False, each on their own line.
print(valid_release_date(date(2018, 7, 11), "Show"))
print(valid_release_date(date(2018, 7, 11), "Movie"))
print(valid_release_date(date(2018, 7, 11), "Pancake"))
print()
##############################################################################
the_string = 5.0

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.
#
#Write some code that will capitalize and print the value of
#the_string. For example, for the initial value of the_string
#above, it should print "I'M A RAMBLIN' WRECK".
#
#You can capitalize a string by calling the_string.upper().
#This will return a capitalized version of the string. (Note
#that this will _not_ modified the_string, but rather just
#return the result if it were to be capitalized.)
#
#However, the_string might not actually be a string! It might
#be an integer, a float, or something else. If that happens,
#then calling the_string.upper() will cause an AttributeError
#to occur. Catch this error and print "The variable was not
#a string!"
#
#Note that you may not use any conditionals in your answer.
#Note also that you should not assume that every error that
#occurs is an Attribute Error! Any other errors should
#not be caught.


#Add your code here!
try:
    print(the_string.upper())
except AttributeError:
    print("The variable was not a string!")
print()
##############################################################################
#Imagine you're playing a game in which every action you
#take grants you some number of experience points. There is
#an item called a Lucky Egg that, when used, doubles the
#number of experience points you earn. The company behind
#the game also runs occasional events where they increase
#how many experience points you earn for each action by 50%,
#100%, or even 200%.
#
#Write a function called find_total_exp. find_total_exp
#should have one positional parameter, a base number of
#experience points. It should also have two keyword
#parameters: lucky_egg, whose default value is False, and
#event_mulitplier, whose default value is 1.
#
#The function should return the number of experience
#points earned based on these two variables. The base number
#of experience points should always be multiplied by the
#event multiplier, and then doubled if lucky_egg is True.
#
#You should convert the final result from a float to an
#integer before returning it. This will automatically round
#down.


#Add your code here!
def find_total_exp(base_points, lucky_egg = False, multiplier = 1):
    points = base_points * multiplier
    if lucky_egg:
        points *= 2
        return int(points)
    else:
        points == points
        return int(points)
        
    
    


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#100
#200
#150
#300
print(find_total_exp(100))
print(find_total_exp(100, lucky_egg = True))
print(find_total_exp(100, multiplier = 1.5))
print(find_total_exp(100, lucky_egg = True, multiplier = 1.5))
print()
##############################################################################
#Write a function called num_factors. num_factors should
#have one parameter, an integer. num_factors should count
#how many factors the number has and return that count as
#an integer
#
#A number is a factor of another number if it divides
#evenly into that number. For example, 3 is a factor of 6,
#but 4 is not. As such, all factors will be less than the
#number itself.
#
#Do not count 1 or the number itself in your factor count.
#For example, 6 should have 2 factors: 2 and 3. Do not
#count 1 and 6. You may assume the number will be less than
#1000.


#Add your code here!
#def num_factors(integer):
def num_factors(integer):
    count = 0
    for i in range(2, integer):
        if integer % i == 0:
            count += 1
    return count  
        
    


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 0, 2, 0, 6, 6, each on their own line.
print(num_factors(5))
print(num_factors(6))
print(num_factors(97))
print(num_factors(105))
print(num_factors(999))
print()
##############################################################################
minimum = 5
maximum = 14
even = False

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.
#
#Write a loop (we suggest a for loop) that prints the numbers
#from minimum to maximum, including minimum and maximum
#themselves. If even is True, print only the even numbers.
#If even is False, print only the odd numbers. You may assume
#minimum will always be less than maximum.
#
#With the initial values for minimum, maximum, and even above,
#this should print 6, 8, 10, 12, 14 -- each number would be on
#its own line, no commas.


#Add your code here!
if even:
    for i in range(minimum, maximum + 1):
        if i % 2 == 0:
            print(i)
elif not even:
    for i in range(minimum, maximum + 1):
        if i % 2 == 1:
            print(i)
print()
##############################################################################
days_since_release = 291
original_price = 85
greatest_hits = False

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Write a conditional that determines the price of a
#newly-released game, movie, or album based on the time since
#it was released.
#
#Assume that a new release loses $2 off its price for every
#full week since it was released. So, two full weeks (14 days)
#after a $60 game is released, it will cost $56.
#
#However, if the release is considered a "greatest hit", it
#loses value half as fast: after two weeks, it will be $58
#instead of $56.
#
#No release will ever fall to below $20, however, no matter
#how fast it loses value or whether it's a greatest hit.
#
#Add some code below to print the current price of the release.
#For example, with the values above, it would pring $58.


#Add your code here! Make sure to print the dollar sign, too.
if original_price > 20:
    if greatest_hits:
        if original_price - (days_since_release //7) > 20:
            print("$" + str(original_price - (days_since_release //7)))
        else:
            print("$20")
    
    elif not greatest_hits:
        if original_price - (2 * (days_since_release // 7)) > 20:
            print("$" + str(original_price - (2 * (days_since_release // 7))))
        else:
            print("$20")
else:
    print("$20")            
