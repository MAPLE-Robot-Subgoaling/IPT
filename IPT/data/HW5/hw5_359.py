
def main():
    wid = int(input("How wide do you want the box?: "))
    height = int(input("How tall do you want the box?: "))
    sym1 = input("Enter a symbol for the box outline: ")
    sym2 = input("Enter a symbol for the box insides: ")
    for y in range(0, (height)):
        if (y == 0 or y == (height - 1)):
            print(sym1 * wid)
        else:
            print(sym1 + (sym2 * (wid - 2)) + sym1)
        
main()
