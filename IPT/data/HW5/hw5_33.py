
def main():
    widthBox = int(input("Please enter the width of the box: "))
    heightBox = int(input("Please enter the height of the box: "))
    outlineBox = str(input("Please enter a symbol for the box outline: "))
    fillBox = str(input("Please enter a symbol for the box fill: "))
    print(outlineBox * widthBox)
    for x in range(1,heightBox-1):
        print(outlineBox+fillBox * (widthBox-2)+outlineBox)
    if heightBox > 1:
        print(outlineBox * widthBox)

main()
