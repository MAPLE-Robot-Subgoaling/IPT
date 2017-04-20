
def main():

    width = int(input("Width of box: "))
    height = int(input("Height of box: "))
    outline = input("Enter symbol for outline: ")
    fill = input("Enter symbol for fill: ")

    print(outline * width)
    
    BORDER = 2
    if height > BORDER:
        for f in range(height - BORDER):
            print (outline + fill * (width - BORDER) + outline)

    if height > 1:
        print(outline * width)


main()
