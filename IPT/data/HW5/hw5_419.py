
def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outerSymbol = input("Please enter a symbol for the box outline: ")
    innerSymbol = input("Plase enter a symbol for the box fill: ")

    for y in range(height):
        line = ""
        if(y == 0 or y == height-1):
            for x in range(width):
                line += outerSymbol
        else:
            line += outerSymbol
            for x in range(width-2):
                line += innerSymbol
            line += outerSymbol
        print( line)
        
main()
