def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: ")) 
    symbol = input("Please enter a symbol for the box outline: ")
    symbol2 = input("Please enter a symbol for the box fill: ")
    for i in range(height):
        if(i == 0 or i == height-1):
            print(symbol*width)
        else:
            print(symbol+symbol2 *(width -2)+symbol)
             
    
main()
