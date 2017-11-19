def main():
    END_HEIGHT = 1
    MULTIPLICATION = 3
    ADDITION = 1
    height = int(input("Please enter the starting height of the hailstone: "))
    while height != END_HEIGHT:
        print("Hail is currently at height", height)
        if height % 2 == 0:
            height //= 2 
        else:
            height = (height * MULTIPLICATION) + ADDITION
    print("Hail stopped at height", END_HEIGHT)
main()
