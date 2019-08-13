#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 16:21:52 2018

@author: meganporter
"""


########################################################################
#Do not change the line of code below. It's at the top of
#the file to ensure that it runs before any of your code.
#You will be able to access french_dict from inside your
#function.
french_dict = {"me": "moi", "hello": "bonjour", 
               "goodbye": "au revoir", "cat": "chat", 
               "dog": "chien", "and": "et"}

#Write a function called french2eng that takes in one string
#parameter called sentence. french2eng should look at each
#word in the sentence and translate it into French if it is
#found in the dictionary, french_dict. If a word is not found
#in the dictionary, do not translate it: use the original
#word. Then, the function should return a string of the
#translated sentence.
#
#You may assume that the sentence you're translating has no
#punctuation. However, you should convert it to lower case
#before translating.
#
#For example:
#
#  french2eng("Hello it's me") -> "bonjour it's moi"
#
#Hint: Use .split() to get a list of strings representing
#each word in the string, then use ' '.join to merge the
#translated list back into one string.
#
#Hint 2: Remember, lists are mutable, so we can change
#individual items in the list. However, to change an item
#in a list, we must change it using its index. We can
#write lines like my_words[1] = new_word.
#
#Hint 3: If you're stuck, try breaking it down into small
#parts. How do you access an item from a list? How do you
#look up a key in a dictionary? How do you change the
#value of an item in a list? How do you check if a key is
#in the dictionary?


#Write your function here!
def french2eng(sentence):
    sentence = sentence.lower()
    string_list = sentence.split()
    word_list = []
    
    for item in string_list:
        if item in french_dict:
            sentence = sentence.replace(item, french_dict[item])
        
        
    return sentence      



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
print(french2eng("Hello it's me"))
print()
#__________________________________________________
french_dict = {"me": "moi", "hello": "bonjour", 
               "goodbye": "au revoir", "cat": "chat", 
               "dog": "chien", "and": "et"}

def french2eng(sentence):
    sentence = sentence.lower()
    sentence_split = sentence.split(" ")
    for i in range(len(sentence_split)):
        
        if sentence_split[i] in french_dict:
            sentence_split[i] = french_dict[sentence_split[i]]
    return " ".join(sentence_split)
print(french2eng("Hello it's me"))
print()
#__________________________________________________
french_dict = {"me": "moi", "hello": "bonjour", 
               "goodbye": "au revoir", "cat": "chat", 
               "dog": "chien", "and": "et"}
def french2eng(sentence):
    sentence = sentence.lower()
    sentence_split = sentence.split(" ")
    result = ""
    
    for word in sentence_split:
        if word in french_dict:
            result += french_dict[word]
        else:
            result += word
        result += " "
    return result.strip()
    
    
    
print(french2eng("Hello it's me"))
print()

########################################################################
#Write a function called most_oscars, which takes in one
#parameter, a dictionary. This dictionary maps names to the
#number of Academy Awards for which they have been nominated.
#This function should return a tuple containing the name and
#number of nominations for the person who has the most
#nominations.
#
#You may assume there will not be a tie for the actor with
#the most nominations (although there may be other ties in
#the list).


#Write your function here!
def most_oscars(dictionary):
    
    maximum = max(dictionary, key=dictionary.get)
    return (maximum, dictionary[maximum])
        
        
    


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: ('Meryl Streep', 20)
nominees = {'Meryl Streep': 20, 'Robert De Niro': 7, 'Michael Caine': 6, 'Maggie Smith': 6}
print(most_oscars(nominees))
print()
#_________________________________________________
def most_oscars(oscar_dict):
    current_max_name = ""
    for person in oscar_dict:
        if current_max_person == "":
            current_max_person = person
            
        elif oscar_dict[current_max_person] < oscar_dict[person]:
            current_max_person = person
    return (current_max_person, oscar_dict[current_max_person])



winners = {'Meryl Streep': 20, 'Robert De Niro': 7, 'Michael Caine': 6, 'Maggie Smith': 6}
print(most_oscars(winners))
print()
########################################################################
#Recall last exercise that you wrote a function, word_lengths,
#which took in a string and returned a dictionary where each
#word of the string was mapped to an integer value of how
#long it was.
#
#This time, write a new function called length_words so that
#the returned dictionary maps an integer, the length of a
#word, to a list of words from the sentence with that length.
#If a word occurs more than once, add it more than once. The
#words in the list should appear in the same order in which
#they appeared in the sentence.
#
#For example:
#
#  length_words("I ate a bowl of cereal out of a dog bowl today.")
#  -> {3: ['ate', 'dog', 'out'], 1: ['a', 'a', 'i'],
#      5: ['today'], 2: ['of', 'of'], 4: ['bowl'], 6: ['cereal']}
#
#As before, you should remove any punctuation and make the
#string lowercase.
#
#Hint: To create a new list as the value for a dictionary key,
#use empty brackets: lengths[wordLength] = []. Then, you would
#be able to call lengths[wordLength].append(word). Note that
#if you try to append to the list before creating it for that
#key, you'll receive a KeyError.


#Write your function here!
def length_words(string):
    dictionary = {}
    string = string.lower()
    punct = ".?,'!"
    
    for item in punct:
        string = string.replace(item, "")
        
    string = string.split()
    
    for item in string:
        lengths = len(item)
        if lengths not in dictionary:
            dictionary[lengths] = []
            
        dictionary[lengths].append(item)
        
    return dictionary

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#{1: ['i', 'a', 'a'], 2: ['of', 'of'], 3: ['ate', 'out', 'dog'], 4: ['bowl', 'bowl'], 5: ['today'], 6: ['cereal']}
#
#The keys may appear in a different order, but within each
#list the words should appear in the order shown above.
print(length_words("I ate a bowl of cereal out of a dog bowl today."))
print()
#_________________________________________________
def length_words(sentence):
    
    sentence = sentence.lower()
    
    to_replace = ".,'!?"
    for mark in to_replace:
        sentence = sentence.replace(mark, "")
        
    sentence = sentence.split(' ')
    word_lengths = {}
    
    
    for word in sentence:
        
        if len(word) not in word_lengths.keys():
            
            word_lengths[len(word)] = []
        
        word_list = word_lengths[len(word)]
        word_list.append(word)
    
    return word_lengths


print(length_words("I ate a bowl of cereal out of a dog bowl today."))
print()
########################################################################
#Write a function called word_lengths, which takes in one
#parameter, a string, and returns a dictionary where each
#word of the string is mapped to an integer representing how
#how long that word is. You should ignore punctuation, and
#all the words should be lowercase. You can assume that the
#only punctuation marks in the string will be periods,
#commas, question marks, exclamation points, and apostrophes.
#
#For example:
#  word_lengths("I ate a bowl of cereal out of a dog bowl today.")
#  -> {'i':1, 'bowl':4, 'today':5, 'out':3, 'dog':3, 'ate':3,
#      'a':1, 'of':2, 'cereal':6}
#
#Hint: Use the split() method to split by spaces, and don't
#forget to remove punctuation marks.  Remember also: strings
#are immutable, so operations like my_string.lower() don't
#change the value of my_string like list methods: to save
#those results, you'd write my_string = my_string.lower().
#
#Your dictionary should not have any duplicate keys (in fact,
#Python won't allow a dictionary to have duplicate keys).


#Write your function here!
def word_lengths(string):
    dictionary = {}
    no_punct = "".join(c for c in string if c not in ('!','.',"'",'?',','))
    no_punct = no_punct.lower()
    word_list = no_punct.split()
    for item in word_list:
        dictionary[item] = len(item)
    
    return dictionary 


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#{'dog': 3, 'today': 5, 'of': 2, 'ate': 3, 'bowl': 4, 'out': 3, 'a': 1, 'cereal': 6, 'i': 1}
#
#The order of the keys may differ, but that's okay!
print(word_lengths("I ate a bowl of cereal out of a dog bowl today."))
print()
#_________________________________________________________

def word_lengths(sentence):
    
    sentence = sentence.lower()
    to_replace = ".,'!?"
    for mark in to_replace:
        #Don't forget about string methods!!!!!
        sentence = sentence.replace(mark, "")
    sentence = sentence.split(' ')
    word_lengths = {}
    for word in sentence:
        
        word_lengths[word] = len(word)
        
    return word_lengths



print(word_lengths("I ate a bowl of cereal out of a dog bowl today."))
print()
########################################################################
#Write a function called population_density. The function
#should take one parameter, which will be a list of
#dictionaries. Each dictionary in the list will have three
#key-value pairs:
#
# - name: the name of the country
# - population: the population of that country
# - area: the area of that country (in km^2)
#
#Your function should return the population density of all
#the countries put together. You can calculate this by
#summing all the populations, summing all the areas, and
#dividing the total population by the total area.
#
#Note that the input to this function will look quite long;
#don't let that scare you. That's just because dictionaries
#take a lot of text to define.


#Add your function here!
def population_density(list_of_dictionaries):
    sum_pop = 0
    sum_area = 0
    for item in list_of_dictionaries:
        sum_pop += item["population"]
        sum_area += item["area"]
    return sum_pop / sum_area   
                       
    
    


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 133.886 (or something around there)
countries = [{"name": "China", "population": 1390700000, "area": 9640821},
             {"name": "India", "population": 1348003000, "area": 3287240},
             {"name": "United States", "population": 325300000, "area": 9826675},
             {"name": "Indonesia", "population": 237556363, "area": 1904569}]
print(population_density(countries))
print()
########################################################################
#In the Pokemon video game series, every Pokemon has six
#stats: HP, Attack, Defense, Special Attack, Special Defense,
#and Speed.
#
#Write a function called total_stats that will take as input
#a list of dictionaries. Each dictionary will have seven
#key-value pairs:
#
# - name: a Pokemon's name
# - hp, attack, defense, special attack, special defense,
#   and speed: an integer representing that Pokemon's stat
#   in that category
#
#Your function should return a single dictionary. The keys
#of the dictionary should be the Pokemon names from the
#original list, and the values should be the _total_ stats
#for each Pokemon (add HP, Attack, Defense, Special Attack,
#Special Defense, and Speed).
#
#For example, if this was one of the dictionaries in the
#original list:
#
#{"name": "Bulbasaur", "HP": 45, "Attack": 49, "Defense": 49,
#"Special Attack": 65, "Special Defense": 65, "Speed: 45}
#
#Then one of the key-value pairs in the dictionary you
#return would be: "Bulbasaur": 318 (45 + 49 + 49 + 65 + 65 +
#45 = 318).


#Add your function here!
def total_stats(list_of_dictionaries):
    new_dict = {}
    for item in list_of_dictionaries:
        value = item["hp"] + item["attack"] + item["defense"] + item["special attack"] +                         item["special defense"] + item["speed"]
        new_dict[item["name"]] = value
    return new_dict    
        
    
    



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print (although the order of the keys may vary):
#{'Bulbasaur': 318, 'Charmander': 309, 'Squirtle': 314}
starters = [{"name": "Bulbasaur", "hp": 45, "attack": 49, "defense": 49, "special attack": 65, "special defense": 65, "speed": 45},
            {"name": "Charmander", "hp": 39, "attack": 52, "defense": 43, "special attack": 60, "special defense": 50, "speed": 65},
            {"name": "Squirtle", "hp": 44, "attack": 48, "defense": 65, "special attack": 50, "special defense": 64, "speed": 43}]
print(total_stats(starters))
print()
#_____________________________________________________________

def total_stats(list_of_pokemon):
    
    for mon in list_of_pokemon:
        
        name = mon["name"]
        
        total_stats = mon["hp"]
        total_stats += mon["attack"]
        total_stats += mon["defense"]
        total_stats += mon["special attack"]
        total_stats += mon["special defense"]
        total_stats += mon["speed"]
        
        results[name] = total_stats
    return results



starters = [{"name": "Bulbasaur", "hp": 45, "attack": 49, "defense": 49, "special attack": 65, "special defense": 65, "speed": 45},
            {"name": "Charmander", "hp": 39, "attack": 52, "defense": 43, "special attack": 60, "special defense": 50, "speed": 65},
            {"name": "Squirtle", "hp": 44, "attack": 48, "defense": 65, "special attack": 50, "special defense": 64, "speed": 43}]
print(total_stats(starters))
print()
########################################################################

#Recall in an earlier problem you were given two lists: one
#list was a student's answers to a test, and the other was
#the answer key. Your goal was to return a score
#representing the number of problems the student got correct.
#
#Let's do that again, but with dictionaries instead of lists.
#Write a function called calculate_score. calculate_score
#should take two parameters: a dictionary of student answers
#and a dictionary of correct answers. Both dictionaries should
#have integers as their keys, and one-character strings as
#their values.
#
#calculate_score should count how many questions the student
#got right. Or, in more precise terms, calculate_score should
#count how many keys for which the associated value is the
#same in the student's dictionary and in the answer key
#dictionary.
#
#As before, it is possible that there will be more answers in
#one than the other. This means that these answers don't
#belong to the same test! If that happens, return -1.


#Add your function here!
def calculate_score(students, teachers):
    if len(students) != len(teachers):
        return -1
        
    for key in students.keys():
        total = 0
        for key in teachers.keys():
            if students[key] == teachers[key]:
                total += 1
           
    return total    


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 3
student_answers = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E"}
correct_answers = {1: "A", 2: "B", 3: "B", 4: "B", 5: "B"}
print(calculate_score(student_answers, correct_answers))
print()
#-----------------------------------------------------------
def calculate_score(student, correct):
    
    if not len(student) == len(correct):
        return -1
    total = 0
    for (question, answer) in student.items():
        if answer == correct[question]:
            
    return total



student_answers = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E"}
correct_answers = {1: "A", 2: "B", 3: "A", 4: "D", 5: "B"}
print(calculate_score(student_answers, correct_answers))
print()

########################################################################
#Write a function called modify_dict. modify_dict takes one
#parameter, a dictionary. The dictionary's keys are people's
#last names, and the dictionary's values are people's first
#names. For example, the key "Joyner" would have the value
#"David".
#
#modify_dict should delete any key-value pair for which the
#key's first letter is not capitalized. For example, the
#key-value pair "joyner":"David" would be deleted, but the
#key-value pair "Joyner":"david" would not be deleted. Then,
#return the modified dictionary.
#
#Remember, the keyword del deletes items from lists and
#dictionaries. For example, to remove the key "key!" from
#the dictionary my_dict, you would write: del my_dict["key!"]
#Or, if the key was the variable my_key, you would write:
#del my_dict[my_key]
#
#Hint: If you try to delete items from the dictionary while
#looping through the dictionary, you'll run into problems!
#We should never change the number if items in a list or
#dictionary while looping through those items. Think about
#what you could do to keep track of which keys should be
#deleted so you can delete them after the loop is done.
#
#Hint 2: To check if the first letter of a string is a
#capital letter, use string[0].isupper().


#Write your function here!
def modify_dict(dictionary):
    lst = []
    new_dict = {}
    for key,value in dictionary.items():
        if key[0].isupper():
            new_dict[key] = value
    
    return new_dict        
            



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print (although the order of the keys may vary):
#  {'Diaddigo':'Joshua', 'Elliott':'jackie'}
my_dict = {'Joshua':'Diaddigo', 'joyner':'David', 'Elliott':'jackie', 'murrell':'marguerite'}
print(modify_dict(my_dict))
print()
#______________________________________________
def modify_dict(name_dict):
    del_list = []
    for key in name_dict:
        
        if key != key.capitalize():
            del_list.append(key)
    for key in del_list:
        del name_dict[key]
    return name_dict



my_dict = {'Joshua':'Diaddigo', 'joyner':'David', 'Elliott':'jackie', 'murrell':'marguerite'}
print(modify_dict(my_dict))
print()
########################################################################
#Write a function called course_info that takes as input a
#list of tuples. Each tuple contains two items: the first
#item in each tuple is a student's name as a string, and the
#second item in each tuple is that student's age as an
#integer.
#
#The function should return a dictionary with two keys.
#The key "students" should have as its value a list of all
#the students (in other words, a list made from the first
#value of each tuple), in the original order in which they
#appeared in the list. The key "avg_age" should have as its
#value a float representing the average age of all the
#students in the list (in other words, the average of all
#the second items in the tuples).
#
#For example:
#
#  course_info([("Jackie", 20), ("Marguerite", 21)])
#  -> {"students": ['Jackie', 'Marguerite'], "avg_age": 20.5}
#
#Hint: Concentrate first on building the list of students
#and calculating the average age. Save creating the
#dictionary for last.


#Write your function here!
def course_info(tuples):
    name_list = []
    count = 0
    sums = 0
    dicti = {}
    for item in tuples:
        name_list.append(item[0])
        count += 1
        sums += item[1]
        avg_age = sums / count
    dicti["students"]= name_list    
    dicti["avg_age"] = avg_age
    return dicti


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print (although the order of the keys may vary):
print(course_info([("Jackie", 20), ("Marguerite", 21)]))
print()
#__________________________________________________
print()

def course_info(student_list):
    students = []
    total_age = 0
    
    for student_tuple in student_list:
        
        student_name, student_age = student_tuple
        
        students.append(student_name)
        
        total_age += student_age
    student_info = {"students": students, "avg_age": total_age/len(student_list)}
    
    return student_info



print(course_info([("Jackie", 20), ("Marguerite", 21)]))
print()
########################################################################



########################################################################
#Write a function called phonebook that takes two lists as
#input:
#
# - names, a list of names as strings
# - numbers, a list of phone numbers as strings
#
#phonebook() should take these two lists and create a
#dictionary that maps each name to its phone number. For
#example, the first name in names should become a key in
#the dictionary, and the first number in numbers should
#become the value corresponding to the first name. Then, it
#should return the dictionary that results.
#
#Hint: Because you're mapping the first name with the first
#number, the second name with the second number, etc., you do
#not need two loops. For a similar exercise, check back on
#Coding Problem 4.3.3, the Scantron grading problem.
#
#You may assume that the two lists have the same number of
#items: there will be no names without numbers or numbers
#without names.


#Write your function here!
def phonebook(names, numbers):
    directory = {}
    for item in range(len(names)):
        directory[names[item]] = numbers[item]
    return directory    
    


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print (although the order of the keys may vary):
#{'Jackie': '404-555-1234', 'Joshua': '678-555-5678', 'Marguerite': '770-555-9012'

name_list = ['Jackie', 'Joshua', 'Marguerite']
number_list = ['404-555-1234', '678-555-5678', '770-555-9012']
print(phonebook(name_list, number_list))
print()
#_______________________________________________________________
def phonebook(name_list, number_list):
    
    phonebook = {}
    
    for i in range(len(name_list)):
        
        name = name_list[i]
        number = number_list[i]
        phonebook[name] = number
        
    return phonebook



name_list = ['Jackie', 'Joshua', 'Marguerite']
number_list = ['404-555-1234', '678-555-5678', '770-555-9012']
print(phonebook(name_list, number_list))
print()
########################################################################
#Recall in the previous problem you counted the number of
#instances of a certain first name in a list of full names.
#You returned a dictionary with the name as the key, and the
#number of times it appeared as the value.
#
#Modify that code such that instead of having a count as the
#value, you instead have a list of the full names that had
#that first name. So, each key in the dictionary would still
#be a first name, but the values would be lists of names.
#Make sure to sort the list of names, too.
#
#Name this new function name_lists.


#Add your function here!
def name_lists(names):
    
    name_dictionary = {}
    list_names = []
    
    
    for item in names:
        split_name = item.split()
        first_name = split_name[0]
        if first_name not in name_dictionary:
            # NOTICE YOU HAVE T0 PUT BRACKETS AROUND THE VALUE to make it
            # a LIST value!!!!
            name_dictionary[first_name] = [item]
        else:
            name_dictionary[first_name].append(item)
        for first_name in name_dictionary:
            ## Notice sort operates on values that are referred to by key
            name_dictionary[first_name].sort()
           
    return name_dictionary

    
    

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print (although the order of the keys may vary):
#{'Shelba': ['Shelba Barthel', 'Shelba Crowley', 'Shelba Fernald', 'Shelba Odle', 'Shelba Fry'],
#'David': ['David Joyner', 'David Zuber'], 'Brenton': ['Brenton Joyner', 'Brenton Zuber'],
#'Maren': ['Maren Fry'], 'Nicol': ['Nicol Barthel']}

name_list = ["David Joyner", "David Zuber", "Brenton Joyner",
             "Brenton Zuber", "Nicol Barthel", "Shelba Barthel",
             "Shelba Crowley", "Shelba Fernald", "Shelba Odle",
             "Shelba Fry", "Maren Fry"]

print(name_lists(name_list))
print()

########################################################################
#Write a function called name_counts. name_counts will take
#as input a list of full names. Each name will be two words
#separated by a space, like "David Joyner".
#
#The function should return a dictionary. The keys to the
#dictionary will be the first names from the list, and the
#values should be the number of times that first name
#appeared.
#
#HINT: Use split() to split names into first and last.


#Add your function here!
def name_counts(names):
    new_list = []
    name_dictionary = {}
    for item in names:
        new_list.append(item.split())
    for item in new_list:
        
        first_name = item[0]
        if first_name in name_dictionary:
            name_dictionary[first_name] += 1
        else:
            name_dictionary[first_name] = 1
            
           
            
    return name_dictionary   
    



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print (although the order of the keys may vary):
#{'Shelba': 5, 'Maren': 1, 'Nicol': 1, 'David': 2, 'Brenton': 2}
name_list = ["David Joyner", "David Zuber", "Brenton Joyner",
             "Brenton Zuber", "Nicol Barthel", "Shelba Barthel",
             "Shelba Crowley", "Shelba Fernald", "Shelba Odle",
             "Shelba Fry", "Maren Fry"]
print(name_counts(name_list))
print()
#_________________________________________
def name_counts(names):
    name_dict = {}
    for name in names:
        split_name = name.split()
        first_name = split_name[0]
        if not first_name in name_dict:
            name_dict[first_name] = 0
        name_dict[first_name] += 1
    return name_dict



name_list = ["David Joyner", "David Zuber", "Brenton Joyner",
             "Brenton Zuber", "Nicol Barthel", "Shelba Barthel",
             "Shelba Crowley", "Shelba Fernald", "Shelba Odle",
             "Shelba Fry", "Maren Fry"]
print(name_counts(name_list))
print()
**********************************************
"""This is how to split a string and count words.  Note the cleanup.  Not
my work"""
myString = "This is the string whose words we would like to count. This string contains some repeated words, as well as some unique words. It contains punctuation, and it contains words that are capitalized in different ways. If the method we write runs correctly, it will count 4 instances of the word 'it', 3 instances of the word 'this', and 3 instances of the word 'count'."

myString = myString.replace(".","") #Remove periods
myString = myString.replace(",","") #Remove commas
myString = myString.replace("'","") #Remove apostrophes
myString = myString.lower() #Make all lower case
mySplitString = myString.split() #Split by spaces

wordDictionary = {} #Create empty dictionary
for word in mySplitString:  #For each word in the split string
    if word in wordDictionary:  #If it's already been found...
        wordDictionary[word] += 1   #Add one to its count
    else:   #Otherwise...
        wordDictionary[word] = 1 #Create it with value 1

print(wordDictionary)
print()
***************************************************
########################################################################
#Write a function called students_present. students_present
#should take as input one parameter, a dictionary. The keys
#of the dictionary will be names, and the values will be one
#of three strings: "Here", "Present", or an empty string "".
#
#Return a list of the keys for whom the corresponding value
#is either "Here" or "Present".


#Add your code here
def students_present(dictionary):
    lst = []
    for item in dictionary:
        if dictionary[item] == "Here" or dictionary[item] == "Present":
            lst.append(item)
    return lst        

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print (although the order of the keys may vary):
#["David", "Marguerite", "Joshua", "Erica"]

student_list = {"David" : "Here", "Marguerite" : "Here",
                "Jackie": "", "Joshua": "Present",
                "Erica": "Here", "Daniel": ""}
print(students_present(student_list))
print()
########################################################################
#Create a function called tup_to_dict. tup_to_dict should take one
#parameter: a list of tuples. You can assume each tuple in
#the list has exactly two values.
#
#The function should return a dictionary where the first item
#in each tuple is the key, and the second item in each tuple
#is the corresponding value.
#
#For example:
# colors = [("turquoise", "#40E0D0"), ("red", "#990000")]
# tup_to_dict(colors) -> {"turquoise":"#40E0D0", "red":"#990000"}
#
#Hint: the previous exercise is very similar; this just turns
#it into a function! All our tuples will be color name-color
#value pairs.


#Write your function here!
def tup_to_dict(tups):
    diction = dict(tups)
    
    return diction    
    



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:  {'Turquoise':'#40E0D0', 'Red':'#990000'}
#
#Don't worry if it prints those in the reverse order; that's
#still correct!
print(tup_to_dict([("Turquoise", "#40E0D0"), ("Red", "#990000")]))
print()
#________________________________________

def tup_to_dict(tuple_list):
    color_dict = {}
    for color_tuple in tuple_list:
        color_name = color_tuple[0]
        color_value = color_tuple[1]
        
        color_dict[color_name] = color_value
    return color_dict



print(tup_to_dict([("Turquoise", "#40E0D0"), ("Red", "#990000")]))
print()
########################################################################
#We've defined a list of tuples below. Each tuple follows
#the format: (name, home state).
#
#Create a dictionary called ta_dict in the space below, where
#the keys are each TA's name, and the values are their home
#state.

ta_info = [("Joshua", "Georgia"),
          ("Jackie", "Vermont"),
          ("Marguerite", "Tennessee")]

#Add your code to create the dictionary as described!
#The first item in each tuple should be a key, and
#the second item in each tuple should be its value.
#Note that you may create this either by reading and
#using the ta_info list of tuples, or you can create
#the dictionary from scratch:


#Create your dictionary here!
ta_dict = {"Joshua": "Georgia", "Jackie": "Vermont", "Marguerite": "Tennessee"}
       
    
    
      


#Now, create three variables: josh_val, jack_val, and
#marg_val. Set josh_val equal to Josh's dictionary value,
#then jack_val equal to Jackie's, then marg_val equal to
#Marguerite's. Remember how to properly access the value
#corresponding to a dictionary key!
#
#Make sure you use dictionary-access syntax to do this.
#Don't create the variables based on new values.


#Create your variables here!
josh_val = ta_dict["Joshua"]
jack_val = ta_dict["Jackie"]
marg_val = ta_dict["Marguerite"]


#If your code works as intended, the following three lines
#will run and print Georgia, Vermont, and Tennessee:


print(josh_val)
print(jack_val)
print(marg_val)
print()
#_____________________________________________________
ta_info = [("Joshua", "Georgia"),
          ("Jackie", "Vermont"),
          ("Marguerite", "Tennessee")]
ta_dict = {"Joshua":"Georgia", "Jackie":"Vermont", "Marguerite":"Tennessee"}

ta_dict = {ta_info[0][0]:ta_info[0][1], ta_info[1][0]:ta_info[1][1], ta_info[2][0]:ta_info[2][1]}

ta_dict = {}
for ta_tuple in ta_info:
    ta_dict[ta_tuple[0]] = ta_tuple[1]
josh_val = ta_dict['Joshua']
jack_val = ta_dict["Jackie"]
marg_val = ta_dict["Marguerite"]
print(josh_val)
print(jack_val)
print(marg_val)
print