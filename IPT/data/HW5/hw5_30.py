
def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outlineSymbol = input("Please enter a symbol for the box outline: ")
    fillSymbol = input("Please enter a symbol for the box fill: ")
    temp = ""

    for x in range(0, height):
        temp = ""
        for y in range(0, width):
            if(x==0 or x==height-1):
                temp = temp + outlineSymbol
            elif(y==0 or y==width-1):
                temp = temp + outlineSymbol
            else:
                temp = temp + fillSymbol

        print(temp)

    print()
main()
