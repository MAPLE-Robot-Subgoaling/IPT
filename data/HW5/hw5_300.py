def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outLine = input("Please enter a symbol for the box outline: ")
    filler = input("Please enter a symbol for the box fill: ")
    boxLine = outLine
    for i in range( 1 , height + 1 ):
        for j in range( 1 , width + 1 ):
            if width == 1 and height == 1:
                break
            elif (i > 1 and i < height) and j != width:
                boxLine += filler
            elif (i > 1 and i < height) and j == width:
                boxLine += outLine
            elif i == 1 or i == height:
                boxLine += outLine
        print(boxLine)
        boxLine = outLine
main()
