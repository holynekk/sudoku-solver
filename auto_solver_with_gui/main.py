import pygame
from pygame.locals import *

FPS = 30

width = 540
height = 540

SQUARESIZE = int(540/3)
CELLSIZE = int(SQUARESIZE/3)
NUMBERSIZE = int(CELLSIZE/3)

def draw_grid():
    for x in range(0, width, CELLSIZE):
        pygame.draw.line(screen, (200, 200, 200), (x, 0), (x, height))
    for y in range(0, width, CELLSIZE):
        pygame.draw.line(screen, (200, 200, 200), (0, y), (width, y))
    for x in range(0, width, SQUARESIZE):
        pygame.draw.line(screen, (0,0,0), (x, 0), (x, height))
    for y in range(0, height+1, SQUARESIZE):
        pygame.draw.line(screen, (0,0,0), (0, y), (width, y))
    return None

def initiateCells():
    current_grid = {}
    full_cell = [1,2,3,4,5,6,7,8,9]
    for x in range(9):
        for y in range(9):
            current_grid[x,y] = list(full_cell)
    return current_grid

def populate_cells(data, x, y, size):
    if size == 'small':
        cell_surf = BASICFONT.render('%s'%(data), True, (200,200,200))
    else:
        cell_surf = LARGEFONT.render('%s'%(data), True, (0,255,0))
    cell_rect = cell_surf.get_rect()
    cell_rect.topleft = (x, y)
    screen.blit(cell_surf, cell_rect)

def display_cells(current):
    x = 0
    y = 0
    for item in current:
        cell_data = current[item]
        for number in cell_data:
            if number != ' ':
                x = ((number-1)%3)
                if number <= 3:
                    y = 0
                elif number <= 6:
                    y = 1
                else:
                    y = 2
                if cell_data.count(' ') < 8:
                    populate_cells(number, (item[0]*CELLSIZE)+(x*NUMBERSIZE), (item[1]*CELLSIZE)+(y*NUMBERSIZE), 'small')
                else:
                    populate_cells(number, (item[0]*CELLSIZE)+(x*NUMBERSIZE), (item[1]*CELLSIZE)+(y*NUMBERSIZE), 'large')
    return None

# Go through each cell in each row
# check if it contains a number which is not in the rest of the row.
def onlyNinX(currentGrid):

    # check all items in currentGrid list
    for item in currentGrid:
        
        # create two empty lists
        allNumbers = []
        currentNumbers = []
        
        # determine all numbers deploy_gameing in the row - store in allNumbers
        for xRange in range(0,9):
            for rowNumbers in currentGrid[(xRange,item[1])]:
                if rowNumbers != ' ':
                    allNumbers.append(rowNumbers)
                    
        # determine numbers deploy_gameing in individual cell being looked at - store in currentNumbers
        for cellNumbers in currentGrid[item]:
            if cellNumbers != ' ':
                currentNumbers.append(cellNumbers)
              

        # look at numbers deploy_gameing in a cell. Check if they only appear in the row once.        
        if len(currentNumbers) > 1: 
            for checkNumber in currentNumbers: 
                if allNumbers.count(checkNumber) == 1:  
                    
                    # at this stage we know checkNumber appears only once, so we now update grid
                    currentState = currentGrid[item] 
                    for individualNumber in currentState:
                        if individualNumber != checkNumber and individualNumber != ' ': 
                            currentState[individualNumber-1] = ' ' 
                            currentGrid[item] = currentState 
    return currentGrid

def onlyNinY(currentGrid):

    # check all items in currentGrid list
    for item in currentGrid:
        
        # create two empty lists
        allNumbers = []
        currentNumbers = []
        
        # determine all numbers deploy_gameing in the column - store in allNumbers
        for yRange in range(0,9):
            for columnNumbers in currentGrid[(item[0],yRange)]:
                if columnNumbers != ' ':
                    allNumbers.append(columnNumbers)
                    
        # determine numbers deploy_gameing in individual cell being looked at - store in currentNumbers
        for cellNumbers in currentGrid[item]:
            if cellNumbers != ' ':
                currentNumbers.append(cellNumbers)
        
        # look at numbers deploy_gameing in a cell. Check if they only appear in the column once.        
        if len(currentNumbers) > 1: 
            for checkNumber in currentNumbers: 
                if allNumbers.count(checkNumber) == 1:  
                    
                    # at this stage we know checkNumber appears only once, so we now update grid
                    currentState = currentGrid[item] 
                    for individualNumber in currentState: 
                        if individualNumber != checkNumber and individualNumber != ' ': 
                            currentState[individualNumber-1] = ' ' 
                            currentGrid[item] = currentState 
                            
    return currentGrid

def onlyNinGrid(grid):

    # check all items in currentGrid list
    for item in grid:

    # determine the co-ordinates for the grid we are dealing with
    
        if item[0] < 3:
            xGrid = [0,1,2]
        elif item[0] > 5:
            xGrid = [6,7,8]
        else: xGrid = [3,4,5]

        if item[1] < 3:
            yGrid = [0,1,2]
        elif item[1] > 5:
            yGrid = [6,7,8]
        else: yGrid = [3,4,5]

        # create two empty lists
        allNumbers = []
        currentNumbers = []

        #iterates through each of the nine numbers in the grid
        for x in xGrid:
            for y in yGrid:
            
                # determine all numbers deploy_gameing in the grid - store in allNumbers
                for gridNumbers in grid[(x,y)]:
                    if gridNumbers != ' ':
                        allNumbers.append(gridNumbers)
                        
            # determine numbers deploy_gameing in individual cell being looked at - store in currentNumbers
        for cellNumbers in grid[item]:
            if cellNumbers != ' ':
                currentNumbers.append(cellNumbers)
        
        # look at numbers deploy_gameing in a cell. Check if they only appear in the grid once.        
        if len(currentNumbers) > 1: 
            for checkNumber in currentNumbers: #
                if allNumbers.count(checkNumber) == 1: 
                    
                    # at this stage we know checkNumber appears only once, so we now update grid
                    currentState = grid[item] 
                    for individualNumber in currentState: 
                        if individualNumber != checkNumber and individualNumber != ' ': 
                            currentState[individualNumber-1] = ' ' 
                            grid[item] = currentState 
                            
    return grid






def draw_box(x, y):
    xbox = ((x*27)/540) * NUMBERSIZE
    ybox = ((y*27)/540) * NUMBERSIZE
    pygame.draw.rect(screen, (0,0,255), (xbox-10, ybox-10, NUMBERSIZE, NUMBERSIZE), 1)

def refresh_grid(currentGrid):
    fullCell = [1,2,3,4,5,6,7,8,9]
    for xCoord in range(0,9):
        for yCoord in range(0,9):
            cellData = currentGrid[xCoord, yCoord]
            if cellData.count(' ') < 8:
                currentGrid[xCoord,yCoord] = list(fullCell) # Copies List
    return currentGrid

def display_selected(x, y, grid):
    x_number = (x*27)/width
    y_number = (y*27)/width

    x_mod = int(x_number % 3)
    y_mod = int(y_number % 3)


    if x_mod == 0:
        choices = [1,4,7]
        number = choices[y_mod]
    elif x_mod == 1:
        choices = [2,5,8]
        number = choices[y_mod]
    else:
        choices = [3,6,9]
        number = choices[y_mod]

    cellx = int(x_number / 3)
    celly = int(y_number / 3)

    current_state = grid[cellx, celly]
    inc_num = 0

    if(current_state[number-1] == ' '):
        return grid

    while inc_num < 9:
        if inc_num+1 != number:
            current_state[inc_num] = ' '
        else:
            current_state[inc_num] = number

        grid[cellx, celly] = current_state
        inc_num += 1
    grid = refresh_grid(grid)
    return grid

def horizontal_remove(currentGrid, item, number):
    for x in range(0,9):
        if x != item[0]:
            currentState = currentGrid[(x,item[1])]
            currentState[number-1] = ' '
            currentGrid[(x,item[1])] = currentState
    return currentGrid

def vertical_remove(currentGrid, item, number):
    for y in range(0,9):
        if y != item[1]:
            currentState = currentGrid[(item[0],y)]
            currentState[number-1] = ' '
            currentGrid[(item[0],y)] = currentState
    return currentGrid

def square_remove(currentGrid, item, number):

    if item[0] < 3:
        xGrid = [0,1,2]
    elif item[0] > 5:
        xGrid = [6,7,8]
    else: xGrid = [3,4,5]

    if item[1] < 3:
        yGrid = [0,1,2]
    elif item[1] > 5:
        yGrid = [6,7,8]
    else: yGrid = [3,4,5]
    
    #iterates through each of the nine numbers in the grid
    for x in xGrid:
        for y in yGrid:
            if (x,y) != item: # for all squares except the one containing the number
                currentState = currentGrid[(x,y)] # isolates the numbers still available for that cell
                currentState[number-1] = ' ' # make them blank.
                currentGrid[(x,y)] = currentState
                currentGrid = onlyNinX(currentGrid)
                currentGrid = onlyNinY(currentGrid)
                currentGrid = onlyNinGrid(currentGrid)
                
    return currentGrid

def solve_sudoku(grid):
    for item in grid:
        data = grid[item]
        if data.count(' ') == 8:
            for number in data:
                if number != ' ':
                    number_exist = number
            grid = horizontal_remove(grid, item, number_exist)
            grid = vertical_remove(grid, item, number_exist)
            grid = square_remove(grid, item, number_exist)
    return grid

def deploy_game():
    global FPSCLOCK, screen
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    screen = pygame.display.set_mode((540,620))

    mouse_clicked = False
    xmouse = 0
    ymouse = 0

    pygame.display.set_caption("Sudoku Solver with Pygame")
    
    global BASICFONT, BASICFONTSIZE, LARGEFONT, LARRGEFONRSIZE
    BASICFONTSIZE = 15
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)
    LARGEFONTSIZE = 60
    LARGEFONT = pygame.font.Font('freesansbold.ttf', LARGEFONTSIZE)

    current_grid = initiateCells()

    screen.fill((255, 255, 255))

    display_cells(current_grid)
    draw_grid()

    run_program = True
    while run_program:
        mouse_clicked = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_program = False
            elif event.type == MOUSEMOTION:
                xmouse, ymouse = event.pos
            elif event.type == MOUSEBUTTONDOWN:
                xmouse, ymouse = event.pos
                mouse_clicked = True
        if mouse_clicked:
            current_grid = display_selected(xmouse, ymouse, current_grid)
        
        solve_sudoku(current_grid)

        screen.fill((255, 255, 255))
        display_cells(current_grid)
        draw_grid()

        draw_box(xmouse, ymouse)

        pygame.display.update()
        FPSCLOCK.tick(FPS)
