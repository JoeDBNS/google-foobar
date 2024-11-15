'''
Minion Labor Shifts / Minion Task Scheduling
==========

Commander Lambda's minions are upset! They're given the worst jobs on the whole space station,
and some of them are starting to complain that even those worst jobs are being allocated unfairly.
If you can fix this problem, it'll prove your chops to Commander Lambda so you can get promoted!

Minions' tasks are assigned by putting their ID numbers into a list, one time for each day they'll
work that task. As shifts are planned well in advance, the lists for each task will contain up
to 99 integers. When a minion is scheduled for the same task too many times, they'll complain about
it until they're taken off the task completely. Some tasks are worse than others, so the number of
scheduled assignments before a minion will refuse to do a task varies depending on the task. You
figure you can speed things up by automating the removal of the minions who have been assigned a
task too many times before they even get a chance to start complaining.

Write a function called answer(data, n) that takes in a list of less than 100 integers and a
number n, and returns that same list but with all of the numbers that occur more than n times
removed entirely. The returned list should retain the same ordering as the original list - you
don't want to mix up those carefully-planned shift rotations! For instance, if data
was [5, 10, 15, 10, 7] and n was 1, answer(data, n) would return the list [5, 15, 7] because 10
occurs twice, and thus was removed from the list entirely.


Test cases
==========

Inputs:
    (int list) data = [1, 2, 3]
    (int) n = 0
Output:
    (int list) []

Inputs:
    (int list) data = [1, 2, 2, 3, 3, 3, 4, 5, 5]
    (int) n = 1
Output:
    (int list) [1, 4]

Inputs:
    (int list) data = [1, 2, 3]
    (int) n = 6
Output:
    (int list) [1, 2, 3]
'''


def answer1(data, n):
    return(list(set([x for x in data if data.count(x) < n + 1])))


def answer2(data, n):
    new_list = []
    
    for val in data:
        if val not in new_list and data.count(val) < n+1:
            new_list.append(val)
            
    return(new_list)


def answer3(data, n):
    new_list = []
    
    data = [x for x in data if data.count(x) < n + 1]
    
    for val in data:
        if val not in new_list:
            new_list.append(val)
            
    return(new_list)


data = [1, 5, 5, 6, 2, 2, 3, 3, 3, 4, 5, 5]
n = 2
print(answer2(data, n))
print(answer3(data, n))
print()

data = [1, 2, 2, 3, 3, 3, 4, 5, 5, 6, 1, 7, 8, 9]
n = 1
print(answer2(data, n))
print(answer3(data, n))
print()

data = [5, 10, 15, 10, 7]
n = 1
print(answer2(data, n))
print(answer3(data, n))