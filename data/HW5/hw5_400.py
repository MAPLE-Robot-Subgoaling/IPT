def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    boxOut = input("Please enter a symbol for the box outline: ")
    boxFill = input("Please enter a symbol for the box fill: ")
    for b in range(0, 1):
        print(boxOut * width)
        second = width // height
        for b in range(0, second):
            print(boxOut + (boxFill * (width - second)) + boxOut)
        print(boxOut * width)
main()
