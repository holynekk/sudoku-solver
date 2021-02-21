
def isPossible(y, x, n, grid):
    # Check whether n is already exist in that row.
    for i in range(9):
        if grid[y][i] == n:
            return False
    # Check whether n is already exist in that column.
    for i in range(9):
        if grid[i][x] == n:
            return False
    # Check whether n is already exist in that 3x3 box.
    xbox = (x//3)*3
    ybox = (y//3)*3
    for i in range(3):
        for j in range(3):
            if grid[ybox+i][xbox+i] == n:
                return False
    # That number can be put in there.  
    return True


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
                return grid
    if all_filled(grid):
        print("AFTER CALCULATION: ")
        print_grid(grid)
    return grid
                    

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