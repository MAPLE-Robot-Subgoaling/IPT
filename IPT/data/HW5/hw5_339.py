
def main():

    print("")

    boxWidth = int(input("Please enter the width of the box: "))
    boxHeight = int(input("Please enter the height of the box: "))
    outline = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box fill: ")

    boxTop = outline
    boxMiddle = ""

    for x in range(boxWidth - 1):

        boxTop = boxTop + outline
        
    for x in range(boxWidth - 2):

        boxMiddle = boxMiddle + fill

    boxMiddle = outline + boxMiddle + outline

    print(boxTop)

    for x in range(boxHeight - 2):

        print(boxMiddle)

    if boxHeight != 1:

        print(boxTop)


main()
