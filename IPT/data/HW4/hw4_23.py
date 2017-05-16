
def main():

    STONE_MIN = 1
    PROMPT_HEIGHT = "Please enter the starting height of the hailstone: "
    MSG_HEIGHT = "Hail is currently at height"
    MSG_DONE = "Hail stopped at height"

    stoneHeight = int(input(PROMPT_HEIGHT))
    
    isHeightDone = (stoneHeight== STONE_MIN)
    isHeightEven = (stoneHeight % 2 == 0)
    isHeightOdd = (stoneHeight % 2 == 1)
    
    while (not isHeightDone): 

        print(MSG_HEIGHT, int(stoneHeight))
        
        if (isHeightEven):
            stoneHeight = stoneHeight / 2
        else:
            stoneHeight = (stoneHeight * 3) + 1

        isHeightDone = (stoneHeight == 1)
        isHeightEven = (stoneHeight % 2 == 0)
        isHeightOdd = (stoneHeight % 2 == 1)

    print(MSG_DONE, int(stoneHeight))

main()



