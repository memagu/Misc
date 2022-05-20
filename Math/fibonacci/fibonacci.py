
currentNumber = 1
midstage = 0
previousNumber = 0
upperLimit = 10
upperStaticLimit = upperLimit

while upperLimit > 0:
    print(str(upperStaticLimit - upperLimit + 1) + ". " + str(currentNumber) + "\n")
    midstage = currentNumber
    currentNumber = previousNumber + currentNumber
    previousNumber = midstage
    upperLimit -= 1