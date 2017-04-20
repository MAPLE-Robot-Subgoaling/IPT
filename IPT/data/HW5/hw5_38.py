def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter the symbol for the box outline: ")
    fill = input("Please enter the symbol for the box fill: ")
    print(outline * width)
    newh = height - 2
    neww = width - 2
    if height > 1:
        for h in range(newh):
            print(outline, fill * neww ,outline)
        print(outline * width)
main()
