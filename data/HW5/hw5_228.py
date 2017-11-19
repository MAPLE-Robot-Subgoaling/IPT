def main():
    width= int(input("Please enter the width of the box:"))
    height= int(input("Please enter the height of the box:"))
    sym= input("Please enter a symbol for the box outline:")
    sym1= input("Please enter a symbol for the box fill:")
    for row in range(height):
        for col in range(width):
            if row == 0 or row == height-1:
                print(sym, end="")
            elif col == 0 or col == width-1:
                print(sym, end="")
            else:
                print(sym1, end="")
        print()
main()
