def main():
    height = int(input("Please enter the starting height of the hailstone: "))
    ADD_FACTOR = 1
    MULTI_FACTOR = 3
    print(" ")
    while height != 1:
        print('Hail is currently at height ',height)
        if (height % 2) == 0:
            height = height // 2
        else:
            height = (height * MULTI_FACTOR) + ADD_FACTOR
    print("Hail stopped at height 1\n")
main()
