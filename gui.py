import pygame
import time
import solver
from pygame.locals import *



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






def print_grid():
    global grid
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




fps = 30

grid_height = 540
grid_width = 540

square_size = int(540/3)
cell_size = int(square_size/3)

def solve_sudoku():
    global grid

    print("before: ")
    print_grid()

    grid = solver.solve(grid)
    print("after: ")
    print_grid()


def draw_solve_button():
    text = BASICFONT.render("Let's Solve", True, (0,0,0))
    cell_rect = text.get_rect()
    cell_rect.topleft = (200, 550)
    screen.blit(text, cell_rect)

    pygame.draw.rect(screen, (0,0,255), (200, 550, 120, 60), 1)


def put_number(data, x, y, size):
    text = LARGEFONT.render("{}".format(data), True, (0,0,0))
    cell_rect = text.get_rect()
    cell_rect.topleft = (x, y)
    screen.blit(text, cell_rect)


def display_numbers():
    for i in range(9):
        for k in range(9):
            if grid[i][k] == 0:
                continue
            else:
                put_number(grid[i][k], k*60, i*60, LARGEFONT)
    return None


def draw_grid():
    for x in range(0, grid_width, cell_size):
        pygame.draw.line(screen, (200, 200, 200), (x, 0), (x, grid_height))
    for y in range(0, grid_height, cell_size):
        pygame.draw.line(screen, (200, 200, 200), (0, y), (grid_width, y))

    for x in range(0, grid_width, square_size):
        pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, grid_height))
    for y in range(0, grid_height+1, square_size):
        pygame.draw.line(screen, (0, 0, 0), (0, y), (grid_width, y))

def main():

    pygame.init()

    global fpsclock, screen, grid

    global BASICFONT, BASICFONTSIZE, LARGEFONT, LARRGEFONRSIZE
    BASICFONTSIZE = 30
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)
    LARGEFONTSIZE = 60
    LARGEFONT = pygame.font.Font('freesansbold.ttf', LARGEFONTSIZE)

    # Creating Sudoku Grid with array 

    '''
    grid = []
    for i in range(9):
        nwlist = []
        for k in range(9):
            nwlist.append(0)
        grid.append(nwlist)
    '''
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

    run_program = True
    while run_program:
        mouse_clicked = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_program = False
            if event.type == MOUSEBUTTONDOWN:
                xmouse, ymouse = event.pos
                mouse_clicked = True

        if mouse_clicked:
            if 200 <= xmouse <= 320 and 550 <= ymouse <= 610:
                solve_sudoku()
            elif ymouse <= 540:
                print("you are in a square")



        screen.fill((255, 255, 255))
        draw_grid()
        draw_solve_button()
        display_numbers()

        pygame.display.update()
        fpsclock.tick(fps)


if __name__ == "__main__":
    main()