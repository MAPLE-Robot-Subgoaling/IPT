def main():

    STOP_HEIGHT = 1
    
    hailHeight = int(input("Please enter the starting height of the hailstone: "))
    
    while hailHeight != STOP_HEIGHT:
        print("Hail is currently at height", hailHeight)
        if (hailHeight % 2) == 0:
            hailHeight = int(hailHeight / 2)
        else:
            hailHeight = int(hailHeight * 3 + 1)
    
    print("Hail stopped at height", hailHeight)

main()
