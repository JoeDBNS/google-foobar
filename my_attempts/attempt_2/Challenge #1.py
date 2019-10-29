
def answer1(x):
    answer = 0
    levelValues = [1]
    
    while (x > 0):
        levelValue = levelValues[len(levelValues) - 1] * 7
        levelValues.append(levelValue)
        x -= 1
    
    for level in levelValues:
        answer += level
    
    return answer


def answer2(x):
    answer = 0
    prevValue = 1
    
    while (x > -1):
        answer += prevValue
        
        prevValue = prevValue * 7
        x -= 1
    
    return answer


# The answer function will accept an int from 1-10 and returns
# an int that is the maximum number of employees with x being the
# number of rows in a hierarchy where each following tier
# can have at most 7 times the row above.
def answer3(x):
    # Initialize variable for maximum employee count.
    # Variable starts at 1 as x will always have a first hierarchy row.
    maxEmployeeValue = 1
    
    # Holds the value for the previously evaluated hierarchy row. 
    # Variable starts at 1 as x will always have a first hierarchy row.
    prevRowValue = 1
    
    # For loop that iterates per number of rows in the hierarchy
    while (x > 0):
        # Evaluate hierarchy row's max employee count based on the
        # previous hierarchy row's value.
        prevRowValue *= 7
        
        # Add the result of the evaluated hierarchy row
        # to the final result variable
        maxEmployeeValue += prevRowValue
        
        # Subtract hierarchy row to progress For loop
        x -= 1
    
    # Return maximum employee count for evaluated rows
    return maxEmployeeValue


n = 1
while n < 11:
    print('\n' + str(n) + ':')
    print('one:', answer1(n))
    print('two:', answer2(n))
    print('thr:', answer3(n))
    n+=1