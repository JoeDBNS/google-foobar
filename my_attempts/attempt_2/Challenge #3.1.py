'''
String cleaning
===============

Your spy, Beta Rabbit, has managed to infiltrate a lab of mad scientists 
who are turning rabbits into zombies. He sends a text transmission to you, 
but it is intercepted by a pirate, who jumbles the message by repeatedly 
inserting the same word into the text some number of times. At each step, 
he might have inserted the word anywhere, including at the beginning or 
end, or even into a copy of the word he inserted in a previous step. By 
offering the pirate a dubloon, you get him to tell you what that word was. 
A few bottles of rum later, he also tells you that the original text was 
the shortest possible string formed by repeated removals of that word, 
and that the text was actually the lexicographically earliest string from 
all the possible shortest candidates. Using this information, can you 
work out what message your spy originally sent?

For example, if the final chunk of text was "lolol," and the inserted 
word was "lol," the shortest possible strings are "ol" (remove "lol" 
from the beginning) and "lo" (remove "lol" from the end). The original 
text therefore must have been "lo," the lexicographically earliest string.

Write a function called answer(chunk, word) that returns the shortest, 
lexicographically earliest string that can be formed by removing occurrences 
of word from chunk. Keep in mind that the occurrences may be nested, and 
that removing one occurrence might result in another. For example, removing 
"ab" from "aabb" results in another "ab" that was not originally present. 
Also keep in mind that your spy's original message might have been an empty string.

chunk and word will only consist of lowercase letters [a-z].
chunk will have no more than 20 characters.
word will have at least one character, and no more than the number of characters in chunk.


Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java


Test cases
==========

Inputs:
    (string) chunk = "lololololo"
    (string) word = "lol"
Output:
    (string) "looo"

Inputs:
    (string) chunk = "goodgooogoogfogoood"
    (string) word = "goo"
Output:
    (string) "dogfood"
'''



def answer1(chunk, word):
    while word in chunk:
        chunk = chunk.replace(word, '')
    return(''.join(sorted(chunk)))


def answer2(chunk, word):
    while word in chunk:
        chunk = ''.join(chunk.rsplit(word, 1))
    return(chunk)


def answer3(chunk, word):
    chunk_rsplit = chunk
    chunk_split = chunk
    
    while word in chunk_rsplit:
        chunk_rsplit = ''.join(chunk_rsplit.rsplit(word, 1))
    
    while word in chunk_split:
        chunk_split = chunk_split.replace(word, '', 1)
    
    if len(chunk_split) == len(chunk_rsplit):
        return(chunk_rsplit)
    elif len(chunk_split) > len(chunk_rsplit):
        return(chunk_rsplit)
    else:
        return(chunk_split)


def answer4(chunk, word):
    chunk_rsplit = chunk
    chunk_split = chunk
    
    while word in chunk_rsplit:
        chunk_rsplit = ''.join(chunk_rsplit.rsplit(word, 1))
    
    while word in chunk_split:
        chunk_split = chunk_split.replace(word, '', 1)
    
    if len(chunk_split) == len(chunk_rsplit):
        return(chunk_rsplit)
    elif len(chunk_split) == 0 and len(chunk_rsplit) != 0:
        return(chunk_rsplit)
    elif len(chunk_split) > len(chunk_rsplit):
        return(chunk_rsplit)
    else:
        return(chunk_split)


def Find_Substring_Indexes(string, sub):
    last_found = -1
    while True:
        last_found = str(string).find(sub, last_found + 1)
        if last_found == -1:  
            break
        yield last_found

def Find_String_Minus_Sub(string_list, rem_word):
    tmp_list = []
    for word in string_list:
        for x in list(Find_Substring_Indexes(word, rem_word)):
            tmp_list.append(word[:x] + word[x + len(rem_word):])
    return(tmp_list)

def answer5(chunk, word):
    chunk_dict = {0: [chunk]}
    dict_itr = 1
    
    while word in str(chunk_dict[dict_itr - 1]):
        if dict_itr not in chunk_dict.keys():
            chunk_dict[dict_itr] = list(set(Find_String_Minus_Sub(chunk_dict[dict_itr - 1], word)))
        else:
            chunk_dict[dict_itr].append(list(set(Find_String_Minus_Sub(chunk_dict[dict_itr - 1], word))))
    
        dict_itr += 1
    
    return( sorted((chunk_dict[dict_itr - 1]))[0] )


    
print(answer5("lolllolol", "lol"))

print(answer5("lolol", "lol"))

print(answer5("lololololo", "lol"))

print(answer5("goodgooogoogfogoood", "goo"))

print(answer5("odogdogodgo", "god"))