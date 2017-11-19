def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = str(input("Please enter a symbol for the box outline: "))
    fill = str(input("Please enter a symbol for the box fill: "))
    for numHeight in range(height):
        if numHeight == 0:
            print(outline * width)
        elif numHeight > 0 and numHeight < height - 1:
            print(outline + (fill * (width - 2)) + outline)
        elif numHeight == height - 1:
            print(outline * width)
main()
