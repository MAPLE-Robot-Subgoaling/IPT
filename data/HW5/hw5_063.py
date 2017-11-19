def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    boxOutline = input("Please enter a symbol for the box outline: ")
    boxFill = input("Please enter a symbol of the box fill: ")
    topAndBot = []
    middle = []
    topRow = ""
    midRow = ""
    for w in range(width):
        topAndBot.append(boxOutline)
        if w == 0 or w == (width - 1):
            middle.append(boxOutline)
        else:
            middle.append(boxFill)
    for l in range(len(topAndBot)):
        topRow = topRow + topAndBot[l]
    for l in range(len(middle)):
        midRow = midRow + middle[l]
    for h in range(height):
        if h == 0 or h == (height - 1):
            print(topRow)
        else:
            print(midRow)            
main()
