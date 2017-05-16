
def main():
    width = int(input(" Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symbolOne = input("Please enter a symbol for the box outline: ")
    symbolTwo = input("Please enter a symbol for the box fill: ")
    for i in range(height):
        if i == 0 or i == height - 1:
            print(symbolOne * width)
        else:
            print(symbolOne + symbolTwo * (width - 2) + symbolOne)
        
    
          
main()
