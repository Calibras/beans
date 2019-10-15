import random
black = int(input("how many black beans you want? "))
white = int(input("how many white beans you want? "))

def findSoultions(black,white):
    solutions = []
    solution = ""
    b = black
    w = white
    # white run
    while True:
        if (b + w) - 1 != 0:
            if (w - 1) != 0:
                solution += "W"
                w -= 1
            else:
                solution += "B"
                b -= 1
        else:
            solutions.append(solution)
            break;
    solution = ""
    b = black
    w = white
    #black run
    while True:
        if (b + w) - 1 != 0:
            if (b - 1) != 0:
                solution += "B"
                b -= 1
            else:
                solution += "W"
                w-= 1
        else:
            solutions.append(solution)
            break
    return solutions
solutions = findSoultions(black, white)
pickedSolution = solutions[random.randrange(0,len(solutions))]
print("all posibil solutions : ")
print(*solutions, sep=", ")
print("picked solution : " + pickedSolution)
