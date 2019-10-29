# string_cleaning



# The Find_Substring_Indexes function accepts two string variables as main and sub
# and yields the first index value for every instance of sub in main. This format 
# is utilized as it accounts for overlapping sub strings within the main string.
def Find_Substring_Indexes(main, sub):
    prev_index = -1
    while True:
        prev_index = main.find(sub, prev_index + 1)
        if prev_index == -1:
            break
        yield prev_index

# The Find_List_Paths function accepts a list of strings as eval_list and 
# a string as rem_word and returns a list of strings representing each unique outcome 
# of removing rem_word at each index it's found per each string in eval_list.
def Find_List_Paths(eval_list, rem_word):
    string_variations = []
    for word in eval_list:
        for x in Find_Substring_Indexes(word, rem_word):
            if word[:x] + word[x + len(rem_word):] not in string_variations:
                string_variations.append(word[:x] + word[x + len(rem_word):])
    return(string_variations)

# The answer function accepts two string variables as chunk and word and returns a 
# string that represents chunk in its shortest and lexigraphically ordered form after 
# removing every instance of word found in chunk in the order that produces the sortest 
# character count.
def answer(chunk, word):
    chunk_dict = {0: [chunk]}
    dict_itr = 1
    
    while word in str(chunk_dict[dict_itr - 1]):
        if dict_itr not in chunk_dict.keys():
            chunk_dict[dict_itr] = Find_List_Paths(chunk_dict[dict_itr - 1], word)
        else:
            chunk_dict[dict_itr].append(Find_List_Paths(chunk_dict[dict_itr - 1], word))
    
        dict_itr += 1
    
    return(sorted((chunk_dict[dict_itr - 1]))[0])



print(answer("lolllolol", "lol"))
print(answer("lolol", "lol"))
print(answer("lololololo", "lol"))
print(answer("goodgooogoogfogoood", "goo"))
print(answer("odogdogodgo", "god"))