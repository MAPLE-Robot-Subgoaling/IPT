def main():
    MIDVAR = 2
    ENDVAR = 1
    widthBox = int(input("Please enter the width of the box: "))
    heightBox = int(input("Please enter the height of the box: "))
    outlineBox = input("Please enter a symbol for the box outline: ")
    fillBox = input("Please enter a symbol for the box fill: ")
    firstLine = widthBox * outlineBox
    print(firstLine)
    midOutline = (heightBox - MIDVAR)
    for i in range(midOutline):
        midBox = (outlineBox + (fillBox * (widthBox - MIDVAR))+ outlineBox)
        print(midBox)
    if heightBox != ENDVAR:
            print(firstLine)
main()
