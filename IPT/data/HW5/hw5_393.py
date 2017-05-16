
def main():

    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symbol = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box fill: ")

    for A in range(0,height):
        if A == 0 or A == (height-1):
            print(symbol * width)

        else:
            print(symbol + (fill * (width-2)) + symbol)

main()
