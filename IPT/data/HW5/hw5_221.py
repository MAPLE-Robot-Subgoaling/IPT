
def main():
    width = int(input("please enter the width of the box"))
    height = int(input("please enter the height of the box"))
    symbol1 = input("enter the symbol for box outline")
    symbol2 = input("enter the symbol for the box fill")
    symbolcon =  symbol1+symbol2*(width-2)+symbol1
    if width>1 and height>1:
        for i in range(1):
            print(symbol1*width,)
            for a in range(1,height-1):
                print(symbolcon)
        print(symbol1*width)
    elif width== 1 and height ==1:
        print(symbol1)
    elif width==1 and height>1:
        for x in range(height):
            print(symbol1)
    else:
        print(symbol1*width)
main()
