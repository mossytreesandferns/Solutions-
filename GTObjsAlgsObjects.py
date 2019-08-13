#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 15:55:32 2018

@author: meganporter
"""



########################################################################
#Copy your Burrito class from the last exercise. Now,
#write a getter and a setter method for each attribute. 
#Each setter should accept a value as an argument. If the 
#value is a valid value, it should set the corresponding 
#attribute to the given value. Otherwise, it should set the 
#attribute to False.
#
#Edit the constructor to use these new setters and getters.
#In other words, if we were to call:
#
# new_burrito = Burrito("spaghetti", True, True, False)
#
#new_burrito.meat would be False because "spaghetti" is not
#one of the valid options. Note that you should NOT try to
#check if the new value is valid in both the constructor and
#the setter: instead, just call the setter from the
#constructor using something like self.set_meat(meat).
#
#Valid values for each setter are as follows:
#
# - set_meat: "chicken", "pork", "steak", "tofu", False
# - set_to_go: True, False
# - set_rice: "brown", "white", False
# - set_beans: "black", "pinto", False
# - set_extra_meat: True, False
# - set_guacamole: True, False
# - set_cheese: True, False
# - set_pico: True, False
# - set_corn: True, False
#
#Make sure you name each setter with the format: 
#"set_some_attribute" and "get_some_attribute"
#
#For example, the getter for meat would be get_meat. The
#getter for to_go would be get_to_go.
#
#Hint: Your code is going to end up *very* long. This
#will be the longest program you've written so far, but
#it isn't the most complex. Complexity and length are
#often very different!
#
#Hint 2: Checking for valid values will be much easier
#if you make a list of valid values for each attribute
#and check the new value against that.


#Write your code here!
class Burrito:
    def __init__(self, meat, to_go, rice, beans, extra_meat=False, guacamole=False, cheese=False, pico=False, corn=False):
        self.meat = meat
        self.to_go = to_go
        self.rice = rice
        self.beans = beans
        self.extra_meat = extra_meat
        self.guacamole = guacamole
        self.cheese = cheese
        self.pico = pico
        self.corn = corn
        
    def get_meat(self):
        return self.meat
    def get_to_go(self):
        return self.to_go
    def get_rice(self):
        return self.rice
    def get_beans(self):
        return beans
    def get_extra_meat(self):
        return self.extra_meat
    def get_guacamole(self):
        return guacamole
    def get_cheese(self):
        return cheese
    def get_pico(self):
        return pico
    def get_corn(self):
        return corn
        
    def set_meat(self, new_meat):
        meats = ["chicken", "pork", "steak", "tofu"]
        if self.meat in meats:
            self.meat = new_meat
        else:
            self.meat = False
    def set_to_go(self, new_to_go):
        to_go = [True]
        if self.to_go in to_go:
            self.to_go = new_to_go
        else:
            self.to_go = False
    def set_rice(self, new_rice):
        rices = ["brown", "white"]
        if self.rice in rices:
            self.rice = new_rice
        else:
            self.rice = False
    def set_beans(self, new_beans):
        beans = ["black", "pinto"]
        if self.beans in beans:
            self.beans = new_beans
        else:
            self.beans = False
    def set_extra_meat(self, new_extra_meat):
        self.extra_meat = new_extra_meat
    def set_guacamole(self, new_guacamole):
        self.guacamole = new_guacamole
    def set_cheese(self, new_cheese):
        self.cheese = new_cheese
    def set_pico(self, new_pico):
        self.pico = new_pico
    def set_corn(self, new_corn):
        self.corn = new_corn

#new_burrito = Burrito("spaghetti", True, "brown", "black")
#print(new_burrito.beans)
#Feel free to add code below to test out the class that
#you've written. It won't be used for grading.
print()
########################################################################
#Write a class called "Burrito". A Burrito should have the 
#following attributes (instance variables):
#
# - meat
# - to_go
# - rice 
# - beans 
# - extra_meat (default: False)
# - guacamole (default: False)
# - cheese (default: False)
# - pico (default: False)
# - corn (default: False)
#
#The constructor should let any of these attributes be
#changed when the object is instantiated. The attributes
#with a default value should be optional. Both positional
#and keyword attributes should be in the order shown above
#(for the autograder to work).


#Write your code here!
class Burrito:
    def __init__(self, meat, to_go, rice, beans, extra_meat=False, guacamole=False, cheese=False, pico=False, corn=False):
        self.meat = meat
        self.to_go = to_go
        self.rice = rice
        self.beans = beans
        self.extra_meat = extra_meat
        self.guacamole = guacamole
        self.cheese = cheese
        self.pico = pico
        self.corn = corn
    def set_meat(self, new_meat):
        self.meat = new_meat
    def set_to_go(self, new_to_go):
        self.to_go = new_to_go
    def set_rice(self, new_rice):
        self.rice = new_rice
    def set_beans(self, new_beans):
        self.beans = new_beans
    def set_extra_meat(self, new_extra_meat):
        self.extra_meat = new_extra_meat
    def set_guacamole(self, new_guacamole):
        self.guacamole = new_guacamole
    def set_cheese(self, new_cheese):
        self.cheese = new_cheese
    def set_pico(self, new_pico):
        self.pico = new_pico
    def set_corn(self, new_corn):
        self.corn = new_corn
        
        


#The code below will test your class. If it is written
#correctly, this will print True, then False. Note,
#though, that we'll test your code against more complex
#test cases when you submit.
newBurrito = Burrito("Tofu", True, True, True)
print(newBurrito.to_go)
print(newBurrito.guacamole)
print()
#_________________________________________________
class Burrito:
    def __init__(self, meat, to_go, rice, beans, extra_meat = False, guacamole = False, cheese = False, pico = False, corn = False):
        
        self.meat = meat
        self.to_go = to_go
        self.rice = rice
        self.beans = beans
        self.extra_meat = extra_meat
        self.guacamole = guacamole
        self.cheese = cheese
        self.pico = pico
        self.corn = corn



newBurrito = Burrito("Tofu", True, True, True)
print(newBurrito.meat)
print(newBurrito.to_go)
print(newBurrito.guacamole)
print()
########################################################################
#The Fibonacci sequence is a number sequence where each
#number is the sum of the previous two numbers. The first
#two numbers are defined as 0 and 1, so the third number is
#1 (0 + 1 = 1), the fourth number is 2 (1 + 1 = 2), the
#fifth number is 3 (1 + 2 = 3), the sixth number is 5
#(2 + 3 = 5), and so on.
#
#Below we've started a class called FibSeq. At any time,
#FibSeq holds two values from the Fibonacci sequence:
#back1 and back2.
#
#Create a new method inside FibSeq called next_number. The
#next_number method should:
#
# - Calculate and return the next number in the sequence,
#   based on the previous 2.
# - Update back2 with the former value of back1, and update
#   back1 with the new next item in the sequence.
#
#This means that consecutive calls to next_number should
#yield each consecutive number from the Fibonacci sequence.
#Calling next_number 5 times would print 1, 2, 3, 5, and 8.


class FibSeq:
    def __init__(self):
        self.back1 = 1
        self.back2 = 0
        
    def next_number(self):
        new_back1 = self.back1 + self.back2
        new_back2 = self.back1
        self.back1 = new_back1
        self.back2 = new_back2
        return new_back1    
        
        
        

#The code below will test your method. It's not used for
#grading, so feel free to change it. As written, it should
#print 1, 2, 3, 5, and 8.
newFib = FibSeq()
print(newFib.next_number())
print(newFib.next_number())
print(newFib.next_number())
print(newFib.next_number())
print(newFib.next_number())
print()
#______________________________________________________
class FibSeq:
    def __init__(self):
        self.back1 = 1
        self.back2 = 0

    def next_number(self):
        
        next_num = self.back1 + self.back2
        
        self.back2 = self.back1
        
        self.back1 = next_num
        return next_num
        


newFib = FibSeq()
print(newFib.next_number())
print(newFib.next_number())
print(newFib.next_number())
print(newFib.next_number())
print(newFib.next_number())
print()
########################################################################
#Here's a long one -- you can do it!
#
#Rewrite the following class so that it uses getters and
#setters for all three variables (title, description,
#completed). The getters should be called: getTitle,
#getDescription,  getCompleted. The setters should be
#called: setTitle, setDescription, setCompleted.
#
#In addition, the setter should check to make sure that
#the new value is the correct type: title and description
#should always be of type str, and completed should always
#be of type bool. If the value is not the right type, set
#the value of the corresponding attribute to None (the
#keyword, not the string "None").
#
#To summarize (and give a to-do list):
# - Create getters and setters for each variable.
# - Check the type of the new value inside the setters,
#   and print an error if it's the wrong type.
#
#Hint: You can check to see if a variable is a string by
#checking the logical expression type(var) == str, where
#var is the variable you're checking. For integers, use
#int instead of str. For floats, use float. For booleans,
#use bool.
#
#Hint 2: Remember to put self before any instance variables
#or methods you're trying to access. For example, to access
#the variable title from within a method, you would need to
#write self.title.


class TodoItem:
    def __init__(self, title, description, completed=False):
        self.title = title
        self.description = description
        self.completed = completed
    def getTitle(self):
        return self.title
    def getDescription(self):
        return self.description
    def getCompleted(self):
        return self.completed
    
    def setTitle(self, newTitle):
        self.title = newTitle
        if type(self.title) == str:
            self.title = newTitle
        else:
            self.title = None
    def setDescription(self, newDescription):
        self.description = newDescription
        if type(self.description) == str:
            self.description = newDescription
        else:
            self.description = None
    def setCompleted(self, newCompleted):
        self.completed = newCompleted
        if type(self.completed) == bool:
            self.completed = newCompleted
        else:
            self.completed = None
        
        
        
        
        
        
#Below are some lines of code that will test your class.
#You can change this code to test how your class behaves
#with different variables and method calls.
#
#If your class works correctly, this will originally print:
#Mow
#Mow the lawn
#False
#True
#None
item = TodoItem("Mow", "Mow the lawn")
print(item.getTitle())
print(item.getDescription())
print(item.getCompleted())
item.setCompleted(True)
print(item.getCompleted())
item.setTitle(False)
print(item.getTitle())
print()
########################################################################
from math import atan2, degrees, radians, sin, cos

#Last problem, you created a new class called Force. Copy that
#class below:

class Force:
    
    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle
        
    def get_horizontal(self):
        
        
        return self.magnitude * cos(radians(self.angle))
    
    def get_vertical(self):
        
        vertical = self.magnitude * sin(radians(self.angle))
        return vertical
    
    def get_angle(self, use_degrees = True):
        
        if use_degrees:
            return self.angle
        else:
            return radians(self.angle)
    

#In this problem, you're going to use that class to calculate
#the net force from a list of forces.
#
#Write a function called find_net_force. find_net_force should
#have one parameter: a list of instances of Force. The
#function should return new instance of Force with the total
#net magnitude and net angle as the values for its magnitude
#and angle attributes.
#
#As a reminder:
#
# - To find the magnitude of the net force, sum all the
#   horizontal components and sum all the vertical components.
#   The net force is the square root of the sum of the squares
#   of the horizontal forces and the vertical foces (i.e.
#   (total_horizontal ** 2 + total_vertical ** 2) ** 0.5)
# - To find the angle of the net force, call atan2 with two
#   arguments: the total vertical and total horizontal
#   forces (in that order).
# - Remember to round both the magnitude and direction to one
#   decimal place. This can be done using round(magnitude, 1)
#   and round(angle, 1).
# - The Force class has three methods: get_horizontal returns
#   a single force's horizontal component. get_vertical
#   returns a single force's vertical component. get_angle
#   returns a single force's angle in degrees (or in radians
#   if you call get_angle(use_degrees = False).
#
#HINT: Don't overcomplicate this. The Force class does a lot
#of your work for you. Use it! You should not need any trig
#functions except atan2, degrees, and radians.


#Add your function here!
def find_net_force(list_of_forces):
    total_vert = 0
    total_horiz = 0
    
    for item in list_of_forces:
        item = Force(item.magnitude, item.get_angle())
        
        angle = radians(item.angle)
        magnitude = item.magnitude
        
        vertical = magnitude * sin(angle)
        total_vert += vertical
        
        horizontal = magnitude * cos(angle)
        total_horiz += horizontal
        
        total_mag = (total_vert ** 2 + total_horiz ** 2) ** .5
        
        force_rad = atan2(total_vert, total_horiz)
        force_deg = degrees(force_rad)
        
        new_instance = Force(round(total_mag, 1), round(force_deg, 1))
        
    return new_instance
    


#Below are some lines of code that will test your object.
#You can change these lines to test your code in different
#ways.
#
#If your code works correctly, this will originally run
#error-free and print:
#103.1
#-14.0

force_1 = Force(50, 90)
force_2 = Force(75, -90)
force_3 = Force(100, 0)
forces = [force_1, force_2, force_3]
net_force = find_net_force(forces)
print(net_force.magnitude)
print(net_force.get_angle())
print()
#_________________________________________________________
def find_net_force(forces):
    
    total_horizontal = 0
    total_vertical = 0
    
    for force in forces:
        total_horizontal += force.get_horizontal()
        total_vertical += force.get_vertical()
    magnitude = (total_horizontal ** 2 + total_vertical ** 2) **0.5
    angle = degrees(atan2(total_vertical, total_horizontal))
    magnitude = round(magnitude, 1)
    angle = round(angle, 1)
    
    return Force(magnitude, angle)


force_1 = Force(50, 90)
force_2 = Force(75, -90)
force_3 = Force(100, 0)
forces = [force_1, force_2, force_3]
net_force = find_net_force(forces)
print(net_force.magnitude)
print(net_force.get_angle())
print()
########################################################################
#Recall in Coding Problem 4.4.4 (and before that, in Coding
#Problem 4.3.9) you built a program for finding the net
#force (magnitude and angle) on an object from several
#individual forces.
#
#In the next two exercises, we're going to convert that
#system into one that uses objects.
#
#To start, create a class called Force. The constructor for
#Force should have two required arguments: magnitude and
#angle. These should be saved to two attributes called
#'magnitude' and 'angle'. You should assume angle is
#initially in degrees, from -180 to 180.
#
#Then, add three methods to Force:
#
# - get_horizontal should return the horizontal component
#   of the force, according to the formula:
#   horizontal = magnitude * cos(angle).
# - get_vertical should return the vertical component of
#   the force, according to the formula:
#   vertical = magnitude * sin(angle).
# - get_angle should return the angle of the force, but
#   should have a keyword parameter called use_degrees.
#   use_degrees should default to True. If use_degrees
#   is true, it should return the angle in degrees; if it
#   is false, it should return the angle in radians.
#
#HINT: Don't overcomplicate this. All we want here is
#a class called Force with four methods: __init__,
#get_horizontal, get_vertical, and get_angle. Note that
#these are not true "getters" even though they have "get"
#in their names: all three will have some reasoning
#beyond just returning a single value.
#
#HINT 2: angle will initially be passed into the
#constructor in degrees. You may store it in either
#degrees or radians. Each approach has different benefits,
#but make sure to keep track of when it's in angles and
#when it's in degrees.

from math import sin, cos, atan2, radians, degrees, sqrt


#Add your code here!
class Force():
    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle
    def get_horizontal(self):
        horizontal = self.magnitude * cos(radians(self.angle))
        return horizontal
    def get_vertical(self):
        vertical = self.magnitude * sin(radians(self.angle))
        return vertical
    def get_angle(self, use_degrees = True):
        if use_degrees:
            return self.angle
        else:
            return radians(self.angle)


#Below are some lines of code that will test your object.
#You can change these lines to test your code in different
#ways.
#
#If your code works correctly, this will originally run
#error-free and print (with room for rounding errors):
#Magnitude: 500
#Horizontal: 250.0
#Vertical: 433.0127018922193
#Angle in Degrees: 60.0
#Angle in Radians: 1.0471975511965976
a_force = Force(500, 60)
print("Magnitude:", a_force.magnitude)
print("Horizontal:", a_force.get_horizontal())
print("Vertical:", a_force.get_vertical())
print("Angle in Degrees:", a_force.get_angle())
print("Angle in Radians:", a_force.get_angle(use_degrees = False))
print()
#______________________________________________________________
from math import sin, cos, atan2, radians, degrees, sqrt

class Force:
    
    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = radians(angle)
    def get_horizontal(self):
        return self.magnitude * cos(self.angle)
    def get_vertical(self):
        return self.magnitude * sin(self.angle)
    def get_angle(self, use_degrees = True):
        if use_degrees:
            return degrees(self.angle)
        else:
            return self.angle
########################################################################
#In Pokemon Go, a Pokemon is defined by several different
#parameters. For simplicity in this problem, we'll say that
#every Pokemon is defined by two parameters: its name, a
#string, and its power level, an integer.
#
#Create a class called Pokemon. The Pokemon class's
#constructor should have two parameters (in addition to self):
#the Pokemon's name and the Pokemon's power. These should be
#assigned to attributes called 'name' and 'power'.
#
#The Pokemon class should also have a method called
#would_defeat. would_defeat will have one parameter: an
#instance of a _different_ Pokemon. would_defeat should
#return True if this Pokemon's power is greater than the
#other Pokemon's power, or False if not.


#Add your code here!
class Pokemon():
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def would_defeat(self, a_different_Pokemon):
        if self.power > a_different_Pokemon.power:
            return True
        else:
            return False



#Below are some lines of code that will test your object.
#You can change these lines to test your code in different
#ways.
#
#If your code works correctly, this will originally run
#error-free and print:
#Pikachu
#500
#False
#True
new_pokemon_1 = Pokemon("Pikachu", 500)
print(new_pokemon_1.name)
print(new_pokemon_1.power)

new_pokemon_2 = Pokemon("Charizard", 2412)
new_pokemon_3 = Pokemon("Squirtle", 312)
print(new_pokemon_1.would_defeat(new_pokemon_2))
print(new_pokemon_1.would_defeat(new_pokemon_3))
print()
########################################################################
#In many areas, different goods are taxed at different rates.
#Areas may charge higher tax rates for items like alcohol,
#gasoline, and soda, and lower tax rates for items like
#grocery items, medicines, and clothes.
#
#Write a class called PurchasedGood. The constructor for
#PurchasedGood should have one positional parameter called
#price, which is the price of the good as a float. It should
#then have two keyword parameters in this order:
# - category, which is the category the good falls into.
#   category should have a default value of "General".
# - tax, which is the sales tax rate. tax should have a
#   default value of 0.07.
#
#These three values should be stored in attributes called
#'price', 'category', and 'tax'.
#
#Then, add a method called calculate_total. calculate_total
#should calculate the price plus the price times the tax
#rate, then round the result to 2 decimal places and return
#the result. Remember, you can round to two decimal places
#using round(total, 2).


#Add your class here!
class PurchasedGood():
    def __init__(self, price, category = "General", tax = 0.07):
        self.price = price
        self.category = category
        self.tax = tax
    def calculate_total(self):
        total = self.price + (self.tax * self.price)
        return total



#Below are some lines of code that will test your object.
#You can change these lines to test your code in different
#ways.
#
#If your code works correctly, this will originally run
#error-free and print ignoring rounding errors):
#5.0
#General
#0.07
#5.35
#5.0
#Grocery
#0.03
#5.15
good_1 = PurchasedGood(5.00)
print(good_1.price)
print(good_1.category)
print(good_1.tax)
print(good_1.calculate_total())

good_2 = PurchasedGood(5.00, category = "Grocery", tax = 0.03)
print(good_2.price)
print(good_2.category)
print(good_2.tax)
print(good_2.calculate_total())
print()
########################################################################
#Below is a class representing a person. You'll see the
#Person class has three instance variables: name, age,
#and GTID. The constructor currently sets these values
#via a calls to the setters.
#
#Create a new function called same_person. same_person
#should take two instances of Person as arguments, and
#returns True if they are the same Person, False otherwise.
#Two instances of Person are considered to be the same if
#and only if they have the same GTID. It does not matter
#if their names or ages differ as long as they have the
#same GTID.
#
#You should not need to modify the Person class.

class Person:
    def __init__(self, name, age, GTID):
        self.set_name(name)
        self.set_age(age)
        self.set_GTID(GTID)

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_GTID(self, GTID):
        self.GTID = GTID

    def get_name(self):
        return self.name

    def get_age(self):
       return self.age

    def get_GTID(self):
        return self.GTID

#Add your code below!
def same_person(person1, person2):
    if person1.GTID == person2.GTID:
        return True
    else:
        return False



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, then False.
person1 = Person("David Joyner", 30, 901234567)
person2 = Person("D. Joyner", 29, 901234567)
person3 = Person("David Joyner", 30, 903987654)
print(same_person(person1, person2))
print(same_person(person1, person3))
print()
########################################################################
#Below are the two class definitions we supplied previously:
#Artist and Song.
#
#Write a function called "get_song_string". It should accept
#one argument which will be a Song object. It should return
#a string in the following format:
#
# "<song name>" - <artist name> (<song year>)
# e.g: 
# "You Belong With Me" - Taylor Swift (2008)
#
#The quotation marks around the song title should be *part*
#of the string.
#
#Hint: You're writing a function, not a method. That means
#the function get_song_string should not be inside either
#of these classes.

class Artist:
    def __init__(self, name, label):
        self.name = name
        self.label = label

class Song:
    def __init__(self, name, album, year, artist):
        self.name = name
        self.album = album
        self.year = year
        self.artist = artist
def get_song_string(song):
    return '"' + song.name + '"' + " - " + song.artist.name + " " + '(' + str(song.year) + ')'

        
#The code below will test your function. It isn't used for
#grading, so feel free to modify it.
newArtist = Artist("Taylor Swift", "Big Machine Records, LLC")
newSong = Song("You Belong With Me", "Fearless", 2008, newArtist)
print(get_song_string(newSong))
print()
########################################################################
#We've given you a class called "Song" that represents
#some basic information about a song. We also wrote a 
#class called "Artist" which contains some basic 
#information about an artist.
#
#Your job is to create three instances of the song class,
#called song_1, song_2, and song_3.
#
#song_1 should have the following attributes:
#   name = "You Belong With Me"
#   album = "Fearless"
#   year = 2008
#   artist.name = "Taylor Swift"
#   artist.label = "Big Machine Records, LLC"
#
#song_2 should have the following attributes:
#   name = "All Too Well"
#   album = "Red"
#   year = 2012
#   artist.name = "Taylor Swift"
#   artist.label = "Big Machine Records, LLC"
#
#song_3 should have the following attributes:
#   name = "Up We Go"
#   album = "Midnight Machines"
#   year = 2016
#   artist.name = "LIGHTS"
#   artist.label = "Warner Bros. Records Inc."
#
#Notice, though, that song_1 and song_2 have the same
#artist and label. That means they should each have the
#SAME instance of artist: do not create separate instances
#of artist for each song.
#
#When your code is done running, there should exist three
#variables: song_1, song_2, and song_3, according to the
#requirements above.

class Artist:
    def __init__(self, name, label):
        self.name = name
        self.label = label

class Song:
    def __init__(self, name, album, year, artist):
        self.name = name
        self.album = album
        self.year = year
        self.artist = artist
        

#Write your code here!
taylor_swift = Artist("Taylor Swift", "Big Machine Records, LLC")
song_1 = Song("You Belong With Me", "Fearless", 2008, taylor_swift)
song_2 = Song("All Too Well", "Red", 2012, taylor_swift)
song_3 = Song("Up We Go", "Midnight Machines", 2016, Artist("LiGHTS", "Warner Bros. Records Inc."))


#Feel free to add code to test your code below.

#print(song_1.artist.name)
#print(song_2.year)
#print(song_3.name)
print()
########################################################################
#Classes can also have references to other instances of
#themselves. Consider this Person class, for example, 
#that allows for an instance of a father and mother
#to be given in the constructor.
#
#Create 3 instances of this class. The first should have 
#the name "Mr. Burdell" with an age of 53. The second
#instance should have a name of "Mrs. Burdell" with an age
#of 53 as well. Finally, make an instance with the name of
#"George P. Burdell" with an age of 25. This final instance
#should also have the father attribute set to the instance 
#of Mr. Burdell, and the mother attribute set to the 
#instance of Mrs. Burdell. Finally, store the instance of 
#George P. Burdell in a variable called george_p. (It does
#not matter what variable names you use for Mr. and Mrs.
#Burdell.)

class Person:
    def __init__(self, name, age, father=None, mother=None):
        self.name = name
        self.age = age
        self.father = father
        self.mother = mother

#Write your code here!
mr_burdell = Person("Mr. Burdell", 53)
mrs_burdell = Person("Mrs. Burdell", 53)
george_p = Person("George P. Burdell", 25, father = mr_burdell, mother = mrs_burdell)





#The code below will let you test your code. It isn't used
#for grading, so feel free to modify it. As written, it
#should print George P. Burdell, Mrs. Burdell, and Mr.
#Burdell each on a separate line.
print(george_p.name)
print(george_p.mother.name)
print(george_p.father.name)
print()
########################################################################
#Previously, you wrote a class called ExerciseSession that
#had three attributes: an exercise name, an intensity, and a
#duration.
#
#Add a new method to that class called calories_burned.
#calories_burned should have no parameters (besides self, as
#every method in a class has). It should return an integer
#representing the number of calories burned according to the
#following formula:
#
# - If the intensity is "Low", 4 calories are burned per
#   minute.
# - If the intensity is "Moderate", 8 calories are burned
#   per minute.
# - If the intensity is "High", 12 calories are burned per
#   minute.
#
#You may copy your class from the previous exercise and just
#add to it.
class ExerciseSession():
    def __init__(self, exercise, intensity, duration):
        self.exercise = exercise
        self.intensity = intensity
        self.duration = duration
        
    def get_exercise(self): #Getter for excercise name
        return self.exercise
    def get_intensity(self): #Getter for excercise intensity
        return self.intensity
    def get_duration(self): #Getter for excercise duration
        return self.duration
    
    def set_exercise(self, new_exercise): #Setter for excercise name
        self.exercise = new_exercise
    def set_intensity(self, new_intensity): #Setter for excercise intensity
        self.intensity = new_intensity
    def set_duration(self, new_duration): #Setter for excercise duration
        self.duration = new_duration

#Add your code here!
    def calories_burned(self): #Method for calculating calories burned
        if self.intensity == "Low":
            return 4 * self.duration
        elif self.intensity == "Moderate":
            return 8 * self.duration
        elif self.intensity == "High":
            return 12 * self.duration


#If your code is implemented correctly, the lines below
#will run error-free. They will result in the following
#output to the console:
#240
#360
new_exercise = ExerciseSession("Running", "Low", 60)
print(new_exercise.calories_burned())
new_exercise.set_exercise("Swimming")
new_exercise.set_intensity("High")
new_exercise.set_duration(30)
print(new_exercise.calories_burned())
print()
########################################################################
#Imagine you're writing an exercise-tracking app like Fitbit
#or MyFitnessPal. Part of your app is that a user can log an
#exercise session by naming the exercise, the intensity, and
#the duration.
#
#Write a class called ExerciseSession. ExerciseSession
#should have a constructor that requires two strings and an
#integer: the strings represent the exercise name and the
#exercise intensity, which will be "Low", "Moderate", or
#"High". The integer will represent the length of the
#exercise session in minutes. These should be saved in the
#instance of the class.
#
#Then, add three getters to the class. The getters should
#be named get_exercise, get_intensity, and get_duration,
#and should return the exercise string, the exercise
#intensity, and the duration, respectively.
#
#The setters should be named set_exercise, set_intensity,
#and set_duration. Each should have one parameter (besides
#self), which should be stored as the new value of
#exercise, intensity, or duration. You may assume only
#valid values will be passed in.
#
#HINT: You don't have to do any logging like you saw in
#the video! That was just an example of one benefit of
#using getters and setters, but this problem does not ask
#you to do that.


#Add your code here!
class ExerciseSession():
    def __init__(self, exercise, intensity, duration):
        self.exercise = exercise
        self.intensity = intensity
        self.duration = duration
        
    def get_exercise(self): #Getter for excercise name
        return self.exercise
    def get_intensity(self): #Getter for excercise intensity
        return self.intensity
    def get_duration(self): #Getter for excercise duration
        return self.duration
    
    def set_exercise(self, new_exercise): #Setter for excercise name
        self.exercise = new_exercise
    def set_intensity(self, new_intensity): #Setter for excercise intensity
        self.intensity = new_intensity
    def set_duration(self, new_duration): #Setter for excercise duration
        self.duration = new_duration
        
        
    



#If your code is implemented correctly, the lines below
#will run error-free. They will result in the following
#output to the console:
#Running
#Low
#60
#Swimming
#High
#30
new_exercise = ExerciseSession("Running", "Low", 60)
print(new_exercise.get_exercise())
print(new_exercise.get_intensity())
print(new_exercise.get_duration())
new_exercise.set_exercise("Swimming")
new_exercise.set_intensity("High")
new_exercise.set_duration(30)
print(new_exercise.get_exercise())
print(new_exercise.get_intensity())
print(new_exercise.get_duration())
print()
########################################################################
#Rewrite the "Number" class from 5.1.2 Coding Exercise 2.
#This time, however, require arguments for value and
#even in the constructor. Then, inside the constructor,
#create new instance variables called value and even that
#copy the values of the arguments passed into the
#constructor.
#
#In other words, rewrite the Number class such that value
#and even behave the way studentName and enrolled behaved
#in the exercise above, and the way firstname and lastname
#behaved in video 5.1.4.1.
#
#Then, as before, create an instance of this class and
#assign it to a variable called "number_instance". value
#should again be set to 101 and even should be set to
#False.
#
#Hint: Remember, the way you initialize the instance will
#have to change, too, based on the changes to the
#constructor that we're requiring.


#Write your code here!
class Number():
    def __init__(self, value, even):
        self.value = value
        self.even = even
number_instance = Number(101, False)
print(number_instance.value)
print(number_instance.even)


#Note that this exercise does not print anything by
#default. You're welcome to add print statements to debug
#your code when running it. Note that the autograder
#will check both your value for number_instance and your
#definition of the class Number.
print()
########################################################################
#Write a class named "Number" with one attribute called 
#"value" which defaults to 0 and another attribute called 
#"even" which defaults to True.
#
#Next, create an instance of this class and assign it to
#a variable called "number_instance".
#
#Then, set the value attribute to 101 and the even
#attribute to False.


#Write your code here!
class Number:
    def __init__(self):
        self.value = 0
        self.even = True

number_instance = Number()
number_instance.value = 101
number_instance.even = False


#Note that this exercise does not print anything by
#default. You're welcome to add print statements to debug
#your code when running it. Note that the autograder
#will check both your value for number_instance and your
#definition of the class Number.