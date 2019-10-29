'''
Prepare The Bunnies' Escape
=====================

You'ew awfully close to destroying the LAMBCHOP doomsday device and freeing Commander Lambda's bunny prisoners, 
but once they're free of the prison blocks, the bunnies are going to need to escape Lambda's space station via 
the escape pods as quickly as possible. Unfortunately, the halls of the space station are a maze of corridors 
and dead ends that will be a deathtrap for the escaping bunnies. Fortunately, Commander Lambda has put you in 
charge of a remodeling project that will give you the opportunity to make things a little easier for the bunnies. 
Unfortunately (again), you can't just remove all obstacles between the bunnies and the escape pods - at most you 
can remove one wall per escape pod path, both to maintain structural integrity of the station and to avoid arousing 
Commander Lambda's suspicions.

You have maps of parts of the space station, each starting at a prison exit and ending at the door to an escape pod. 
The map is represented as a matrix of 0s and 1s, where 0s are passable space and 1s are impassable walls. The door 
out of the prison is at the top left (0, 0) and the other door into the escape pod is at the bottom right (w-1, h-1).

Write a function answer(map) that generates the length of the shortest path from the prison door to the escape pod, 
where you are allowed to remove one wall as part of your remodeling plans. The path length is the total number of nodes 
you pass through, counting both the entrance and exit nodes. The starting and ending positions are always passable (0). 
The map will always be solvable, though you may or may not need to remove a wall. The height and width of the map can 
be from 2 to 20. Moves can only be made in cardinal directions; no diagonal moves are allowed.


Test cases
=====================

Inputs:
    (int) maze = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
Output:
    (int) 7

Inputs:
    (int) maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
Output:
    (int) 11
'''


def answer1(maze):
    paths = [[[0, 0]]]
    
    brkfor = 0
    while brkfor == 0:
        tmpPaths = []
        for path in paths:
            if path[-1] != [len(maze)-1, len(maze[0])-1]:
                if path[-1][0]-1 > -1 and maze[path[-1][0]-1][path[-1][1]] == 0:
                    tmpPaths.append(path + [[path[-1][0]-1, path[-1][1]]])
                    
                if path[-1][0]+1 < len(maze) and maze[path[-1][0]+1][path[-1][1]] == 0:
                    tmpPaths.append(path + [[path[-1][0]+1, path[-1][1]]])
                    
                if path[-1][1]-1 > -1 and maze[path[-1][0]][path[-1][1]-1] == 0:
                    tmpPaths.append(path + [[path[-1][0], path[-1][1]-1]])
                    
                if path[-1][1]+1 < len(maze[0]) and maze[path[-1][0]][path[-1][1]+1] == 0:
                    tmpPaths.append(path + [[path[-1][0], path[-1][1]+1]])
            else:
                brkfor = 1
                paths = path + [[len(maze)-1, len(maze[0])-1]]
        
        if brkfor != 1:
            paths = tmpPaths
    
    return(len(paths)-1, paths)


def answer2(maze):
    paths = [[[0, 0]]]
    
    brkfor = 0
    while brkfor == 0:
        tmpPaths = []
        for path in paths:
            if path[-1] != [len(maze)-1, len(maze[0])-1]:
                if path[-1][0]-1 > -1 and maze[path[-1][0]-1][path[-1][1]] == 0 and [path[-1][0]-1, path[-1][1]] not in path:
                    tmpPaths.append(path + [[path[-1][0]-1, path[-1][1]]])
                    
                if path[-1][0]+1 < len(maze) and maze[path[-1][0]+1][path[-1][1]] == 0 and [path[-1][0]+1, path[-1][1]] not in path:
                    tmpPaths.append(path + [[path[-1][0]+1, path[-1][1]]])
                    
                if path[-1][1]-1 > -1 and maze[path[-1][0]][path[-1][1]-1] == 0 and [path[-1][0], path[-1][1]-1] not in path:
                    tmpPaths.append(path + [[path[-1][0], path[-1][1]-1]])
                    
                if path[-1][1]+1 < len(maze[0]) and maze[path[-1][0]][path[-1][1]+1] == 0 and [path[-1][0], path[-1][1]+1] not in path:
                    tmpPaths.append(path + [[path[-1][0], path[-1][1]+1]])
            else:
                brkfor = 1
                paths = path + [[len(maze)-1, len(maze[0])-1]]
        
        if brkfor != 1:
            paths = tmpPaths
    
    return(len(paths)-1, paths)


def answer3(maze):
    mazeLenY = len(maze)
    mazeLenX = len(maze[0])
    paths = [[[0, 0, False]]]
    
    brkfor = 0
    while brkfor == 0:
        tmpPaths = []
        for path in paths:
            if path[-1][0:2] != [mazeLenY-1, mazeLenX-1]:
                lastPathY = path[-1][0]
                lastPathX = path[-1][1]
                lastPathZ = path[-1][2]
                
                # +1
                if lastPathY-1 > -1 and maze[lastPathY-1][lastPathX] == 0 and [lastPathY-1, lastPathX] not in path:
                    tmpPaths.append(path + [[lastPathY-1, lastPathX, lastPathZ]])
                    
                if lastPathY+1 < mazeLenY and maze[lastPathY+1][lastPathX] == 0 and [lastPathY+1, lastPathX] not in path:
                    tmpPaths.append(path + [[lastPathY+1, lastPathX, lastPathZ]])
                    
                if lastPathX-1 > -1 and maze[lastPathY][lastPathX-1] == 0 and [lastPathY, lastPathX-1] not in path:
                    tmpPaths.append(path + [[lastPathY, lastPathX-1, lastPathZ]])
                    
                if lastPathX+1 < mazeLenX and maze[lastPathY][lastPathX+1] == 0 and [lastPathY, lastPathX+1] not in path:
                    tmpPaths.append(path + [[lastPathY, lastPathX+1, lastPathZ]])


                # +2 (straight path)
                if lastPathY-2 > -1 and maze[lastPathY-1][lastPathX] == 1 and maze[lastPathY-2][lastPathX] == 0 and [lastPathY-1, lastPathX] not in path and lastPathZ != True:
                    tmpPaths.append(path + [[lastPathY-1, lastPathX, True]] + [[lastPathY-2, lastPathX, True]])
                    
                if lastPathY+2 < mazeLenY and maze[lastPathY+1][lastPathX] == 1 and maze[lastPathY+2][lastPathX] == 0 and [lastPathY+1, lastPathX] not in path and lastPathZ != True:
                    tmpPaths.append(path + [[lastPathY+1, lastPathX, True]] + [[lastPathY+2, lastPathX, True]])
                    
                if lastPathX-2 > -1 and maze[lastPathY][lastPathX-1] == 1 and maze[lastPathY][lastPathX-2] == 0 and [lastPathY, lastPathX-1] not in path and lastPathZ != True:
                    tmpPaths.append(path + [[lastPathY, lastPathX-1, True]] + [[lastPathY, lastPathX-2, True]])
                    
                if lastPathX+2 < mazeLenX and maze[lastPathY][lastPathX+1] == 1 and maze[lastPathY][lastPathX+2] == 0 and [lastPathY, lastPathX+1] not in path and lastPathZ != True:
                    tmpPaths.append(path + [[lastPathY, lastPathX+1, True]] + [[lastPathY, lastPathX+2, True]])

            else:
                brkfor = 1
                paths = path + [[mazeLenY-1, mazeLenX-1]]
        
        if brkfor != 1:
            paths = tmpPaths
    
    return(len(paths)-1, paths)






def Test_answer(testCase, maze, passVal):
    retVal = answer3(maze)
    if retVal[0] == passVal:
        print('Test Case', testCase, ':\tPass')
    else:
        print('\nTest Case', testCase, ':\tFail')
        print('Correct:', passVal)
        print('Actual:\t', retVal[0])
        print('Path:\t', retVal[1], '\n')





testCase = 1
#[
#    [0, 1, 1, 0], 
#    [0, 0, 0, 1], 
#    [1, 1, 0, 0], 
#    [1, 1, 1, 0]
#]
maze = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
passVal = 7
Test_answer(testCase, maze, passVal)



testCase = 2
#[
#    [0, 0, 0, 0, 0, 0], 
#    [1, 1, 1, 1, 1, 0], 
#    [0, 0, 0, 0, 0, 0], 
#    [0, 1, 1, 1, 1, 1], 
#    [0, 1, 1, 1, 1, 1], 
#    [0, 0, 0, 0, 0, 0]
#]
maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
passVal = 11
Test_answer(testCase, maze, passVal)



testCase = 3
#[
#    [0, 0, 0, 0, 0, 0], 
#    [1, 0, 1, 1, 1, 0], 
#    [0, 0, 0, 0, 0, 0], 
#    [0, 1, 1, 1, 0, 1], 
#    [0, 1, 1, 1, 1, 1], 
#    [0, 0, 0, 0, 0, 0]
#]
maze = [[0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
passVal = 11
Test_answer(testCase, maze, passVal)



testCase = 4
#[
   #[0, 0, 0, 0, 0, 0], 
   #[1, 0, 1, 1, 1, 0], 
   #[1, 0, 0, 1, 0, 1], 
   #[0, 1, 0, 1, 1, 1], 
   #[0, 1, 1, 0, 0, 0], 
   #[0, 0, 0, 0, 1, 0]
#]
maze = [[0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 1, 1, 1], [0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0]]
passVal = 11
Test_answer(testCase, maze, passVal)