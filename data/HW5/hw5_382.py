def main():
    width=input("Please enter the width of the box: ")
    height=input("Please enter the height of the box: ")
    symbol=input("Please enter a symbol for the box outlines: ")
    fill=input("Please enter a symbol for the box fill: ")
    width=int(width)
    height=int(height)
    for i in range(height):
        print(symbol*width)
main()
