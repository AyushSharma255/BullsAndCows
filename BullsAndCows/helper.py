from random import randint

def giveCowsAndBulls(realNum, guessNum):
    cows = 0
    bulls = 0

    for i in range(3):
        if str(realNum)[i] == str(guessNum)[i]:
            bulls += 1
        else:
            for x in range(3):
                if str(realNum)[i] == str(guessNum)[x]:
                    cows += 1
                    break

    return cows, bulls

def isUnique(guessNum):
    digits = set()

    for i in range(3):
        digits.add(map(int, str(guessNum)))

    if len(digits) == 3:
        return True

    return False

def genNum():
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    randNum = ""

    for i in range(3):
        randNum += str(digits.pop(randint(0, len(digits) - 1)))

    randNum = int(randNum)

    return randNum
