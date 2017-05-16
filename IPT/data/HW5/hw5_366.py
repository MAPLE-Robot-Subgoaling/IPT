
def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symbol = input("Please enter a symbol for the box outline:")
    fill = input("Please enter a symbol for the box fill:")
    height= height-2

    if height>1 or width>1:
        print(symbol*width)
        for w in range(0,height):
            print(symbol+(fill*(width-2)+symbol))
        print(symbol*width)
    else:
        print(symbol)
    
    

    


main()






















