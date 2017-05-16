
def main():
    width = (int(input("Please enter the width of the box: ")))
    height = (int(input("Please enter the height of the box: ")))
    widthList = range(width)
    heightList = range(height)
    outline = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box fill: ")
    line = ""

    for x in heightList:
        if(x == 0 or x == height - 1):
            for w in widthList:
                line = line + outline
        else:
            for w in widthList:
                if (w == 0 or w == width - 1):
                    line = line + outline
                else:
                    line = line + fill
        print(line)
        line = ""

main()
