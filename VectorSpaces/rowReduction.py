import numpy

def echelonForm(m, n, augmentedMatrix):

    numpy.set_printoptions(3)
    xPivot = []
    yPivot = []
    yIndex = 0
    i = 0
    # row reduction forward phase
    while i < m:
        # print(augmentedMatrix[i][i+yIndex])
        # find a staring row with pivot position
        if augmentedMatrix[i][i + yIndex] == 0:
            for j in range(i + 1, m):
                if augmentedMatrix[j][0] != 0:
                    augmentedMatrix[[0, j]] = augmentedMatrix[[j, 0]]
                    break

        if augmentedMatrix[i][i + yIndex] == 0:
            yIndex += 1
            continue
        if abs(augmentedMatrix[i][i + yIndex]) > 0.0001:
            xPivot.append(i)
            yPivot.append(i + yIndex)

        # row replacement operations to create
        # zeros in all positions below the pivot.
        for k in range(i + 1, m):
            if augmentedMatrix[k][i + yIndex] != 0:
                augmentedMatrix[k:k + 1] -= (augmentedMatrix[i:i + 1] * augmentedMatrix[k][i + yIndex]) / \
                                            augmentedMatrix[i][i + yIndex]
        i += 1

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


    for i in range(m):
        for j in range(n):
            augmentedMatrix[i][j] = round(augmentedMatrix[i][j], 5)
    xPivot.reverse()
    yPivot.reverse()
    pivots = (xPivot, yPivot)
    return pivots
