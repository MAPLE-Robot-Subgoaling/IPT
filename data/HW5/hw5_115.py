def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symbol = input("Please enter a symbol for the box outline: ")
    symbol1 = input("Please enter a symbole for the box fill: ")
    for i in range(0,height):
       if i==0 or i == height-1:
           print(symbol*width)
       else:
           print(symbol,symbol1*int(width-2),symbol)
main()
