# zombit_monitoring



# The answer function will accept a list of pairs [start, end] where
# end > start and each value is between 1 and 2^30 - 1. Based on the
# provided list, the answer function will return an int that is the
# total number of unique hours that is found throughout all pairs.
def answer(intervals):
    # Sort the intervals list by pair start values.
    intervals = sorted(intervals)
    
    # Holds the value of the comparison pair.
    # Initialized with value of the first sorted intervals pair.
    compPair = intervals[0]
    
    # Holds final pairs list with all overlaping pair values combined.
    intervals_final = []
    
    # Holds final count of unique hours based on final pairs list.
    finalCount = 0
    
    # While loop that iterates through sorted interval pairs
    # starting with the second pair.
    x = 1
    while x < len(intervals):
        
        # If current pair and comparison pair overlap,
        if compPair[1] >= intervals[x][0]:
            # Set comparison pair equal to earliest start and
            # latest end values in overlaping pairs.
            compPair = sorted({ 
                min(compPair[0], intervals[x][0]), 
                max(compPair[1], intervals[x][1]) 
            })
        
        # If current pair and comparison pair do not overlap,
        else:
            # Append comparison pair to final pairs list.
            intervals_final.append(compPair)
            
            # Set comparison pair equal to current pair.
            compPair = [ intervals[x][0], intervals[x][1] ]
        
        # Progress while loop.
        x += 1
    
    # Append final comparison pair to final pairs list.
    intervals_final.append(compPair)
    
    # For loop that iterates through final pairs list.
    for key, value in intervals_final:
        # Subtract pair's start value from end value and 
        # add to final unique hour count.
        finalCount += value - key

    # Return total number of unique hours found throughout all pairs.
    return finalCount



# PROOF:
intervals1 = [[1, 3], [3, 6]]
intervals2 = [[10, 14], [4, 18], [19, 20], [19, 20], [13, 20]]
intervals3 = [[10, 14], [19, 20], [19, 20], [2, 4], [13, 17], [16, 20], [3, 5], [20, 21], [22, 23]]
intervals4 = [[10, 14], [19, 20], [19, 27], [2, 4], [13, 17], [16, 20], [3, 5], [20, 21], [22, 23], [32, 45], [38, 44], [88, 89]]
intervals5 = [[10, 12], [18, 21], [19, 27], [2, 4], [13, 17], [16, 20], [3, 5], [20, 21], [22, 23], [32, 45], [38, 44], [88, 89]]

print('1:', answer(intervals1))
print('2:', answer(intervals2))
print('3:', answer(intervals3))
print('4:', answer(intervals4))
print('5:', answer(intervals5))