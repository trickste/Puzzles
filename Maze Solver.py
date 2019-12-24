mat = [[1, 0, 0, 0, 0],
       [1, 0, 1, 1, 1],
       [1, 1, 1, 0, 1],
       [1, 0, 0, 1, 1],
       [1, 1, 1, 0, 1]]

n = 5

new_mat = [[0 for i in range(n)] for j in range(n)]


def issafe(mat, x, y):
    if x < n and y < n and x > -1 and y > -1 and mat[x][y] == 1 and new_mat[x][y] == 0:
        return True
    return False


def solmaze(mat, x, y):
    if x == n - 1 and y == n - 1:
        return True
    for i in range(4):
        new_x = x + mov_x[i]
        new_y = y + mov_y[i]
        if issafe(mat, new_x, new_y):
            new_mat[new_x][new_y] = 1
            if solmaze(mat, new_x, new_y):
                return True
            new_mat[new_x][new_y] = 0
    return False


def printmat(mat):
    for x in range(len(mat)):
        for y in range(len(mat[x])):
            print(mat[x][y], end=' ')
        print('')


mov_x = [1, 0, -1, 0]
mov_y = [0, 1, 0, -1]

new_mat[0][0] = 1
if solmaze(mat, 0, 0):
    printmat(new_mat)
else:
    print("nope")
