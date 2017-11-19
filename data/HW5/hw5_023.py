def main():
    widthBox = int(input("Please enter the width of the box:"))
    heightBox = int(input("Please enter the height of the box:"))
    outlineBox = input("Please enter a symbol for the box outline:")
    fillBox = input("Please enter a symbol for the box fill:")
    for o in outlineBox:
        print(outlineBox * widthBox)
    for f in (fillBox * (heightBox - 2)):
        insideBox = (outlineBox + (fillBox * (widthBox - 2)) + outlineBox)
        print(insideBox)
    for o in outlineBox:
        print(outlineBox * widthBox)
main()
