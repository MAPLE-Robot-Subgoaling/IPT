

def main():

    boxWidth = int(input("Please enter the width of the box: "))

    boxHeight = int(input("Please enter the height of the box: "))

    outlineSymbol = input("Please enter a symbol for the box outline: ")

    fillSymbol = input("Please enter a symbol for the box fill: ")

        
    boxCounter = 0

    for i in range(boxCounter, boxHeight):
        if(boxCounter ==  (boxHeight-1) or boxCounter == 0):
            print(outlineSymbol  * boxWidth)
            boxCounter = boxCounter +1
        else:
            print(outlineSymbol + fillSymbol *(boxWidth -2) + outlineSymbol)
            boxCounter = boxCounter +1 


main()
