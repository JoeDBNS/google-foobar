intervals1 = [[1, 3], [3, 6]]
intervals2 = [[10, 14], [4, 18], [19, 20], [19, 20], [13, 20]]
intervals3 = [[10, 14], [19, 20], [19, 20], [2, 4], [13, 17], [16, 20], [3, 5], [20, 21], [22, 23]]


def answer1(intervals):
    monitor_hours = {
        1 : False, 2 : False, 3 : False,
        4 : False, 5 : False, 6 : False,
        7 : False, 8 : False, 9 : False,
        10 : False, 11 : False, 12 : False,
        13 : False, 14 : False, 15 : False,
        16 : False, 17 : False, 18 : False,
        19 : False, 20 : False, 21 : False,
        22 : False, 23 : False, 24 : False
    }
    hourCount = 0
    for hourSet in intervals:
        for hour in range(hourSet[0], hourSet[1]):
            monitor_hours[hour] = True
    for key, value in monitor_hours.items():
        if value == True:
            hourCount += 1
    return hourCount


def answer2(intervals):
    monitor_hours = []
    for hourSet in intervals:
        for hour in range(hourSet[0], hourSet[1]):
            if hour not in monitor_hours:
                monitor_hours.append(hour)
    return len(monitor_hours)


def answer3(intervals):
    int_sorted = sorted(intervals)
    int_last = int_sorted[0]
    int_final = []
    
    x = 0
    while x < len(int_sorted) - 1:
        
        #print('{0}:{1}\t{2}\t{3}'.format(x, int_sorted[x], int_sorted[x+1], int_last))
        
        if int_sorted[x][1] >= int_last[0]:
            int_last = sorted({ min(int_last[0], int_sorted[x+1][0]), max(int_last[1], int_sorted[x+1][1]) })
            
        else:
            int_final.append(int_last)
            int_last = sorted({ int_sorted[x][0], int_sorted[x][1]} )
        
        x += 1
    
    if not int_final:
        int_final.append(int_last)
        
    elif int_final and int_final[len(int_final)] != int_last:
        int_final.append(int_last)

    return int_final


def answer4(intervals):
    int_sorted = sorted(intervals)
    int_last = int_sorted[0]
    int_final = []
    finalCount = 0
    
    x = 0
    while x < len(int_sorted):
        
        if int_last[1] >= int_sorted[x][0]:
            int_last = sorted({ min(int_last[0], int_sorted[x][0]), max(int_last[1], int_sorted[x][1]) })
            
        else:
            int_final.append(int_last)
            int_last = [ int_sorted[x][0], int_sorted[x][1] ]
        
        x += 1
    
    if not int_final:
        int_final.append(int_last)
        
    elif int_final and int_final[len(int_final)-1] != int_last:
        int_final.append(int_last)
    
    for key, value in int_final:
        finalCount += value - key

    return finalCount


def answer5(intervals):
    intervals = sorted(intervals)
    compPair = intervals[0]
    intervals_final = []
    finalCount = 0
    x = 1
    while x < len(intervals):
        if compPair[1] >= intervals[x][0]:
            compPair = sorted({ min(compPair[0], intervals[x][0]), max(compPair[1], intervals[x][1]) })
        else:
            intervals_final.append(compPair)
            compPair = [ intervals[x][0], intervals[x][1] ]
        x += 1
    intervals_final.append(compPair)
    for key, value in intervals_final:
        finalCount += value - key
    return finalCount

print(answer4(intervals1))
print(answer4(intervals2))
print(answer4(intervals3))
print()
print(answer5(intervals1))
print(answer5(intervals2))
print(answer5(intervals3))