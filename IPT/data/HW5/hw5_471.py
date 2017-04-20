
def main():

    widthBox = int(input("Please enter the width of the box: "))
    heightBox = int(input("Please enter the height of the box: "))
    outlineBox = input("Please enter a symbol for the box outline: ")
    fillBox = input("Please enter a symbol for the box fill: ")
    
    if (widthBox != 1 and heightBox != 1):
        print(outlineBox * widthBox)
        for i in range(heightBox - 2):
            print(outlineBox + (fillBox * (widthBox - 2)) + outlineBox)
        print(outlineBox * widthBox)
    else:
        print(outlineBox)
main()
