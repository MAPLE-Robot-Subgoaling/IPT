
def main():

    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symbolOut = input("Please enter a symbol for the box outline: ")
    symbolIn = input("Please enter a symbol for the box fill: ")

    heightList = list(range(0,height - 2,1))

    print(symbolOut * width)

    for h in heightList:
        print((symbolOut) + symbolIn * (width - 2) + (symbolOut))

    if height != 1:
        print(symbolOut * width)
        
main()
