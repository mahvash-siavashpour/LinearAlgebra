import numpy

n = int(input())

matrixA = []

for i in range(n):
    x = input().split()
    c = []
    for j in range(n):
        c.append(float(x[j]))
    matrixA.append(c)

matrixA = numpy.array(matrixA)

matrixb = []
x = input().split()
for i in range(n):
    matrixb.append(float(x[i]))

matrixb = numpy.array(matrixb)
matrixb = matrixb.reshape(n, 1)

augmentedMatrix = numpy.concatenate((matrixA, matrixb), axis=1)

print(augmentedMatrix)
print("____________________")

xPivot = []
yPivot = []
yIndex = 0

# row reduction forward phase
for i in range(n):
    # find a staring row with pivot position
    if augmentedMatrix[i][i + yIndex] == 0:
        for j in range(i + 1, n):
            if augmentedMatrix[j][0] != 0:
                augmentedMatrix[[0, j]] = augmentedMatrix[[j, 0]]
                break
        print(augmentedMatrix)
        print("____________________")

    if augmentedMatrix[i][i + yIndex] == 0:
        yIndex += 1
        continue

    xPivot.append(i)
    yPivot.append(i + yIndex)

    # row replacement operations to create
    # zeros in all positions below the pivot.
    for k in range(i + 1, n):
        if augmentedMatrix[k][i + yIndex] != 0:
            augmentedMatrix[k:k + 1] -= (augmentedMatrix[i:i + 1] * augmentedMatrix[k][i + yIndex]) / \
                                        augmentedMatrix[i][i + yIndex]
            print(augmentedMatrix)
            print("____________________")

xPivot.reverse()
yPivot.reverse()

# row reduction backward phase
for i, j in zip(xPivot, yPivot):

    # scaling to set value 1 to pivot positions
    augmentedMatrix[i:i + 1] /= augmentedMatrix[i][j]

    # row replacement operations to create
    # zeros in all positions above the pivot.
    for k in range(0, i):
        if augmentedMatrix[k][j] != 0:
            augmentedMatrix[k:k + 1] -= (augmentedMatrix[i:i + 1] * augmentedMatrix[k][j]) / augmentedMatrix[i][j]
            print(augmentedMatrix)
            print("____________________")

if len(xPivot) == n:
    for i in range(n):
        print("x{} = {}".format(i, augmentedMatrix[i][n]))
elif n - 1 in yPivot:
    print("No Answers")
else:
    print("Infinite Answers")