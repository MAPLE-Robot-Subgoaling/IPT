def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box fill: ")
    if(height == 0 or height == 1):
        print(outline * width)
    if(height == 2):
        print(outline * width)
        print(outline * height)
    if(height > 2):
        print(outline * width)
        for num in range(0, height - 2):
            print(outline + (fill * (width - 2)) + outline)
        print(outline * width)
main()
