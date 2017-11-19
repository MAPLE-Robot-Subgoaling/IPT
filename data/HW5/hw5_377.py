def main():
    width = int(input("Please enter the width of the box."))
    height = int(input("Please enter the height of the box."))
    outSym = str(input("Please enter a symbol for the box outline."))
    fillSym = str(input("Please enter a symbol for the box to fill."))
    for i in range(0, width):
        print(outSym)
    for i in range(0, height):
        print(fillSym)
main()
