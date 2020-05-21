import numpy
from rowReduction import echelonForm
from numpy.linalg import svd

x = input().split()
m, n = int(x[0]), int(x[1])

# read matrix from console
matrix = []
for i in range(m):
    x = input().split()
    c = []
    for j in range(n):
        c.append(float(x[j]))

    matrix.append(c)

matrix = numpy.array(matrix)

c =[]
for i in range(m):
    c.append(float(0))

zeroMatrix = []
zeroMatrix.append(c)
zeroMatrix = numpy.array(zeroMatrix).reshape(m, 1)
augmentedMatrix = numpy.concatenate((matrix, zeroMatrix), axis=1)
pivots = echelonForm(m, n, augmentedMatrix)
xPivots = pivots[0]
yPivots = pivots[1]
print("Matrix: ")
print(matrix)
print()
print("Echelon:")
print(augmentedMatrix)
print()

nullSpace = []

# to find the null space bases we need to find the linear combination of variables and try to find
# the vectors of variable coefficients
print("Null Space Bases:")
for i in range(n):
    if i not in yPivots:
        nullSpace = []
        for j in range(n):
            if j in yPivots:
                index = yPivots.index(j)
                nullSpace.append(augmentedMatrix[xPivots[index]][i] * (-1))
            elif j == i:
                nullSpace.append(1)
            else:
                nullSpace.append(0)
        nullSpace = numpy.array(nullSpace).reshape(n, 1)
        print(nullSpace, end="\n\n")

print()

# using pivot columns in the transposed form of matrix and finding column space of
# transposed matrix which is the same as row space of main matrix
# this is same as using pivot rows in the main matrix
print("Row Space Bases: ")
for i in xPivots:
    print(matrix[i, :n].reshape(1, n))

print()
print("Column Space Bases:")
for i in yPivots:
    print(matrix[:, i].reshape(m, 1), end=",\n\n")

print("Linear combination of other columns of matrix: ")
for i in range(n):
    if i not in yPivots:
        print(matrix[:, i].reshape(m, 1))
        print(" = ")
        for j in xPivots:
            print(augmentedMatrix[j][i], end="")
            print(matrix[:, yPivots[j]].reshape(m, 1))
            if j+1 < xPivots.__len__():
                print(" + ")
        print("\n\n")

