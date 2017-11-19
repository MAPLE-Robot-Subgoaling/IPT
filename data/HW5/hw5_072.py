def main():
    wid1 = int(input("Please enter the width of the box: "))
    hei1 = int(input("Please enter the height of the box: "))
    symb1 = str(input("Please enter a symbol for the box outline: "))
    symb2 = str(input("Please enter a symbol for the box fill: "))
    print(symb1 * wid1)
    for i in range(hei1 - 2):
        i = (symb1 + (symb2 * (wid1 - 2)) + symb1)
        print(i)
    print(symb1 * wid1)
main()
