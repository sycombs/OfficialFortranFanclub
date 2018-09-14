import pygame, sys, time, random
from pygame.locals import *

from Cell import *

def recReveal(grid, rows, cols):

    if rows>=grid.get_height() or rows<0 or cols>=grid.get_width() or cols<0 or grid.board[rows][cols].isRevealed==True:
        return

    grid.board[rows][cols].set_revealed()


    if grid.board[rows][cols].get_cell_textRep()=='M':
        print("game over")

    elif grid.board[rows][cols].get_cell_textRep()!='-':
        print("Stop point- ", rows, ":", cols, ":", grid.board[rows][cols].get_cell_textRep())

    elif grid.board[rows][cols].get_cell_textRep()=='-':
        print(rows, ":", cols, ":", grid.board[rows][cols].get_cell_textRep())
        recReveal(grid, rows-1, cols-1)
        recReveal(grid, rows-1, cols)
        recReveal(grid, rows-1, cols+1)
        recReveal(grid, rows, cols+1)
        recReveal(grid, rows+1, cols+1)
        recReveal(grid, rows+1, cols)
        recReveal(grid, rows+1, cols-1)
        recReveal(grid, rows, cols-1)

    return

def board_create(grid):
    #print(grid.get_height(), " by ", grid.get_width())
    for rows in range(grid.get_height()):
        for cols in range(grid.get_width()):
            #print(rows, ":", cols)
            if grid.board[rows][cols].textRep=='M':
                adjacent(grid, rows-1, cols-1)
                adjacent(grid, rows-1, cols)
                adjacent(grid, rows-1, cols+1)
                adjacent(grid, rows, cols+1)
                adjacent(grid, rows+1, cols+1)
                adjacent(grid, rows+1, cols)
                adjacent(grid, rows+1, cols-1)
                adjacent(grid, rows, cols-1)

    return

def adjacent(grid, rows, cols):
    if rows>=grid.get_height() or rows<0 or cols>=grid.get_width() or cols<0 or grid.board[rows][cols].isRevealed==True:
        return

    grid.board[rows][cols].set_num_adj_mines(int(grid.board[rows][cols].numAdjacent)+1)
    grid.board[rows][cols].textRep=grid.board[rows][cols].numAdjacent
    return

def game_over():
    global FPSCLOCK, DISPLAYSURFACE  #Testing purposes
    global BASICFONT, TEXTFONT, RESET_SURF, RESET_RECT, QUIT_SURF, QUIT_RECT

    pygame.init()  #Testing purposes
    pygame.display.set_caption('Minesweeper')  #Testing purposes
    FPSCLOCK = pygame.time.Clock()  #Testing purposes
    DISPLAYSURFACE = pygame.display.set_mode((800, 600))  #Testing purposes
    BASICFONT = pygame.font.SysFont('Courier New', 30)
    TEXTFONT = pygame.font.SysFont('Courier New', 40)
    RESET_SURF, RESET_RECT = drawButton('New Game', (0, 0, 0), (225, 225, 225), 300/3, 200*.75)
    QUIT_SURF, QUIT_RECT = drawButton('Quit', (0, 0, 0), (225, 225, 225), 300*.75, 200*.75)
    MENU_SURF = pygame.Surface((300,200))
    MENU_RECT = placeSurface(MENU_SURF, 800/2, 600/2)

    RESET_RECT.move_ip(MENU_RECT.left,MENU_RECT.top)
    QUIT_RECT.move_ip(MENU_RECT.left,MENU_RECT.top)

    mouse_x = 0
    mouse_y = 0

    DISPLAYSURFACE.fill((0,0,0))

    while True:
        mouseClicked = False
        spacePressed = False

        DISPLAYSURFACE.fill((0,0,0))  #Testing purposes

        DISPLAYSURFACE.blit(MENU_SURF, MENU_RECT)
        MENU_SURF.fill((255,255,255))
        drawText("Game Over", TEXTFONT, ((0,0,0)), MENU_SURF, 300*.5, 200*.25)

        DISPLAYSURFACE.blit(RESET_SURF, RESET_RECT)
        DISPLAYSURFACE.blit(QUIT_SURF, QUIT_RECT)

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mouse_x, mouse_y = event.pos
            elif event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                mouseClicked = True

        if RESET_RECT.collidepoint(mouse_x, mouse_y):
            highlightButton(DISPLAYSURFACE, RESET_RECT)
            if mouseClicked:
                print("New Game")

        # check if show box is clicked
        if QUIT_RECT.collidepoint(mouse_x, mouse_y):
            highlightButton(DISPLAYSURFACE, QUIT_RECT)
            if mouseClicked:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        FPSCLOCK.tick(30)

def drawButton(text, textColor, backgroundColor, center_x, center_y):

    butSurf = BASICFONT.render(text, True, textColor, backgroundcolor)
    buttonRect = butSurf.get_rect()
    buttonRect.centerx = center_x
    buttonRect.centery = center_y

    return (butSurf, buttonRect)

def placeSurface(screen, center_x, center_y):

    surfRect = screen.get_rect()
    surfRect.centerx = center_x
    surfRect.centery = center_y

    return newRect

def drawText(text, font, color, surface, x, y):

    textSurf = font.render(text, True, color)
    textRect = textSurf.get_rect()
    textRect.centerx = x
    textRect.centery = y
    surface.blit(textobj, textrect)

def highlightButton(screen, buttonRect):

    linewidth = 4
    pygame.draw.rect(screen, (0, 128, 0), (buttonRect.left-linewidth, buttonRect.top-linewidth, buttonRect.width+2*linewidth, buttonRect.height+2*linewidth), linewidth)
