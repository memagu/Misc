import pygame
import time
pygame.init()

#settings
resolution = 1000
lineThickness = resolution/100
linePositionFraction = resolution/3 - lineThickness/2



#loop variables
startScreen = True
endScreen = True
gameOver = False
quitGame = False

#game loop
while quitGame == False:

    #setup variables
    boardPositions = ["none", "none", "none", "none", "none", "none", "none", "none", "none"]
    colorSienna = (160, 82, 45)
    colorSaddlebrown = (139, 69, 19)
    colorBlack = (0, 0, 0)
    playerOne = ""
    playerTwo = ""
    turn = 0
    fontStyleDisplayText = pygame.font.SysFont(None, int(resolution/15))
    fontStyledisplayTextXO = pygame.font.SysFont(None, int(resolution/5))


    #setup functions
    def drawBoard():
        display.fill(colorSienna)
        pygame.draw.rect(display, colorSaddlebrown, [linePositionFraction, 0, lineThickness, resolution])
        pygame.draw.rect(display, colorSaddlebrown, [2 * linePositionFraction, 0, lineThickness, resolution])
        pygame.draw.rect(display, colorSaddlebrown, [0, linePositionFraction, resolution, lineThickness])
        pygame.draw.rect(display, colorSaddlebrown, [0, 2 * linePositionFraction, resolution, lineThickness])

    def displayPosition(msg, color, position):
        message = fontStyledisplayTextXO.render(msg, True, color)
        column = position // 3
        row = position % 3
        y = resolution * column / 3 + resolution / 6 - message.get_rect().height / 2
        x = resolution * row / 3 + resolution / 6 - message.get_rect().width / 2
        display.blit(message, [x, y])

    def displayText(msg, color):
        message = fontStyleDisplayText.render(msg, True, color)
        display.blit(message, [resolution / 2 - message.get_rect().width / 2, resolution / 2 - resolution * 0.3])


    def regPos(position):
        global turn
        if boardPositions[position] == "none" and playerOne == "X" and turn % 2 == 0:
            boardPositions[position] = playerOne
            turn += 1
        elif boardPositions[position] == "none" and turn % 2 == 0:
            boardPositions[position] = playerOne
            turn += 1
        elif boardPositions[position] == "none" and playerOne == "X":
            boardPositions[position] = playerTwo
            turn += 1
        elif boardPositions[position] == "none":
            boardPositions[position] = playerTwo
            turn += 1
        else:
            pass

        #print(turn % 2)

    def mouseToColumnAndRow(mouseXY):
        c = mouseXY[0] // (resolution // 3)
        r = mouseXY[1] // (resolution // 3)
        return c, r

    def columnAndRowToPosition(column, row):
        return row * 3 + column


    time.sleep(0.2)

    #display setup
    display = pygame.display.set_mode((resolution, resolution))
    pygame.display.update()
    pygame.display.set_caption("Tic Tac Toe game by Melker")


    #startscreen
    while startScreen == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                startScreen = False
                gameOver = True
                endScreen = False
                quitGame = True

        drawBoard()
        displayText("Player one, choose to play as X or O!", colorBlack)
        displayPosition("X", colorBlack, 3)
        displayPosition("O", colorBlack, 5)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePosition = pygame.mouse.get_pos()

            c, r = mouseToColumnAndRow(mousePosition)
            pos = columnAndRowToPosition(c, r)

            if pos == 3:
                playerOne = "X"
                playerTwo = "O"
                gameOver = False
                break
            elif pos == 5:
                playerOne = "O"
                playerTwo = "X"
                gameOver = False
                break
            else:
                pass


        #print(event)

    time.sleep(0.2)

    #game
    while gameOver == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
                endScreen = False
                quitGame = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePosition = pygame.mouse.get_pos()

            c, r = mouseToColumnAndRow(mousePosition)
            regPos(columnAndRowToPosition(c, r))

        else:
            pass


        drawBoard()

        for index, msg in enumerate(boardPositions):
            if msg != "none":
                displayPosition(msg, colorBlack, index)


        pygame.display.update()
        #print(boardPositions)
        #print(event)


        #win detect
        if boardPositions[0] == boardPositions[3] == boardPositions[6] != "none":
            gameOver = True
        elif boardPositions[1] == boardPositions[4] == boardPositions[7] != "none":
            gameOver = True
        elif boardPositions[2] == boardPositions[5] == boardPositions[8] != "none":
            gameOver = True
        elif boardPositions[0] == boardPositions[1] == boardPositions[2] != "none":
            gameOver = True
        elif boardPositions[3] == boardPositions[4] == boardPositions[5] != "none":
            gameOver = True
        elif boardPositions[6] == boardPositions[7] == boardPositions[8] != "none":
            gameOver = True
        elif boardPositions[0] == boardPositions[4] == boardPositions[8] != "none":
            gameOver = True
        elif boardPositions[2] == boardPositions[4] == boardPositions[6] != "none":
            gameOver = True
        elif "none" not in boardPositions:
            gameOver = True
        else:
            pass

    time.sleep(1)

    while endScreen == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                endScreen = False
                quitGame = True

        drawBoard()
        displayText("Do you want to play another game?", colorBlack)
        displayPosition("Yes", colorBlack, 3)
        displayPosition("No", colorBlack, 5)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePosition = pygame.mouse.get_pos()

            c, r = mouseToColumnAndRow(mousePosition)
            pos = columnAndRowToPosition(c, r)

            if pos == 3:
                break
            elif pos == 5:
                quitGame = True
                break
            else:
                pass

pygame.quit()
quit()