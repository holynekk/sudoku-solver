import pygame
import time
import solver
from pygame.locals import *

fps = 30

grid_height = 540
grid_width = 540

square_size = int(540/3)
cell_size = int(square_size/3)

# Draw a square around selected item.
def draw_rectangle(x, y, bool_var):
    if bool_var:
        pygame.draw.rect(screen, (0, 0, 255), (x, y, cell_size, cell_size), 1)
    else:
        pygame.draw.rect(screen, (255, 0, 0), (x, y, cell_size, cell_size), 1)

# Solving sudoku function that calls helper solve function in solver.py
def solve_sudoku(grid):
    grid = solver.create_copy(grid)
    return grid


# Lock button stores the number that are currently on grid and make them unchangable.
def draw_lock_button():
    text = BASICFONT.render("Lock Nums", True, (0,0,0))
    cell_rect = text.get_rect()
    cell_rect.topleft = (52, 570)
    
    pygame.draw.rect(screen, (200,200,200), (45, 550, 120, 60))
    screen.blit(text, cell_rect)

# Solve button shows the solution of current grid with the help of solver.py 
def draw_solve_button():
    text = BASICFONT.render("Let's Solve", True, (0,0,0))
    cell_rect = text.get_rect()
    cell_rect.topleft = (217, 570)
    
    pygame.draw.rect(screen, (102,255,102), (210, 550, 120, 60))
    screen.blit(text, cell_rect)

    # Solve button shows the solution of current grid with the help of solver.py 
def draw_reset_button():
    text = BASICFONT.render("Reset", True, (0,0,0))
    cell_rect = text.get_rect()
    cell_rect.topleft = (405, 570)
    
    pygame.draw.rect(screen, (255,102,102), (375, 550, 120, 60))
    screen.blit(text, cell_rect)

# Printing the number on screen 
def put_number(data, x, y, size, locked_indexes):
    if (int(y/60), int(x/60)) not in locked_indexes:
        text = LARGEFONT.render("{}".format(data), True, (200,200,200))
    else:
        text = LARGEFONT.render("{}".format(data), True, (0,0,0))
    cell_rect = text.get_rect()
    cell_rect.topleft = (x, y)
    screen.blit(text, cell_rect)

# Renders all the grid in every loops.
def display_numbers(grid, locked_indexes):
    for i in range(9):
        for k in range(9):
            if grid[i][k] == 0:
                continue
            else:
                put_number(grid[i][k], k*60, i*60, LARGEFONT, locked_indexes)
    return None

# Draws the horizontal and vertical lines.
def draw_grid():
    # Gray colored lines which seperates small cells.
    for x in range(0, grid_width, cell_size):
        pygame.draw.line(screen, (200, 200, 200), (x, 0), (x, grid_height))
    for y in range(0, grid_height, cell_size):
        pygame.draw.line(screen, (200, 200, 200), (0, y), (grid_width, y))
    # Black colored lines which seperates 3x3 squares.
    for x in range(0, grid_width, square_size):
        pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, grid_height))
    for y in range(0, grid_height+1, square_size):
        pygame.draw.line(screen, (0, 0, 0), (0, y), (grid_width, y))


def deploy_game():

    pygame.init()
    global fpsclock, screen

    global BASICFONT, BASICFONTSIZE, LARGEFONT, LARRGEFONRSIZE
    BASICFONTSIZE = 20
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)
    LARGEFONTSIZE = 60
    LARGEFONT = pygame.font.Font('freesansbold.ttf', LARGEFONTSIZE)

    # Creating Sudoku Grid with array 

    grid = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    locked_indexes = []

    # This part is constructing an empty grid, but for quick 
    # demonstration I have built default grid like above.
    # Before locking numbers, user can delete all numbers
    # and set its own grid

    fpsclock = pygame.time.Clock()

    table_width = 540
    table_height = 540

    screen = pygame.display.set_mode((540, 620))
    pygame.display.set_caption("Sudoku Solver")

    screen.fill((255, 255, 255))
    draw_grid()

    mouse_clicked = False
    xmouse = 0
    ymouse = 0

    locked = 0

    

    run_program = True
    while run_program:
        mouse_clicked = False

        xindex = int(xmouse/60)
        yindex = int(ymouse/60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_program = False
            if event.type == MOUSEBUTTONDOWN:
                xmouse, ymouse = event.pos
                mouse_clicked = True
            if event.type == KEYDOWN:
                if (yindex, xindex) not in locked_indexes:
                    if event.key == K_BACKSPACE:
                        grid[yindex][xindex] = 0
                    elif event.key == K_1:
                        if solver.isPossible(yindex, xindex, 1, grid):
                            grid[yindex][xindex] = 1
                    elif event.key == K_2:
                        if solver.isPossible(yindex, xindex, 2, grid):
                            grid[yindex][xindex] = 2
                    elif event.key == K_3:
                        if solver.isPossible(yindex, xindex, 3, grid):
                            grid[yindex][xindex] = 3
                    elif event.key == K_4:
                        if solver.isPossible(yindex, xindex, 4, grid):
                            grid[yindex][xindex] = 4
                    elif event.key == K_5:
                        if solver.isPossible(yindex, xindex, 5, grid):
                            grid[yindex][xindex] = 5
                    elif event.key == K_6:
                        if solver.isPossible(yindex, xindex, 6, grid):
                            grid[yindex][xindex] = 6
                    elif event.key == K_7:
                        if solver.isPossible(yindex, xindex, 7, grid):
                            grid[yindex][xindex] = 7
                    elif event.key == K_8:
                        if solver.isPossible(yindex, xindex, 8, grid):
                            grid[yindex][xindex] = 8
                    elif event.key == K_9:
                        if solver.isPossible(yindex, xindex, 9, grid):
                            grid[yindex][xindex] = 9

        if mouse_clicked:
            if 240 <= xmouse <= 360 and 550 <= ymouse <= 610:
                if locked:
                    grid = solve_sudoku(grid)
            if 375 <= xmouse <= 495 and 550 <= ymouse <= 610:
                locked = 0
                locked_indexes = []
                grid = []
                for i in range(9):
                    nwlist = []
                    for k in range(9):
                        nwlist.append(0)
                    grid.append(nwlist)
            elif 60 <= xmouse <= 180 and 550 <= ymouse <= 610:
                if not locked:
                    locked = 1
                    for i in range(9):
                        for k in range(9):
                            if grid[i][k]!= 0:
                                locked_indexes.append((i,k))
                    print(locked_indexes)
            elif ymouse <= 540:
                xmouse = xmouse//60 * 60
                ymouse = ymouse//60 * 60

        screen.fill((255, 255, 255))
        draw_grid()
        draw_solve_button()
        draw_lock_button()
        draw_reset_button()
        display_numbers(grid, locked_indexes)

        if ymouse <= 540:
            if (yindex, xindex) in locked_indexes:
                draw_rectangle(xmouse, ymouse, False)
            else:
                draw_rectangle(xmouse, ymouse, True)
        pygame.display.update()
        fpsclock.tick(fps)


if __name__ == "__main__":
    deploy_game()