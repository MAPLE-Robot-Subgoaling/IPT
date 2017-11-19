def main():
    box = []
    lastChar = []
    myWidth = int(input("Please enter the width of the box: "))
    myHeight = int(input("Please enter the height of the box: "))
    outLine = input("Please enter a symbol for the box outline: ")
    fill = input("PLease enter a symbol for the box fill: ")
    STOPPER = myWidth - 2
    for x in range(myHeight - 1):
        if x == 0:
            box.append(outLine)
        else:
            box.append(fill)
    lastChar.append(outLine)
    box = box + lastChar
    for a in box:
        if myWidth == 1:
            print(outLine)
        else:
            print(outLine + (a * STOPPER) + outLine)
main()
