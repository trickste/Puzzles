n = int(input())

mat = [[0 for i in range(n)] for j in range(n)]


def isvalid(mat, x, y):
    # left
    i = y - 1
    while i > -1:
        if mat[x][i] == 1:
            return False
        i -= 1

    # left digonal up
    i = x - 1
    j = y - 1
    while i > -1 and j > -1:
        if mat[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # left digonal down
    i = x + 1
    j = y - 1
    while i > n and j < -1:
        if mat[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def NQsolve(mat, col):
    if col >= n:
        return True
    for x in range(n):
        if isvalid(mat, x, col):
            mat[x][col] = 1
            if NQsolve(mat, col + 1) == True:
                return True
            mat[x][col] = 0
    return False


def printn(mat):
    for x in range(n):
        for y in range(n):
            print(mat[x][y], end=' ')
        print('')


if NQsolve(mat, 0):
    printn(mat)
else:
    print('sol not found')
