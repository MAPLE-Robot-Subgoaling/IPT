
def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline =input("Please enter the symbol for the box outline: ")
    fill = input("Please enter the symbol for the box fill: ")
    
    i = 1
    total = outline * width
    print(total)
    center = outline * width

    for h in range(0 , height):
        while i > 0 and i < width:
            center[i] = fill
            i+1
            print(total)


main()
