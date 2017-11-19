def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    usrSym = input("Please enter a symbol for the box outline: ")
    usrSym2 = input("Please enter a symbol for the box fill: ")
    for nums in range(height):
        if nums == 0 or nums == height - 1:
            print(usrSym * width)
3
        else:
            print(usrSym + (usrSym2 * (width - 2)) + usrSym)
main()
