
def main():

    width= input("please enter the width of the box: ")
    width= int(width)
    height= input("pleas enter the height of the box: ")
    height= int(height)
    symbol= input("pleas enter a symbol for the box outline: ")
    fill= input("pleas enter a symbol for the box fill: ")

    for n in range(height):
        if (n==0):
            print(symbol*width)
        elif(n==(height-1)):
            print(symbol*width)
        else:
            print(symbol + fill*(width-2) + symbol)
main()
