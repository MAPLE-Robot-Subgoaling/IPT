def main():
    STOP_HEIGHT = 1
    ODD_MOD = 1
    EVEN_MOD = 0
    height = int(input("Please enter the starting height of the hailstone: "))
    while height != STOP_HEIGHT:
        while (height % 2) == EVEN_MOD:
            print("The current height is" , height)
            height = height // 2
        if height == STOP_HEIGHT:
            print("The hailstone stopped at height 1.")
        while (height % 2) == ODD_MOD and height != STOP_HEIGHT:
            print("The current height is" , height)
            height = (height * 3) + 1
main()
