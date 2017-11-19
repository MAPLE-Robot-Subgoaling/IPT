def main():
    outer = input("Please enter a symbol for the box outline: ")
    width = int(input("Please enter the width of the box: "))
    inner = input("Please enter a symbol for the box to be filled with: ")
    height = int(input("Please enter the height of the box: "))
    firstLine = width * outer
    print ( firstLine )
    if height > 2:
        innerLine = outer + inner * ( width - 2 ) + outer
        for i in range(height - 2): 
            print (innerLine)
    if height > 1: 
        print ( firstLine )
main()
