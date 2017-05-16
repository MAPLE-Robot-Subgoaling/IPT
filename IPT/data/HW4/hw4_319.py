


def main():

    height = int(input("Please enter the starting height of the hailstone "))
    print("Hail is curently at", height)

    while height != 1:
        height = str(height)
        if height[-1] == "0" or height[-1] == "2" or height[-1] == "4" or height[-1] == "6" or height[-1] == "8":
            height = int(height)
            height = height // 2
            print("Hail is currently at height", height)
        elif height[-1] == "1" or height[-1] == "3" or height[-1] == "5" or height[-1] == "7" or height[-1] == "9":
            height = int(height)
            height = height * 3 + 1
            print("Hail is currently at height", height)


    print("The hailstone stopped at height 1")



main()
