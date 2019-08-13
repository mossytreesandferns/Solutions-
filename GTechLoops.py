#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 22:56:08 2018

@author: meganporter
"""

mystery_string = "Lucy"

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#There's an easy way to do this exercise, and a hard way. For
#a hint on the easier way, revisit the sample answers for the
#previous coding exercise.
#
#Above we've created a variable called mystery_string. Write
#some code that will print the first letter of the string on
#the first line, the first two letters on the second line,
#the first three letters on the third line, etc., until it
#prints the entire string on the last line.
#
#For example, if the string was "Lucy", then the output would
#be:
#
#L
#Lu
#Luc
#Lucy
#
#Hint: to print without automatically starting a new line,
#include the text end="" inside the print statement's
#parentheses. For example, print("Hello", end="") will print
#the word "Hello" without starting a new line afterward. So,
#calling it twice would print "HelloHello" on one line
#instead of two lines.

length_string = len(mystery_string)
#Add your code here!

for i in range(length_string):
    for j in range(i + 1):
        print(mystery_string[j], end = "")
    print() 

##############################################################################


#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#This is a tough one! Stick with it, you can do it!
#
#Write a program that will print the times table for the
#value given by mystery_int. The times table should print a
#two-column table of the products of every combination of
#two numbers from 1 through mystery_int. Separate consecutive
#numbers with either spaces or tabs, whichever you prefer.
#
#For example, if mystery_int is 5, this could print:
#
#1	2	3	4	5
#2	4	6	8	10
#3	6	9	12	15
#4	8	12	16	20
#5	10	15	20	25
#
#To do this, you'll want to use two nested for loops; the
#first one will print rows, and the second will print columns
#within each row.
#
#Hint: How can you print the numbers across the row without
#starting a new line each time? With what you know now, you
#could build the string for the row, but only print it once
#you've finished the row. There are other ways, but that's
#how to do it using only what we've covered so far.
#
#Hint 2: To insert a tab into a string, use the character
#sequence "\t". For example, "1\t2" will print as "1	2".
#
#Hint 3: Need to just start a new line without printing
#anything else? Just call print() with no arguments in the
#parentheses.
#
#Hint 4: If you're stuck, try first just printing out all
#the products in one flat list, each on its own line. Once
#that's working, then worry about how to organize it into
#a table.

mystery_int = 5

#Add your code here!
for i in range(1, mystery_int + 1):
    print()
    for j in range(1, mystery_int + 1):
        print(i * j, end = " ")
        
for i in range(1, mystery_int + 1):
    row_string = ""
    for j in range(1, mystery_int + 1):
        product = i * j
        row_string += str(product) + "\t"
    print(row_string)
    
print()    
        

##############################################################################

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Recall our earlier problem where you printed out beats based
#on measures and beats per measure (3.3.5 Coding Exercise 1).
#In that exercise, you printing out 1 through the number of beats
#in a measure over and over depending on the number of measures.
#
#Copy and modify your code, but this time, you should replace the
#number 1 with the number of the current measure. So, the first
#number in each measure will always rise.
#
#For example, instead of 1 2 3 4 1 2 3 4 1 2 3 4 (with each
#number on its own line), you'd now print 1 2 3 4 2 2 3 4 3 2 3 4,
#and so on.
#
#You can use our sample answer from that problem if you'd prefer.
#
#HINT: One approach would involve adding a conditional.


#Add your code here! Using the original values of the variables
#above, this will initially print the following numbers (but each
#on their own line):
#1 2 3 4 2 2 3 4 3 2 3 4 4 2 3 4 5 2 3 4
beats_per_measure = 4
measures = 5

i = 0
for i in range (1,measures + 1):
    num_measure = i
    print(num_measure)
    for i in range(2, beats_per_measure + 1):
        print(i)
print()

for measure in range(0, measures):   
    for beat in range(1, beats_per_measure + 1):
        if beat == 1:
            print(measure + 1)
        else:
            print(beat) 
print()            
##############################################################################


#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Print all the letters from start_character to end_character,
#each on their own line. Include start_character and
#end_character themselves.
#
#Remember, you can convert a letter to its underlying ASCII
#number using the ord() function. ord("A") would give 65.
#ord("Z") would give 90. You can use these values to write
#your loop.
#
#You can also convert an integer into its corresponding ASCII
#character using the chr() function. chr(65) would give "A".
#chr(90) would give "Z". So, for this problem, you'll need
#to convert back and forth between ordinal values and
#characters based on whether you're trying to loop over
#numbers or print letters.
#
#You may assume that both start_character and end_character
#are uppercase letters (although you might find it fun to
#play around and see what happens if you put other characters
#in instead!).


#Add your code here! With the original values for
#start_character and end_character, this will print the
#letters from A to Z, each on their own line.
start_character = "A"
end_character = "O"

for i in range(ord(start_character), ord(end_character) + 1):
    print(chr(i))
##############################################################################


#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Use a while loop to create a countdown from mystery_int to
#0. Count down by 3s: if mystery_int is 46, then you should
#print 46, 43, 40, etc. Do not print any number lower than 0.
#Note that you should print both the original value of
#mystery_int and 0 if you land on it exactly.


#Add your code here!

mystery_int = 46

while mystery_int >= 0:
    print(mystery_int)
    mystery_int -= 3
##############################################################################
#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Above is a list of strings. Don't worry if this syntax is a
#little unfamiliar, we'll talk you through it and then cover
#it more in chapter 4.3.
#
#Write some code that will count the number of instances of
#the letter 't' in the list of strings. Count both capital
#'T' and lower-case 't'. Then, print the number of instances
#of the letter 't'.
#
#For example, with the list declared above, you would print
#6: two in the first string, three in the second, one in the
#third.
#
#Because we haven't used lists very extensively, we've
#gotten you started. The loop below will iterate through each
#string in the list. Next, you want to iterate through each
#letter in the current string, check if it's a t, and
#increment a counter if so.

mystery_list = ["Taylor Swift", "Twenty Two", "Georgia Tech"]
#You'll want to add some code before the loop here.
count = 0

for string in mystery_list:
    #Add your code to read through the string and count the
    #t's and T's here!
    for letter in string:
        if letter == 'T' or letter == 't':
            count += 1

print(count)
print()
##############################################################################
#-----------------------------------------------------------
#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Write some code below that will count and print how many
#times mystery_character appears in mystery_string. You may
#not use the string class's .count method.
#
#With the original values for mystery_string and
#mystery_character, your code should initially print 4. Only
#count characters with the same case as mystery_character
#(in other words, here you would ignore capital A).

mystery_string = "Hello! What a fine day it is today."
mystery_character = "o"

#Add your code here!

count = 0

for i in mystery_string:
    if i == mystery_character:
        count += 1
print(count)


##############################################################################
#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Use a loop to find the sum of all numbers between 0 and
#mystery_int, including bounds (meaning that if
#mystery_int = 7, you add 0 + 1 + 2 + 3 + 4 + 5 + 6 + 7).
#
#However, there's a twist: mystery_int might be negative.
#So, if mystery_int was -4, you would -4 + -3 + -2 + -1 + 0.
#
#There are a lot of different ways you can do this. Most of
#them will involve using a conditional to decide whether to
#add or subtract 1 from mystery_int.
#
#You may use either a for loopor a while loop to solve this,
#although we recommend using a while loop.


#Add your code here!
mystery_int = -7

sum = 0

if mystery_int >= 0:
    for i in range(0, mystery_int + 1):
        sum += i
    print(sum)
elif mystery_int < 0:  
    for i in range(mystery_int, 0):
        sum += i
    print(sum)
    
current_sum = 0
if mystery_int > 0:
    while mystery_int > 0:
        current_sum += mystery_int
        mystery_int -= 1
else:
    while mystery_int < 0:
        current_sum += mystery_int
        mystery_int += 1
print(current_sum)



current_sum = 0
if mystery_int > 0:
    for i in range(0, mystery_int + 1):
        current_sum += i
else:
    for i in range(mystery_int, 0):
        current_sum += i
print(current_sum)


current_sum = 0
if mystery_int > 0:
    for i in range(0, mystery_int + 1):
        current_sum += i
else:
    for i in range(0, mystery_int - 1, -1):
        current_sum += i
print(current_sum) 
 

current_sum = 0
while not mystery_int == 0:
    
    current_sum += mystery_int
    
    
    if mystery_int < 0:
        mystery_int += 1
    else:
        mystery_int -= 1
print(current_sum)



if mystery_int < 0:
    change = 1
else:
    change = -1

current_sum = 0
while not mystery_int == 0:
    current_sum += mystery_int
    mystery_int += change
print(current_sum) 


if mystery_int < 0:
    change = -1
else:
    change = 1



current_sum = 0
for i in range(0, mystery_int + change, change):
    current_sum += i
print(current_sum)

current_sum = 0
while not mystery_int == 0:
    current_sum += mystery_int
    mystery_int -= mystery_int // abs(mystery_int)
print(current_sum)

print()
##############################################################################
#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Add some code below that will find and print the sum of
#every odd number between 0 and mystery_int. This time,
#exclude the bounds (e.g. if mystery_int was 51, add the odds
#from 1 to 49, but not 51).
#
#Hint: There are multiple ways to do this!
mystery_int = 25

sum = 0

#Add your code here!
for i in range(1, mystery_int, 2):
    sum += i
print(sum)
#____________________________________________________-
current_sum = 0
for i in range(1, mystery_int, 2):
    current_sum += i
print(current_sum)


#Here's the solution using the modulus operator:

current_sum = 0
for i in range(1, mystery_int):
    if i % 2 == 1:
        current_sum += i
print(current_sum)
    
print()
##############################################################################

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Write a for loop that prints every third number from 1 to
#mystery_int inclusive (meaning that if mystery_int is 7, it
#prints 1, 4, and 7). Print each number on a separate line.
#
#Hint: There are multiple ways to do this! You might use the
#modulus operators, or you could use the third argument for
#range().

mystery_int = 7

i = 1

#Add your code here!
for i in range(1, mystery_int + 1, 3):
    print(i)
for i in range(1, mystery_int + 1):
    if i % 3 == 1:
        print(i)
        
print()
##############################################################################        
#Runs this loop 20 times
for i in range(1, 21):  
    #Checks if i is even
    if i % 2 == 0:  
        #Skips the rest of the code block if so
        continue
    #Prints that i is odd
    print(i, "is odd.")  
print("Done!")

##############################################################################
#Creates listOfStrings and assigns it a list of strings each with 
#multiple words
listOfStrings = ["This is the first string", "This is the second string",
                 "This is the third string", "This is the fourth string",
                 "This is the fifth string"]
numSpaces = 0
#Loops over each string in listOfStrings
for currentString in listOfStrings: 
    #Loops over each character in currentString
    for currentCharacter in currentString:  
        #Checks if the current character is a space
        if currentCharacter == " ": 
            numSpaces += 1

numWords = numSpaces + len(listOfStrings)  
print("There are", numWords, "words in these strings.")

##############################################################################
#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#In music, a song's time signature is given in terms of beats
#per measure. A common time signature is 4 beats per measure:
#for every measure of music, a conductor might count from 1
#to 4 with the tempo of the music.
#
#A song then has a number of measures. For example, a short
#song might have only 5 measures. In which case, a conductor
#would count from 1 to 4 five times. If the time signature had
#instead been 3 beats per measure, she would could from 1 to 3
#five times instead.
#
#Write a nested for loop that will print out the beats of the
#piece of music. For example, if the song had 4 beats per
#measure and only 2 measures, this would print out:
#
#1
#2
#3
#4
#1
#2
#3
#4
#
#We print from 1 to 4 before starting over because there are
#4 beats per measure, and we print them all twice because there
#are two measures.


#Add your code here! Using the original values of the variables
#above, this will initially print 1 through 4 five times for a
#total of 20 lines.
beats_per_measure = 3
measures = 5

i = 0

for i in range (1,measures + 1):
    for i in range(1, beats_per_measure + 1):
        print(i)

print()
##############################################################################
        
count = 0
for x in range(3):
    for x in range(3):
        count = count + x
print(count)

print()
##############################################################################
list1 = ["Alison", "Mina", "Leticia", "Elaine", "Sonny", "Benito"]
list2 = ["Yuri", "Andrew", "Mina", "Elaine", "Charles", "Alison"]
for name1 in list1:
    for name2 in list2:
        if name1 == name2:
            print(name1)
print()
###############################################################################

#Imagine if we wanted to print the times tables for the numbers 1
#through 10. In other words, we want to multiply 1 times every number
#from 1 to 10, 2 by every number from 1 through 20, etc. How would we
#do that?
#
#Well, let's look at the phrasing: for every number from 1 to 10, we
#want to multiply it by every number from 1 to 10. Notice the word
#'every' is twice in that description. 'Every' is one of those words
#that gives away the need for a loop. So, it sounds like we're going
#to need two loops! Note also that the second loop is running through
#the numbers 1 to 10 for every number in the first loop.
#
#So, what would this look like?

print("First Example:")

#For every number from 1 to 10...
for i in range(1, 11):
    #For every number from 1 to 10...
    for j in range(1, 11):
        #Print the product of the two numbers.
        print(i, "times", j, "equals", i*j)
        
#Notice that the loop on line 18 is controlled by the loop on line 16.
#So, each iteration of the loop on line 16, the loop on line 18 runs
#10 times.
#
#That's an ugly flat list, though. What if we wanted to print them more
#like an actual table? We can do that! We just have to make use of a
#trick we haven't quite learned... you'll do that later!
print()

###############################################################################

num = 6

result = 1
for i in range(1, num):
    #print(i, result)
    result *= i
print(result)

result = 1
for i in range(1, num + 1):
    #print(i, result)
    result *= i
print(result)

print()

###############################################################################
#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Above are three values. Run a while loop until all three
#values are less than or equal to 0. Every time you change
#the value of the three variables, print out their new values
#all on the same line, separated by single spaces. For
#example, if their values were 3, 4, and 5 respectively, your
#code would print:
#
#2 3 4
#1 2 3
#0 1 2
#-1 0 1
#-2 -1 0


#Add your code here!

mystery_int_1 = 3
mystery_int_2 = 4
mystery_int_3 = 5

while mystery_int_1 > 0 or mystery_int_2 > 0 or mystery_int_3 > 0:
    mystery_int_1 -= 1
    mystery_int_2 -= 1
    mystery_int_3 -= 1
    print(mystery_int_1, mystery_int_2, mystery_int_3)
    
print()    

###############################################################################
mystery_value = 87

while mystery_value <= 100:
    mystery_value += 9
    print(mystery_value)

while not mystery_value > 100:
    mystery_value += 9
    print(mystery_value)
    
print()
###############################################################################
#Write a for-each loop that lists each character in
#mystery_string with its index. For example, if the string
#was "abc", the output would be:
#0 a
#1 b
#2 c
#
#Note that the first item is #0, the second is #1, and so
#on! We'll talk about why that is in Unit 4.
#
#Hint: You'll need a separate variable to keep track of how
#many letters you've printed! You may not use the range
#function on this problem.

mystery_string = "CS1301"


index = -1               

for i in mystery_string:
    index += 1
    print(index, i)
    
count = 0
for letter in mystery_string:
    print(count, letter)
    count += 1    


i = 0
for letter in mystery_string:
    print(index, letter)
    i += 1


for i in range(0, len(mystery_string)):
    print(i, mystery_string[i])

print()
##################################################################################

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







