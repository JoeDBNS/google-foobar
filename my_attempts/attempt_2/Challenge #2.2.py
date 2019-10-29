'''
Name that rabbit
================

"You forgot to give Professor Boolean's favorite rabbit specimen a name? 
You know how picky the professor is! Only particular names will do! Fix 
this immediately, before you're... eliminated!"

Luckily, your minion friend has already come up with a list of possible 
names, and we all know that the professor has always had a thing for 
names with lots of letters near the 'tail end' of the alphabet, so to 
speak. You realize that if you assign the value 1 to the letter A, 2 to B, 
and so on up to 26 for Z, and add up the values for all of the letters, 
the names with the highest total values will be the professor's favorites. 
For example, the name Annie has value 1 + 14 + 14 + 9 + 5 = 43, while the 
name Earz, though shorter, has value 5 + 1 + 18 + 26 = 50. 

If two names have the same value, Professor Boolean prefers the 
lexicographically larger name. For example, if the names were AL 
(value 13) and CJ (value 13), he prefers CJ.

Write a function answer(names) which takes a list of names and 
returns the list sorted in descending order of how much the professor 
likes them.  

There will be at least 1 and no more than 1000 names. 
Each name will consist only of lower case letters.
The length of each name will be at least 1 and no more than 8.


Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java


Test cases
==========

Inputs:
    (string list) names = ["annie", "bonnie", "liz"]
Output:
    (string list) ["bonnie", "liz", "annie"]

Inputs:
    (string list) names = ["abcdefg", "vi"]
Output:
    (string list) ["vi", "abcdefg"]
'''


# Works but fails final test!
def answer1(name_list):
    alph_dict = { 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26 }
    name_totals = []
    name_final = []
    
    for name in name_list:
        name_val = 0
        
        for letter in name:
            name_val += alph_dict[letter]
        
        name_totals.append(name_val)
    
    for x in sorted(name_totals, reverse=True):
        name_final.append(name_list[name_totals.index(x)])
    
    return(name_final)


def answer2(name_list):
    alph_dict = { 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26 }
    name_totals = []
    name_final = []
    
    # ["a", "z", "abcd", "j", "abc", "ab", "x"]
    
    for name in name_list:
        name_val = 0
        
        for letter in name:
            name_val += alph_dict[letter]
        
        name_totals.append(name_val)
        
    # [1, 26, 10, 10, 6, 3, 24]
    
    for x in sorted(name_totals, reverse=True):
        name_final.append(name_list[name_totals.index(x)])
    
    # ['z', 'x', 'abcd', 'abcd', 'abc', 'ab', 'a']
    
    return(name_final)


def answer3(name_list):
    name_list = sorted(name_list, reverse = True)
    letter_val = { 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26 }
    name_totals = []
    name_totals_used = []
    name_final = []
    
    for name in name_list:
        name_val = 0
        
        for letter in name:
            name_val += letter_val[letter]
        
        name_totals.append(name_val)
    
    for idx, val in enumerate(sorted(name_totals, reverse = True)):
        if name_totals.count(val) > 1 and val in name_totals_used:
            name_final.append(name_list[[i for i, n in enumerate(name_totals) if n == val][name_totals_used.count(val)]])
        else:
            name_final.append(name_list[name_totals.index(val)])
        
        name_totals_used.append(val)
    
    return(name_final)


def answer4(names):
    letter_values = { 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26 }
    
    names = sorted(names, reverse = True)
    names_final = []
    name_totals = []
    name_totals_used = []
    
    for name in names:
        name_val = 0
        
        for letter in name:
            name_val += letter_values[letter]
        
        name_totals.append(name_val)
    
    for idx, val in enumerate(sorted(name_totals, reverse = True)):
        names_final.append(names[[i for i, n in enumerate(name_totals) if n == val][name_totals_used.count(val)]])
        
        name_totals_used.append(val)
    
    return(names_final)


names = ["a", "z", "abcd", "abc", "ab", "j", "aaaabbb", "x"]
print(answer3(names))
print(answer4(names))

names = ["abcdefg", "vi"]
print(answer3(names))
print(answer4(names))

names = ["annie", "bonnie", "liz"]
print(answer3(names))
print(answer4(names))

names = ["annie", "bonnie", "bozcie", "liz"]
print(answer3(names))
print(answer4(names))