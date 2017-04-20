
def main():

    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symbol = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box fill: ")
    
    for heightCount in range(height):

        if heightCount == 0 or heightCount == (height - 1):
            print(symbol * width)

        else:
            print(symbol + fill * (width - 2) + symbol)
               

main()
