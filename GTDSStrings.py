#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 09:13:23 2018

@author: meganporter
"""

############################################################################
#Write a function called "replace_all" that accepts three 
#arguments:
#
# - target_string, a string in which to search.
# - find_string, a string to search for.
# - replace_string, a string to use to replace every instance
#   of the value of find.
#
#The arguments will be provided in this order. Your function
#should mimic the behavior of "replace", but you cannot use
#that function in your implementation. Instead, you should
#find the result using a combination of split() and join(),
#or some other method.
#
#Hint: This exercise can be complicated, but it can also
#be done in a single short line of code! Think carefully about
#the methods we've covered.


#Write your function here!
def replace_all(target, find, replace):
    return target.replace(find, replace)



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: "In case I don't see ya, bad afternoon, bad evening,
#and bad night!"
target = "In case I don't see ya, good afternoon, good evening, and good night!"
find = "good"
replace = "bad"
print(replace_all(target, find, replace))
print()

#############################################################################
#Write a function called after_second that accepts two 
#arguments: a target string to search, and string to search
#for. The  function should return everything in the first
#string *after* the *second* occurrence of the search term.
#You can assume  there will always be at least two
#occurrences of the search term in the first string. 
#
#For example:
#  after_second("11223344554321", "3") -> 44554321
#
#The search term "3" appears at indices 4 and 5. So, this
#returns everything from the index 6 to the end.
#
#  after_second("heyyoheyhi!", "hey") -> hi!
#
#The search term "hey" appears at indices 0 and 5. The
#search term itself is three characters. So, this returns
#everything from the index 8 to the end.
#
#Hint: This may be more complicated than it looks! You'll
#have to look at the length of the search string and
#either modify the target string or take advantage of the
#extra arguments you can pass to find().


#Write your function here!
def after_second(target, search):
    location1 = target.find(search)
    location2 = target.find(search, location1 + 1)
    return target[location2 + len(search):]


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print 44554321 and hi!, each on their own line.
print(after_second("11223344554321", "3"))
print(after_second("heyyoheyhi!", "hey"))
print()
#_____________________________________________
#And here's a solution in a single line:

def after_second(target, search):
	return target[target.find(search, target.find(search) + len(search)) + len(search):]

#Don't fret if that's hard to follow! Try parsing it from the outside in. At
#the top level, we're returning a substring of search. At the end, we see a
#colon, then a bracket, so almost the entire line is calculating where to
#start the substring.
#
#Within that, we're adding two things: the result of a call to target.find(),
#and the result of a call to len(). The complexity is in the call to
#target.find().
#
#Within target.find(), we're searching for the search term, starting at
#the index given by target.find(search) + len(search). That itself gives
#the first location of search, so this is giving the second location of
#search.
#
#Sure enough, this method is what you get if you just copy/paste the
#different parts of sample_answer_1.py into the variables into which
print()

#############################################################################
#This one is a challenge. There's a lot going on: splitting
#up strings, removing unnecessary characters, converting to
#integers, and running a big conditional. Our solution to
#this is 34 lines -- you can do it!
#
#In web development, it is common to represent a color like 
#this:
#
#  rgb(red_val, green_val, blue_val)
#
#where red_val, green_val and blue_val would be substituted 
#with values from 0-255 telling the computer how much to 
#light up that portion of the pixel. For example:
#
# - rgb(255, 0, 0) would make a color red. 
# - rgb(255, 255, 0) would make yellow, because it is equal 
#   parts red and green. 
# - rgb(0, 0, 0) would make black, the absence of all color.
# - rgb(255, 255, 255) would make white, the presence of all
#   colors equally.
#
#Don't let the function-like syntax here confuse you: here,
#these are just strings. The string "rgb(0, 255, 0)"
#represents the color green.
#
#Write a function called "find_color" that accepts a single 
#argument expected to be a string as just described. Your
#function should return a simplified version of the color
#that is represented according to the following rules:
#
# If there is more red than any other color, return "red".
# If there is more green than any other color, return "green".
# If there is more blue than any other color, return "blue".
# If there are equal parts red and green, return "yellow".
# If there are equal parts red and blue, return "purple".
# If there are equal parts green and blue, return "teal".
# If there are equal parts red, green, and blue, return "gray".
# (even though this might be white or black).


#Write your function here!
def find_color(string):
    str1 = string.replace("(", "")
    str2 = str1.replace(")", "")
    str3 = str2.replace("rgb", "")
    strf = str3.split(",")
    int0 = int(strf[0])
    int1 = int(strf[1])
    int2 = int(strf[2])
    if int0 > int1 and int0 > int2:
        return "red"
    elif int1 > int2 and int1 > int0:
        return "green"
    elif int2 > int0 and int2 > int1:
        return "blue"
    elif int0 == int1 and not int0 == int2:
        return "yellow"
    elif int0 == int2 and not int0 == int1:
        return "purple"
    elif int1 == int2 and not int1 == int0 :
        return "teal"
    elif int0 == int1 and int0 == int2:
        return "gray"



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: red, purple, gray, each on their own line.
print(find_color("rgb(125, 50, 75)"))
print(find_color("rgb(125, 17, 125)"))
print(find_color("rgb(2, 55, 55)"))
print()
#___________________________________________

def find_color(color_string):
    
    color_string = color_string[4:-1]
    
    #Now, color_string is a string with three numbers
    #separated by two commas. So, we can split by
    #commas...
    
    cs_split = color_string.split(",")
    
    #And now, strings for red, green, and blue are the
    #first, second, and third items in the list:
    
    red, green, blue = int(cs_split[0]), int(cs_split[1]), int(cs_split[2])
    
    #And that's all! split() gave us a list of three
    #strings, and we can access each item in that
    #list using the same syntax we use to access
    #individual characters from a string: cs_split[0]
    #gave the first string, cs_split[1] gave the second,
    #and so on.
    
    if red > green and red > blue:
        return "red"
    elif green > red and green > blue:
        return "green"
    elif blue > green and blue > red:
        return "blue"
    elif red == green and red == blue:
        return "gray"
    elif red == green:
        return "yellow"
    elif red == blue:
        return "purple"
    elif green == blue:
        return "teal"
#############################################################################
#Write a function called string_finder. string_finder should
#take two parameters: a target string and a search string.
#The function will look for the search string within the
#target string.
#
#The function should return a string representing where in
#the target string the search string was found:
#
# - If search string is at the very beginning of target
#   string, then return "Beginning". For example:
#   string_finder("Georgia Tech", "Georgia") -> "Beginning"
#
# - If search string is at the very end of target string,
#   then return "End". For example:
#   string_finder("Georgia Tech", "Tech") -> "End"
#
# - If search string is in target string but not at the
#   very beginning or very end, then return "Middle. For
#   example:
#   string_finder("Georgia Tech", "gia") -> "Middle"
#
# - If search string is not in target string at all, then
#   return "Not found". For example:
#   string_finder("Georgia Tech", "Idaho") -> "Not found"
#
#Assume that we're only interested in the first instance
#of the search string if it appears multiple times in the
#target string, and that search string is definitely
#shorter than target string.
#
#Hint: Don't be surprised if you find that the "End" case
#is the toughest! You'll need to look at the lengths of
#both the target string and the search string.


#Write your function here!
def string_finder(target_string, search_string):
    end = len(target_string)
    index = target_string.find(search_string)
    if index == 0:
        return "Beginning"
    elif 0 < index < end and str(target_string[-1]) != str(search_string[-1]):
        return "Middle"
    elif 0 < index < end and str(target_string[-1]) == str(search_string[-1]):
        return "End"
    elif search_string not in target_string:
        return "Not found"

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: Start, Middle, End, Not found, each on their own
#line.
print(string_finder("Georgia Tech", "Georgia"))
print(string_finder("Georgia Tech", "gia"))
print(string_finder("Georgia Tech", "Tech"))
print(string_finder("Georgia Tech", "Idaho"))
print()

#________________________________________________

def string_finder(target, search):
    
    #Next, the best thing to do would be to go ahead and get
    #and store the index where search is found within
    #target. That's more efficient than calling find() a
    #bunch of times:
    
    index = target.find(search)
    
    #Now based on that index, we can decide where search
    #was found within target. First, find() returns -1 if
    #the string is not found, so if index is less than 0,
    #we can say "Not found":
    
    if index < 0:
        return "Not found"
    
    #Next, 0 is the index for the beginning of the string.
    #So, if index is 0, then search is at the beginning of
    #target:
    
    elif index == 0:
        return "Beginning"
    
    #Now things get trickier. For the search string to be
    #at the end of the target string, it has to be found
    #at an index earlier than the length of the target
    #string. Specifically, it has to be its own length
    #away from the end of the target string. So, we can
    #find that by subtracting the length of the search
    #string from the length of the target string.
    #
    #For example, "Georgia Tech" has 12 characters, and
    #"Tech" has 4 characters. For "Tech" to occur at the
    #end of "Georgia Tech", it must start at index 8,
    #which puts the locations of its characters at
    #indices 8, 9, 10, and 11 (which are the last four
    #indices of a 12-character string since Python is
    #0-indexed).
    
    elif index == len(target) - len(search):
        return "End"
    
    #Finally, the above conditions rule out everything
    #except search being in the middle of target. So,
    #we can return "Middle" if we reach here:
    
    else:
        return "Middle"


print(string_finder("Georgia Tech", "Georgia"))
print(string_finder("Georgia Tech", "gia"))
print(string_finder("Georgia Tech", "Tech"))
print(string_finder("Georgia Tech", "Idaho"))
print()
#############################################################################
#Write a function called "quote_this" that accepts two 
#strings as arguments: a string representing a quote and
#a string of a name. The function should return a new
#string with the quote surrounded by quotation marks (")
#followed by a dash and the given name. For example:
#
#a = quote_this("Try and fail, but never fail to try.",
#"Jared Leto")
#print(a) 
#
#Will print:
#"Try and fail, but never fail to try." -Jared Leto
#
#If the code were to continue, this:
#
#b = quote_this(a, "Michael Scott")
#print(b)
#
#Would print:
#""Try and fail, but never fail to try." -Jared Leto"
#- Michael Scott


#Write your function here!
def quote_this(string1, string2):
    
    return '"' + string1 + '"' + " -" + string2

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print the same output as the examples above.
a = quote_this("Try and fail, but never fail to try.", "Jared Leto")
print(a) 
b = quote_this(a, "Michael Scott")
print(b)
print()


#############################################################################
#Recall that input from a user is always in the form of a string. 
#Write a function called "input_type" that gets user input and 
#determines what kind of string the user entered. The user input
#will be supplied as an argument to the function like normal.
#
#  - Your function should return "integer" if the string only
#    contains characters 0-9.
#  - Your function should return "float" if the string only
#    contains the numbers 0-9 and at most one period.
#  - You should return "boolean" if the user enters "True" or
#    "False". 
#  - Otherwise, you should return "string".


#Write your function here!
def input_type(string):
    chars = "zxcvbnmasdfghjklqwertyuiopZXCVBNMASDFGHJKLQWERTYUIOP,/;'[]\=-<>?:\"{}|+_)(*&^%$#@!~`"
    num = "1234567890." 
    if "." in string:
        for i in string:
            if i not in chars:
                return "float"
    elif string.isdigit():
        return "integer"
    elif string == "True" or string == "False":
        return "boolean"
    else:
        return "string"
    


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#string
#boolean
#float
#integer
print(input_type(""))
print(input_type("False"))
print(input_type("7.432621"))
print(input_type("2788"))
print()
#_______________________________

#Remember, user_input is always a string initially, so we
#can't use the type() function. Instead, we should first
#check to see if it's either the string "True" or the string
#"False". If not, we should try to cast it as an integer,
#and return "integer" if we can. If we can't, we should
#try to cast it as a float and return "float" if we can.
#If it wasn't "True" or "False", can't be cast as an integer,
#and can't be cast as a float, then it's just a regular
#string.

def input_type(user_input):
    if user_input == "True" or user_input == "False":
        return "boolean"

    #Notice that we didn't use an else here. The only way
    #the next line is reachable is if line 13 didn't run,
    #so we don't need an else.
    
    try:
        int(user_input)
        
        #If user_input is not a string representing an
        #integer, then line 20 above will cause an error.
        #So, line 27 will only be reached if user_input
        #is a string holding an error.
        
        return "integer"
    
    except:
        
        #We can only reach this point if user_input was
        #neither "True" or "False" and if it caused an
        #error when casting to an integer. So, we try
        #to cast it to a float:
        
        try:
            float(user_input)
            
            #Return "float" if the above operation didn't
            #cause an error:
            
            return "float"
        
        except:
            
            #And return "string" if it did:
            
            return "string"



print(input_type(""))
print(input_type("False"))
print(input_type("7.432621"))
print(input_type("2788"))
print()
#############################################################################
#Write a function called 'string_type' which accepts one
#string argument and determines what type of string it is. 
#
# - If the string is empty, return "empty".
# - If the string is a single character, return "character".
# - If the string represents a single word, return "word".
#   The string is a single word if it has no spaces.
# - If the string is a whole sentence, return "sentence".
#   The string is a sentence if it contains spaces, but
#   at most one period.
# - If the string is a paragraph, return "paragraph". The
#   string is a paragraph if it contains both spaces and
#   multiple periods (we won't worry about other
#   punctuation marks).
# - If the string is multiple paragraphs, return "page".
#   The string is a paragraph if it contains any newline
#   characters ("\n").
#
#Hint: think carefully about what order you should check
#these conditions in.
#
#Hint 2: remember, there exists a count() method that
#counts the number of times a string appears in another
#string. For example, "blah blah blah".count("blah")
#would return 3.


#Write your function here!
def string_type(string):
    if len(string) > 1:
        if "\n" in string:
            return "page"
        elif string.count(".") > 1:
            return "paragraph"
        elif string.count(" ") > 1:
            return "sentence"
        elif " " not in string:
            return "word"
    elif len(string) == 1:
        return "character"
    elif string == "":
        return "empty"



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#empty
#character
#word
#sentence
#paragraph
#page
print(string_type(""))
print(string_type("!"))
print(string_type("CS1301."))
print(string_type("This is too many cases!"))
print(string_type("There's way too many ostriches. Why are there so many ostriches. The brochure said there'd only be a few ostriches."))
print(string_type("Paragraphs need to have multiple sentences. It's true.\nHowever, two is enough. Yes, two sentences can make a paragraph."))
print()
#____________________________________________________
#This problem is made easier by testing the string types in
#generally descending order. It's easy, for instance, to
#check for a page because if "\n" is in the string, the
#string is a page no matter what else. Similarly, if there
#are more than one period and a space, then it's a paragraph
#no matter what. Then, if there's a space, then it's a
#sentence as long as neither of the earlier cases were True.
#
#Then, the "character" and "empty" conditions are easy to
#test (length is 1 or 0, respectively). If none of those
#conditions are true, then we have a string greater than
#length 2 with no spaces, so it must be a word!

def string_type(input_string):
    
    if "\n" in input_string:
        return "page"
    
    elif input_string.count(".") > 1 and " " in input_string:
        return "paragraph"
    
    elif " " in input_string:
        return "sentence"
    
    elif len(input_string) == 0:
        return "empty"
    
    elif len(input_string) == 1:
        return "character"
    
    else:
        return "word"
print()    
#############################################################################
#Write a function called "in_parentheses" that accepts a 
#single argument, a string representing a sentence that
#contains some words in parentheses. Your function should
#return the contents of the parentheses.
#
#For example:
#
# in_parentheses("This is a sentence (words!)") -> "words!"
#
#If no text appears in parentheses, return an empty string.
#Note that there are several edge cases introduced by this:
#all of the following function calls would return an empty
#string:
#
# in_parentheses("No parentheses")
# in_parentheses("Open ( only")
# in_parentheses("Closed ) only")
# in_parentheses("Closed ) before ( open")
#
#You may assume, however, that there will not be multiple
#open or closed parentheses.


#Write your function here!
def in_parentheses(string):
    lpar = string.find("(")
    rpar = string.find(")")
    if "(" in string and ")" in string:
        return string[lpar + 1: rpar]
    else:
        return "O"
    
    



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print (including the blank lines):
#words!
#
#as he is doing right now
#
#
#!

print(in_parentheses("This is a sentence (words!)."))
print(in_parentheses("No parentheses here!"))
print(in_parentheses("David tends to use parentheses a lot (as he is doing right now). It tends to be quite annoying."))
print(in_parentheses("Open ( only"))
print(in_parentheses("Closed ) only"))
print(in_parentheses("Closed ) before ( open"))
print(in_parentheses("That's a lot of test cases(!)"))
print()
#______________________
 

def in_parentheses(sentence):
 
    if "(" in sentence and ")" in sentence:

        if sentence.find("(") < sentence.find(")"):
 
            return sentence[sentence.find("(") : sentence.find(")")]

    return ""

def in_parentheses(sentence):
    try:
        return sentence[sentence.index("(") + 1:sentence.index(")")]
    except ValueError:
        return ""
print(in_parentheses("This is a sentence (words!)."))
print(in_parentheses("No parentheses here!"))
print(in_parentheses("David tends to use parentheses a lot (as he is doing right now). It tends to be quite annoying."))
print(in_parentheses("Open ( only"))
print(in_parentheses("Closed ) only"))
print(in_parentheses("Closed ) before ( open"))
print(in_parentheses("That's a lot of test cases(!)"))
#############################################################################
#Write a function called "num_changer" that accepts a string 
#of digits (0-9). You should make an integer from the digits 
#of the even indices and another number from the digits in 
#the odd indices. Return the sum of these two numbers. You 
#can assume the given string will have a length of at least 
#2 digits.
#
#For example, if the string was "123456", you would split
#this into two integers, 135 and 246. Adding them would give
#381. Or if the string was "13579", you would split this into
#159 and 37, then add them to get 196.
#
#Hint: You can do this with loops, but it's easier to do
#this with string slicing. Remember how we could pass a third
#argument to range() that would tell range how many numbers
#to skip? You can do something similar with string slices: if
#you include second colon in a string slice, the number
#that follows it lets you skip characters in the string. For
#example:
#
# "Hello, world!"[1:9] -> This gives "ello, wo".
# "Hello, world!"[1:9:2] -> This gives "el,w". Including :2
#    in the string slice skips every other letter. 
# "Hello, world!" [::3] -> This gives "Hl r!". Leaving the
#    first two spots blank tells it to look at the entire
#    string, but putting :3 at the end says to only take
#    every third character (H, l, space, r, and !).
#
#Hint 2: Remember, Python is zero-indexed. That means the
#first number in the string is at position 0, and so it goes
#in the even list.


#Write your function here!
def num_changer(int_string):
    even = int_string[0::2]
    odd = int_string[1::2]
    return int(even) + int(odd)
    
    


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 123456 -> 381
string_int = "123456"
result = num_changer(string_int)
print(string_int + " -> " + str(result))
print()
#___________________________________
def num_changer(digits):
    
    #Next, we'll run a loop over each character in digits
    #and assign it to either even_digits or odd_digits
    #depending on its index. That means, though, that we
    #first must create the strings even_digits and
    #odd_digits to add to:
    
    even_digits = ""
    odd_digits = ""
    
    for i in range(0, len(digits)):
        
        if i % 2 == 0:
            
            
            
            even_digits += digits[i]
            
        else:
            
            odd_digits += digits[i]
    return int(even_digits) + int(odd_digits)
print()

#############################################################################
#Write function called third_character that accepts a
#string as an argument and returns the third character
#of the string. If the user inputs a string with fewer than
#3 characters, return "Too short". 


#Write your function here!
def third_character(string):
    if len(string) >= 3:
        return string[2]
    else:
        return "Too short"


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 1, o, and "Too short", each on a different line.
print(third_character("CS1301"))
print(third_character("Georgia Tech"))
print(third_character("GT"))
print()
#___________________________________
def third_character(input_string):
    if len(input_string) > 2:
        return input_string[2]
    else:
        return "Too short"
    
    
#Or, we can try to return the third character, and catch
#the error that may arise:

def third_character(input_string):
    try:
        return input_string[2]
    except TypeError:
        return "Too short"
print()    
#############################################################################
def valid_char(char):
    if ord(char) in range(33, 127):
        return True
    else:
        return False
       


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, False, True, False

print(valid_char("a"))
print(valid_char(" "))
print(valid_char("!"))
print(valid_char("☺"))
print()

#_____________________________________________

#On asciitable.com, we find that the valid characters all
#have ordinals from 33 (!) to 126 (~). So, we want to check
#whether the ordinal for character falls between 33 and 126:

def valid_char(character):
    return 33 <= ord(character) <= 126

#We could also check if character is between "!" and "~",
#but that looks a little strange since there's no obvious
#'alphabetical order' behind punctuation marks.


print(valid_char("a"))
print(valid_char(" "))
print(valid_char("!"))
print(valid_char("☺"))
print()
#############################################################################
#Recall in Unit 3 you wrote a function that would count the
#number of words in a string using loops. Now that you know
#something about string methods, though, let's do that again
#using a different approach.
#
#Write a function called "num_words" that accepts a string 
#as an argument and returns the number of words in the 
#string. You can assume all words are separated by a space,
#and that the string has at least one word. You do not need
#to worry about punctuation.
#
#For example:
#
#  num_words("Veni, Vidi, Vici.") -> 3
#
#This time, you may not use any loops. Hint: split() might
#come in handy.


#Write your function here!
def num_words(string):
    num = string.split(" ")
    return len(num)
     


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 3, 2, 1, each on their own line.
print(num_words("Vini, Vidi, Vici."))
print(num_words("Hello, world!"))
print(num_words("HeyDavidwhyaren'ttherespacesinthissentence"))
print()

def num_words(sentence):
    
    #Using what we know now, we might see that the split()
    #method can help us here! The split() method splits the
    #string into a list of smaller strings, dividing it
    #wherever the string that appears in parentheses is
    #found. So, "two words".split(" ") would split into a
    #list of two strings: "two" and "words".
    #
    #So, however many strings come out of the split(" ")
    #call is the number of words in our sentence:
    
    return len(sentence.split(" "))
    
    #Given the assumption in the problem that spaces always
    #indicate a new word, we could also use the string
    #class's count() method. The count() method counts
    #the number of instances of the string in parentheses.
    #We'll want to add one because there is always one more
    #word than spaces:
    #
    #return sentence.count(" ") + 1
    

print(num_words("Vini, Vidi, Vici."))
print(num_words("Hello, world!"))
print(num_words("HeyDavidwhyaren'ttherespacesinthissentence"))
print()
#############################################################################
myString = "ABCDEABCDEABCDE"

#Prints the first index of "CDE" in myString
print(myString.find("CDE")) 
#Prints the first index of "CDE" in myString after 5
print(myString.find("CDE", 5)) 
#Prints the first index of "CDE" in myString after 8
print(myString.find("CDE", 13)) 
#Prints the first index of "CDE" in myString between 4 and 10
print(myString.find("CDE", 4, 10)) 
#Prints the first index of "CDE" in myString between 3 and 6
print(myString.find("CDE", 3, 6))
print()


#Write a function called fancy_find. fancy_find should have
#two parameters: search_within and search_for.
#
#fancy_find should check if search_for is found within the
#string search_within. If it is, it should print the message
#"[search_for] found at index [index]!", with [search_for]
#and [index] replaced by the value of search_for and the
#index at which it is found. If search_for is not found
#within search_within, it should print, "[search_for] was
#not found within [search_within]!", again with the values
#of search_for and search_within.
#
#For example:
#
#  fancy_find("ABCDEF", "DEF") -> "DEF found at index 3!"
#  fancy_find("ABCDEF", "GHI") -> "GHI was not found within ABCDEF!"


#Add your function here!
def fancy_find(search_within, search_for):
    if search_within.find(search_for) >= 0:
        return search_for + " found at index " + str(search_within.find(search_for)) + "!"
    else:
        return search_for + " was not found within " + search_within + "!"


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#DEF found at index 3!
#GHI was not found within ABCDEF!

print(fancy_find("ABCDEF", "DEF"))
print(fancy_find("ABCDEF", "GHI"))
print()

def fancy_find(search_within, search_for):
    
    #Now, there are two ways we could do this. We could use
    #the in operator to check if search_for is within
    #search_within, and if it is, then find its index.
    #
    #However, the find() method will return -1 if search_for
    #is not found in search_within anyway, and that's all
    #we need for our conditional. So, first we use the
    #find() method and save the index:
    
    index = search_within.find(search_for)
    
    #If search_for was found, that means index will be a
    #positive number. So, if it's a number greater than or
    #equal to 0...
    
    if index >= 0:
        
        #...then we return that the string was found! Because
        #index is an integer, we need to convert it to a
        #string to concatenate it with the other strings:
        
        return search_for + " found at index " + str(index) + "!"
    
    else:
        
        #If index wasn't greater than or equal to 0, then that
        #means search_for was not found in search_within. So,
        #we return that message instead:
        
        return search_for + " was not found within " + search_within + "!"



print(fancy_find("ABCDEF", "DEF"))
print(fancy_find("ABCDEF", "GHI"))


#############################################################################
#Write a function called "scramble" that accepts a string
#as an argument and returns a new string. The new string 
#should start with the last half of the original string
#and end with the first half. 
#
#If the length of the string is odd, split the string 
#at the floor of the length / 2 (in other words, the second
#half is the longer half).
#
#For example:
#  scramble("abcd") -> "cdab"
#  screamble("abcde") -> "cdeab"
#  scramble("railroad")) -> "roadrail"
#  scramble("fireworks")) -> "worksfire"


#Write your function here!
def scramble(string):
    floor = len(string)//2
    second_half = string[0:floor]
    first_half = string[floor:]
   
    return first_half + second_half


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print the results you see in the examples above.

string1 = "abcd"
string2 = "abcde"
string3 = "railroad"
string4 = "fireworks"
print(string1 + " -> " + scramble(string1))
print(string2 + " -> " + scramble(string2))
print(string3 + " -> " + scramble(string3))
print(string4 + " -> " + scramble(string4))
print()
#______________________________________________


#############################################################################
#Write a function called "last_n" that accepts two arguments:
#a string search_string and an integer n. The function should
#return the last n characters from search_string. If
#search_string is shorter than n characters, then it should
#return the entire value of search_string.


#Write your function here!
def last_n(search_string, integer):
    if len(search_string) > integer:
        return search_string[-integer:]
    else:
        return search_string



#The code below will test your function. If your function
#works correctly, this should print 789, saur, and 1.
print(last_n("123456789", 3))
print(last_n("Bulbasaur", 4))
print(last_n("1", 5))
print()

#There are a lot of complicated approaches we could take
#here, but the simplest is just a string slicing operation.
#If we want to start n characters from the end, then we grab
#a slice that starts at -n and goes until the end.

def last_n(search_string, n):
    return search_string[-n:]

#We also don't need any special reasoning to handle instances
#where search_string is shorter than n characters; by
#default, Python just grabs the entire string if that is the
#case.


print(last_n("123456789", 3))
print(last_n("Bulbasaur", 4))
print(last_n("1", 5))
print()
##############################################################################
string = "adsfasdf"
print(string[9:12])
#-----------------------------------------------------------
#Write a function called align_right. align_right should
#take two parameters: a string (a_string) and an integer
#(string_length), in that order.
#
#The function should return the same string with spaces
#added to the left so that the text is "right aligned" in a
#string. The number of spaces added should make the total
#string length equal string_length.
#
#For example: align_right("CS1301", 10) would return the
#string "    CS1301". Four spaces are added to the left so
#"CS1301" is right-aligned and the total string length is
#10.
#
#HINT: Remember, len(a_string) will give you the number of
#characters currently in a_string.


#Add your function here!
def align_right(a_string, string_length):
    counter = 0
    space = " "
    for i in range(1, len(a_string)):
        counter += 1
        num_spaces = string_length - counter
    return num_spaces * space + a_string    


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: "    CS1301"
print(align_right("CS1301", 10))
print()

def align_right(a_string, string_length):
    
    #Next, we need to figure out how many spaces we need to
    #add. We want the total length to be string_length, and
    #the current length is the length of a_string. So, our
    #number of spaces to add is the differences:
    
    num_spaces = string_length - len(a_string)
    
    #So, we return that many spaces, plus the original
    #string:
    
    return " " * num_spaces + a_string



print(align_right("CS1301", 10))

#############################################################################

def steps():
    string = "111\n\t222\n\t\t333"
    return string

#The line below will test your function.
print(steps())
print()

def steps():
    
    #Then, we're only ever returning the exact same string.
    #The goal is to work with \n and \t. So, here's the
    #answer:
    
    return "111\n\t222\n\t\t333"


print(steps())
#############################################################################
#Write a function called random_marks. random_marks should
#take three parameters, all integers. It should return a
#string.
#
#The first parameter represents how many apostrophes should
#be in the string. The second parameter represents how many
#quotation marks should be in the string. The third
#parameter represents how many apostrophe-quotation mark
#pairs should be in the string.
#
#For example, random_marks(3, 2, 3) would return this
#string: #'''""'"'"'"
#
#Note that there are three apostrophes, then two quotation
#marks, then three '" pairs.


#Add your function here!
def random_marks(int1, int2, int3):
    apo = 0
    quo = 0
    pair = 0
    for i in range(1, int1 + 1):
        apo += 1
        apos = "'"
    for j in range(1, int2 + 1):
        quo += 1
        quos = '"'
    for k in range (1, int3 + 1):
        pair += 1
        pairs = ''''"'''
    return (apo * apos) + (quo * quos) + (pair * pairs)    
    


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: '''""'"'"'"

print(random_marks(3, 2, 4))