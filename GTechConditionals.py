#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 16:23:57 2018

@author: meganporter
"""

"""Georgia Tech Coding Problems"""



#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Ever been at a loss for what to do for your significant
#other for Valentine's Day? Let's right some code to generate
#a gift recommendation!
#
#The variables above give the length of the relationship in
#number of years, months, and days. Add some code below to
#print a gift recommendation based on these values:
#
# - If you've been dating for at least 4 years, give them a
#   dog ("dog").
# - If you've been dating for at least 1 year but less than
#   4 years, give them a watch ("watch").
# - If you've been dating for at least 6 months but less than
#   1 year, give them concert tickets ("concert tickets").
# - If you've been dating for at least a day but less than 6
#   months, give them candy ("candy").
# - If aren't actually dating, go big or go home: give them
#   a yacht to sail away together ("yacht").
#
#Note that no matter what, you should only print one gift.


#Add your code here!

years = 2
months = 9
days = 4

if days == 0 and months == 0 and years == 0:
    print("yacht")
elif days >= 1 and months < 6 and years == 0:
    print("candy")
elif months >= 6 and years == 0:
    print("concert tickets")
elif years >= 1 and years < 4:
    print("watch")
elif years >= 4 :
    print("dog")
    
print() 
print()

if years >= 4:
    print("dog")
elif years >= 1:
    print("watch")
elif months >= 6 and years < 1:
    print("concert tickets")
elif months < 6 and days >= 1:
    print("candy")
elif days == 0 and months == 0 and years == 0:
    print("yacht")

print()   

if years >= 4:
    print("dog")
elif years >= 1:
    print("watch")
elif months >= 6:
    print("concert tickets")
elif months >= 1 or days >= 1:
    print("candy")
else:
    print("yacht")

##############################################################################

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Around Georgia Tech, there are plenty of places to get a
#late night bite to eat. However, they have different hours,
#so when choosing where to go, you have to think about who's
#still open!
#
#Imagine you're choosing between the following restaurants:
#
# - Barrelhouse: Closes at 11:00PM
# - Taco Bell: Closes at 2:00AM
# - Cookout: Closes at 3:00AM
# - Waffle House: Never closes. Ever.
#
#Assume that this list is also a priority list: if Barrelhouse
#is open, you choose Barrelhouse. If not, you choose Taco Bell
#if it's open. If not, you choose Cookout if it's open. If
#not, you choose Waffle House.
#
#However, there are two wrinkles:
#
# - We're using 12-hour time.
# - hour will always represent a time from 10PM to 5AM.
#
#That means that if hour is 10 or 11, it's PM; if hour is
#12, 1, 2, 3, 4, or 5, it's AM. This will make your reasoning
#a little more complex. You may assume that all four
#restaurants open later than 6AM, though, so you don't have
#to worry about opening time, just closing time.
#
#Add some code below that will print what restaurant you'll
#go to based on the current values of hour and minute.


#Add your code here!

hour = 4
minute = 45

if hour == 10:
    print("Barrelhouse")
elif hour == 11 or hour == 12 or hour == 1:
    print("Taco Bell")
elif hour == 2:
    print("Cookout")
else:
    print("Waffle House")
    
    
hour += 3
if hour > 12:
    hour -= 12

if hour < 2:
    print("Barrelhouse")
elif hour < 5:
    print("Taco Bell")
elif hour < 6:
    print("Cookout")
else:
    print("Waffle House")    


##############################################################################

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#The United States has a movie rating system that rates
#movies with one of five ratings: G, PG, PG-13, R, and NC-17.
#Although some of the ratings are not binding, imagine that
#you are a parent who decides on the following rules:
#
# - Any child can see a G-rated movie.
# - To see a PG-rated movie, your child must be 8 or older.
# - To see a PG-13-rated movie, your child must be 13 or older.
# - To see an R-rated movie, your child must be 17 or older.
# - Your child may never see an NC-17 movie.
#
#The variables above give a rating and a child's age. Use
#these variables to select and print one of these two
#messages based on the criteria above:
#
# - "You may see that movie!"
# - "You may not see that movie!"
#
#However, there's one trick: you may not use the 'and' operator
#anywhere in this code!


#Add your code here!

rating = "NC-17"
age = 21

if rating == "NC-17":
    print("You may not see that movie!")
elif rating == "R":
    if age >= 17:
        print("You may see that movie!")
    else:
        print("You may not see that movie!")
elif rating == "PG-13":
    if age >= 13:
        print("You may see that movie!")
    else:
        print("You may not see that movie!")
elif rating == "PG":
    if age >= 8:
        print("You may see that movie!")
    else:
        print("You may not see that movie!")
elif rating == "G":
    print("You may see that movie!")
    
    
    
permission = True

if rating == "NC-17":
    permission = False
elif rating == "R":
    if age < 17:
        permission = False
elif rating == "PG-13":
    if age < 13:
        permission = False
elif rating == "PG":
    if age < 8:
        permission = False

if permission:
    print("You may see that movie!")
else:
    print("You may not see that movie!")    



##############################################################################

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Atlanta is full of great coffee places. Unfortunately, great
#coffee is usually expensive. The variables above will
#contain a balance and a cafe name. Below are the prices of
#a cup of coffee at each of three locations:
#
# - Octane: $6
# - Galloway: $5
# - Starbucks: $4
# - Revelator: $3
# - Dunkin: $2
#
#Add some code above that will print one of the following
#two messages depending on whether the value of balance is
#high enough to buy a cup of coffee at the given cafe.
#
# - If it is sufficient, print "With [balance] dollars, I
#   can buy coffee at [cafe]"
# - If it is not sufficient, print "With [balance] dollars,
#   I cannot buy coffee at [cafe]"

cafe = "Galloway"
balance = 1

affirmative = "With {} dollars, I can buy coffee at {}".format(balance,cafe)
negative = "With {} dollars, I cannot buy coffee at {}".format(balance, cafe)

if cafe == "Octane":
    if balance >= 6:
        print(affirmative)
    else:
        print(negative)
elif cafe == "Galloway":
    if balance >= 5:
        print(affirmative)
    else:
        print(negative)
elif cafe == "Starbucks":
    if balance >= 4:
        print(affirmative)
    else:
        print(negative)
elif cafe == "Revelator":
    if balance >= 3:
        print(affirmative)
    else:
        print(negative)
elif cafe == "Dunkin":
    if balance >= 2:
        print(affirmative)
    else:
        print(negative)
        
        
can_afford = True

if cafe == "Octane" and balance < 6:
    can_afford = False
if cafe == "Galloway" and balance < 5:
    can_afford = False
if cafe == "Starbucks" and balance < 4:
    can_afford = False
if cafe == "Revelator" and balance < 3:
    can_afford = False
if cafe == "Dunkin" and balance < 2:
    can_afford = False
if can_afford:
    print("With", balance, "dollars, I can buy coffee at", cafe)
else:
    print("With", balance, "dollars, I cannot buy coffee at", cafe)        


can_afford = "can"

if cafe == "Octane" and balance < 6:
    can_afford = "cannot"
if cafe == "Galloway" and balance < 5:
    can_afford = "cannot"
if cafe == "Starbucks" and balance < 4:
    can_afford = "cannot"
if cafe == "Revelator" and balance < 3:
    can_afford = "cannot"
if cafe == "Dunkin" and balance < 2:
    can_afford = "cannot"

print("With", balance, "dollars, I", can_afford, "buy coffee at", cafe)

#################################################################################

principal = 5000
rate = 0.05
time = 10
goal = 7000


import math

#Remember, you can access e with math.e.

amount = principal * math.e ** (rate * time)
extra_money = amount - goal
needed_money = goal - amount


#Add your code here! Feel free to copy your code from 
#problem 2.4.5.
if amount > goal:
    print("You'll exceed your goal by", round(extra_money,2))
else:
    print("You'll fall short of your goal by", round(needed_money,2))

print()

amount = amount = principal * math.e ** (rate * time)
difference = amount - goal

if difference > 0:
    print("You'll exceed your goal by " + str(round(difference, 2)))
else:
    print("You'll fall short of your goal by " + str(round(-difference, 2)))

print()

amount = amount = principal * math.e ** (rate * time)
difference = amount - goal

if difference > 0:
    print("You'll exceed your goal by", (round(difference, 2)))
else:
    print("You'll fall short of your goal by", (round(-difference, 2)))
    
##############################################################################    
    

#Imagine you're deciding what you want to cook. The boolean
#variables above state whether or not you have each of those
#four ingredients.
#
#Here are the dishes you know how to cook and their
#ingredients:
#
# 1. pancakes: egg, milk, butter, flour
# 2. omelette: egg, milk, butter
# 3. custard: egg, milk
# 4. poached eggs: egg
#
#The list above is also a priority list. If you have the
#ingredients for pancakes, you'll make pancakes instead of
#any of the other dishes. If you're missing flour but have
#the other ingredients, you'll make an omlette. You'll only
#make poached eggs if the only ingredient you have is eggs.
#
#Complete the program below such that it prints which dish
#you'll make based on the ingredients you have handy. All
#the dishes should appear exactly as shown above: all lower
#case, spelled the same way. If you do not have the
#ingredients to make any of these dishes, then print the
#text "Go to the store!"


#Add your code here!
    
egg = True
milk = True
butter = True
flour = True    

if egg and milk and butter and flour:
    print("pancakes")
elif egg and milk and butter:
    print("omelette")
elif egg and milk:
    print("custard")
elif egg:
    print("poached eggs")
else:
    print("Go to the store!")

if egg:
    if milk:
        if butter:
            if flour:
                print("pancakes")
            else:
                print("omelette")
        else:
            print("custard")
    else:
        print("poached eggs")
else:
    print("Go to the store!")
    
  #############################################################################  
    


#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.
#
#In Bryan Cranston's autobiography, he describes how after
#his success on Breaking Bad, he developed a scoring system
#for evaluating new scripts that he received.
#
#First, he would assign the script a grade -- A, B, C, D, or
#F -- in each of five categories: Story, Text, Role, Director,
#and Cast.
#
#Then, he would tally those grades into a total score for the
#script, according to the following chart:
#
#            A   B   C   D   F
# Story     +6  +5  +4  +2  +0
# Text      +5  +4  +3  +1  +0
# Role      +4  +3  +2  +1  +0
# Director  +3  +2  +1  +0  +0
# Cast/Misc +2  +1  +0  +0  +0
#
#For example: an A story, B text, C role, D directory, and
#F cast would get a score of 12: +6 for the story, +4 for the
#text, +2 for the role, +0 for the director, and +0 for the
#cast.
#
#Then, based on that score, the script would be assigned a
#category (note these are slightly different from the image
#because we've excluded the time variable):
#
# 20: Perfect score
# 17 to 19: Must do
# 14 to 16: Seriously consider
# 12 to 13: On the bubble
# 11 or below: Pass
#
#The variables above give the letter grades assigned to each
#of the five components. Write a program that calculates the
#total score he would assign to the script represented by
#these variables. Then on the next line, print the category
#he would assign to that script. For example, for the values
#above, this program would print:
#
#12
#Pass
#
#HINT: This is a *long* program. It's not particularly
#complex -- you're doing the same thing over and over, However,
#that 'same thing' required 4-8 lines each time you do it. Our
#answer is 46 lines long! So, don't think you're off-track just
#because you're writing a lot of lines.
  
story = "F"
text = "F"
role = "F"
director = "F"
cast = "F" 

story_score = 0
text_score = 0
role_score = 0
director_score = 0
cast_score = 0

#Add your code here!
if story == "A":
    story_score += 6
elif story == "B":
    story_score += 5
elif story == "C":
    story_score += 4
elif story == "D":
    story_score += 2
elif story == "F":
    story_score == story_score

if text == "A":
    text_score += 5
elif text == "B":
    text_score += 4
elif text == "C": 
    text_score += 3
elif text == "D":
    text_score += 1


if role == "A":
    role_score += 4
elif role == "B":
    role_score += 3
elif role == "C": 
    role_score += 2
elif role == "D":
    role_score += 1


if director == "A":
    director_score += 3
elif director == "B":
    director_score += 2
elif director == "C": 
    director_score += 1

if cast == "A":
    cast_score += 2
elif cast == "B":
    cast_score += 1

total_score = story_score + text_score + role_score + director_score + cast_score
print(total_score)

if total_score == 20: 
    print("Perfect score")
elif 17 <= total_score <= 19:
    print("Must do")
elif 14 <= total_score <= 16:
    print("Seriously consider")
elif total_score == 12 or total_score == 13:
    print("On the bubble")
elif total_score <= 11:
    print("Pass")
    
#--------------------------------------------    
    
story_dict = {"A": 6, "B": 5, "C": 4, "D": 2, "F": 0}
text_dict = {"A": 5, "B": 4, "C": 3, "D": 1, "F": 0}
role_dict = {"A": 4, "B": 3, "C": 2, "D": 1, "F": 0}
director_dict = {"A": 3, "B": 2, "C": 1, "D": 0, "F": 0}
cast_dict = {"A": 2, "B": 1, "C": 0, "D": 0, "F": 0}


total_score = 0
total_score += story_dict[story]
total_score += text_dict[text]
total_score += role_dict[role]
total_score += director_dict[director]
total_score += cast_dict[cast]
print(total_score)

if total_score >= 20:
    print("Perfect score")
elif total_score >=17:
    print("Must do")
elif total_score >= 14:
    print("Seriously consider")
elif total_score >= 12:
    print("On the bubble")
else:
    print("Pass")    
  
    
#############################################################################    
    

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Diamonds are typically evaluated according to four aspects:
# - Cut: The way the diamond is cut
# - Clarity: How clear or flawless the diamond is, rated
#   as F (the best), IF, VVS, VS, SI, or I (the worst)
# - Color: How colorless the diamond is, rated from "D" (the
#   best) to "Z" (the worst)
# - Carat: How large the diamond is, weighed in carats
#
#Cut is usually a matter of personal preference. Clarity,
#color, and carat are matters of value: the clearer, more
#colorless, and larger a diamond is, the greater its value.
#
#Imagine you're shopping for a diamond. You have your
#preferred cuts, and you have a budget in mind. You're shown
#a diamond whose characteristics are represented by the cut,
#color, clarity, and carat variables above. You'll buy the
#diamond if its cost is less than your budget, and if its
#cut is one of your preferred cuts.
#
#At this store, every diamond has a base cost of 100.
#
#For every color rating worse than "D", the cost decreases by
#2%. An "F" color diamond would be worth 0.96 * the diamond
#cost otherwise because "F" is two colors worse than "D".
#
#A diamond's value is doubled for every level of clarity above
#I. A "VVS"-clarity diamond is worth 8 * the diamond cost
#otherwise because "VVS" is three levels higher than I, and
#doubling its value three times raises its value by 8x total.
#
#After finding its price based on color and clarity, its price
#is multiplied by its weight in carats.
#
#Your program should print "I'll take it!" if you will buy the
#diamond, "No thanks" if you will not. To purchase it, its price
#must be less than your budget and its cut must be one of your
#preferred cuts.
#
#HINT: You can find the number of characters between two
#characters by using the ord() function. ord("E") - ord("D")
#is 1; ord("Z") - ord("D") is 22.
#
#HINT 2: We haven't covered lists, but we did cover how to
#see if an item is present in a list using the 'in' operator
#in chapter 2.3.


#Add your code here!

cut = "Emerald"
clarity = "F"
color = "E"
carat = 1.1
budget = 3600
preferred_cuts = ["Emerald", "Cushion", "Princess", "Oval"]

cost = 100

if clarity == "I":
    cost *= 1
elif clarity == "SI":
    cost *= 2
elif clarity == "VS":
    cost *= 4
elif clarity == "VVS":
    cost *= 8
elif clarity == "IF":
    cost *= 16
elif clarity == "F":
    cost *= 32
    

color_deduction = (ord(color) - ord("D")) * .02 * cost
total_cost = carat * (cost - color_deduction)

if cut in preferred_cuts and total_cost < budget:
    print("I'll take it!")
else:
    print("No thanks")   
    
    
#_________________________________________________

if cut in preferred_cuts:
    
    cost = 100
    
    percent_off = (ord(color) - ord("D")) * 0.02
    
    cost *= 1 - percent_off
    
    if not clarity == "I":
        cost *= 2
        
        if not clarity == "SI":
            cost *= 2
            
           
            if not clarity == "VS":
                cost *= 2
                
                if not clarity == "VVS":
                    cost *= 2
                    
                    if not clarity == "IF":
                        cost *= 2

    cost *= carat
    if cost <= budget:
        print("I'll take it!")
    else:
        print("No thanks")
else:
    print("No thanks")    
 
    
    ##########################################################################
    

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#There are (at least) three special types of full moons:
#
# - Super Moon: the full moon occurs when the moon is at its
#   closest approach to earth (less than 230,000km away).
# - Blue Moon: the second full moon in a calendar month. In
#   other words, any full moon on the 29th, 30th, or 31st of
#   a month.
# - Blood Moon: a lunar eclipse during a full moon.
#
#Write a program that will print out the type of moon --
#"Full Moon", "Super Moon", "Blue Moon", "Blood Moon", based
#on the values of the variables above. Note that for the moon
#to be any of these special kinds of moons, it must also be
#full.
#
#Note, though, that multiple modifiers can be true at the same
#time. We could have a Super Blue Moon, a Blue Blood Moon, or
#even a Super Blue Blood Moon.
#
#Always print those modifiers in that order. If any of these
#special modifiers is present, do not include the word "Full".
#If none of them are present, but the moon is Full, then print
#"Full Moon". If none of them are present at all, print "Moon".


#Add your code here!
    
phase = "Full"
distance = 220000
date = 29
eclipse = True

full_moon = phase == "Full"
super_moon = distance < 230000
blue_moon = date == 29 or date == 30 or date == 31
blood_moon = eclipse == True

if full_moon and blood_moon and blue_moon and super_moon:
    print("Super Blue Blood Moon")
elif full_moon and blood_moon and blue_moon:
    print("Blue Blood Moon")
elif full_moon and blood_moon and super_moon:
    print("Super Blood Moon")
elif full_moon and blue_moon and super_moon:
    print("Super Blue Moon")
elif full_moon and blood_moon:
    print("Blood Moon")
elif full_moon and blue_moon:
    print("Blue Moon")
elif full_moon and super_moon:
    print("Super Moon")
elif  full_moon:
    print("Full Moon")
else:
    print("Moon")    
#______________________________________________________________________________    
    
result = "Moon"
if phase == "Full":
    # Note that these nested if statements, not elif, will all print if true
    if eclipse:
        result = "Blood " + result
    if date >= 29:
        result = "Blue " + result
    if distance < 230000:
        result = "Super " + result
    if not (eclipse or date >= 29 or distance < 230000):
        result = "Full Moon"
print(result)   
    
    
    
    
    
    
    
    
    