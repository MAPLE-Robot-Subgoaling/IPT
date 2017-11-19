def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box fill: ")
    h = 0
    w = 0
    boxLine = ""
    for h in range(0,height):
        boxLine = ""
        if (h == 0) or (h == height-1):
            boxLine = outline * width
        else:
            for w in range(0,width):
                if (w == 0) or (w == width-1):
                    boxLine = boxLine + outline
                else:
                    boxLine = boxLine + fill
        print(boxLine)
    print("")
main()
