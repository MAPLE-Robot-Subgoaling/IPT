


def main():

    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outlineSymbol = input("Please enter a symbol for the box outline: ")
    boxFillSymbol = input("Please enter a symbol for the box fill: ")
    
    for i in range(height):
        displayString = ''
        for j in range(width):
            if i == 0 or j == 0 or i == height - 1 or j == width - 1:
                displayString = displayString + outlineSymbol      
            else:
                displayString = displayString + boxFillSymbol
                
        print(displayString)


main()
