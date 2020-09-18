from sys import stdin

def spiralPrint(mat, nRows, mCols):
    startRow, startCol, endRow, endCol = 0, 0, nRows-1, mCols-1
    while startRow<=endRow and startCol<=endCol:
        # Print startRow 
        for j in range(startCol, endCol+1): 
            print(mat[startRow][j], end=' ')
        startRow += 1
        if startRow>endRow or startCol>endCol: 
            break 
        # Print endCol 
        for i in range(startRow, endRow+1): 
            print(mat[i][endCol], end=' ') 
        endCol -= 1 
        if startRow>endRow or startCol>endCol: 
            break 
        for j in range(endCol, startCol-1, -1):
            print(mat[endRow][j], end=' ')
        endRow -= 1 
        if startRow>endRow or startCol>endCol:
            break 
        # Print startCol 
        for i in range(endRow, startRow-1, -1): 
            print(mat[i][startCol], end=' ') 
        startCol += 1 
#Taking Input Using Fast I/O
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    mat, nRows, mCols = take2DInput()
    spiralPrint(mat, nRows, mCols)
    print()

    t -= 1
