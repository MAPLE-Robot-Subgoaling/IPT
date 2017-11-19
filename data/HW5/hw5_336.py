def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height if the box: "))
    outline = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box fill: ")
    topBottomBorder = outline * width
    middleRows = outline + (fill * (width-2)) + outline
    for b in range (0, height):
        if ((b == 0) or (b == height-1)):
            print(topBottomBorder)
        else:
            print(middleRows)
main()
