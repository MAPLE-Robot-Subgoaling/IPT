def main():
    curHeight = int(input("Please enter the starting height of the hailstone: "))
    REPEATER = 1
    while REPEATER != 0:
        if curHeight == 1:
            print("Hail stopped at height", int(curHeight))
            REPEATER = 0
        elif curHeight%2 == 0:
            print("Hail is currently at height", int(curHeight))
            curHeight /=  2
        else:
            print("Hail is currently at height", int(curHeight))
            curHeight = (curHeight*3) + 1
main()
