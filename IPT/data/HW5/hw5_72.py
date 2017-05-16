
def main():
    
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outlineSymbol = input("Please enter a symbol for the box outline: ")
    fillSymbol = input("Please enter a symbol for the box fill: ")
    
    for h in range(height):
        if(h == 0 or h == height-1):
            print(outlineSymbol * width)
        else:
            middleString = "";
            for w in range(width):
                if(w == 0 or w == width-1):
                    middleString += outlineSymbol
                else:
                    middleString += fillSymbol
            print(middleString)
            

main()