
def main():

    print("Please enter the starting height of the hailstone: ")    
    stoneHeight = int(input())
    
    while stoneHeight != 1:

        print("Hail is currently at height", stoneHeight)
        if stoneHeight % 2 == 0:
            stoneHeight = stoneHeight / 2
        else:
            stoneHeight = stoneHeight * 3 + 1
        stoneHeight = int(stoneHeight)
        

    print("Hail stopped at height", stoneHeight)

main()
