def main():
    BOTTOM_LIST = 0
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box outline: ")
    boxString = ""
    for i in list(range(BOTTOM_LIST, height)):
        if i == BOTTOM_LIST or i == height - 1:
            boxString = outline * width
            print(boxString)
        else:
            for j in list(range(BOTTOM_LIST, width)):
                if j == BOTTOM_LIST or j == width - 1:
                    boxString += outline
                else:
                    boxString += fill
            print(boxString)
        boxString = ""
main()
