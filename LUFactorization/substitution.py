import numpy


def forward_substitution(matrix):
    n = len(matrix[:, 0])
    m = len(matrix[0, :])
    for i in range(n):
        # find a staring row with pivot position
        if matrix[i][i] == 0:
            for j in range(i + 1, n):
                if matrix[j][0] != 0:
                    matrix[[0, j]] = matrix[[j, 0]]
                    break

        if m == n + 1:
            matrix[i][m - 1] /= matrix[i][i]
        matrix[i][i] /= matrix[i][i]
        # row replacement operations to create
        # zeros in all positions below the pivot.
        for k in range(i + 1, n):
            if m == n + 1:
                matrix[k][m - 1] -= matrix[k][i] * matrix[i][m-1]
            matrix[k][i] -= matrix[k][i]
    # return matrix


def backward_substitution(matrix):
    n = len(matrix[:, 0])
    m = len(matrix[0, :])
    for i in range(n - 1, -1, -1):

        # scaling to set value 1 to pivot positions
        if m == n + 1:
            matrix[i][m - 1] /= matrix[i][i]
        matrix[i][i] /= matrix[i][i]
        # row replacement operations to create
        # zeros in all positions above the pivot.
        for k in range(i - 1, -1, -1):
            if m == n + 1:
                matrix[k][m - 1] -= matrix[k][i] * matrix[i][m-1]
            matrix[k][i] -= matrix[k][i]
    # return matrix


def find_inverse(matrixA, matrixL, matrixU):
    n = len(matrixA[:, 0])
    identity = numpy.identity(n)
    AInverse = []
    for i in range(n):
        augmentedMatrix = numpy.concatenate((matrixL, identity[:, [i]]), axis=1)
        forward_substitution(augmentedMatrix)
        augmentedMatrix = numpy.concatenate((matrixU, augmentedMatrix[:, [n]]), axis=1)
        backward_substitution(augmentedMatrix)
        AInverse.append(augmentedMatrix[:, n])
    AInverse = numpy.array(AInverse)
    AInverse = numpy.transpose(AInverse)
    return AInverse
