

def main():

    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enterthe height of the box: "))
    outline = input("Please enter the symbol for the outline: ")
    inside = input("Please enter the symbol to fill the box: ")
    rowList = range(height)

    for a in rowList:
        if a == rowList[0] or a == rowList[-1]:
            print(outline * width)
        else:
            print(outline + inside * (width - 2) + outline)

main()
