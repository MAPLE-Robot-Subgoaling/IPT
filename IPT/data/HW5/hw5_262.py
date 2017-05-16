
def main():
    wid_box = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symbol = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box fill: ")    
    for i in range (height):
        if i == 0 or i == height - 1:
            print(height * symbol)
        else:
            print(symbol + ((height - 2) * fill) + symbol)
main()
