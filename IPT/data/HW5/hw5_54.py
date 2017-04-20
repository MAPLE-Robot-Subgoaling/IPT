
def main():
    width = int(input("Please enter the width of the box:"))
    height = int(input("Please enter the height of the box:"))
    symbolOut = input("Please enter a symbol for the box outline:")
    symbolFill= input("Please enter a symbol for the box fill:")
    for i in range(0, height):
        if i==0 or i==height-1:
            print(symbolOut*width)
        else:
            print(symbolOut+ symbolFill*(width-2)+ symbolOut)

main()


