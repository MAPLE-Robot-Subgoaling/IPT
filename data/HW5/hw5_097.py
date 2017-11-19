def main():
    print("Welcome to the box designer.")
    width=int(input("Please enter a positive width of the box: "))
    height=int(input("Please enter a positive height of the box: "))
    outerSymbol=input("Please enter a symbol for the box outline: ")
    innerSymbol=input("Please enter a symbol for the box fill: ")
    for h in range(0,height):
        stringLine=''
        for w in range(0,width):
            if (h == 0 or h == height-1 or w == 0 or w == width-1):
                stringLine=stringLine+outerSymbol
            else:
                stringLine=stringLine+innerSymbol
        print(stringLine)
main()
