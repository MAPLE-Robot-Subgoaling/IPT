def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter the symbol for the box outline: ")
    fill = input("Please enter the fill for the box: ")
    for a in range(height):
        for b in range(width):
            if a in [0, height-1] or b in [0, width-1]:
                print(outline, end = '')
            else:
                print(fill, end = '')
        print()
main()
