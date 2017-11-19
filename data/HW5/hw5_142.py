def main():
    boxWidth = 0
    boxHeight = 0
    outlineChar = ""
    fillChar = ""
    boxWidth = int(input("Please enter the width of the box:"))
    boxHeight = int(input("Please enter the height of the box: "))
    outlineChar = input("Please enter a symbol for the box outline: ")
    fillChar = input("Please enter a symbol for the box fill")
    for  i in range(0, boxHeight):
        if (i == 0) or (i ==  boxHeight - 1):
            print(outlineChar * boxWidth)
        else:
            print(outlineChar + (fillChar * (boxWidth-2)) + outlineChar)
main()
