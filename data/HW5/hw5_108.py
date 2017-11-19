def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter a symbol for the box outline: ")
    boxFiller = input("Please enter a symbol for the box fill: ")
    for i in range(0, height):
        if(i == 0):
            print(outline * width)
        elif(i == height - 1):
            print(outline * width)
        else:
            print(outline + (boxFiller * (width - 2)) + outline)
main()
