
def main():

    BOARDER = 2

    boxWidth = int(input("Please enter the width of the box: "))
    boxHeight = int(input("Please enter the height of the box: "))
    boxOut = input("Please enter a symbol for the box outline: ")
    boxFill = input("Please enter a symbol for the box fill: ")


    print(boxOut * boxWidth)

    fillWidth = boxWidth - BOARDER
    fillHeight = boxHeight - BOARDER

    fillList = list(range(fillHeight))

    for i in fillList:
        i = (boxOut + (boxFill * fillWidth) + boxOut)
        print(i)
  
    if boxHeight > 1:
        print(boxOut * boxWidth)


main()
