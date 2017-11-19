def main():
    width = int(input("Pease enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter the symbol for the box outline: ")
    fill = input("Pease enter a symbol for the box fill: ")
    if height != 1:
        print(width *outline)
        for i in range(0, height -2):
            print(outline + fill*(width-2) + outline)
        print(width * outline)
    if width == 1 and height == 1:
        print(outline)
main()
