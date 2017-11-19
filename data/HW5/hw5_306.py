def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box fill: ")
    if(width != 0 and height != 0):
        for i in range(height):
            if((i == 0) or (i == height - 1)) and (width != 0):
                print(outline * width)
            else:
                print(outline + (fill * (width - 2)) + outline)
main()
