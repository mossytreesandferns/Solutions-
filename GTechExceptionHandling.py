#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 11:18:12 2018

@author: meganporter
"""
""" I DON"T KNOW HOW TO HANDLE MULTIPLE SPACES"""
##Now let's make things a little more challenging.
##
##Last exercise, you wrote a function called word_count that
##counted the number of words in a string essentially by
##counting the spaces. However, if there were multiple spaces
##in a row, it would incorrectly add additional words. For
##example, it would have counted the string "Hi   David" as
##4 words instead of 2 because there are two additional
##spaces.
##
##Revise your word_count method so that if it encounters
##multiple consecutive spaces, it does *not* count an
##additional word. For example, these three strings should
##all be counted as having two words:
##
## "Hi David"
## "Hi   David"
## "Hi                 David"
##
##Other than ignoring consecutive spaces, the directions are
##the same: write a function called word_count that returns an
##integer representing the number of words in the string, or
##return "Not a string" if the input isn't a string. You may
##assume that if the input is a string, it starts with a
##letter word instead of a space.
#
##Write your function here!
#def word_count(my_string):
#    num_spaces = 0
#    try:
#        
#        for i in my_string:
#            if i == " ":
#                num_spaces += 1
#        num_words = num_spaces + 1
#        return num_words
#            
#    except:
#        print("Not a string")
#    
#
##Below are some lines of code that will test your function.
##You can change the value of the variable(s) to test your
##function with different inputs.
##
##If your function works correctly, this will originally
##print:
##Word Count: 4
##Word Count: 2
##Word Count: Not a string
##Word Count: Not a string
##Word Count: Not a string
#
#print("Word Count:", word_count("Four words are here!"))
#print("Word Count:", word_count("Hi    David"))
#print("Word Count:", word_count(5))
#print("Word Count:", word_count(5.1))
#print("Word Count:", word_count(True))
############################################################################
a_list = [1, 2, 3, 4, 5]
list_index = 7

#-----------------------------------------------------------
#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#In this problem, we're going to use some unfamiliar syntax.
#You'll learn more about this syntax in Unit 4. For now,
#though, you don't need to understand the syntax. All you
#need to know is that right now, this code will cause an
#error with the values supplied above.
#
#Revise this code so that this error is caught, and the
#message "Invalid index!!" is printed. However, your revision
#must meet these requirements, too:
#
# - If the values of the variables above are changed so
#   that the error doesn't occur, the program should behave
#   the same way that it does now.
# - The two first and last lines, "Accessing index..." and
#   "Done!", should print whether or not an error occurs.
# - If a *different* error occurs from the one that arises
#   initially, your code should instead print "Unknown
#   error!"
#
#HINT: You won't be able to do this without running the code
#first and seeing what the error is. So, try it out first!

#Revise this code:
print("Accessing index...")

try:
    result = a_list[list_index]
    print("Value at index:", result)
except IndexError:
    print("Invalid index!!")
except:
    print("Unknown error!")
print("Done!")

############################################################################

"""Again with the returning Nonetype upon evaluation even though my except
statement is printing okay"""
#Write your function here!
def word_count(my_string):
    num_spaces = 0
    try:
        
        for i in my_string:
            if i == " ":
                num_spaces += 1

        num_words = num_spaces + 1
        return num_words
            
    except:
        print("Not a string")
     
        

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 
#Word Count: 4
#Word Count: 1
#Word Count: 7
#Word Count: Not a string
#Word Count: Not a string
#Word Count: Not a string

print("Word Count:", word_count("Four words are here!"))
print("Word Count:", word_count("One."))
print("Word Count:", word_count("There are seven words in this sentence."))
print("Word Count:", word_count(5))
print("Word Count:", word_count(5.1))
print("Word Count:", word_count(True))

############################################################################
"""I don't know why the Vocareum is returning a nonetype error when it prints as 
instructed for me"""

#In Chapter 3.4, we wrote a function called find_pressure
#that calculated pressure given number of moles,
#temperature, volume, and optionally, a value for R. If no
#value was given for R, we assumed its value should be
#0.082057.
#
#However, as written, that function could crash: what about
#when the user enters a Volume of 0? That would cause a
#ZeroDivisonError! (In addition to breaking the laws of
#physics, but there's no Python error for that.)
#
#Revise that find_pressure function to catch that error. If
#that error occurs, return the string "Volume must be
#greater than 0." Otherwise, the function should work just
#as it did before.
#
#Feel free to copy your answer to that exercise and work
#from there. If you'd prefer to start from scratch, remember:
#you're creating a function called find_pressure that returns
#a value for pressure given variables n, T, V, and optionally
#R, according to this formula:
#
# Pressure = (nRT) / V
#
#You may not use a conditional. R should have a default value
#of 0.082057.


#Write your function here!
def find_pressure(n, T, V, R = 0.82057):
    
    try:
        pressure = (n*R*T)/ V
        return pressure
    except ZeroDivisionError:
        print("Volume must be greater than 0.")
  



#You may use these lines to test your function. With the
#values initially supplied here, your function should return
#"Volume must be greater than 0."
test_n = 10
test_T = 298
test_V = 0
test_R = 62.364 #Torr!
find_pressure(test_n, test_T, test_V, R = test_R)

############################################################################
given_items = ["one", "two", 3, 4, "five", ["six", "seven", "eight"]]

#Write a program that iterates through the items in the
#given list. For each item, you should attempt to iterate
#through the item and print each character seperately. 
#
#If this second part fails, print "Not iterable" -- but
#even if the second part fails, you should still go on
#to the next item in the list.
#
#Hint: Although we'll cover lists more in Unit 4, all
#you need to know right now is that this syntax will run
#a loop over a list, a string, or any other iterable
#type of information:
#
#  for item in given_items:
#
#To iterate over the items in 'item', you can do the
#same thing: for subitem in item:
#
#Start out by building the nested for-each loops that
#you'll need. Then, identify where the error is
#occurring to figure out where to put the try-except
#structure.
#
#This one's tricky, but you can do it!


#Add your code here!
for item in given_items:
    try:
        for char in item:
            print(char)
    except:
        print("Not iterable")
print()        

###########################################################################
mystery_value = 0

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Write a program that divides mystery_value by mystery_value
#and prints the result. If that operation results in an
#error, divide mystery_value by (mystery_value + 5) and then
#print the result. If that still fails, multiply mystery_value
#by 5 and print the result. You may assume one of those three
#things will work.
#
#You may not use any conditionals.
#
#Hint: You're going to want to test one try/except structure
#inside another! Think carefully about whether the second
#one should go inside the try block or the except block.


#Add your code here!


try:
    result = mystery_value / mystery_value
    print(result)
except ZeroDivisionError:
    result =mystery_value / (mystery_value + 5) 
    print(result)
except:
    result = mystery_value * 5
    print(result)
 print()   
#_________________________________________________________
 #This can be kind of a big problem, so let's break it down
#into chunks.
#
#What do we want to try first? Well, our first step is to
#try to divide mystery_value by itself. So, we'll try
#(literally) that:

try:
    print(mystery_value / mystery_value)
    
#We know that might not work, both logically (what if
#mystery_value is 0?) and because the directions told us it
#might not. So, if it doesn't work, we want to catch that
#error. So, we jump straight to having ane except block:
except:
    
    #Now at this point, we can forget how we got here. We
    #don't need to worry about the earlier error. All we
    #need to know is that if we get here, we should try
    #to divide mystery_value by itself plus 5. So, we
    #try that:
    try:
        print(mystery_value / (mystery_value + 5))
        
    #Like before, the directions tipped us off that this
    #might not work, and we know this won't work if
    #mystery_value isn't a number. So, we need to handle
    #another error:
    except:
        print(mystery_value * 5)
    
    #Notice that this except is at the same level of
    #indentation as the second try. It only reacts if the
    #second try hits an error. If we were able to perform
    #our original mystery_value / mystery_value operation,
    #then we never need to even look here!
##############################################################################
words = ["dog", "sparrow", "cat", "frog"]

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#This program is supposed to print the location of the 'o'
#in each word in the list. However, line 18 causes an
#error if 'o' is not in the word. Add try/except blocks
#to print "Not found" when the word does not have an 'o'.
#However, when the current word does not have an 'o', the
#program should continue to behave as it does now.
#
#Hint: don't worry that you don't know how line 18 works.
#All you need to know is that it may cause an error.
#
#You may not use any conditionals.


#Fix this code!

for word in words:
    try: 
        print(word.index("o"))
    except:
        print("Not found")
print()        
##############################################################################
#Write a function called get_integer that takes as input one
#variable, my_var. If my_var can be converted to an integer,
#do so and return that integer. If my_var cannot be converted
#to an integer, return a message that says, "Cannot convert!"
#
#For example, for "5" as the value of my_var, get_integer would
#return the integer 5. If the value of my_var is the string
#"Boggle.", then get_integer would return a string with the
#value "Cannot convert!"
#
#Do not use any conditionals or the type() function.


#Write your function here!
def get_integer(my_var):
    try:
        return int(my_var)
    except:
        return "Cannot convert"
print()    


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 5, Cannot convert!, and 5.

print(get_integer("5"))
print(get_integer("Boggle."))
print(get_integer(5.1))
print()
##############################################################################

#Right now, the code below will encounter an error when num
#is 0, but it will not print anything when it does, and then
#it will keep running for num = 1, num = 2, and num = 3
#afterwards. Modify this code so that once it hits an error,
#the loop stops altogether.
#
#You still should not print anything when the error is
#encountered, and the loop definition on line 10 should not
#be changed.

try:    
    for num in range(-3, 3):
    
	    print(5 / num)
except:
    pass
print()
##############################################################################
def has_a_vowel(a_str):
    for letter in a_str:
        if letter in "aeiou":
            return True
        else:
            return False
print(has_a_vowel("")) 
print()

"""SUGGESTION FOR HOW TO DEBUG THIS CODE"""
def has_a_vowel(a_str):
    print("Starting...")
    for letter in a_str:
        print("Checking", letter)
        if letter in "aeiou":
            print(letter, "is a vowel, returning True")
            return True
        else:
            print(letter, "is not a vowel, returning False")
            return False
    print("Done!")
    

##############################################################################
mystery_value = "9"

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Create a program that divides 10 by mystery_value and 
#prints the result. In the case that mystery_value is 
#equal to 0, print "Can't divide by zero". If for any other
#reason the operation fails, print "Not possible".
#
#You may not use any conditionals or the type() function.


#Add your code here!
try:
    print(10 / mystery_value)
except ZeroDivisionError:
    print("Can't divide by zero")
except:
    print("Not possible")
print()
############################################################################
mystery_value = 0

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Create a program that divides 10 by mystery_value and prints
#the result. In the case that mystery_value is equal to 0,
#print "Not possible". Do not catch any other errors. This
#means there will be an uncaught error in the correct answer!
#
#You may not use any conditionals or the type() function.


#Add your code here!
try:
    print(10 / mystery_value)
    print("No error occurred")
except ZeroDivisionError:
    print("Not possible")

############################################################################
mystery_value = "9"

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Create a program that divides 10 by mystery_value and prints
#the result. In the case that an error occurs, print "Not
#possible".
#
#Use error handling to determine if an error will occur; do
#not use the type() function. You might be surprised how many
#types Python can divide by 10!


#Add your code here!
try: 
    new_var = 10 / mystery_value
    print(new_var)
except:
    print("Not possible")
    
print()
    
    
    #____________________________
    
    
    #With error handling, we always want to "try" what we want
#to accomplish, and then catch an "exception" if it fails.
#So, we try what we want to accomplish:

try:
    print(10 / mystery_value)
    
#And then if it fails, we print that it failed:
except:
    print("Not possible")