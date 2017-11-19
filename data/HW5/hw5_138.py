def main():
    width = int(input("Please enter the width of the box:"))
    height = int(input("Please enter the height of the box:"))
    outlineSymbol = input("Please enter a symbol for the box outline:")
    fillSymbol = input("Please enter a symbol for the box fill:")
    topBottom = ""
    for x in range(0, width):
        topBottom += outlineSymbol
    inner = ""
    if((width - 2) > 0):
        for x in range(0, width - 2):
            inner += fillSymbol
    if(height > 0):
        print(topBottom)
    if((height - 2) > 0):
        for x in range(0, height-2):
            inside = outlineSymbol + inner + outlineSymbol
            print(inside)
    if(height > 1):   
        print(topBottom)
main()
