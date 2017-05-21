

puzzle = [
        [3,0,0,5,0,0,0,0,0],
        [0,5,0,0,3,0,8,0,4],
        [0,0,0,7,0,0,0,6,5],
        [8,4,0,0,1,0,0,5,0],
        [0,0,0,0,0,0,6,1,0],
        [9,3,0,0,8,0,0,2,0],
        [0,0,0,4,0,0,0,3,6],
        [0,2,0,0,6,0,7,0,1],
        [7,0,0,8,0,0,0,0,0]
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

notCandidates =[
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
    clearCandidates()
    for i in range(9):
        for j in range(9):           
            if puzzle[i][j] == 0:
                sq = findMySquare(i, j)
                zeroCounter += 1
                for k in range(9):
                    if k+1 not in puzzle[i] and k+1 not in [x[j] for x in puzzle] and k+1 not in [b for a in sq for b in a]:
                        if k+1 not in candidates[i][j] and k+1 not in notCandidates[i][j]:
                            candidates[i][j].append(k+1)
    return zeroCounter

def clearCandidates():
    for a in range(9):
        for b in range(9):
            candidates[a][b].clear()

def solve():
    for i in range(9):
        for j in range(9):
            if len(candidates[i][j]) == 1:
                puzzle[i][j] = candidates[i][j][0]
                del candidates[i][j][0]
    clearCandidates()

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

#insertIntoRows
def insertIntoRows(row,column,value):
    puzzle[row][column] = value
    candidates[row][column].clear()
    return


#findPosAndInsertValue
def findPosAndInsertValue(box,row,column,value):
    if box == 1:
        puzzle[row][column] = value
        candidates[row][column].clear()
        return
    elif box == 2:
        puzzle[row][column + 3] = value
        candidates[row][column + 3].clear()
        return
    elif box == 3:
        puzzle[row][column + 6] = value
        candidates[row][column + 6].clear()
        return
    elif box == 4:
        puzzle[row + 3][column] = value
        candidates[row + 3][column].clear()
        return
    elif box == 5:
        puzzle[row + 3][column + 3] = value
        candidates[row + 3][column + 3].clear()
        return
    elif box == 6:
        puzzle[row + 3][column + 6] = value
        candidates[row + 3][column + 6].clear()
        return
    elif box == 7:
        puzzle[row + 6][column] = value
        candidates[row + 6][column].clear()
        return
    elif box == 8:
        puzzle[row + 6][column + 3] = value
        candidates[row + 6][column + 3].clear()
        return
    elif box == 9:
        puzzle[row + 6][column + 6] = value
        candidates[row + 6][column + 6].clear()
        return
    else:
        print('Not a valid box!!!')

#ifOnlyOneInColumn
def ifOnlyOneInColumn(columns):
    z3 = 10
    x3 = 10

    k = 1
    for i in columns:
        for j in range(1,10):
            if sum(x.count(j) for x in i) == 1:
                #print('There is', sum(x.count(j) for x in i),str(j) + ' in column',k)
                for x in i:
                    if j in x:
                        z3 = i.index(x)
                        x3 = columns.index(i)
                        insertIntoRows(z3,x3,j)
        k += 1

    zeroCounter = findCandidates()
########################################################################################
#ifOnlyOneInRow
def ifOnlyOneInRow(rows):
    z2 = 10
    x2 = 10

    k = 1
    for i in rows:
        for j in range(1,10):
            if sum(x.count(j) for z in i for x in z) == 1:
                #print('There is',sum(x.count(j) for z in i for x in z),str(j) + ' in row',k)
                for z in i:
                    for x in z:
                        if j in i[i.index(z)][z.index(x)]:
                            z2 = i.index(z)
                            x2 = z.index(x)
                            insertIntoRows(k-1, x2, j)

        k += 1
    zeroCounter = findCandidates()
##########################################################################################
#ifOnlyOneInBox
def ifOnlyOneInBox(boxes):
    k = 1
    
    z1 = 10
    x1 = 10

    for i in boxes:
        for j in range(1,10):
            if sum(x.count(j) for z in i for x in z) == 1:
                #print('There is',sum(x.count(j) for z in i for x in z),str(j) + ' in box',k)
                for z in i:
                    for x in z:
                        if j in i[i.index(z)][z.index(x)]:
                            z1 = i.index(z)
                            x1 = z.index(x)
                            #print(i.index(z),z.index(x))
                            findPosAndInsertValue(k,z1,x1,j)
                            #k=box, z1=row, x1=column
        k += 1
    zeroCounter = findCandidates()
#################################################################################################
#candidateTrimmingRow
def candidateTrimmingRow(boxes):
    boxNumber = 1

    for i in boxes:
        for j in range(1,10):
            if j in i[0] and j not in i[1] and j not in i[2]:
                #remove from candidates and insert into not candidates
                if boxNumber == 1:
                    #remove j from candidates[0][3:]
                    candidates[0][3:].remove(j)
                    notCandidates[0][3:].append(j)
                    printIt(notCandidates)
                elif boxNumber == 2:
                    #remove j from candidates[0][:3] and candidates[0][6:]
                    candidates[0][:3].remove(j)
                    candidates[0][6:].remove(j)
                    notCandidates[0][:3].append(j)
                    notCandidates[0][6:].append(j)
                    printIt(notCandidates)
                elif boxNumber == 3:
                    #remove j from candidates[0][:6]
                    candidates[0][:6].remove(j)
                    notCandidates[0][:6].append(j)
                    printIt(notCandidates)
                elif boxNumber == 4:
                    #remove j from candidates[3][3:]
                    candidates[3][3:].remove(j)
                    notCandidates[3][3:].append(j)
                    printIt(notCandidates)
                elif boxNumber == 5:
                    #remove j from candidates[3][:3] and candidates[3][6:]
                    candidates[3][:3].remove(j)
                    candidates[3][6:].remove(j)
                    notCandidates[3][:3].append(j)
                    notCandidates[3][6:].append(j)
                    printIt(notCandidates)
                elif boxNumber == 6:
                    #remove j from candidates[3][:6]
                    candidates[3][:6].remove(j)
                    notCandidates[3][:6].append(j)
                    printIt(notCandidates)
                elif boxNumber == 7:
                    #remove j from candidates[6][3:]
                    candidates[6][3:].remove(j)
                    notCandidates[6][3:].append(j)
                    printIt(notCandidates)
                elif boxNumber == 8:
                    #remove j from candidates[6][:3] and candidates[6][6:]
                    candidates[6][:3].remove(j)
                    candidates[6][6:].remove(j)
                    notCandidates[6][:3].append(j)
                    notCandidates[6][6:].append(j)
                    printIt(notCandidates)
                elif boxNumber == 9:
                    #remove j from candidates[6][:6]
                    candidates[6][:6].remove(j)
                    notCandidates[6][:6].append(j)
                    printIt(notCandidates)
            elif j in i[1] and j not in i[0] and j not in i[2]:
                #remove from candidates and insert into not candidates
                if boxNumber == 1:
                    #remove j from candidates[1][3:]
                    candidates[1][3:].remove(j)
                    notCandidates[1][3:].append(j)
                    printIt(notCandidates)
                elif boxNumber == 2:
                    #remove j from candidates[1][0:3] and candidates[1][6:]
                    candidates[1][:3].remove(j)
                    candidates[1][6:].remove(j)
                    notCandidates[1][:3].append(j)
                    notCandidates[1][6:].append(j)
                    printIt(notCandidates)
                elif boxNumber == 3:
                    #remove j from candidates[1][:6]
                    candidates[1][:6].remove(j)
                    notCandidates[1][:6].append(j)
                    printIt(notCandidates)
                elif boxNumber == 4:
                    #remove j from candidates[4][3:]
                    candidates[4][3:].remove(j)
                    notCandidates[4][3:].append(j)
                    printIt(notCandidates)
                elif boxNumber == 5:
                    #remove j from candidates[4][:3] and candidates[4][6:]
                    candidates[4][:3].remove(j)
                    candidates[4][6:].remove(j)
                    notCandidates[4][:3].append(j)
                    notCandidates[4][6:].append(j)
                    printIt(notCandidates)
                elif boxNumber == 6:
                    #remove j from candidates[4][:6]
                    candidates[4][:6].remove(j)
                    notCandidates[4][:6].append(j)
                    printIt(notCandidates)
                elif boxNumber == 7:
                    #remove j from candidates[7][3:]
                    candidates[7][3:].remove(j)
                    notCandidates[7][3:].append(j)
                    printIt(notCandidates)
                elif boxNumber == 8:
                    #remove j from candidates[7][:3] and candidates[7][6:]
                    candidates[7][:3].remove(j)
                    candidates[7][6:].remove(j)
                    notCandidates[7][:3].append(j)
                    notCandidates[7][6:].append(j)
                    printIt(notCandidates)
                elif boxNumber == 9:
                    #remove j from candidates[7][:6]
                    candidates[7][:6].remove(j)
                    notCandidates[7][:6].append(j)
                    printIt(notCandidates)
            elif j in i[2] and j not in i[0] and j not in i[1]:
                #remove from candidates and insert into not candidates
                if boxNumber == 1:
                    #remove j from candidates[2][3:]
                    candidates[2][3:].remove(j)
                    notCandidates[2][3:].append(j)
                    printIt(notCandidates)
                elif boxNumber == 2:
                    #remove j from candidates[2][0:3] and candidates[2][6:]
                    candidates[2][:3].remove(j)
                    candidates[2][6:].remove(j)
                    notCandidates[2][:3].append(j)
                    notCandidates[2][6:].append(j)
                    printIt(notCandidates)
                elif boxNumber == 3:
                    #remove j from candidates[2][:6]
                    candidates[2][:6].remove(j)
                    notCandidates[2][:6].append(j)
                    printIt(notCandidates)
                elif boxNumber == 4:
                    #remove j from candidates[5][3:]
                    candidates[5][3:].remove(j)
                    notCandidates[5][3:].append(j)
                    printIt(notCandidates)
                elif boxNumber == 5:
                    #remove j from candidates[5][:3] and candidates[5][6:]
                    candidates[5][:3].remove(j)
                    candidates[5][6:].remove(j)
                    notCandidates[5][:3].append(j)
                    notCandidates[5][6:].append(j)
                    printIt(notCandidates)
                elif boxNumber == 6:
                    #remove j from candidates[5][:6]
                    candidates[5][:6].remove(j)
                    notCandidates[5][:6].append(j)
                    printIt(notCandidates)
                elif boxNumber == 7:
                    #remove j from candidates[8][3:]
                    candidates[8][3:].remove(j)
                    notCandidates[8][3:].append(j)
                    printIt(notCandidates)
                elif boxNumber == 8:
                    #remove j from candidates[8][:3] and candidates[8][6:]
                    candidates[8][:3].remove(j)
                    candidates[8][6:].remove(j)
                    notCandidates[8][:3].append(j)
                    notCandidates[8][6:].append(j)
                    printIt(notCandidates)
                elif boxNumber == 9:
                    #remove j from candidates[8][:6]
                    candidates[8][:6].remove(j)
                    notCandidates[8][:6].append(j)
                    printIt(notCandidates)

        boxNumber += 1
    zeroCounter = findCandidates()
#############################################################################
#processOfElimination
def processOfElimination():
    
    ################################
    # Boxes 1 # if only one in box #
    ################################

    b1 = [x[:3] for x in candidates[:3]]
    b2 = [x[3:6] for x in candidates[:3]]
    b3 = [x[6:] for x in candidates[:3]]
    b4 = [x[:3] for x in candidates[3:6]]
    b5 = [x[3:6] for x in candidates[3:6]]
    b6 = [x[6:] for x in candidates[3:6]]
    b7 = [x[:3] for x in candidates[6:]]
    b8 = [x[3:6] for x in candidates[6:]]
    b9 = [x[6:] for x in candidates[6:]]

    boxes = [b1,b2,b3,b4,b5,b6,b7,b8,b9]
    
    ifOnlyOneInBox(boxes)

    ##################################
    # Boxes 2 # candidateTrimmingRow #
    ##################################

    candidateTrimmingRow(boxes)
    
    ##################################
    # Boxes 3 # candidateTrimmingCol #
    ##################################
    #TODO
    #candidateTrimmingCol(boxes)
    
    #############################
    # Rows # if only one in row #
    #############################
    r1 = [candidates[0]]
    r2 = [candidates[1]]
    r3 = [candidates[2]]
    r4 = [candidates[3]]
    r5 = [candidates[4]]
    r6 = [candidates[5]]
    r7 = [candidates[6]]
    r8 = [candidates[7]]
    r9 = [candidates[8]]
    
    rows = [r1,r2,r3,r4,r5,r6,r7,r8,r9]
    
    ifOnlyOneInRow(rows)

    ###################################
    # Columns # if only one in column #
    ###################################

    c1 = [x[0] for x in candidates[:]]
    c2 = [x[1] for x in candidates[:]]
    c3 = [x[2] for x in candidates[:]]
    c4 = [x[3] for x in candidates[:]]
    c5 = [x[4] for x in candidates[:]]
    c6 = [x[5] for x in candidates[:]]
    c7 = [x[6] for x in candidates[:]]
    c8 = [x[7] for x in candidates[:]]
    c9 = [x[8] for x in candidates[:]]

    columns = [c1,c2,c3,c4,c5,c6,c7,c8,c9]

    ifOnlyOneInColumn(columns)

#############################################
#testing
#findCandidates()
#printIt(puzzle)
#printIt(candidates)
#processOfElimination()

def main():
    zeroCounter = findCandidates()
    lastZeroCounter = 0

    for i in range(100):
        if zeroCounter == 0:
            print('Solved!!!')
            printIt(puzzle)
            break

        if lastZeroCounter == zeroCounter:
            print('calling POE!!!')
            processOfElimination()
            zeroCounter = findCandidates()
            if lastZeroCounter == zeroCounter:
                print('I give up!!!')
                
                printIt(candidates)

                break

        lastZeroCounter = zeroCounter
        printIt(puzzle)
        print('There are',zeroCounter,'zeros')
        solve()
        zeroCounter = findCandidates()




main()





