    
def main():
    
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outlineSymbol = input("Please enter a symbol for the box outline: ")
    fillSymbol = input("Please enter a symbol for the box fill: ")

    heightList = list(range(height))
    
    for n in heightList:
        
        if n == 0 or n == height - 1:
            print(outlineSymbol * width)
        else:
            print(outlineSymbol+ fillSymbol * (width - 2)+outlineSymbol) 
main()

