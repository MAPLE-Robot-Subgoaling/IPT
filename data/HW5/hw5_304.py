def main():
    width= int(input("Please enter the width of the box:"))
    height = int(input("Please enter the height of the box:"))
    symbol1= input("Please enter a symbol for the box outline:")
    symbol2= input("Please enter a symbol for the box fill:")
    print(width*symbol1)
    for element in range(height-2):
        print(symbol1 + symbol2*(width-2)+symbol1)
    if(height!=1):
        print(width*symbol1)
main()
