def main():
    height = int(input("Please enter the height of the stone: "))
    while height != 1:
        print("The current height is", height)
        if height % 2 == 1:
            height = height * 3 + 1
        else:
            height = height / 2
    print("It stopped at height 1.0")
main()
