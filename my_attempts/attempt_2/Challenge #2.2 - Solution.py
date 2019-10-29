# name_that_rabbit



# The answer function will accept a list of lower case name strings 
# and will return that same list but ordered based on the sum of the 
# letter values for each name. Names with total letter values that 
# occur more than once will then be ordered lexicographically.
def answer(names):
    # Assign each letter to a number value, 'a' being the lowest and 'z' being the highest.
    letter_values = { 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26 }
    
    # Sort the names list reverse-alphabetically to accommodate for 
    # lexicographically sorting names of the same total letter values.
    names = sorted(names, reverse = True)
    
    # Holds final names list ordered by name's total letter values.
    names_final = []
    
    # Holds list of letter value totals for each name.
    name_totals = []
    
    # Holds list of letter value totals used in names_final list.
    name_totals_used = []
    
    # Calculate letter values per each name and add results to name_totals list.
    for name in names:
        name_val = 0
        
        for letter in name:
            name_val += letter_values[letter]
        
        name_totals.append(name_val)
    
    # Loop through name_totals ordered by greatest to least. For each value, find its 
    # unordered index and add the names list value with the same index to the 
    # names_final list. Then add letter value total to name_totals_used list.
    for idx, val in enumerate(sorted(name_totals, reverse = True)):
        
        # If statement accounts for .index() only finding index for first value occurrence.
        # Only using List Comprehension as needed saves on processing time.
        if name_totals.count(val) > 1 and val in name_totals_used:
            names_final.append(names[[i for i, n in enumerate(name_totals) if n == val][name_totals_used.count(val)]])
            
        else:
            names_final.append(names[name_totals.index(val)])
        
        name_totals_used.append(val)
    
    # Return final names list ordered by name's total letter values.
    return(names_final)



# PROOF:
name_list1 = ["abcdefg", "vi"]
name_list2 = ["annie", "bonnie", "liz"]
name_list3 = ["annie", "bonnie", "liz", "bozcie"]
name_list4 = ['aaaabbb', 'z', 'j', 'abcd', 'a', 'abc', 'ab', 'x']

print(answer(name_list1))
print(answer(name_list2))
print(answer(name_list3))
print(answer(name_list4))