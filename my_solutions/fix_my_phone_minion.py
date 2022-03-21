'''
Fix My Phone, Minion!
=====================

"She escaped? This can't be happening! Get me the security team!"

Professor Boolean, a notorious mad scientist, just found out his 
precious rabbit specimen has escaped! He rushes to call
his security minions on the lab phone. However, the rabbit escapee 
hacked the phone to speed her escape! She left a sign
with the following clues: Each digit that is dialed has to be a 
number that can be reached by a knight chess piece from
the last digit dialed - that is, you must move precisely 2 spaces 
in one direction, and then 1 space in a perpendicular
direction to dial the next correct number. You can dial any number 
you want to start with, but subsequent numbers must
obey the knight's move rule.

The lab phone has the numbers arranged in the following way: 
1, 2, 3 in the first row; 
4, 5, 6 in the second row; 
7, 8, 9 in the third row; 
and blank, 0, blank in the fourth row.

123
456
789
 0 

For example, if you just dialed a 1, the next number you 
dial has to be either a 6 or an 8.  If you just dialed a 6, the
next number must be a 1 or 7.

Professor Boolean wants you to find out how many different 
phone numbers he can dial under these conditions. Write a
function called answer(x, y, z) that computes the number of 
phone numbers one can dial that start with the digit x, end
in the digit y, and consist of z digits in total. Output this 
number as a string representing the number in base-10.

x and y will be digits from 0 to 9. z will be between 1 and 100, inclusive.
'''


options_dict = {
    1: [ 6, 8 ],
    2: [ 7, 9 ],
    3: [ 8, 4 ],
    4: [ 3, 9, 0 ],
    5: [],
    6: [ 1, 7, 0 ],
    7: [ 2, 6 ],
    8: [ 1, 3 ],
    9: [ 2, 4 ],
    0: [ 4, 6 ]
}

options_dict_string = {
    '1': [ '6', '8' ],
    '2': [ '7', '9' ],
    '3': [ '8', '4' ],
    '4': [ '3', '9', '0' ],
    '5': [],
    '6': [ '1', '7', '0' ],
    '7': [ '2', '6' ],
    '8': [ '1', '3' ],
    '9': [ '2', '4' ],
    '0': [ '4', '6' ]
}

def answer1(start, end, count):
    srt = str(start)
    end = str(end)
    depth = 0
    paths = [srt]
    
    for path in paths:
        for option in options_dict_string[path[-1]]:
            paths.append(path + option)
        
        if len(paths[-1]) > count:
            del paths[-1]
            break
    
    return len([p for p in paths if len(p) == count and p[-1:] == end])


def answer2(start, end, count):
    srt = str(start)
    end = str(end)
    init = [srt]
    
    while len(init[0]) < count:
        nxtInit = []
        for x in init:
            for y in options_dict_string[x[-1]]:
                nxtInit.append(x + y)
        
        init = nxtInit
    
    return len([p for p in init if p[-1:] == end])


def answer3(start, end, count):
    srt = str(start)
    end = str(end)
    paths = [srt]
    i = 1
    
    while i < count:
        tmpPaths = []
        for path in paths:
            for val in options_dict_string[path]:
                tmpPaths.append(val)
        
        paths = tmpPaths
        i += 1
    
    return len([p for p in paths if p == end])


def answer4(start_val, end_val, max_count):
    end_val = str(end_val)
    attempts = [str(start_val)]
    working_attempts = []
    completed_attmepts = []
    matching_attempts = []

    while len(attempts) > 0:
        for index, attempt in enumerate(attempts):
            if len(attempt) == max_count:
                completed_attmepts.append(attempt)
                del attempts[index]
            else:
                for next_step in options_dict_string[attempt[-1]]:
                    working_attempts.append(attempt + next_step)

        attempts = working_attempts
        working_attempts = []
    
    for attempt in completed_attmepts:
        if attempt[-1] == end_val:
            matching_attempts.append(attempt)

    return len(matching_attempts)


def answer5(start_val, end_val, max_count):
    end_val = str(end_val)
    attempts = [str(start_val)]
    next_steps = []

    iter_count = -1
    while iter_count < max_count:
        for attempt in attempts:
            for next_step in options_dict_string[attempt]:
                next_steps.append(next_step)
        attempts = next_steps
        next_steps = []
        iter_count += 1

    return attempts.count(end_val)


def answer6(start_val, end_val, max_count):
    path_count = { 0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0 }
    path_count[start_val] = 1

    i = 1
    while i < max_count:
        temp_path_count = { 0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0 }
        for path, cnt in path_count.items():
            for val in options_dict[path]:
                temp_path_count[val] += cnt

        path_count = temp_path_count
        i += 1

    print(path_count)

    return path_count[end_val]

print(answer6(0, 6, 3))
print(answer6(6, 4, 4))
print(answer6(1, 2, 4))
print(answer6(0, 4, 2))
print(answer6(6, 4, 7))
print(answer6(2, 4, 98))
print(answer6(0, 6, 6))
