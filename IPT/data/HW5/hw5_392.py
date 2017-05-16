def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symOut = input("Please enter a symbol for the box outline: ")
    symFill = input("Please enter a symbol for the box fill: ")
    print(symOut*width)
    for i in range(height-2):
        print(symOut+symFill*(width-2)+symOut) 
    if width  > 1 or  height > 1:
        print(symOut*width)
main()
