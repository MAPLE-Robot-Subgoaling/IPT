def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter a symbol for the box outline: ")
    filler = input("Please enter a symbole for the box fill: ")
    boxWidth = []
    boxHeight = []
    boxGrid = []
    for i in range(width):
        boxWidth.append(i)
    boxGrid = [[boxWidth]*height]
    print(boxGrid)
main()
