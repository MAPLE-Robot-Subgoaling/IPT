def main():
    height = int(input("Please enter an integer starting height for the stone."))
    print("The hail started at height " + str(height))
    while height != 1:
        if height % 2 == 0:
            height = height // 2
            print("The current height of the hail is " + str(height))
        elif height % 2 == 1:
            height = height * 3 + 1
            print("The current height of the hail is " + str(height))
    print("The hail stopped at height 1.")
main()
