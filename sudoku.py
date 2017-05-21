

puzzle = [
        [0,3,7,5,0,0,4,9,6],
        [0,9,4,6,7,3,0,0,0],
        [6,5,2,0,0,0,3,1,7],
        [9,0,5,7,0,6,0,8,3],
        [0,8,3,0,1,5,9,6,0],
        [0,6,1,3,8,9,7,0,5],
        [0,0,6,0,5,0,0,3,0],
        [5,0,9,8,3,0,6,7,0],
        [3,0,8,0,6,7,0,0,0]
        ]

candidates =[
        [[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[]],
        [[],[],[],[],[],[],[],[],[]]
        ]

zeroCounter = 0

#print([i[3] for i in puzzle])
def findCandidates():
    zeroCounter = 0
    for i in range(9):
        for j in range(9):           
            if puzzle[i][j] == 0:
                sq = findMySquare(i, j)
                zeroCounter += 1
                for k in range(9):
                    if k+1 not in puzzle[i] and k+1 not in [x[j] for x in puzzle] and k+1 not in [b for a in sq for b in a]:
                        if k+1 not in candidates[i][j]:
                            candidates[i][j].append(k+1)
    return zeroCounter

def solve():
    for i in range(9):
        for j in range(9):
            if len(candidates[i][j]) == 1:
                puzzle[i][j] = candidates[i][j][0]
                del candidates[i][j][0]
    for a in range(9):
        for b in range(9):
            candidates[a][b].clear()

#findMySquare
def findMySquare(a, b):
    if a >= 0 and a <= 2:
        if b >=0 and b <= 2:
            return [x[:3] for x in puzzle[:3]]
        elif b >= 3 and b <= 5:
            return [x[3:6] for x in puzzle[:3]]
        else:
            return [x[6:] for x in puzzle[:3]]
    elif a >=3 and a <=5:
        if b >=0 and b <= 2:
            return [x[:3] for x in puzzle[3:6]]
        elif b >= 3 and b <= 5:
            return [x[3:6] for x in puzzle[3:6]]
        else:
            return [x[6:] for x in puzzle[3:6]]
    else:
        if b >=0 and b <= 2:
            return [x[:3] for x in puzzle[6:]]
        elif b >= 3 and b <= 5:
            return [x[3:6] for x in puzzle[6:]]
        else:
            return [x[6:] for x in puzzle[6:]]

#printIt
def printIt(x):
    for i in range(len(x)):
        print(x[i])


zeroCounter = findCandidates()
lastZeroCounter = 0

for i in range(100):
    if zeroCounter == 0:
        print('Solved!!!')
        printIt(puzzle)
        break

    if lastZeroCounter == zeroCounter:
        print('I give up!!!')
        break

    lastZeroCounter = zeroCounter
    printIt(puzzle)
    print('There are',zeroCounter,'zeros')
    solve()
    zeroCounter = findCandidates()










