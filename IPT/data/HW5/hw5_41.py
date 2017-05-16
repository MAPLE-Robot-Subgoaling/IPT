
def main():
    print("It's time to draw a box!")
    boxWidth = int(input("How wide should it be? >"))
    boxHeight = int(input("And how tall? >"))
    symOutline = input("What symbol should I outline the box with? >")
    symFill = input("What symbol should I use to fill it in? >")

    fullLine = ""
    for h in range(boxWidth):
        fullLine = fullLine + symOutline

    fillerLine = symOutline
    for i in range(boxWidth - 2):
        fillerLine = fillerLine + symFill
    fillerLine = fillerLine + symOutline

    for j in range(boxHeight):
        if j == 0 or j == boxHeight - 1:
            print(fullLine)
        else:
            print(fillerLine)

main()
