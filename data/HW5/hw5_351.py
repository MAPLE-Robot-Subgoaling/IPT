def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter a symbol for the box outline: ")
    boxFill = input("Please enter a symbol for the box fill: ")
    if height == 1 and width == 1:
        print(outline)
    else:
        print(outline * width)
        for i in range(0, height - 2):
            print(outline + boxFill * (width - 2) + outline )
        print(outline * width)
main()
