def main():
    print("WELCOME !")
    width=input("Please enter the width of the box ? ")
    height=input("Please enter the height of the box ? ")
    symbol=input("Please enter a symbol for the box outline: ")
    symbolIn=input("Please enter a symbol for the box fill: ")
    width=range(int(width))
    height=range(int(height))
    for i in width:
        i=symbol
        print(symbol)
    for r in height:
        r=symbol
        print(symbol)
main()
