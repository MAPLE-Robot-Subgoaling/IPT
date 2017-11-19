def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter the symbol for the outline of the box: ")
    filler = input("Please enter the symbol to fill the box: ")
    for i in range(height):
        if i==0:
            print(outline * width)
        elif i < height-1:
            print(outline + (filler * (width-2)) + outline)
        else:
            print(outline * width)
main()
