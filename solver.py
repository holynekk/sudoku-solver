import time

def next_empty(grid):
    for i in range(9):
        for k in range(9):
            if grid[i][k] == 0:
                return (i, k)
    return None


def isPossible(row, col, n, grid):
    # Check whether n is already exist in that row.
    for i in range(9):
        if grid[row][i] == n:
            return False
    # Check whether n is already exist in that column.
    for i in range(9):
        if grid[i][col] == n:
            return False
    # Check whether n is already exist in that 3x3 box.
    xbox = col//3
    ybox = row//3
    for i in range(ybox * 3, ybox*3+3):
        for k in range(xbox * 3, xbox*3+3):
            if grid[i][k] == n:
                return False
    # That number can be put in there.  
    return True

copy = list()

def solve(grid):
    print_grid(grid)
    inds = next_empty(grid)
    if not inds:
        global copy
        copy = grid
        return True
    else:
        row, col = inds

    for i in range(1, 10):
        if isPossible(row, col, i, grid):
            grid[row][col] = i
            if solve(grid):
                return True
            grid[row][col] = 0

    return False


def create_copy(grid):
    global copy

    solve(grid)
    print_grid(copy)
    return copy

'''
def solve(grid):
    # Scanning grid for empty square.
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for i in range(1, 10):
                    if isPossible(y, x, i, grid):
                        grid[y][x] = i
                        solve(grid)
                        grid[y][x] = 0
                print("return ledik moruk")
                return grid
    print_grid(grid)
'''

# To print grid into console
def print_grid(grid):
    for i in range(9):
        if(i % 3 == 0 and i != 0):
            print("- - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(str(grid[i][j]))
            else:
                print(str(grid[i][j]) + " ", end="")
    print('\n')


def all_filled(grid):
    for i in range(9):
        if grid[i].count(0) > 0:
            return False
    return True
