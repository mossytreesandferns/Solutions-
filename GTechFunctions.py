#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 23:10:58 2018

@author: meganporter
"""


#In this problem, your goal is to write a function that can
#either count all the vowels in a string or all the consonants
#in a string.
#
#Call this function count_letters. It should have two
#parameters: the string in which to search, and a boolean
#called find_consonants. If find_consonants is True, then the
#function should count consonants. If it's False, then it
#should instead count vowels.
#
#Return the number of vowels or consonants in the string
#depending on the value of find_consonants. Do not count
#any characters that are neither vowels nor consonants (e.g.
#punctuation, spaces, numbers).


#Add your code here!

def count_letters(string, find_consonants):
    consonants = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"  
    vowels = "AEIOUaeiou"
    num_consonants = 0
    num_vowels = 0
    for i in string:
        if i in consonants:
                num_consonants += 1
        if i in vowels:
                num_vowels += 1
                
    if find_consonants == True:
        return num_consonants
    else:
        return num_vowels
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print 14, then 7.

a_string = "Up with the white and gold"

print(count_letters(a_string, True))
print(count_letters(a_string, False))    


print()

#Let's look at three different ways to do this. They'll all
#have the same function signature:
def count_letters(a_string, find_consonants):
    
    #First, we'll start a counter:
    count = 0
    
    #Then, we'll iterate through each character in the
    #string:
    for character in a_string:
        
        #There are two conditions under which we'll add 1 to
        #the counter. Either the character is a vowel and
        #we're not looking for consonants...
        if character in "aeiou" and not find_consonants:
            count += 1
            
        #...or the character is a consonant and we are
        #looking for consonants...
        elif character in "bcdfghjklmnpqrstvwxyz" and find_consonants:
            count += 1
    
    #When we're done going through the string, we return
    #our count.
    return count




a_string = "up with the white and gold"

print(count_letters(a_string, True))
print(count_letters(a_string, False))


prinf()

#It might be confusing, though, to have those conditionals
#inside the loop. So, we could switch that.
#
#We start with the same function definition:
def count_letters(a_string, find_consonants):
    
    #And we still need a counter:
    count = 0
    
    #But this time, we'll check what we're looking for
    #first. If we're looking for consonants...
    if find_consonants:
        
        #...then we loop through looking for consonants:
        for character in a_string:
            if character in "bcdfghjklmnpqrstvwxyz":
                count += 1
        
    #If we weren't looking for consonants:
    else:
        
        #...then we loop through looking for vowels:
        for character in a_string:
            if character in "aeiou":
                count += 1

    #Either way, we return the result when we're done:
    return count

    #This way is less ideal because we define the loop
    #twice, on lines 15 and 23. Only one runs, but we
    #usually try to limit our repeated code. Still, this
    #isn't bad.
    
    
a_string = "up with the white and gold"

print(count_letters(a_string, True))
print(count_letters(a_string, False))

print()

#We could take this yet a step further, though. What if
#we created separate functions for finding vowels and
#consonants?

def count_vowels(a_string):
    count = 0
    for character in a_string:
        if character in "aeiou":
            count += 1
    return count

def count_consonants(a_string):
    count = 0
    for character in a_string:
        if character in "bcdfghjklmnpqrstvwxyz":
            count += 1
    return count

#If we have those, writing count_letters itself becomes
#easy. We just have it look at find_consonants to see
#which of those other two functions it should call:
def count_letters(a_string, find_consonants):
    
    if find_consonants:
        return count_consonants(a_string)
    else:
        return count_vowels(a_string)
    
    
a_string = "up with the white and gold"

print(count_letters(a_string, True))
print(count_letters(a_string, False))

print()


##############################################################################
#In this problem, you should write three functions:
#word_count, letter_count, and average_word_length.
#
#word_count should take as input a string. It should return
#the number of words in the string. You may assume that the
#number of words in the string will be one more than the
#number of spaces in the string.
#
#letter_count should take as input a string. It should return
#the number of letters in the string. You may assume that
#the string is only letters and spaces: no punctuation or
#numbers.
#
#average_word_length should take as input a string. It should
#return the average length of the words in the string. You
#can find the average length by dividing the number of letters
#by the number of words.
#
#Your implementation for average_word_length *must* call
#word_count and letter_count.


#Add your code here!
def word_count(string):
    num_spaces = 0
    word_count = 0
    for i in string:
        if i == " ":
            num_spaces += 1
    word_count = num_spaces + 1
    return word_count
    
def letter_count(string):
    num_chars = 0
    num_spaces = 0
    for i in string:
        num_chars += 1
        if i == " ":
             num_spaces += 1
    num_letters = num_chars - num_spaces
    return num_letters
    
def average_word_length(string):
    average = letter_count(string) / word_count(string)
    return average
    
#Below are some lines of code that will test your function.
#You can change the value of the variable to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 3.5
a_string = "Up with the white and gold"
#print(word_count(a_string))
#print(letter_count(a_string))
print(average_word_length(a_string))

print()

#___________________________________________________________________________
#First, let's start with letter count. There are a few ways
#we could implement letter count, but because we know our
#string is only spaces and letters, we can do this an easy
#way.
#
#First, we create the function:
def letter_count(a_string):
    
    #Then, start the counter:
    letters = 0
    
    #Then, we loop through each letter in the function:
    for character in a_string:
        
        #If it's not a space, then it must be a letter!
        if not character == " ":
            letters += 1
            
    #Finally, we return how many letters we found.
    return letters

#word_count is the exact opposite. Instead of counting the
#characters that are not spaces, we only want to count the
#spaces:
def word_count(a_string):
    
    #Here, we'll initialize our initial count to 1 because
    #each space starts a new word -- that means we have one
    #word to begin with.
    words = 1
    
    #Now, same loop:
    for character in a_string:
        
        #But opposite condition:
        if character == " ":
            words += 1
            
    return words

#With those two functions, our word length function is simple.
#We divide the results of letter_count by the results of
#word_count.
def average_word_length(a_string):
    return letter_count(a_string) / word_count(a_string)



a_string = "Up with the white and gold"

print(average_word_length(a_string))

print()
##############################################################################
#Recall Coding Problem 2.4.4. In that problem, you calculated
#the damage done by an attack based on several parameters.
#
#Convert your code from there into two functions, one called
#calculate_damage and one called calculate_modifier.
#
#Your function for calculate_damage must call calculate_modifier;
#it may not calculate the modifier separately. As such,
#calculate_damage should accept all ten parameters: STAB,
#Type, Critical, Other, Random, Level, Attack, Defense, and
#Base. You'll need to pass STAB, Type, Critical, Other, and
#Random to calculate_modifier.
#
#Make sure the parameters to each function follow the order
#shown above.
#
#As a reminder, damage is calculated using this formula:
#courses.edx.org/asset-v1:GTx+CS1301xII+1T2018+type@asset+block@DamageCalc.png
#
#Modifier is calculated using this formula:
#https://studio.edx.org/asset-v1:GTx+CS1301+1T2017+type@asset+block@ModifierCalc.png

#damage = (((2*Level+10)/250) * (attack/defense) * base + 2 ) * modifier

#modifier = STAB * Type * Critical * other * (random element[0.85, 1])

#Modifier = STAB * Type * Critical * Other * Random
#fraction_1 = (2 * Level + 10)/250
#fraction_2 = (Attack / Defense)
#Damage = (fraction_1 * fraction_2 * Base + 2) * Modifier

#Add your code here!

def calculate_modifier(STAB, Type, Critical, Other, Random):
    modifier = STAB * Type * Critical * Other * Random
    return modifier
    
def calculate_damage(STAB, Type, Critical, Other, Random, Level, Attack, Defense, Base):
    modifier = calculate_modifier(STAB, Type, Critical, Other, Random)
    damage = (((2*Level+10)/250) * (Attack/Defense) * Base + 2 ) * modifier
    return damage

#Below are some lines of code that will test your function.
#You can change the value of the variable to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 16.0
STAB = 1
Type = 0.25
Critical = 2
Other = 1
Random = 1
Level = 50
Attack = 125
Defense = 110
Base = 60

print(calculate_damage(STAB, Type, Critical, Other, Random, Level, Attack, Defense, Base))

print()

def calculate_modifier(STAB, Type, Critical, Other, Random):
    return STAB*Type*Critical*Other*Random

def calculate_damage(STAB, Type, Critical, Other, Random, Level, Attack, Defense, Base):
    
    initial_damage = ((2 * Level + 10) / 250) * (Attack / Defense) * Base + 2
    modifier = calculate_modifier(STAB, Type, Critical, Other, Random)
    return initial_damage * modifier
    
    
    
    
STAB = 1
Type = 0.25
Critical = 2
Other = 1
Random = 1
Level = 50
Attack = 125
Defense = 110
Base = 60

print(calculate_damage(STAB, Type, Critical, Other, Random, Level, Attack, Defense, Base))
print()

##############################################################################
#Consult this blood pressures chart: http://bit.ly/2CloACs
#
#Write a function called check_blood_pressure that takes two
#parameters: a systolic blood pressure and a diastolic blood
#pressure, in that order. Your function should return "Low",
#"Ideal", "Pre-high", or "High" -- whichever corresponds to
#the given systolic and diastolic blood pressure.
#
#You should assume that if a combined blood pressure is on the
#line between two categories (e.g. 80 and 60, or 120 and 70),
#the result should be the higher category (e.g. Ideal and
#Pre-high for those two combinations).
#
#HINT: Don't overcomplicate this! Think carefully about in
#what order you should check the different categories. This
#problem could be easy or extremely hard depending on the
#order you change and whether you use returns or elifs wisely.


#Add your code here!
def check_blood_pressure(systolic, diastolic):
    if systolic < 90 and diastolic < 60:
        return "Low"
    elif systolic < 120 and diastolic < 80:
        return "Ideal"
    elif systolic < 140 and diastolic < 90:
        return "Pre-high"
    else:
        return "High"


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: Ideal
test_systolic = 133
test_diastolic = 80

print(check_blood_pressure(test_systolic, test_diastolic))

print()


##############################################################################
#Basketball coach Phil Jackson says that in order for an NBA
#team to be a contender for a championship, they need to win
#40 games before they lose 20 games.
#
#Write a function called is_a_contender that will take three
#parameters: a team name (a string), a number of wins (an
#integer), and a number of losses (an integer).
#
#Based on these parameters, the function should return one
#of three strings:
#
# - If the team is a contender (at least 40 wins and fewer
#   than 20 losses), return "The [team name] are a contender!"
# - If the team is not a contender (less than 40 wins and at least
#   20 losses), return "The [team name] are not a contender!"
# - If it cannot be determined (both values are higher or both
#   values are lower), return "The [team name] might be a contender!"


#Add your code here!
def is_a_contender(team_name, num_wins, num_losses):
    if num_wins >= 40 and num_losses < 20:
        return "The " + team_name + " are a contender!"
    elif num_wins < 40 and num_losses >= 20:
        return "The " + team_name + " are not a contender!"
    elif (num_wins >= 40 and num_losses > 20) or (num_wins < 40 and num_losses <= 20):
        return "The " + team_name + " might be a contender!"


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: "The Hawks are not a contender!".

test_team_name = "Hawks"
test_wins = 40
test_losses = 26

print(is_a_contender(test_team_name, test_wins, test_losses))

print()


def is_a_contender(team, wins, losses):
    
    
    if wins >= 40 and losses < 20:
        return "The " + team + " are a contender!"
    
    elif wins < 40 and losses >= 20:
        return "The " + team + " are not a contender!"
    #Notice how the third set of relational operators were not necessary
    else:
        return "The " + team + " might be a contender!"

test_team_name = "Hawks"
test_wins = 18
test_losses = 40

print(is_a_contender(test_team_name, test_wins, test_losses))
##############################################################################
#Last problem, we wrote a function that calculated pressure
#given number of moles, temperature, and volume. We told you
#to assume a value of 0.082057 for R. This value means that
#pressure must be given in atm, or atmospheres, one of the
#common units of measurement for pressure.
#
#atm is the most common unit for pressure, but there are
#others: mmHg, Torr, Pa, kPa, bar, and mb, for example. what
#if pressure was sent in using one of these units? Our
#calculation would be wrong!
#
#So, we want to *assume* that pressure is in atm (and thus,
#that R should be 0.082057), but we want to let the person
#calling our function change that if need be. So, revise
#your find_pressure function so that R is a keyword parameter.
#Its default value should be 0.082057, but the person calling
#the function can override that. The name of the parameter for
#the gas constant must be R for this to work.
#
#As a reminder, you're writing a function that calculates:
#
# P = (nRT) / V
#


#Write your function here! You may copy your work from 3.4.5
#if you'd like.

def find_pressure(n, T, V, R = 0.082057):
    
    return (n * R * T) / V



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: "Result: 37168.944".
test_n = 10
test_T = 298
test_V = 5
test_R = 62.364 #Torr!
print("Result:", find_pressure(test_n, test_T, test_V, R = test_R))

print()



##############################################################################
#In chemistry, the ideal gas law states:
#
# pressure * volume = # of moles * gas constant * temperature
#
#This is usually abbreviated to:
#
# PV = nRT
#
#We can solve this for any of these five variables, but let's
#solve it for Pressure. In terms of Pressure, the ideal gas
#law states:
#
# P = (nRT) / V
#
#Write a function called find_pressure that takes as input
#three variables: number of moles, temperature, and volume.
#You can call these variables in the function whatever you
#want, but they must be specified in that order: moles, then
#temperature, then volume. You should assume all three are
#floats. Then, return as output your calculation for
#pressure. For the gas constant, you should use the value 
#0.082057.
#
#Hint: Python's rounding errors can change based on the
#order of the multipliers. If you're having difficulty with
#your answer being off by tiny fractions, change the order
#of the numbers to match the order in the formula above.


#Write your function here!
def find_pressure(n_moles, temperature, volume):
    gas_constant = 0.082057
    pressure = (n_moles * gas_constant * temperature) / volume
    return pressure


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: "Result: 48.905972000000006". The extra zeroes and
#the 6 are rounding errors by Python.
test_n = 10
test_T = 298
test_V = 5
print("Result:", find_pressure(test_n, test_T, test_V))

print()

def find_pressure(n, T, V):
    R = 0.082057
    return (n * R * T) / V
"""I wonder if it's okay python convention to abbreviate variable names to 
single letters if the formula being worked with is well known?"""

test_n = 10
test_T = 298
test_V = 5
print("Result:", find_pressure(test_n, test_T, test_V))

##############################################################################

#Write a function called lucky_sevens that takes in one
#parameter, a string variable named a_string. Your function
#should return True if there are exactly three '7's in
#a_string. If there are less than three or more than three
#'7's, the function should return False.
#
#For example:
#  - lucky_sevens("happy777bday") should return True.
#  - lucky_sevens("h7app7ybd7ay") should also return True.
#  - lucky_sevens("happy77bday") should return False.
#  - lucky_sevens("h777appy777bday") should also return False.
#
#Hint: Remember in Chapter 3.3, we covered how to use a loop
#to look at each character in a string.


#Write your function here!

def lucky_sevens(a_string):    
    i = 0                
    for char in a_string:
        if char == "7":
                i += 1
    if i == 3:
        return True
    else:
        return False    
                              
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, True, False, False, each on their own line
print(lucky_sevens("happy777bday"))
print(lucky_sevens("h7app7ybd7ay"))
print(lucky_sevens("happy77bday"))
print(lucky_sevens("h777appy777bday"))

print()
def lucky_sevens(a_string):
    
    
    count = 0
    for letter in a_string:
        if letter == "7":
            
            count += 1
    #
    #count == 3 will resolve to True if count is 3, False
    #otherwise. So, we can just return it directly:
    
    return count == 3


#There are lots of other ways we could do this. We'll cover
#them more in Chapter 4.2.

print(lucky_sevens("happy777bday"))
print(lucky_sevens("h7app7ybd7ay"))
print(lucky_sevens("happy77bday"))
print(lucky_sevens("h777appy777bday"))

print()
##############################################################################

#A year is considered a leap year if it abides by the
#following rules:
#
#  - Every 4th year IS a leap year, EXCEPT...
#  - Every 100th year is NOT a leap year, EXCEPT...
#  - Every 400th year IS a leap year.
#
#This starts at year 0. For example:
#
#  - 1993 is not a leap year because it is not a multiple of 4.
#  - 1996 is a leap year because it is a multiple of 4.
#  - 1900 is not a leap year because it is a multiple of 100,
#    even though it is a multiple of 4.
#  - 2000 is a leap year because it is a multiple of 400,
#    even though it is a multiple of 100.
#
#Write a function called is_leap_year. is_leap_year should
#take one parameter: year, an integer. It should return the
#boolean True if that year is a leap year, the boolean False
#if it is not.


#Write your function here!
def is_leap_year(year):
    div_not = year % 4 != 0
    div_four = year % 4 == 0
    div_four_hun = year % 400 == 0
    div_one_hun = year % 100 == 0
    if (div_one_hun and not div_four_hun) or div_not:
        return False
    elif div_four or div_four_hun:
        return True


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print False, True, False, and True, each preceded by the
#label "[year] is a leap year:".
print("1993 is a leap year:", is_leap_year(1993))
print("1996 is a leap year:", is_leap_year(1996))
print("1900 is a leap year:", is_leap_year(1900))
print("2000 is a leap year:", is_leap_year(2000))

print()


def is_leap_year(year):
    
    #Now, we want to return true if year is a multiple
    #of 400, or if it's a multiple of 4 but not a
    #multiple of 100. We could do that all on one line:
    
    return year % 400 == 0 or (year % 4 == 0 and not year % 100 == 0)
    
    #Or, we might flesh that out a little more. To see
    #that the method below works, comment out line 10.
    
    #First, return True if it's a multiple of 400.
    if year % 400 == 0:
        return True
    
    #Then, return True if it's a multiple of 4...
    elif year % 4 == 0:
        
        #...and not a multiple of 100. Remember, if it's
        #a multiple of 400, it would have returned True
        #up on line 17, so we don't need to recheck that
        #here:
        if not year % 100 ==0:
            return True
    
    #The only way this line is reachable is if we haven't
    #previously returned True. So, the answer must be
    #False.
    return False

print("1993 is a leap year:", is_leap_year(1993))
print("1996 is a leap year:", is_leap_year(1996))
print("1900 is a leap year:", is_leap_year(1900))
print("2000 is a leap year:", is_leap_year(2000))
##############################################################################
#In the previous coding problem, you created a function
#called hide_and_seek that printed the numbers from 1 to 10.
#Now, however, we want to extend that. What if we want to
#count to 20? 30?
#
#Modify your previous function so that it takes as input one
#parameter: count. Then, instead of printing the numbers from
#1 to 10, it should print the numbers from 1 to the value of
#count. Then, end with "Ready or not, here I come!"


#Write your function here!
def hide_and_seek(count):
    for i in range(1, count + 1):
        print(i)
    print("Ready or not, here I come!")    


#The function call below will test your function. We'll delete
#and overwrite this with other calls to hide_and_seek with
#different numbers during grading:
hide_and_seek(36)
print()

##############################################################################
#Write a function called hide_and_seek. The function should
#have no parameters and return no value; instead, when
#called, it should just print the numbers from 1 through 10,
#follow by the text "Ready or not, here I come!". Each
#number and the message at the end should be on its own
#line.
#
#Then, call the function.
#
#There should be no print statements outside the function.


#Write your function here!
def hide_and_seek():
    for i in range(1, 11):
        print(i)
    print("Ready or not, here I come!")


#Call your function here!
hide_and_seek()
print()

##############################################################################


#Write a function called snowed_in that will determine
#whether school is closed based on the weather and
#temperature. We'll pretend the school is in Georgia, where
#a little snow or sub-freezing temperatures are enough to
#close down schools!
#
#The function should take three parameters:
#
# - temperature, a float
# - weather, a string
# - is_celsius, a boolean
#
#The function should return True if temperature is below
#freezing (32 if is_celsius is False, 0 if is_celsius is
#True) or if weather is "snowy". Otherwise, it should
#return False.
#
#Note, however, that is_celsius should be an optional
#argument. If the function call does not supply a value for
#is_celsius, assume it is True.
#
#For example:
#
# snowed_in(15, "sunny") -> False
# is_celsius is assumed to be True, so 15 is not below
# freezing.
#
# snowed_in(15, "sunny", is_celsius = False) -> True
# is_celsius is False, so 15 is below freezing.
#
# snowed_in(15, "snowy", is_celsius = True) -> True
# The weather is "snowy", so the temperature doesn't matter.


#Write your function here!
def snowed_in(temperature, weather, is_celsius = True):
    if weather == "snowy":
        return True
    if temperature < 32 and is_celsius == False:
        return True
    elif temperature < 0 and is_celsius == True:
        return True
    else:
        return False
    


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print False, True, and True, each on their own line.

print(snowed_in(15, "sunny")) #Should print False
print(snowed_in(15, "sunny", is_celsius = False)) #Should print True
print(snowed_in(15, "snowy", is_celsius = True)) #Should print True
print(snowed_in(15, "snowy", is_celsius = False))
print(snowed_in(15, "snowy"))

print()

def snowed_in(temperature, weather, is_celsius = True):
    
    #Inside the function, we don't have to worry about
    #where is_celsius's value came from. So, we can start
    #with our reasoning.
    #
    #As soon as we find one reason that school would be
    #closed, we can go ahead and return True. For
    #example, if the weather is snowy, then the
    #temperature doesn't matter. So, let's go ahead and
    #return True if the weather is snowy:
    
    if weather == "snowy":
        return True
    elif temperature < 0 and is_celsius:
        return True
    elif temperature < 32 and not is_celsius:
        return True
    
    
    return False

snowed_in(15, "sunny") #Should print False
snowed_in(15, "sunny", is_celsius = False) #Should print True
snowed_in(15, "snowy", is_celsius = True) #Should print True

print()

"""This code is so perfect!"""
def snowed_in(temperature, weather, is_celsius = True):
    
    return weather == "snowy" or temperature < 0 or (temperature < 32 and not is_celsius)

snowed_in(15, "sunny") #Should print False
snowed_in(15, "sunny", is_celsius = False) #Should print True
snowed_in(15, "snowy", is_celsius = True) #Should print True
print()
##############################################################################
#We've written the function, reverse, below. This function
#takes a string and returns the reverse of it. There are two
#scope errors somewhere in the code. Read through all the
#code below to find and fix the errors, so that the function
#produces the correct output and the result of the function
#is correctly printed. Note that you should not change the
#three lines that are already present in the function, but
#you may add lines before them, or you may change or add to
#the lines outside the function.
#
#Note that your goal here is to fix both the function itself
#and the program as a whole. So, your function should be
#able to be called on a new string, and the program when
#run should print the reverse of the string originally on
#line 29.


def reverse(a_string):
    #You may add code before the following three lines.
    rev = ""
    
    #Don't change these three lines.
    for i in range(len(a_string)-1, -1, -1):
        rev = rev + a_string[i]
    return rev


#You may change or add to the following lines.
backwards = reverse("This string should be reversed!")
print(backwards)
print()

#If you run the original code, the first error you encounter
#is inside the function, on the line rev = rev + a_string[i].
#The error is that the variable rev is being used on the
#right side of the expression before it's actually given
#a value. The first time that line is called, it adds
#a_string[i] to the current value of rev, but rev has no
#current value.
#
#So, we first need to create rev with an empty string so that
#it exists when we need it. So, we add that before the
#current code inside the function:

def reverse(a_string):
    #You may add code before the following three lines.
    
    rev = "" #THIS LINE IS NEW!
    
    #Don't change these three lines.
    for i in range(len(a_string)-1, -1, -1):
        rev = rev + a_string[i]
    return rev

#After making that change, though, there is still a problem
#on the lines below. The error is the same. The last line
#tries to print rev when rev does not have a value. But
#wait: didn't we give rev a value inside the function
#reverse()? And aren't we calling reverse() before trying
#to print rev?
#
#Remember, the variable rev is created inside the function
#reverse(). That means it only exists inside that function.
#When the function is over, it ceases to exist, unless it's
#returned: and if it's returned, we need to capture the
#result. So, that's what we need to do: modify the first
#line below to capture the result.

rev = reverse("This string should be reversed!")
print(rev)

#Now when rev is returned on line 21, the right side of
#line 37 is replaced by that value. So, the variable rev
#created on line 37 (a different variable with the same
#name as the one inside the function) receives that value,
#and we can print it on line 38.
print()
##############################################################################

#Below we've written a function that is supposed to take in
#four parameters and produce a string representing the cost
#of a person's weekly soda consumption. Below the function
#definition, we're calling the function.
#
#However, right now, the code is erroring out. Fix this code
#without changing the code inside the function. You may
#change either the function declaration (on line 11) or the
#function call on line 27.

def soda_habit(preferred_soda, sodas_per_week, calories_per_soda, price_per_soda):
    
    #Above, we've moved preferred_soda to the beginning and
    #sodas_per_week to the end, so our original function
    #call will work.
     #calories_per_soda, preferred_soda
    #Don't change the body of this function!
    
    money_spent = price_per_soda * sodas_per_week
    calories_consumed = calories_per_soda * sodas_per_week
    
    summary_string = "You're spending $" + str(money_spent) + " on " + preferred_soda + " per week! "
    summary_string += " That's " + str(calories_consumed) + " calories!"
    
    return summary_string


print(soda_habit("Coca-Cola", 9, 140, 1.75)
print()



#The issue here is that the order in which arguments are
#passed into the function doesn't match the order of the
#parameters of the function.
#
#In the function call, we're passing in the name of the
#soda, then the price, then the number of calories, then
#the number of cans. However, the function declaration
#expects to get the number of cans first and the name of the
#soda last.
#
#Generally, functions are more permanent, so we usually
#want to modify our function call. So, let's leave the
#function alone...

def soda_habit(sodas_per_week, price_per_soda, calories_per_soda, preferred_soda):
    
    #Don't change the body of this function!
    
    money_spent = price_per_soda * sodas_per_week
    calories_consumed = calories_per_soda * sodas_per_week
    
    summary_string = "You're spending $" + str(money_spent) + " on " + preferred_soda + " per week! "
    summary_string += " That's " + str(calories_consumed) + " calories!"
    
    return summary_string


#And instead fix the order of arguments in the function call.
#It expects the number first and the name last, so let's make
#that change:
result = soda_habit(9, 1.75, 140, "Coca-Cola")
print(result)

#However, if we're the ones writing the function and no one has
#used it yet, then changing the order in the function declaration
#might be ok. Check out sample_answer_2.py to see.
print()
#If there's the chance that someone else has already used
#the function, then we don't want to mess with the function
#declaration: that could mess up their code without them
#doing anything! However, if we're writing the function for
#the first time, we could modify its declaration instead:

def soda_habit(preferred_soda, price_per_soda, calories_per_soda, sodas_per_week):
    
    #Above, we've moved preferred_soda to the beginning and
    #sodas_per_week to the end, so our original function
    #call will work.
    
    #Don't change the body of this function!
    
    money_spent = price_per_soda * sodas_per_week
    calories_consumed = calories_per_soda * sodas_per_week
    
    summary_string = "You're spending $" + str(money_spent) + " on " + preferred_soda + " per week! "
    summary_string += " That's " + str(calories_consumed) + " calories!"
    
    return summary_string



result = soda_habit("Coca-Cola", 1.75, 140, 9)
print(result)
##############################################################################

#Write a function called total_volume. total_volume should
#have four parameters, all integers. The first three
#parameters should represent the length, width, and height
#of a box respectively. The fourth should represent the
#number of boxes.
#
#The function should return an integer representing the
#total volume represented by the given boxes. For example,
#if the length is 10, the width is 2, the height is 2, and
#there are 4 boxes, then the total volume would be 160:
#((10 * 2 * 2) * 4) = 160.



def total_volume(a_length, a_width, a_height, box_count):
    return a_length * a_width * a_height * box_count

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: "A square with side length 4 has an area of 16".

print(total_volume(5, 4, 6, 8))

##############################################################################
#Write a function called greeting. greeting should have one
#parameter, a string representing a name. It should return
#a string with the message "Hi [name]!", where the value of
#the parameter is used in place of [name].
#
#For example:
#
# greeting("David") -> "Hi David!"


def greeting(input_name):
    return "Hi " + input_name + "!"


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: "Hi David!"

print(greeting("David"))
print()


##############################################################################
#Helping us develop this class are a team of teaching
#assistants, often called TAs for short.
#
#Write a function called my_TAs. The function should take as
#input three strings: first_TA, second_TA, and third_TA. It
#should return as output the string, "[first_TA], [second_TA],
#and [third_TA] are awesome!", with the values replacing the
#variable names.
#
#For example, my_TAs("Sridevi", "Lucy", "Xu") would return
#the string "Sridevi, Lucy, and Xu are awesome!"
#
#Hint: Notice that because you're returning a string instead
#of printing a string, you can't use the print() statement
# -- you'll have to create the string yourself, then return
#it!


#Write your function here!
def my_TAs(first_TA, second_TA, third_TA):
    string = str(first_TA) + ", " + str(second_TA) + ", and " + str(third_TA) + " are awesome!"
    return string    


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: "Joshua, Jackie, and Marguerite are awesome!".
test_first_TA = "Joshua"
test_second_TA = "Jackie"
test_third_TA = "Marguerite"
print(my_TAs(test_first_TA, test_second_TA, test_third_TA))
print()


def my_TAs(first_TA, second_TA, third_TA):
    
    #Now that we're in the function, we want to create the
    #string. Because we're creating and returning the string
    #instead of printing it directly, we have to use addition
    #operators to add together the individual parts
    #
    #We could do this piece-by-piece:
    
    result_string = ""
    result_string += first_TA
    result_string += ", "
    result_string += second_TA
    result_string += ", and "
    result_string += third_TA
    result_string += " are awesome!"
    
    #And then return it:
    return result_string

#Now that the function is created, we can run this file and
#see the correct output.
#
#There are other ways we could do this, though. Check out
#sample_answer_2.py and sample_answer_3.py for more advanced
#answers.


test_first_TA = "Joshua"
test_second_TA = "Jackie"
test_third_TA = "Marguerite"
print(my_TAs(test_first_TA, test_second_TA, test_third_TA))

def my_TAs(first_TA, second_TA, third_TA):
    
    #Python's string data type has a method called .format.
    #We'll talk about classes and methods more in Unit 5. For
    #now, though, it's not terribly hard to read:
    
    result_string = "{0}, {1}, and {2} are awesome!".format(first_TA, second_TA, third_TA)
    
    #{0}, {1}, and {2} are placeholders inside the string for
    #where the values of certain variables will go. Then, after
    #the string, we put .format(, and then list the variables
    #in order. The first one will replace {0}, the second will
    #replace {1}, and the third will replace {2}.
    #
    #The result is a shorter line of code that can be a little
    #easier to organize since you don't have to deal with all
    #the addition operators and substrings.
    
    return result_string


test_first_TA = "Joshua"
test_second_TA = "Jackie"
test_third_TA = "Marguerite"
print(my_TAs(test_first_TA, test_second_TA, test_third_TA))
##############################################################################

#Write a function that takes in one integer parameter, the
#side length of a square, and returns the area. The function
#should be named find_area, and have one parameter:
#side_length.


#Write your function here!
def find_area(side_length): 
    result = side_length **2
    return result


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: "A square with side length 4 has an area of 16".

test_side_length = 4
print("A square with side length", test_side_length, "has an area of", find_area(test_side_length))

print()
def find_area(side_length):
    
    #Now, we want to return the area of a square whose sides
    #are length side_length. This is just side_length
    #squared, so we could either do side_length ** 2 or
    #side_length * side_length. Let's do the first one.
    
    return side_length ** 2

#Now that we have that, we can test our code. When we run
#this file, it will print, "A square with side length 4
#has an area of 16".

test_side_length = 4
print("A square with side length", test_side_length, "has an area of", find_area(test_side_length))

##############################################################################
#Write a function called get_todays_date that returns
#today's date as a string, in the form year/month/day.
#For example, if today is January 15th, 2017, then it
#would return 2017/1/15.
#
#Remember, you took care of the string formatting part of
#this exercise in 2.2.9 Coding Exercise 1! Now, you're
#converting it to a function that returns the string.
#
#Note that the line below will let you access today's date
#using date.today() anywhere in your code.
from datetime import date
my_date = date.today()
year = my_date.year
month = my_date.month
day = my_date.day
 

#Write your function here!
def get_todays_date():
    sum_date = str(year) + "/" + str(month) + "/" + str(day)
    return sum_date

#If you want to test your code, you can do so by calling
#your function below. However, this is no longer required
#for grading.
print(get_todays_date())

print()

from datetime import date

#First, we know we want a function called get_todays_date.
#So, let's create it:

def get_todays_date():
    #Next, we know we need to actually access today's date
    #to be able to print it. The comments in the directions
    #tell us how: date.today()
    
    todays_date = date.today()
    
    #By default, str(todays_date) doesn't give us the format
    #we want. So, we need to create our result manually.
    #
    #We could do this in one long line, but let's break it
    #up. First, let's just create the empty string that we
    #will eventually return:
    
    date_string = ""
    
    #Now, let's add each piece that we need to it one by one.
    #Remember, to add an integer to a string, we first need
    #to convert it to a string using str(). It might have
    #been a while since you've done that since until now,
    #you've been mostly printing integers directly.
    
    date_string += str(todays_date.year)
    date_string += "/"
    date_string += str(todays_date.month)
    date_string += "/"
    date_string += str(todays_date.day)
    
    #Now, date_string has the value we wanted to return. So,
    #we return it:
    
    return date_string

#Now, outside the function, we'll find that if we call the
#function, it will print the right output:
print(get_todays_date())
##############################################################################
#Take a look at the three functions completely written
#below. It's your job to correctly call each function with
#the following parameters:
#
#  Function 1: the string "Black Horse and a Cherry Tree" 
#  Function 2: no parameters
#  Function 3: these five numbers: 80, 80, 95, 86, 79

#Function 1
def cherry_pie(song):
    if ("Cherry" in song):
        print("Sheee's my cherry pie")
    else:
        print("Huh... must be an American Pie.")

#Function 2
def should_I_go_to_Waffle_House():
    print(True)

#Function 3
def average_grades(num1, num2, num3, num4, num5):
    sum = num1 + num2 + num3 + num4 + num5
    average = sum / 5
    print(average)


#Add your function calls here! Don't change any of the
#code above.
cherry_pie("Black Horse and a Cherry Tree")
should_I_go_to_Waffle_House()
average_grades(80,80,95,86,79)
print()
##############################################################################
#When writing out mathematical equations for younger
#audiences, we usually want to use the traditional division
#and multiplication symbols, ÷ and ×, instead of slashes and
#asterisks. These keys aren't on the keyboard, though. So,
#let's write functions that will print them.
#
#First, write two functions: one called print_division_symbol
#and one called print_multiplication_symbol. The functions
#should do what their names suggest: print_division_symbol
#should print a division symbol, print_multiplication_symbol
#should print a multiplication symbol. You can copy the
#characters for those symbols from these directions.
#
#Then, after writing those two functions, call them in the
#same order: print_division_symbol, then
#print_multiplication_symbol. The output of your code should
#thus be ÷, then ×, each on their own line.
#
#Note that you don't need to worry about the end="" thing
#you saw in the video: just print the symbols on their own
#lines. Note also that if you receive a UnicodeEncodeError,
#try submitting your code instead of running it: that error
#happens sometimes, but only affects Run, not Submit.
#
#HINT: you're writing two functions. You don't want one to
#be inside the other.


#Write your two functions here!
def print_division_symbol():
    print('÷')    

def print_multiplication_symbol():
    print('×')

#Call your two functions here!
print_division_symbol()
print_multiplication_symbol()
