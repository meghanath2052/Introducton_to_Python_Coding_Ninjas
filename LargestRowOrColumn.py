'''
    In order to print two or more integers in a line separated by a single 
    space then you may consider printing it with the statement, 

    print(str(num1) + " " + str(num2))

'''

from sys import stdin

def findLargest(arr, nRows, mCols):
    rowmax = -2147483648
    rowindex = 0
    for i in range(nRows):
        sum = 0
        for j in range(mCols):
            sum = sum + arr[i][j]
        if sum > rowmax:
            rowmax = sum
            rowindex = i
    colmax = -2147483648
    colindex = 0
    for i in range(mCols):
        sum = 0
        for j in range(nRows):
            sum = sum + arr[j][i]
        if sum > colmax:
            colmax = sum
            colindex = i
    if rowmax >= colmax:
        print("row" + " " + str(rowindex) + " " + str(rowmax))
    else:
        print("column" + " " + str(colindex) + " " + str(colmax))
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
    findLargest(mat, nRows, mCols)

    t -= 1
