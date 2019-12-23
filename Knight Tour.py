n = int(input())
mat = [[-1 for i in range(n)] for j in range(n)]


def isSafe(mat, x, y):
    if (x > -1) and (y > -1) and (x < n) and (y < n) and (mat[x][y] == -1):
        return True
    return False


def ksolve(mat, x, y, val):
    if val == (n * n)+1:
        return True
    for i in range(8):
        new_x = x + move_x[i]
        new_y = y + move_y[i]
        if isSafe(mat, new_x, new_y):
            mat[new_x][new_y] = val

            if ksolve(mat, new_x, new_y, val + 1):
                return True
            mat[new_x][new_y] = -1

    return False


def printmat(mat):
    for x in range(len(mat)):
        for y in range(len(mat[x])):
            print(mat[x][y], end=' ')
        print('')


move_x = [2, 1, -1, -2, -2, -1, 1, 2]
move_y = [1, 2, 2, 1, -1, -2, -2, -1]
val = 1
mat[0][0] = val
if ksolve(mat, 0, 0, val+1):
    printmat(mat)
else:
    print('Nope')
