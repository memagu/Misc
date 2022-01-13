
#Importing modules and initializing pygame
import pygame
import time
import random
pygame.init()

#Settings
resolution = (1024, 1024)
snakeSize = 32
gameSpeed = 15
snakeLength = 2
snakeLengthAddAmount = 1
wallTeleport = False

#Setup variables
x = resolution[0]/2
y = resolution[1]/2
xChange = 0
yChange = 0
xFood = 0
yFood = 0
foodOnScreen = 0
clock = pygame.time.Clock()
fontStyle = pygame.font.SysFont(None, 32)
colorGreen = (0, 255, 0)
colorYellow = (255, 255 ,0)
colorRed = (255, 0, 0)
backgroundColor = (0, 64, 0)
segments = []
gameOver = False

#Setup functions
def displayText(msg, color):
    message = fontStyle.render(msg, True, color)
    display.blit(message, [resolution[0]/2 - message.get_rect().width/2, resolution[1]/2 - 100])

#Display setup
display = pygame.display.set_mode(resolution)
pygame.display.update()
pygame.display.set_caption("Snake game by Melker")

#Game
while gameOver != True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

#food
    if foodOnScreen == 0:
        xFood = random.randrange(0, 16, 1)*32
        yFood = random.randrange(0, 16, 1)*32
        foodOnScreen = 1
    else:
        pass

#Key response
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] or pressed[pygame.K_w]:
            xChange = 0
            yChange = -snakeSize
        elif pressed[pygame.K_LEFT] or pressed[pygame.K_a]:
            xChange = -snakeSize
            yChange = 0
        elif pressed[pygame.K_DOWN] or pressed[pygame.K_s]:
            xChange = 0
            yChange = snakeSize
        elif pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
            xChange = snakeSize
            yChange = 0
        else:
            pass

#Check if snake head in wall
    if wallTeleport == True:
        if x < 0:
            x = resolution[0]
        elif x > resolution[0] - snakeSize:
            x = -snakeSize
        elif y < 0:
            y = resolution[1]
        elif y > resolution[1] - snakeSize:
            y = -snakeSize
        else:
            pass
    else:
        if x < 0 or x > resolution[0] - snakeSize or y < 0 or y > resolution[1] - snakeSize:
            gameOver = True
        else:
            pass

#Assemble snake
    segments.append([x, y])
    if len(segments) > snakeLength:
        del segments[0]
    else:
        pass

    x += xChange
    y += yChange

#check for food at head
    if x == xFood and y == yFood:
        foodOnScreen = 0
        snakeLength += snakeLengthAddAmount
    else:
        pass

#Check for body at head
    for segment in segments[0:]:
        if [x, y] in segments and snakeLength > 2:
            gameOver = True
        else:
            pass

#Draw snake
    display.fill(backgroundColor)
    pygame.draw.rect(display, colorRed, [xFood, yFood, snakeSize, snakeSize])
    for segment in segments:
        pygame.draw.rect(display, colorGreen, [segment[0], segment[1], snakeSize, snakeSize])
    pygame.draw.rect(display, colorYellow, [x, y, snakeSize, snakeSize])
    # print(str(x) + ", " + str(y))

    pygame.display.update()

    clock.tick(gameSpeed)

    print(event)

#Game over
displayText("You lost at " + str(snakeLength) + "/" + str(int(resolution[0]/2)) + "points", colorRed)
pygame.display.update()
time.sleep(2)
pygame.quit()
quit()
