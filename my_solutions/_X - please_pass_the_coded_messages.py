'''
Please Pass the Coded Messages
==============================

You need to pass a message to the bunny prisoners, but to avoid detection, the
code you agreed to use is... obscure, to say the least. The bunnies are given
food on standard-issue prison plates that are stamped with the numbers 0-9 for
easier sorting, and you need to combine sets of plates to create the numbers
in the code. The signal that a number is part of the code is that it is divisible
by 3. You can do smaller numbers like 15 and 45 easily, but bigger numbers like
144 and 414 are a little trickier. Write a program to help yourself quickly create
large numbers for use in the code, given a limited number of plates to work with.

You have L, a list containing some digits (0 to 9). Write a function answer(L) which
finds the largest number that can be made from some or all of these digits and is
divisible by 3. If it is not possible to make such a number, return 0 as the answer.
L will contain anywhere from 1 to 9 digits.  The same digit may appear multiple times
in the list, but each element in the list may only be used once.


Test cases
==========

Inputs:
    (int list) l = [3, 1, 4, 1]
Output:
    (int) 4311

Inputs:
    (int list) l = [3, 1, 4, 1, 5, 9]
Output:
    (int) 94311
'''


# Notes:
#   Some numbers may just not be used, as in second example.
#   
#   
#   
#   
#   
#   
#   


def answer1_SwapListItemPositions(num_list, swap_pos):
    pos_1 = num_list[swap_pos - 1]
    pos_2 = num_list[swap_pos]

    num_list[swap_pos - 1] = pos_2
    num_list[swap_pos] = pos_1

    return num_list


def answer1_BuildNumberFromList(num_list):
    number = ''
    for num_val in num_list:
        number += str(num_val)
    return int(number)


def answer1(L):
    cur_pos = len(L) - 1
    L.sort(reverse=True)

    while answer1_BuildNumberFromList(L) % 3 != 0:
        answer1_SwapListItemPositions(L, cur_pos)
        cur_pos -= 1

    return L


print(answer1([3, 1, 4, 1])) # 4311
print(answer1([3, 1, 4, 1, 5, 9])) # 94311