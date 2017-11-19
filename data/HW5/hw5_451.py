def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the bos: "))
    outline = str(input("Please enter a symbol for the box outline: "))
    fill = str(input("Please enter a symbol for the box fill: "))
    innerSize = height - 2
    print(width * outline)
    for a in range(innerSize):
        print(outline + fill * (width - 2)  + outline)
    if height > 2:
        print(width * outline)
main()
