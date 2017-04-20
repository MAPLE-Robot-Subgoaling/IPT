
def main ():

    width = int(input("What is the width of the box: "))
    height = int(input("What is the height of the box: "))
    boxOutline = input("What symbol do you want to use for the box's outline: ")
    boxFill = input("What symbol do you want to use to fill the box: ")
    upperLimit = height - 1
    fillWidth = width - 2
    for x in range (height):
        if x == 0 or x == upperLimit:
            print (boxOutline * width)
        else:
            print (boxOutline + (boxFill * fillWidth) + boxOutline)

main ()
