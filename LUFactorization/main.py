import numpy
import copy

n = int(input())
matrixA = []

for i in range(n):
    x = input().split()
    c = []
    for j in range(n):
        c.append(float(x[j]))
    matrixA.append(c)

matrixA = numpy.array(matrixA)

matrixU = copy.deepcopy(matrixA)
xPivot = []
yPivot = []
yIndex = 0

LColumns = []
# row reduction for creating U matrix
for i in range(n):
    # find a staring row with pivot position
    if matrixU[i][i + yIndex] == 0:
        for j in range(i + 1, n):
            if matrixU[j][0] != 0:
                matrixU[[0, j]] = matrixU[[j, 0]]
                break

    if matrixU[i][i + yIndex] == 0:
        yIndex += 1
        continue

    xPivot.append(i)
    yPivot.append(i + yIndex)
    LColumns.append(list(copy.deepcopy(matrixU[i:, i + yIndex])))

    # row replacement operations to create
    # zeros in all positions below the pivot.
    for k in range(i + 1, n):
        if matrixU[k][i + yIndex] != 0:
            matrixU[k:k + 1] -= (matrixU[i:i + 1] * matrixU[k][i + yIndex]) / \
                                matrixU[i][i + yIndex]
print(matrixU)
print(matrixA)

# creating L matrix

matrixL = []
for i in range(n):
    c = []
    j = -1
    for j in range(i):
        c.append(0)
    column = LColumns[i]
    for k in range(0, n-j-1):
        c.append(column[k]/column[0])
    matrixL.append(c)

matrixL = numpy.column_stack(matrixL)
print(matrixL)

