def main():

    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symbol1 = str(input("Please enter a symbol for the box outline: "))
    symbol2 = str(input("Please enter a symbol for the box fill :"))

    print("",symbol1*width)
    for x in range(2,height):
        print(symbol1,symbol2*(width-2),symbol1)
    print("",symbol1*width)
main()
