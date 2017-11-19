def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box fill: ")
    print(width * outline)
    for x in range(1,height):
        print(outline + (width - 2) * fill + outline)
    print(width * outline)
main()
