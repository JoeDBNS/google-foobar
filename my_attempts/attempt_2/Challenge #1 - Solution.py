# minion_hierarchy



# The answer function will accept an int from 1-10 and returns
# an int that is the maximum number of employees with x being the
# number of rows in a hierarchy where each following tier
# can have at most 7 times the row above.
def answer(x):
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



# PROOF
n = 1
while n < 11:
    print(str(n) + ':', answer(n))
    n+=1