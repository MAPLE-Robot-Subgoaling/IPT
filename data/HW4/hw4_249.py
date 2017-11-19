def main():
    height = int(input("What is the starting height of the hail? "))
    while height != 1:
        print("Hail is currently at height", height)
        if (height % 2) == 0:
            height = int(height / 2)
        else:
            height = (height * 3) + 1
    print("Hail stopped at height", height)
main()
