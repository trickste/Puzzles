mat = [[5, -1, -1, -1, 7, -1, -1, 1, -1],
       [-1, -1, 4, -1, -1, 6, -1, -1, 9],
       [7, -1, -1, -1, -1, -1, -1, 6, -1],
       [6, -1, -1, 9, 5, -1, -1, -1, -1],
       [-1, 5, 2, 6, 4, 8, -1, -1, -1],
       [8, -1, -1, 3, -1, -1, -1, -1, -1],
       [2, -1, 5, 8, -1, -1, -1, 4, -1],
       [1, -1, 8, -1, -1, -1, -1, -1, 7],
       [-1, 9, -1, -1, -1, -1, 2, 5, -1]]

n = 9


def issafe(mat, x, y, val):
    # row
    for i in range(n):
        if val == mat[x][i]:
            return False

    # column
    for i in range(n):
        if val == mat[i][y]:
            return False

    # Subdivision
    block_x = int(x / 3)
    block_y = int(y / 3)

    sub_x = 3 * block_x
    sub_y = 3 * block_y

    for i in range(sub_x, sub_x + 3):
        for j in range(sub_y, sub_y + 3):
            if val == mat[i][j]:
                return False

    return True


def find_blank(mat):
    for x in range(len(mat)):
        for y in range(len(mat[x])):
            if mat[x][y] == -1:
                return (x, y)

    else:
        return False


def solsudo(mat):
    if (not find_blank(mat)):
        return True

    i, j = find_blank(mat)
    for val in range(1, 10):
        if issafe(mat, i, j, val):
            mat[i][j] = val
            if solsudo(mat):
                return True
            mat[i][j] = -1

    return False


def printmat(mat):
    for x in range(len(mat)):
        for y in range(len(mat[x])):
            print(mat[x][y], end=' ')
        print('')


if solsudo(mat):
    printmat(mat)
else:
    print("Nope")
