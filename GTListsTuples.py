#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 23:21:37 2018

@author: meganporter
"""


############################################################################
#Write a function called one_dimensional_booleans.
#one_dimensional_booleans should have two parameters:
#a list of booleans called bool_list and a boolean called
#use_and. You may assume that bool_list will be a list
#where every value is a boolean (True or False).
#
#The function should perform as follows:
#
# - If use_and is True, the function should return True if
#   every item in the list is True (simulating the and
#   operator).
# - If use_and is False, the function should return True if
#   any item in the list is True (simulating the or
#   operator).


#Write your function here!
def one_dimensional_booleans(bool_list, use_and):
    if use_and:
        if bool_list[0] and bool_list[1] and bool_list[2]:
            return True
        else:
            return False
    elif not use_and:
        if bool_list[0] or bool_list[1] or bool_list[2]:
            return True
        else:
            return False
        


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, False, True, False.
print(one_dimensional_booleans([True, True, True], True))
print(one_dimensional_booleans([True, False, True], True))
print(one_dimensional_booleans([True, False, True], False))
print(one_dimensional_booleans([False, False, False], False))
print()
#_________________________________________

def one_dimensional_booleans(bool_list, use_and):
    
    #There are a lot of different ways you could do this.
    #You could, for example, loop over each item in the
    #list and update a running result based on the new
    #value.
    #
    #Let's try it a simpler way, though. If use_and was
    #False, then our logic is pretty simple: we just
    #return whether 'True' is anywhere in the list:
    
    if not use_and:
        return True in bool_list
    
    #If use_and was True, our logic is just a little bit
    #more complicated. First, we want to find our whether
    #False is in the list. If it is, then we want to
    #return False; if it's not (meaning all the values
    #are True), then we want to return True. So, we want
    #to return the *opposite* of False in bool_list. We
    #can do that with the not operator:
    
    else:
        return not False in bool_list
    
    #Note that we could actually compress these four lines
    #down into only one, but it makes the logic a little
    #harder to follow:
    #
    #return (use_and and True in bool_list) or (not use_and and not False in bool_list)



print(one_dimensional_booleans([True, True, True], True))
print(one_dimensional_booleans([True, False, True], True))
print(one_dimensional_booleans([True, False, True], False))
print(one_dimensional_booleans([False, False, False], False))
print()

############################################################################
#A significant part of introductory physics is calculating
#the net force on an object based on several different
#magnitudes and directions. If you're unfamiliar with how
#this works, we recommend checking out this WikiHow article:
#https://www.wikihow.com/Find-Net-Force
#
#Each force acting on the object is defined by its angle and
#magnitude. The process for calculating net force is:
#
# - For each force, break the force into its horizontal and
#   vertical components. The horizontal component can be
#   calculated as magnitude * cos(angle), and the vertical
#   component can be calculated as magnitude * sin(angle).
# - Sum all the horizontal components to find the total
#   horizontal force, and sum the vertical components to find
#   the total vertical force.
# - Use the Pythagorean theorem to calculate the total
#   magnitude: sqrt(total_horizontal ^ 2 + total_vertical ^ 2)
# - Use inverse tangent to calculate the angle:
#   atan(total_vertical / total_horizontal)
#
#Write a function called find_net_force. find_net_force should
#take one parameter as input: a list of 2-tuples. Each 2-tuple
#in the list is a (magnitude, angle) pair. angle will be in
#degrees between -180 and 180.
#
#Return a 2-tuple containing the final magnitude and angle of
#all the forces. angle should again be in degrees. You should
#round both magnitude and angle to one decimal place, which
#you can do using round(magnitude, 1) and round(angle, 1).
#
#To do this, you'll need to use a few functions from the math
#module in Python. The line below will import these:

from math import sin, cos, tan, asin, acos, atan2, radians, degrees, sqrt

#sin, cos, and tan are the trigonometric functions for sine,
#cosine, and tangent. Each takes one argument, an angle in
#radians, and returns its sine, cosine, or tangent.
#
#asin, acos, and atan2 are their inverse functions. Each
#takes two arguments, a vertical component and a horizontal
#component (in that order), and returns the corresponding
#angle in radians.
#
#Note that sin, cos, and tan all assume the angle is in
#radians, and asin, acos, and atan2 will all return an
#angle in radians. So, you'll need to convert your angles to
#radians before or after using these functions, using things
#like this: angle_in_radians = radians(angle)
#           angle_in_degrees = degrees(angle_in_radians)

#sqrt will find the square root of a number, e.g. sqrt(4) = 2.
#Note that you should only need sin, cos, atan, degrees,
#radians, and sqrt: we've imported the others just in case you
#want to use them.


#Add your function here!
def find_net_force(forces):
    sum_x = 0
    sum_y = 0
    for tup in forces:
        angle = radians(tup[1])
        #print(angle)
        x_force = tup[0] * cos(angle)
        y_force = tup[0] * sin(angle)
        sum_x += x_force
        #print(sum_x)
        sum_y += y_force
        #print(sum_y)
    
    final_mag = sqrt(sum_x **2 + sum_y ** 2)
    final_rad = atan2(sum_y,sum_x)
    final_deg = degrees(final_rad)
    return round(final_mag, 1), round(final_deg, 1)
    



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: (87.0, 54.4)

forces = [(10, 90), (10, -90), (100, 45), (20, 180)]
print(find_net_force(forces))
print()
#_____________________________________

def find_net_force(forces):
    total_horizontal = 0
    total_vertical = 0
    for force in forces:
        magnitude, angle = force
        angle = radians(angle)
        horizontal = magnitude * cos(angle)
        vertical = magnitude * sin(angle)
        total_horizontal += horizontal
        total_vertical += vertical
    net_magnitude = sqrt(total_horizontal**2 + total_vertical**2)
    net_magnitude = round(net_magnitude, 1)
    net_angle = atan2(total_vertical, total_horizontal)
    net_angle = degrees(net_angle)
    net_angle = round(net_angle, 1)
    return (net_magnitude, net_angle)

forces = [(10, 90), (10, -90), (100, 45), (20, 180)]
print(find_net_force(forces))
############################################################################

#Write a function called string_splitter that replicates the
#function of the string type's split() method, assuming that
#we're splitting at spaces. string_splitter should take as
#input a string, and return as output a list of the
#individual words from the string, assuming that words were
#divided by spaces. The spaces themselves should not be in
#the list that your function returns.
#
#You may assume that there will never be more than one space
#in a row, and that the string will neither start nor end
#with a space. However, you should not assume there will
#always be a space.
#
#You may not use Python's built-in split() method.
#
#For example:
#
#  string_splitter("Hello world") -> ['Hello', 'world']


#Write your function here!
def string_splitter(string):
    lis = []
    emp_str = ""
    for i in string:
        if i == " ":
            lis.append(emp_str)
            emp_str = ""
        else:
            emp_str += i
    if emp_str:
        lis.append(emp_str)
    return lis    
                 



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: ['Hello', 'world']
print(string_splitter("Hello world"))
print()

#_______________________________________

def string_splitter(a_string):
    
    words = []
    while " " in a_string:
        index = a_string.find(" ")
        words.append(a_string[:index])
        a_string = a_string[index + 1:]
    words.append(a_string)
    
    return words


print(string_splitter("Hello, world"))
############################################################################

#Imagine you're writing some code for an exercise tracker.
#The tracker measures heart rate, and should display the
#average heart rate from an exercise session.
#
#However, the tracker doesn't automatically know when the
#exercise session began. It assumes the session starts the
#first time it sees a heart rate of 100 or more, and ends
#the first time it sees one under 100.
#
#Write a function called average_heart_rate.
#average_heart_rate should have one parameter, a list of
#integers. These integers represent heart rate measurements
#taken 30 seconds apart. average_heart_rate should return
#the average of all heart rates between the first 100+
#heart rate and the last one. Return this as an integer
#(use floor division when calculating the average).
#
#You may assume that the list will only cross the 100 beats
#per minute threshold once: once it goes above 100 and below
#again, it will not go back above.


#Add your function here!
def average_heart_rate(beats):
    hearts = []
    sum = 0
    for beat in beats:
        if beat >= 100:
            hearts.append(beat)
    for beat in hearts:
        sum += beat
    
        
    return sum//len(hearts)     
        



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print 114 (because there are 14 measurements from 102 to
#101, their sum is 1609, and 1609 // 14 is 114).
beats = [72, 77, 79, 95, 102, 105, 112, 115, 120, 121, 121,
         125, 125, 123, 119, 115, 105, 101, 96, 92, 90, 85]
print(average_heart_rate(beats))
print()
#------------------------------------------------------------------


def average_heart_rate(rates):
    measuring = False
    for rate in rates:
        if rate >= 100:
            measuring = True
        else:
            measuring = False
        if measuring:
            total += rate
            count += 1
    return total // count
beats = [72, 77, 79, 95, 102, 105, 112, 115, 120, 121, 121,
         125, 125, 123, 119, 115, 105, 101, 96, 92, 90, 85]
print(average_heart_rate(beats))
print()

def average_heart_rate(rates):
    total = 0
    count = 0
    for rate in rates:
        if rate >= 100:
            total += rate
            count += 1
    return total // count


beats = [72, 77, 79, 95, 102, 105, 112, 115, 120, 121, 121,
         125, 125, 123, 119, 115, 105, 101, 96, 92, 90, 85]
print(average_heart_rate(beats))
############################################################################
#Write a function called wish_list. wish_list should have
#four parameters, in this order: 
#
# - a list of strings, representing a list of items on a
#   wish list
# - a string, representing a particular item
# - a float, representing the cost of this item
# - a float, representing your budget
#
#If the item is on the list and you can afford it (cost is
#less than or equal to budget), return the string,
#"You should buy a [item name]!", replacing [item name]
#with the string.
#
#If the item is on the list but you can't afford it,
#return the string, "You should save up for a [item name]!",
#replacing [item name] with the string.
#
#If the item is not on the list, you should return the
#string "You probably don't want to buy a [item name].",
#replacing [item name] with the string.
#
#HINT: You do not need a loop to solve this. You can use
#one, but you don't need one.


#Add your function here!
def wish_list(wishes, wish_item, cost, budget):
    if wish_item in wishes:
        if budget >= cost:
            return "You should buy a " + wish_item + "!"
        else:
            return "You should save up for a " + wish_item + "!"
    else: 
        return "You probably don't want to buy a " + wish_item + "."
    



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: "You should save up for a bugle!"

wish_list_items = ["bugle", "trumpet", "banjo", "tuba"]
selected_item = "bugle"
item_cost = 199.99
budget = 150.00

print(wish_list(wish_list_items, selected_item, item_cost, budget))
print()
############################################################################
#Write a function called find_max_sales. find_max_sales will
#have one parameter: a list of tuples. Each tuple in the
#list will have two items: a string and an integer. The
#string will represent the name of a movie, and the integer
#will represent that movie's total ticket sales (in millions
#of dollars).
#
#The function should return the movie from the list that
#had the most sales. Return only the movie name, not the
#full tuple.


#Write your function here!
from operator import itemgetter

def find_max_sales(tup):
    tup = sorted(tup,key=itemgetter(1), reverse = True)
    #sorted([tup],key=lambda x: x[1], reverse=True)
    return tup[0][0]
    
    
        
    


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: Rogue One
movie_list = [("Finding Dory", 486), ("Captain America: Civil War", 408), ("Deadpool", 363), ("Zootopia", 341), ("Rogue One", 529), ("The Secret Life of Pets", 368), ("Batman v Superman", 330), ("Sing", 268), ("Suicide Squad", 325), ("The Jungle Book", 364)]
print(find_max_sales(movie_list))
print()
#_________________________________

def find_max_sales(movie_list):
    current_max_movie = ""
    current_max_sales = -1
    for movie_tuple in movie_list:
        if movie_tuple[1] > current_max_sales:
            current_max_sales = movie_tuple[1]
            current_max_movie = movie_tuple[0]
    return current_max_movie
movie_list = [("Finding Dory", 486), ("Captain America: Civil War", 408), ("Deadpool", 363), ("Zootopia", 341), ("Rogue One", 529), ("The Secret Life of Pets", 368), ("Batman v Superman", 330), ("Sing", 268), ("Suicide Squad", 325), ("The Jungle Book", 364)]
print(find_max_sales(movie_list))
print()
#_________________________________\
def find_max_sales(movie_list):
    current_max_tuple = movie_list[0]
    for movie_tuple in movie_list:
        if movie_tuple[1] > current_max_tuple[1]:
            current_max_tuple = movie_tuple
    return current_max_tuple[0]
print()

############################################################################
#Write a function called solve_right_triangle. The function
#solve_right_triangle should have three parameters: opposite, 
#adjacent, and use_degrees. opposite and adjacent will be
#floats, and use_degrees will be a boolean. use_degrees
#should be a keyword parameter, and it should have a
#default value of False.
#
#The function should return a tuple containing the
#hypotenuse and angle of the right triangle (in that order).
#If use_degrees is False, the angle should be in radians.
#If use_degrees is True, the angle should be in degrees.
#
#Remember, the formula for the hypotenuse of a right
#triangle is the square root of the sum of the squared side
#lengths. You can find arctan using math.atan(), passing in
#the quotient of the opposite and adjacent as the argument.
#By default, math.atan() returns the angle in radians; you
#can pass that angle as an argument into the math.degrees()
#method to convert it to degrees; for example:
#
# angle_in_degrees = math.degrees(angle_in_radians)

import math


#Write your function here!
def solve_right_triangle(opposite, adjacent, use_degrees = False):
    hypotenuse = math.sqrt(opposite ** 2 + adjacent ** 2)
    angle_rad = math.atan(opposite/adjacent)
    angle_deg = math.degrees(angle_rad)
    if use_degrees:
        angle = angle_deg
    else:
        angle = angle_rad
    return hypotenuse, angle    
    


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#(5.0, 0.6435011087932844)
#(5.0, 36.86989764584402)
print(solve_right_triangle(3.0, 4.0))
print(solve_right_triangle(3.0, 4.0, use_degrees = True))
print()
#_____________________________________
def solve_right_triangle(opposite, adjacent, use_degrees = False):
    hypotenuse = (opposite ** 2 + adjacent ** 2) ** 0.5
    angle = math.atan(opposite / adjacent)
    if use_degrees == True:
        angle = math.degrees(angle)
    return (hypotenuse, angle)
    

print(solve_right_triangle(3.0, 4.0))
print(solve_right_triangle(3.0, 4.0, use_degrees = True))
print()
############################################################################
#If it does not, the student does not get a point.
#
#If the lists do not have the same number of items, return
#-1 to indicate that the answer key did not belong to the
#same test as the student's answers.\
#
#Hint: in the past, lots of people have tried to do this using
#the index() method. That won't work! You'll need to track the
#index yourself.


#Write your function here!
def grade_scantron(answers, key):
    if len(answers) != len(key):
        return -1
    count = 0
    for item in range(len(answers)):
        if answers[item] == key[item]:
            count += 1
    return count
                



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 7
test_answers = ["A", "B", "B", "A", "D", "A", "B", "A", "E"]
test_key = ["A", "B", "B", "A", "D", "E", "B", "A", "D"]
print(grade_scantron(test_answers, test_key))
print()

############################################################################
#Write a function called attendance_check. attendance_check
#should have two parameters: roster and present. Both roster
#and present will be lists of strings. Return a list (sorted
#alphabetically) of all strings in the list roster that are
#not in the list present. In other words, if roster is a
#list of students enrolled in a class and present is a list
#of students in class today, return a list of students that
#are absent.
#
#You may assume that every item in each list will be a
#string. You may also assume that every name in the list
#present will be in the list roster. If no students are
#absent, return an empty list.


#Write your function here!
def attendance_check(roster, present):
    not_present = []
    for item in roster:
        if item not in present:
            not_present.append(item)
            not_present.sort()
    return not_present


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 
#['Ferguson', 'Winston']
test_roster = ['Jessica', 'Nick', 'Winston', 'Schmidt', 'Cece', 'Ferguson']
test_present = ['Nick', 'Cece', 'Schmidt', 'Jessica']
print(attendance_check(test_roster, test_present))
print()
#_______________________________________________
def attendance_check(roster, present):
    absent = []
    for name in roster:
        if not name in present:
            absent.append(name)
    absent.sort()
    return absent



test_roster = ['Jessica', 'Nick', 'Winston', 'Schmidt', 'Cece', 'Ferguson']
test_present = ['Nick', 'Cece', 'Schmidt', 'Jessica']
print(attendance_check(test_roster, test_present))

############################################################################
#Write a function, called lucky_sevens, that takes in one
#parameter, a list of integers, and returns True if the list
#has three '7's  in a row and False if the list doesn't.
#
#For example:
#
#  lucky_sevens([4, 7, 8, 2, 7, 7, 7, 3, 4]) -> True
#  lucky_sevens([4, 7, 7, 2, 8, 3, 7, 4, 3]) -> False
#
#Hint: As soon as you find one instance of three sevens, you
#could go ahead and return True -- you only have to find it
#once for it to be True! Then, if you get to the end of the
#function and haven't returned True yet, then you might
#want to return False.

"""This isn't working and I don't understand why. What is it about the last list
that prevents the function from iterating properly?"""
#Write your function here!
def lucky_sevens(list1):
    for i in list1:
        if list1[i] == 7:
            for i in range(i, i + 3):
                if list1[i] == 7:
                    return True
            else:
                return False
                
print(lucky_sevens([4, 7, 8, 2, 7, 7, 7, 3, 4]))
print(lucky_sevens([4, 7, 1, 2, 8, 3, 7, 4, 3]))
print(lucky_sevens([7, 7, 7, 4, 1, 2, 9, 6, 6, 8, 9, 9, 5, 6, 9, 7, 7, 7]))                
        
def lucky_sevens(list1):
    for i in list1:
        if list1[i] == 7:
            if list1[i + 1] == 7:
                if list1[i + 2] == 7:
                    return True
            else:
                return False   
        



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, then False
print(lucky_sevens([4, 7, 8, 2, 7, 7, 7, 3, 4]))
print(lucky_sevens([4, 7, 1, 2, 8, 3, 7, 4, 3]))
print(lucky_sevens([7, 7, 7, 4, 1, 2, 9, 6, 6, 8, 9, 9, 5, 6, 9, 7, 7, 7]))
############################################################################
#We've learned a lot in this chapter. Let's try to use a lot
#of it for one final exercise.
#
#Write a function called sort_artists. sort_artists will
#take as input a list of tuples. Each tuple will have two
#items: the first item will be a string holding an artist's
#name, and the second will be an integer representing their
#total album sales (in millions).
#
#Return a tuple of two lists. The first list in the
#resulting tuple should be all the artists sorted
#alphabetically. The second list should be all the revenues
#sorted in descending numerical order.
#
#For example:
# artists = [("The Beatles", 270.8), ("Elvis Presley", 211.5), ("Michael Jackson", 183.9)]
# sort_artists(artists) -> (["Elvis Presley", "Michael Jackson", "The Beatles"], [270.8, 211.5, 183.9])
#
#Notice that artists is a list of tuples (brackets first,
#then parentheses), but sort_artists outputs a tuple of
#lists (parentheses first, then brackets).


#Write your function here!
def sort_artists(l_tup):
    list1 = []
    list2 = []
    for tup in l_tup:
        list1.append(tup[0])
        list2.append(tup[1])
        list1.sort()
        list2.sort(reverse = True)
        #list2.reverse()
        tup_total = (list1, list2)
    return tup_total    
            


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#(['Elvis Presley', 'Michael Jackson', 'The Beatles'], [270.8, 211.5, 183.9])  
artists = [("The Beatles", 270.8), ("Elvis Presley", 211.5), ("Michael Jackson", 183.9)]
print(sort_artists(artists))
print()

############################################################################
#Write a function called sum_lists. sum_lists should take
#one parameter, which will be a list of lists of integers.
#sum_lists should return the sum of adding every number from
#every list.
#
#For example:
#
# list_of_lists = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# sum_list(list_of_lists) -> 67


#Add your code here!
def sum_lists(lists):
    total = 0
    for group in lists:
        sum1 = 0
        for item in group:
            sum1 += item
        total += sum1
    return total    



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 78
list_of_lists = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(sum_lists(list_of_lists))
print()
#_______________________________________________

def sum_lists(list_of_lists):
    
    total = 0
    for a_list in list_of_lists:
        for item in a_list:
            total += item
    return total
list_of_lists = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(len(list_of_lists))
print(sum_lists(list_of_lists))

############################################################################
#Write a function called multiply_strings. Multiply
#strings should have one parameter, a list of strings.
#It should return a modified list according to the
#following changes:
#
# - Every string stored at an even index should be
#   doubled.
# - Every string stored at an index that is a multiple
#   of 3 should be tripled.
# - Every other string should remain unchanged.
#
#These changes should "stack": the string stored at index
#6 should be duplicated six times (2 * 3).
#
#Then, return the new list. You may assume that 0 is a
#multiple of 2 and 3.
#
#Hint: To do this, you need to modify the values of the
#list using their indices, e.g. a_list[1]. If you're not
#using their indices, your answer won't work!


#Write your function here!
def multiply_strings(a_list):
    for i in range(len(a_list)):
        if i % 2 == 0:
            a_list[i] *= 2
        elif i % 2 == 0 and i % 3 == 0:
            a_list[i] *= 2*3
        elif i % 3 == 0:
            a_list[i] *= 3
    return a_list
        


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 
#['AAAAAA', 'B', 'CC', 'DDD', 'EE', 'F', 'GGGGGG']
test_list = ["A", "B", "C", "D", "E", "F", "G"]
print(multiply_strings(test_list))
print()

#____________________________________________________

def multiply_strings(a_list):
    
    for i in range(0, len(a_list)):
        if i % 2 == 0:
            a_list[i] *= 2
        if i % 3 == 0:
            a_list[i] *= 3
    return a_list


test_list = ["A", "B", "C", "D", "E", "F", "G"]
print(multiply_strings(test_list))
print()
############################################################################
#Write a function called modify_list. modify_list will
#take one parameter, a list. It should then modify the
#list in the following ways, in this order:
#
# - Sort the list (using the default sort method).
# - Reverse the order of the list.
# - Delete the last three items of the list.
# - Removes one instance the integer 7 from the list, if
#   it's present.
# - Double the values of the first and third items in
#   the list.
#
#It should then return the resulting list. You may assume
#the list will start with at least six items.
#
#Hint: Remember Python is 0-indexed. The second item
#does not have an index of 2.
#
#Hint 2: Remember, the list.remove() function removes items
#by value, not by index. Note also that if the item you're
#trying to remove is not found in the list, remove() will
#throw an error: so, you'll want to avoid that one way or
#another!


#Write your code here!
def modify_list(a_list):
    a_list.sort()
    a_list.reverse()
    del a_list[-3:]
    if 7 in a_list:
        a_list.remove(7)
    else:
       pass
    a_list.insert(0, a_list[0] * 2)
    a_list.remove(a_list[1])
    a_list.insert(2, a_list[2] * 2)
    a_list.remove(a_list[3])
    return a_list


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#[178, 81, 75.0, 4, 3.141592653589793, 3]
import math
print(modify_list([7, 4, 3, 2.0, 81, 37.5, 89, math.pi, -2, math.e]))
print(modify_list([47, 38.03364336337719, 11, 86.94074746905194, 35, 7, 46.24080820515947, 73, 43.331713446409815, 41, 66.04598414445204]))
print()
#___________________________________________________

def modify_list(a_list):
    
    a_list.sort()
    a_list.reverse()
    del a_list[-3:]
    
    if 7 in a_list:
        a_list.remove(7) #no pass needed
    a_list[0] *= 2 #no insert and delete needed
    a_list[2] *= 2
    
    return a_list


import math
print(modify_list([7, 4, 3, 2.0, 81, 37.5, 89, math.pi, -2, math.e]))

############################################################################
#Remember asciitable.com from an earlier exercise? We're
#going to use it again. Remember, ordinal values for
#characters are given in the 'Dec' column of asciitable.com.
#
#Write a function called character_info. character_info will
#take as input a string with only one character. It should
#return a 3-tuple with three pieces of information:
#
# - In the first spot, the character itself.
# - In the second spot, the ordinal value of the character,
#   obtained using the ord() function (e.g. ord("a") -> 97).
# - In the third spot, what type of character it is: either
#   "letter", "number", or "punctuation".
#
#You may assume that anything that is not a letter (either
#upper or lower case) or a number is punctuation. You may
#also assume the ordinal will be between 32 (" ") and 126
#("~").


#Write your function here!
def character_info(char):
    one = char
    two = ord(char)
    if 33 <= two <= 47 or 58 <= two <= 64 or 91 <= two <= 96 or 123 <= two <= 126:
        return (one, two, "punctuation")
    elif 48 <= ord(char) <=57:
        return (one, two, "number")
    elif 65 <= two <= 90 or 97 <= two <= 122:
        return (one, two, "letter")
    
    
     
    
        
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#('q', 113, 'letter')
#('7', 55, 'number')
#('`', 96, 'punctuation')
print(character_info("q"))
print(character_info("7"))
print(character_info("`"))
print()

def character_info(a_char):
    
    ordinal = ord(a_char)
    if ordinal >= 48 and ordinal <= 57:
        char_type = "number"
    elif (ordinal >= 65 and ordinal <= 90) or (ordinal >=97 and ordinal <= 122):
        char_type = "letter"
    else:
        char_type = "punctuation"
    
    return (a_char, ordinal, char_type)
    
        

print(character_info("q"))
print(character_info("7"))
print(character_info("`"))
############################################################################
#Write a function called unpack_and_reverse that will
#accept one parameter, a tuple with at least three items.
#The function should return a new tuple with only the first
#three items, but listed in reverse order.
#
#For example:
#
# a_tuple = ("a", "b", "c", "d", "e")
# unpack_and_reverse(a_tuple) -> ("c", "b", "a")
#
#However, to do this, you should not access any value in
#the tuple directly (e.g. with a_tuple[1]). Instead, you
#should use tuple unpacking to unpack them into variables.
#You also should not touch any items past the third item
#in the tuple: use tuple slicing instead to only access
#the first three.


#Write your function here!
def unpack_and_reverse(a_tuple):
    new_tuple = a_tuple[::-1]
    return new_tuple[-3:]
        


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#('c', 'b', 'a')
#('h', 'g', 'f')
#('k', 'j', 'i')
print(unpack_and_reverse(("a", "b", "c", "d", "e")))
print(unpack_and_reverse(("f", "g", "h")))
print(unpack_and_reverse(("i", "j", "k", "l", "m", "n", "o", "p", "q", "r")))
print()
#_____________________________________________________
#def unpack_and_reverse(a_tuple):
#    item1, item2, item3 = a_tuple[0:3]
#    return (item3, item2, item1)
def unpack_and_reverse(a_tuple):
    item1, item2, item3 = a_tuple[0:3]
    return (item3, item2, item1)


print(unpack_and_reverse(("a", "b", "c", "d", "e")))
print(unpack_and_reverse(("f", "g", "h")))
print(unpack_and_reverse(("i", "j", "k", "l", "m", "n", "o", "p", "q", "r")))
############################################################################
#Write a function called string_length. string_length should
#have one parameter, a string. It should return a 2-tuple:
#the first item in the 2-tuple should be the string itself,
#and the second item should be the length of the string as
#given by the len() function.


#Write your function here!
def string_length(string):
    return (string, len(string))


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 
print(string_length("Hello, world!"))
print(string_length("CS1301"))
print(string_length("Some people pronounce it 'toople'. Others pronounce it 'tuhple'. Either is correct."))