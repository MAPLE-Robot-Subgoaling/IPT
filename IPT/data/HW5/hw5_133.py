def main():
    width = input("Please enter the width of the box: ")
    height = input("Please enter the height of the box: ")
    sym1 = input("Please enter a symbol for the box outline: ")
    sym2 = input("Plese enter a symbol for the box fil: ")
    for y in range(0,int(height)):
        for x in range(0,int(width)):
            if y == 0 or y == int(height)-1:
                print(sym1, end = " ")
            else:
                if x==0 or x == int(width)-1:
                    print(sym1, end = " ")
                else:
                    print(sym2, end = " ")
        print("")
main()
