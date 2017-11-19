def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symb1 = input("Please enter a symbol for the box outline: ")
    symb2 = input("Please enter a symbol for the box fill: ")
    for i in range (0, height):
        if (i==0) or (i ==height-1):
            print(symb1*height)
        else:
            print (symb1+ symb2*(height-2)+ symb1)
main()
