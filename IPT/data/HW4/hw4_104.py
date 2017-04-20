
def main():

    print("Welcome to the Hail Height Calculator Program (HHCP)")

    startHeight = int(input("Please enter the starting height: "))
    print("Hail is currently at height", startHeight)

    while startHeight > 1:

        if startHeight % 2 == 0:
            startHeight = int(startHeight / 2)
            print("Hail is currently at height",startHeight)
        
        elif startHeight % 2 == 1:
            startHeight = int((startHeight * 3) + 1)
            print("Hail is currently at height",startHeight)

    if startHeight == 1:
        print("Hail stopped at height 1.")

main()
