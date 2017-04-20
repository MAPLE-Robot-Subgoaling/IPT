
def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box fill: ")
    
    for floor in range (height):
        if (floor == 0 or floor == (height - 1)):
            print(outline * width)
        else:
            print(outline + (fill * (width - 2)) + outline)

main()
