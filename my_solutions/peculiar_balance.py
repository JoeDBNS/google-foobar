'''
Peculiar Balance
================

Can we save them? Beta Rabbit is trying to break into a 
lab that contains the only known zombie cure - but there's 
an obstacle. The door will only open if a challenge is 
solved correctly. The future of the zombified rabbit 
population is at stake, so Beta reads the challenge: 
There is a scale with an object on the left-hand side, 
whose mass is given in some number of units. Predictably, 
the task is to  balance the two sides. But there is a 
catch: You only have this peculiar weight set, having 
masses 1, 3, 9, 27, ... units. That is, one  for each 
power of 3. Being a brilliant mathematician, Beta 
Rabbit quickly discovers that any number of units 
of mass can be balanced  exactly using this set. To 
help Beta get into the room, write a method called 
answer(x), which outputs a list of strings representing 
where the weights should be  placed, in order for the 
two sides to be balanced, assuming that weight on the 
left has mass x units. The first element of the output 
list should correspond to the 1-unit weight, the second 
element to the 3-unit weight, and so on. 
Each string is one of:
    "L" : put weight on left-hand side
    "R" : put weight on right-hand side
    "-" : do not use weight
To ensure that the output is the smallest possible, 
the last element of the list must not be "-". x will 
always be a positive integer, no larger than 1000000000.
'''


# https://math.stackexchange.com/questions/119606/represent-every-natural-number-as-a-summation-subtraction-of-distinct-power-of/119622#119622
# https://rosettacode.org/wiki/Balanced_ternary

def answer1(x):
    powerList = []
    result = ['R']
    
    # Generate powerList
    while True:
        powerIteration = 3**(len(powerList))
        if sum(powerList) + powerIteration >= x:
            powerList.append(powerIteration)
            break
        else:
            powerList.append(powerIteration)
    
    x -= powerList[len(powerList) - 1]
    powerList.pop()
    
    while powerList:
        curPowerListVal = powerList[len(powerList) - 1]
        
        if x >= curPowerListVal:
            x -= curPowerListVal
            result[0:0] = 'R'
            powerList.pop()
        elif x >= curPowerListVal - sum(powerList):
            x = curPowerListVal - x
            result[0:0] = 'L'
            powerList.pop()
        else:
            result[0:0] = '-'
            powerList.pop()
        
    return result


def answer2(x):
    powerList = []
    sumPowerList = [0]
    result = []
    # Generate powerList
    while True:
        powerIteration = 3**(len(powerList))
        if sum(powerList) + powerIteration >= x:
            powerList.append(powerIteration)
            powerList.append(3**(len(powerList) + 1))
            break
        else:
            powerList.append(powerIteration)
    for i in range(1, len(powerList)):
        sumPowerList.append(sum(powerList[0:i]))
    while x:
        curPowerListVal = powerList[len(powerList) - 1]
        if x >= curPowerListVal:
            x -= curPowerListVal
            result[0:0] = 'L'
        elif x >= curPowerListVal - sumPowerList[len(powerList) - 1]:
            x = curPowerListVal - x
            result[0:0] = 'R'
        else:
            result[0:0] = '-'
        powerList.pop()
    return result


def answer3(x):
    if x == 0: return([])
    if (x % 3) == 0: return(['-'] + answer3(x // 3))
    if (x % 3) == 1: return(['R'] + answer3(x // 3))
    if (x % 3) == 2: return(['L'] + answer3((x + 1) // 3))


def answer4(x):
    if x == 0:
        return([])
    
    if (x % 3) == 0:
        return(['-'] + answer3(x // 3))
    
    if (x % 3) == 1:
        return(['R'] + answer3(x // 3))
    
    if (x % 3) == 2:
        return(['L'] + answer3((x + 1) // 3))


def answer5(x):
    if x == 0:
        return([])
    
    if (x % 3) == 0:
        return(['-'] + answer5(x // 3))
    
    if (x % 3) == 1:
        return(['R'] + answer5(x // 3))
    
    if (x % 3) == 2:
        return(['L'] + answer5((x + 1) // 3))


for x in range(39, 40):
    print(x, ": ", answer5(x), end='\r')