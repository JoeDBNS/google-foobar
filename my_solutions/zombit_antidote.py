'''
Zombit Antidote
===============

Forget flu season. Zombie rabbits have broken loose 
and are terrorizing Silicon Valley residents! Luckily, 
you've managed to steal a zombie antidote and set up a 
makeshift rabbit rescue station. Anyone who catches a 
zombie rabbit can schedule a meeting at your station to 
have it injected with the antidote, turning it back from 
a zombit to a fluffy bunny. Unfortunately, you have a 
limited amount of time each day, so you need to maximize 
these meetings. Every morning, you get a list of requested 
injection meetings, and you have to decide which to attend 
fully. If you go to an injection meeting, you will join it 
exactly at the start of the meeting, and only leave exactly 
at the end.

Can you optimize your meeting schedule? The world needs 
your help!

Write a method called answer(meetings) which, given a 
list of meeting requests, returns the maximum number 
of non-overlapping meetings that can be scheduled. 
If the start time of one meeting is the same as the end 
time of another, they are not considered overlapping.

meetings will be a list of lists. Each element of the
meetings list will be a two element list denoting a 
meeting request. The first element of that list will be 
the start time and the second element will be the end 
time of that meeting request.

All the start and end times will be non-negative 
integers, no larger than 1000000. 
The start time of a meeting will always be less than 
the end time.

The number of meetings will be at least 1 and will be 
no larger than 100.
The list of meetings will not necessarily be ordered 
in any particular fashion.


Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

'''


def answer1(input):
    input = sorted(input)
    input_final = [input[0]]
    
    x = 1
    while x < len(input):
        if input[x][0] >= input_final[len(input_final) - 1][1]:
            input_final.append(input[x])
        
        x += 1
    
    return(len(input_final))


x = [[1, 3], [3, 6]]
print(answer1(x))

x = [[1, 3], [3, 6], [8, 9]]
print(answer1(x))

x = [[10, 14], [4, 18], [19, 20], [19, 20], [13, 20]]
print(answer1(x))

x = [[10, 14], [19, 20], [19, 20], [2, 4], [13, 17], [16, 20], [3, 5], [20, 21], [22, 23]]
print(answer1(x))

x = [[10, 14], [19, 20], [19, 27], [2, 4], [13, 17], [16, 20], [3, 5], [20, 21], [22, 23], [32, 45], [38, 44], [88, 89]]
print(answer1(x))

x = [[10, 12], [18, 21], [9, 27], [2, 4], [13, 17], [16, 20], [3, 5], [20, 21], [22, 23], [32, 45], [38, 44], [88, 89]]
print(answer1(x))