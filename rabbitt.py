import sys
def rabbit(mat, visited, x, y):
    return 0 <= x < len(mat) and 0 <= y < len(mat[0]) and \
           not (mat[x][y] == 0 or visited[x][y])

def shortestpath(mat, visited, i, j, dest, min_dist=sys.maxsize, dist=0):

    if (i, j) == dest:
        return min(dist, min_dist)
    visited[i][j] = 1

    # go to the bottom cell
    if rabbit(mat, visited, i + 1, j):
        min_dist = shortestpath(mat, visited, i + 1, j, dest, min_dist, dist + 1)

    # go to the right cell
    if rabbit(mat, visited, i, j + 1):
        min_dist = shortestpath(mat, visited, i, j + 1, dest, min_dist, dist + 1)

    # go to the top cell
    if rabbit(mat, visited, i - 1, j):
        min_dist = shortestpath(mat, visited, i - 1, j, dest, min_dist, dist + 1)

    # go to the left cell
    if rabbit(mat, visited, i, j - 1):
        min_dist = shortestpath(mat, visited, i, j - 1, dest, min_dist, dist + 1)

    # backtrack: remove (i, j) from the visited matrix
    visited[i][j] = 0

    return min_dist

def length(mat, src, dest):

    i, j = src
    x, y = dest
    if not mat or len(mat) == 0 or mat[i][j] == 0 or mat[x][y] == 0:
        return -1
    (M, N) = (len(mat), len(mat[0]))
    visited = [[False for _ in range(N)] for _ in range(M)]
    min_dist = shortestpath(mat, visited, i, j, dest)
    if min_dist != sys.maxsize:
        return min_dist
    else:
        return -1

if __name__ == '__main__':

    mat = [
        [1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1],
        [0, 0, 1, 0, 1, 1],
        [1, 0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0, 0],
        [1, 0, 1, 1, 1, 1],
    ]

    src = (0, 0)
    dest = (5, 4)

    min_dist = length(mat, src, dest)

    if min_dist != -1:
        print("Matrix=", mat)
        print("The shortest path from Rabbit to the carrot= ", min_dist)
    else:
        print("rabbit can't reach the carrot")
