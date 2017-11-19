def main():
    width = int(input("Please enter the width of the box:"))
    height = int(input("Please enter the height of the box:"))
    symbol = input("Please enter a symbol for the box outline:")
    fill = input("Please enter a symbol for the box to fill:")
    newHeight = 1
    for s in symbol:
        print(s*width)
        while newHeight < height and newHeight < height - 1:
            print(s + fill*(width - 2) + s)
            newHeight = newHeight + 1
        newHeight = newHeight + 1
        if newHeight == height:
            print(s*width)
main()
