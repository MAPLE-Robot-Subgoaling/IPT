
def main():

    width = int(input("Please enter the width of the box: " ))
    height = int(input("Please enter the height of the box: " ))
    outline = input("Please enter a symbol for the box outline: " )
    fill = input("Please enter a symbol for the box fill: ")
    currentWidth = 0
    currentHeight = 0
    boxHeight = [0, height-1, 1]
    boxFill = [1, height-1, 1]

    for currentHeight in boxHeight:
        if currentHeight == 0:
            print(outline * width)
            currentHeight + 1
        for currentHeight in boxFill:
            print(outline + (fill * (width - 2)) + outline)
            currentHeight + 1
    else:
        print(outline * width)

main()
