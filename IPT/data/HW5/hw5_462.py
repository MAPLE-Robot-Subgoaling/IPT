
def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symbol =  input("Please enter the symbol for the box outline: ")
    fill = input("Please enter the symbol for the box fill: ")
    for row in range(height):
        for col in range(width):
            if row in [0, height-1] or col in [0, width-1]:
                print(symbol, end="")
            else:
                print(fill, end="")
    
        print('\n')
main()

