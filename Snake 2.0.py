# Snake 2.0 .py
# Joey LaRocca
# 4/25/2016

'''
Basic Snake Game with an Acorn
'''


import random
import pygame
import sys
from pygame.locals import *

Snakespeed= 15
Window_Width= 800
Window_Height= 500
Cell_Size = 20 #Width and height of the cells
assert Window_Width % Cell_Size == 0, "Window width must be a multiple of cell size."     #Ensuring that the cells fit perfectly in the window. eg if cell size was 10     and window width or windowheight were 15 only 1.5 cells would fit.
assert Window_Height % Cell_Size == 0, "Window height must be a multiple of cell size."  #Ensuring that only whole integer number of cells fit perfectly in the window.
Cell_W= int(Window_Width / Cell_Size) #Cell Width 
Cell_H= int(Window_Height / Cell_Size) #Cellc Height


White= (255,255,255)
Black= (0,0,0)
Brown= (139,69,19) #Defining element colors for the program.
Green= (0,255,0)
DARKGreen= (0,155,0)
DARKGRAY= (40,40,40)
YELLOW= (255,255,0)
Red_DARK= (150,0,0)
BLUE= (0,0,255)
BLUE_DARK= (0,0,150)


BGCOLOR = Black # Background color


UP = 'up'
DOWN = 'down'      # Defining keyboard keys.  
LEFT = 'left'
RIGHT = 'right'

HEAD = 0 # Syntactic sugar: index of the snake's head

def main():
    global SnakespeedCLOCK, DISPLAYSURF, BASICFONT

    pygame.init()
    SnakespeedCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((Window_Width, Window_Height))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Snake')

    while True:
        runGame()


def runGame():
    # Set a random start point.
    startx = random.randint(5, Cell_W - 6)
    starty = random.randint(5, Cell_H - 6)
    snakeCoords = [{'x': startx,     'y': starty},
                  {'x': startx - 1, 'y': starty},
                  {'x': startx - 2, 'y': starty}]
    direction = RIGHT

    # Start the acorn in a random place.
    acorn = getRandomLocation()

    while True: # main game loop
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT ) and direction != RIGHT:
                    direction = LEFT
                elif (event.key == K_RIGHT ) and direction != LEFT:
                    direction = RIGHT
                elif (event.key == K_UP ) and direction != DOWN:
                    direction = UP
                elif (event.key == K_DOWN ) and direction != UP:
                    direction = DOWN
                elif event.key == K_ESCAPE:
                    terminate()

        # check if the Snake has hit itself or the edge
        if snakeCoords[HEAD]['x'] == -1 or snakeCoords[HEAD]['x'] == Cell_W or     snakeCoords[HEAD]['y'] == -1 or snakeCoords[HEAD]['y'] == Cell_H:
            return # game over 
        for snakeBody in snakeCoords[1:]:
            if snakeBody['x'] == snakeCoords[HEAD]['x'] and snakeBody['y'] == snakeCoords[HEAD]    ['y']: 
                return # game over

        # check if Snake has eaten an acorn
        if snakeCoords[HEAD]['x'] == acorn['x'] and snakeCoords[HEAD]['y'] == acorn['y']:
            # don't remove snake's tail segment
            acorn = getRandomLocation() # set a new acorn somewhere
        else:
            del snakeCoords[-1] # remove snake's tail segment

        # move the snake by adding a segment in the direction it is moving
        if direction == UP:
            newHead = {'x': snakeCoords[HEAD]['x'], 'y': snakeCoords[HEAD]['y'] - 1}
        elif direction == DOWN:
            newHead = {'x': snakeCoords[HEAD]['x'], 'y': snakeCoords[HEAD]['y'] + 1}
        elif direction == LEFT:
            newHead = {'x': snakeCoords[HEAD]['x'] - 1, 'y': snakeCoords[HEAD]['y']}
        elif direction == RIGHT:
            newHead = {'x': snakeCoords[HEAD]['x'] + 1, 'y': snakeCoords[HEAD]['y']}
        snakeCoords.insert(0, newHead)
        DISPLAYSURF.fill(BGCOLOR)
        drawGrid()
        drawSnake(snakeCoords)
        drawAcorn(acorn)
        drawScore(len(snakeCoords) - 3)
        pygame.display.update()
        SnakespeedCLOCK.tick(Snakespeed)

def terminate():
    pygame.quit()
    sys.exit()


def getRandomLocation():
    return {'x': random.randint(0, Cell_W - 1), 'y': random.randint(0, Cell_H - 1)}



def drawScore(score):
    scoreSurf = BASICFONT.render('Score: %s' % (score), True, White)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (Window_Width - 120, 10)
    DISPLAYSURF.blit(scoreSurf, scoreRect)


def drawSnake(snakeCoords):
    for coord in snakeCoords:
        x = coord['x'] * Cell_Size
        y = coord['y'] * Cell_Size
        snakeSegmentRect = pygame.Rect(x, y, Cell_Size, Cell_Size)
        pygame.draw.rect(DISPLAYSURF, DARKGreen, snakeSegmentRect)
        snakeInnerSegmentRect = pygame.Rect(x + 4, y + 4, Cell_Size - 8, Cell_Size - 8)
        pygame.draw.rect(DISPLAYSURF, Green, snakeInnerSegmentRect)


def drawAcorn(coord):
    x = coord['x'] * Cell_Size
    y = coord['y'] * Cell_Size
    acornRect = pygame.Rect(x, y, Cell_Size, Cell_Size)
    pygame.draw.rect(DISPLAYSURF, Brown, acornRect)


def drawGrid():
    for x in range(0, Window_Width, Cell_Size): # draw vertical lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, Window_Height))
    for y in range(0, Window_Height, Cell_Size): # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (Window_Width, y))




if __name__ == '__main__':
    try:
        main()
    except SystemExit:
            pass
