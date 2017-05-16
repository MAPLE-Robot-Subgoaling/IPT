

def main():

    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outerSymbol = input("Please enter a symbol for the box outline: ")
    innerSymbol = input("Please enter a symbol for the box fill: ")



    for h in range(height):
        if h == 0 or h == height - 1:
            print(outerSymbol * width)
        elif h > 0 and h < height - 1:
            print(outerSymbol + innerSymbol * (width - 2) + outerSymbol)     



main()
