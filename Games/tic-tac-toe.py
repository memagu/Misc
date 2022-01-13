import pygame
import time
pygame.init()

#settings
resolution = 500
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


    def displayText(msg, color):
        message = fontStyleDisplayText.render(msg, True, color)
        display.blit(message, [resolution / 2 - message.get_rect().width / 2, resolution / 2 - resolution * 0.3])


    def displayText1(msg, color):
        message = fontStyledisplayTextXO.render(msg, True, color)
        display.blit(message, [resolution / 6 - message.get_rect().width / 2, resolution / 6 - message.get_rect().height / 2])


    def displayText2(msg, color):
        message = fontStyledisplayTextXO.render(msg, True, color)
        display.blit(message, [resolution / 2 - message.get_rect().width / 2, resolution / 6 - message.get_rect().height / 2])


    def displayText3(msg, color):
        message = fontStyledisplayTextXO.render(msg, True, color)
        display.blit(message, [resolution * 5 / 6 - message.get_rect().width / 2, resolution / 6 - message.get_rect().height / 2])


    def displayText4(msg, color):
        message = fontStyledisplayTextXO.render(msg, True, color)
        display.blit(message, [resolution / 6 - message.get_rect().width / 2, resolution / 2 - message.get_rect().height / 2])


    def displayText5(msg, color):
        message = fontStyledisplayTextXO.render(msg, True, color)
        display.blit(message, [resolution / 2 - message.get_rect().width / 2, resolution / 2 - message.get_rect().height / 2])


    def displayText6(msg, color):
        message = fontStyledisplayTextXO.render(msg, True, color)
        display.blit(message, [resolution * 5 / 6 - message.get_rect().width / 2, resolution / 2 - message.get_rect().height / 2])


    def displayText7(msg, color):
        message = fontStyledisplayTextXO.render(msg, True, color)
        display.blit(message, [resolution / 6 - message.get_rect().width / 2, resolution * 5 / 6 - message.get_rect().height / 2])


    def displayText8(msg, color):
        message = fontStyledisplayTextXO.render(msg, True, color)
        display.blit(message, [resolution / 2 - message.get_rect().width / 2, resolution * 5 / 6 - message.get_rect().height / 2])


    def displayText9(msg, color):
        message = fontStyledisplayTextXO.render(msg, True, color)
        display.blit(message, [resolution * 5 / 6 - message.get_rect().width / 2, resolution * 5 / 6 - message.get_rect().height / 2])


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
        displayText4("X", colorBlack)
        displayText6("O", colorBlack)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePosition = pygame.mouse.get_pos()

            if 0 < mousePosition[0] < resolution / 3 and resolution / 3 < mousePosition[1] < resolution * 2 / 3:
                playerOne = "X"
                playerTwo = "O"
                gameOver = False
                break
            elif resolution * 2 / 3 < mousePosition[0] < resolution and resolution / 3 < mousePosition[1] < resolution * 2 / 3:
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

            if 0 < mousePosition[0] < resolution / 3 and 0 < mousePosition[1] < resolution / 3:
                regPos(0)

            elif resolution / 3 < mousePosition[0] < resolution * 2 / 3 and 0 < mousePosition[1] < resolution / 3:
                regPos(1)

            elif resolution * 2 / 3 < mousePosition[0] < resolution and 0 < mousePosition[1] < resolution / 3:
                regPos(2)

            elif 0 < mousePosition[0] < resolution / 3 and resolution / 3 < mousePosition[1] < resolution * 2 / 3:
                regPos(3)

            elif resolution / 3 < mousePosition[0] < resolution * 2 / 3 and resolution / 3 < mousePosition[1] < resolution * 2 / 3:
                regPos(4)

            elif resolution * 2 / 3 < mousePosition[0] < resolution and resolution / 3 < mousePosition[1] < resolution * 2 / 3:
                regPos(5)

            elif 0 < mousePosition[0] < resolution / 3 and resolution * 2 / 3 < mousePosition[1] < resolution:
                regPos(6)

            elif resolution / 3 < mousePosition[0] < resolution * 2 / 3 and resolution * 2 / 3 < mousePosition[1] < resolution:
                regPos(7)

            elif resolution * 2 / 3 < mousePosition[0] < resolution and resolution * 2 / 3 < mousePosition[1] < resolution:
                regPos(8)

            else:
                pass

        else:
            pass


        drawBoard()


        if boardPositions[0] != "none":
            displayText1(boardPositions[0], colorBlack)
        else:
            pass

        if boardPositions[1] != "none":
            displayText2(boardPositions[1], colorBlack)
        else:
            pass

        if boardPositions[2] != "none":
            displayText3(boardPositions[2], colorBlack)
        else:
            pass

        if boardPositions[3] != "none":
            displayText4(boardPositions[3], colorBlack)
        else:
            pass

        if boardPositions[4] != "none":
            displayText5(boardPositions[4], colorBlack)
        else:
            pass

        if boardPositions[5] != "none":
            displayText6(boardPositions[5], colorBlack)
        else:
            pass

        if boardPositions[6] != "none":
            displayText7(boardPositions[6], colorBlack)
        else:
            pass

        if boardPositions[7] != "none":
            displayText8(boardPositions[7], colorBlack)
        else:
            pass

        if boardPositions[8] != "none":
            displayText9(boardPositions[8], colorBlack)
        else:
            pass


        pygame.display.update()
        #print(boardPositions)
        print(event)


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
        displayText4("Yes", colorBlack)
        displayText6("No", colorBlack)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePosition = pygame.mouse.get_pos()

            if 0 < mousePosition[0] < resolution / 3 and resolution / 3 < mousePosition[1] < resolution * 2 / 3:
                break
            elif resolution * 2 / 3 < mousePosition[0] < resolution and resolution / 3 < mousePosition[1] < resolution * 2 / 3:
                quitGame = True
                break
            else:
                pass

pygame.quit()
quit()