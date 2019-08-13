#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 20:40:28 2018

@author: meganporter
"""


############################################################################
#Recall Coding Problem 4.3.9 (Advanced), the free body
#diagram problem. If you were unable to solve that, we've
#included the sample answer in the dropdown in the top left
#-- feel free to use that to write your answer to this
#problem.
#
#Revise your code from that problem to use a file instead of
#a list as its parameter. Name this new function
#find_net_force_from_file. The function should take one
#parameter, the name of a file. The function should return
#the net magnitude and direction, just as it did in the other
#problem.
#
#Each line of the file will have two numbers, both integers:
#the first number will be the magnitude, and the second
#number will be the angle (in degrees, from -180 to 180).
#There will be a space between them.
#
#HINT: You may have multiple functions in your code if you
#want!
#
#HINT 2: Try to write this such that you can reuse as much
#of your earlier code as possible. Remember, when loading
#from a file, any text you load is initially a string. You'll
#almost certainly need to use the split() method.

from math import sin, cos, tan, asin, acos, atan2, radians, degrees, sqrt

#Add your function here!
def find_net_force_from_file(file):
    file = open(file)
    file = file.readlines()
    file_list = []
    
    for item in file:
        item = item.strip("\n").split(' ')
        file_list.append(item)
        item[0] = float(item[0])
        item[1] = float(item[1])
        
    sum_x = 0
    sum_y = 0
    for lst in file_list:
        angle = radians(lst[1])
        #print(angle)
        x_force = lst[0] * cos(angle)
        y_force = lst[0] * sin(angle)
        sum_x += x_force
        #print(sum_x)
        sum_y += y_force
        #print(sum_y)
    
    final_mag = sqrt(sum_x **2 + sum_y ** 2)
    final_rad = atan2(sum_y,sum_x)
    final_deg = degrees(final_rad)
    return round(final_mag, 1), round(final_deg, 1)            
    
    file.close()



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: (87.0, 54.4)
print(find_net_force_from_file("a_few_angles.txt"))
print()
#__________________________________________________
from math import sin, cos, tan, asin, acos, atan2, radians, degrees, sqrt

def find_net_force_from_file(filename):
    file = open(filename)
    forces = []
    for line in file:
        
        split_line = line.split()
        
        magnitude = int(split_line[0])
        angle = int(split_line[1])
        new_force = (magnitude, angle)
        forces.append(new_force)
    file.close()
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
    
    print(total_vertical, total_horizontal)
    net_angle = atan2(total_vertical, total_horizontal)
    net_angle = degrees(net_angle)
    net_angle = round(net_angle, 1)
    
    return (net_magnitude, net_angle)
print(find_net_force_from_file("a_few_angles.txt"))
print()
#______________________________________________________________________
from math import sin, cos, tan, asin, acos, atan2, radians, degrees, sqrt

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
def find_net_force_from_file(filename):
    file = open(filename)
    
    forces = []
    for line in file:
        split_line = line.split()
        magnitude = int(split_line[0])
        angle = int(split_line[1])
        new_force = (magnitude, angle)
        forces.append(new_force)
    file.close()
    result = find_net_force(forces)
    return result
print(find_net_force_from_file("a_few_angles.txt"))
print()

############################################################################
#Write a function called st_dev. st_dev should have one
#parameter, a filename. The file will contain one integer on
#each line. The function should return the population standard
#deviation of those numbers.
#
#The formula for population standard deviation can be found here:
#edge.edx.org/asset-v1:GTx+gt-mooc-staging1+2018_T1+type@asset+block@stdev.PNG
#
#The formula is a bit complex, though, and since this is a
#CS class and not a math class, here are the steps you would
#take to calculate it manually:
#
# 1. Find the mean of the list.
# 2. For each data point, find the difference between that
#    point and the mean. Square that difference, and add it
#    to a running sum of differences.
# 4. Divide the sum of differences by the length of the
#    list.
# 5. Take the square root of the result.
#
#You may assume for this problem that the file will contain
#only integers -- you don't need to worry about invalid
#files or lines. The easiest way to take the square root is
#to raise it to the 0.5 power (e.g. 2 ** 0.5 will give the
#square root of 2).
#
#HINT: You might find this easier if you load all of the
#numbers into a list before trying to calculate the average.
#Either way, you're going to need to loop over the numbers
#at least twice: once to calculate the mean, once to
#calculate the sum of the differences.


#Add your function here!
def st_dev(name):
    file = open(name, "r")
    file = file.readlines()
    file_list = []
    total = 0
    vari = 0
    
    
    for item in file:
        file_list.append(item)
        item = int(item)
        total += item
        mean = total / len(file_list)
        """Why is a second for loop necessary?  Is there a limit to how many 
        mathematical operations can be contained in a single loop?"""
    for item in file:
        item = int(item)
        var = (mean - item) ** 2
        vari += var
        variance = vari / len(file_list)
        stDev = variance ** .5
    print(total)
    print(mean)
    print(vari)
    print(variance)
   
    return stDev    
    file.close()


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print 27.796382658340438 (or something around there).
print(st_dev("some_numbers.txt"))
print()
#_------____________________------------------------------
def st_dev(filename):
    file = open(filename)
    numbers = []
    total = 0
    for line in file:
        this_number = int(line)
        numbers.append(this_number)
        total += this_number
    file.close()
    mean = total / len(numbers)
    total_difference = 0
    for number in numbers:
        this_difference = (number - mean) ** 2
        total_difference += this_difference
    result = (total_difference / len(numbers)) ** 0.5
    return result


print(st_dev("some_numbers.txt"))
print()
############################################################################
#Write a function called average_file. average_file should
#have one parameter: a filename.
#
#The file should have an integer on each line. average_file
#should return the average of these integers. However, if
#any of the lines of the file are _not_ integers,
#average_file should return the string "Error reading file!"
#
#Remember, by default, every time you read a line from a
#file, it's interpreted as a string.


#Add your function here!
def average_file(name):
    file = open(name, "r")
    file = file.readlines()
    
    try:
        sum = 0
        for i in file:
            sum += int(i)
        return sum / len(file)
    except:
        return "Error reading file!"
    
    file.close()



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 5.0, then Error reading file!
#
#You can select valid_file.txt and invalid_file.txt from
#the dropdown in the top left to preview their contents.
print(average_file("valid_file.txt"))
print(average_file("invalid_file.txt"))
print()
#_____________________________________________
def average_file(filename):
    file = open(filename)
    total = 0
    count = 0
    
    try:
        for line in file:
            value = int(line)
            total += value
            count += 1
    except ValueError:
        file.close()
        return "Error reading file!"
    else:
        file.close()
        return total / count
print(average_file("valid_file.txt"))
print(average_file("invalid_file.txt"))

print()

############################################################################
#Write a function called "angry_file_finder" that accepts a
#filename as a parameter. The function should open the file,
#read it, and return True if the file contains "!" on every
#line. Otherwise the function should return False. 
#
#Hint: there are lots of ways to do this. We'd suggest using
#either the readline() or readlines() methods. readline()
#returns the next line in the file; readlines() returns a
#list of all the lines in the file.


#Write your function here!
def angry_file_finder(file):
    file = open(file, "r")
    file = file.readlines()
    
    if all("!" in line for line in file):
        return True
    return False

    file.close()

    
     
                
        
       
#if all([x[2] == 0 for x in lista])


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True
print(angry_file_finder("AngryFileFinderInput.txt"))
print()
#_____________________________________
def angry_file_finder(filename):
    file_reader = open(filename)
    for line in file_reader:
        if not "!" in line:
            file_reader.close()
            return False
    file_reader.close()
    return True
    # Note that ther is no else statement and the second return is in line 
    #with  the for statement
    
    
print(angry_file_finder("AngryFileFinderInput.txt"))
print()
#______________________________________

#After rearranging, this also works:

def angry_file_finder(filename):
    file_reader = open(filename)
    for line in file_reader:
        if "!" in line:
            file_reader.close()
            return True
    file_reader.close()
    return False
print()
############################################################################
#Write a function called "load_file" that accepts one 
#parameter: a filename. The function should open the
#file and return the contents.#
#
# - If the contents of the file can be interpreted as
#   an integer, return the contents as an integer.
# - Otherwise, if the contents of the file can be
#   interpreted as a float, return the contents as a
#   float.
# - Otherwise, return the contents of the file as a
#   string.
#
#You may assume that the file has only one line.
#
#Hints:
#
# - Don't forget to close the file when you're done!
# - Remember, anything you read from a file is
#   initially interpreted as a string.


#Write your function here!
def load_file(file_name):
    file = open(file_name, "r")
    file_list = []

    for item in file:
        try:
            int(item)
            return int(item)
        except ValueError:
            pass

        try:
            float(item)
            return float(item)
        except ValueError:
            pass
        

            return str(item)   
        file.close()
   
    
    
    

#________________________________________________
contents = load_file("LoadFromFileInput.txt")
print(contents)
print(type(contents))
print()

def load_file(filename):
    
    file_reader = open(filename, "r")
    
    contents = file_reader.readline()
    try:
        return int(contents)
    
    except:
        try:
            return float(contents)
        
        except:
            return contents
    finally:
        file_reader.close()
contents = load_file("LoadFromFileInput.txt")
print(contents)
print(type(contents))
print()
#________________________________________________


def load_file(filename):
    
    file_reader = open(filename, "r")
    contents = file_reader.readline()
    file_reader.close()
    
    try:
        return int(contents)
    
    except:
        pass
    
    try:
        return float(contents)
    
    except:
        return contents
contents = load_file("LoadFromFileInput.txt")
print(contents)
print(type(contents))
print()

############################################################################
#Write a function called "find_coffee" that expects a 
#filename as a parameter. The function should open the 
#given file and return True if the file contains the word 
#"coffee". Otherwise, the function should return False.
#
#Hint: look up the read() method if you want to do this
#more simply than you might do with readline().


#Write your function here!
def find_coffee(file):
    coffee = open(file, "r")
    coff = coffee.read()
    if "coffee" in coff:
        return True
    else:
        return False
    coffee.close()
    
    
    

""".read() reads an entire file while .readline() only reads the whole of
one line"""
#You can test your function with the provided files named 
#"coffeeful.txt" and "coffeeless.txt". With their original
#text, the lines below should print True, then False. You
#may also edit the files by selecting them in the drop
#down in the top left to try your code with different
#input.
print(find_coffee("coffeeful.txt"))
print(find_coffee("coffeeless.txt"))
print()
#_____________________________
def find_coffee(filename):
    
    #First we open the file as usual. Note that if we don't
    #supply a read mode, Python assumes "read", so we don't
    #actually need to include the "r" in the call to
    #open() -- but we could.
    
	file_reader = open(filename)
    
    #Then we read the file into a variable called contents:
    
	contents = file_reader.read()
    
    #Then we check if "coffee" appears in that string:
    
	result = "coffee" in contents
    
    #Close the file...
    
	file_reader.close()
    
    #Then return the result!
    
	return not result  

    #We could compress this a bit as well, but not down
    #to one line because we need to be able to close the
    #file.



print(find_coffee("coffeeful.txt"))
print(find_coffee("coffeeless.txt"))
print()
############################################################################
#Write a function called "append_to_file" that accepts
#two parameters: a filename and some data that will
#be an integer or a string to write. The function 
#should open the file and add the data to the end of
#the file. Each new call to append_to_file should add
#the new contents on a new line.
#
#Hints:
#
# - Don't forget to close the file when you're done!
# - If the data isn't a string already, you may need
#   to convert it.
# - Remember, this code has no print statements, so
#   when you run it, don't expect to see any output
#   on the right! You could add print statements if
#   you want a confirmation the code is done running.
# - You can put the variable for the filename in the
#   same place where we put text like OutputFile.txt
#   in the videos.


#Write your function here!
def append_to_file(file, data):
    working_file = open(file, "a")
    working_file.write(str(data)  + "\n")
    working_file.close()
    #print("done")
    return
#Other method:
    #print(str(data), file = working_file)


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print nothing. However, if you open AppendToFileOutput.txt
#in the top left after running it, the contents of the
#file should be another instance of 1301 every time you
#run this file.
append_to_file("AppendToFileOutput.txt", 1301)
print()
############################################################################
#Write a function called "write_file" that accepts two 
#parameters: a filename and some data that will either 
#be an integer or a string to write. The function 
#should open the file and write the data to the file.
#
#Hints:
#
# - Don't forget to close the file when you're done!
# - If the data isn't a string already, you may need
#   to convert it, depending on the approach you
#   choose.
# - Remember, this code has no print statements, so
#   when you run it, don't expect to see any output
#   on the right! You could add print statements if
#   you want a confirmation the code is done running.
# - You can put the variable for the filename in the
#   same place where we put text like OutputFile.txt
#   in the videos.


#Write your function here!
def write_file(file_name, data):
    written_file = open(file_name, "w")
    written_file.write(str(data))
    written_file.close()
    #print("done")
    return



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print nothing. However, if you open WriteFileOutput.txt
#in the top left after running it, the contents of the
#file should be 1301.
write_file("WriteFileOutput.txt", 1301)