def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symbol = str(input("Please enter a symbol to outline the box: "))
    fill = str(input("Please enter a symbol for the box to fill: "))
    print(symbol*width)
    for j in range(height):
        print(symbol+(fill*(width-2))+symbol)
    print(symbol*width)
main()
