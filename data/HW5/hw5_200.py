def main():
    width = int(input("Please enter the width of the box: "))
    heightNum = int(input("Please enter the hieght if the box: "))
    height = range(heightNum)
    sym1 = input("Please enter the symbol for the outline: ")
    sym2 = input("Please enter the symbol to fill the box: ")
    for i in height:
        if i == 0 or i == heightNum - 1:
            print(sym1*width)
        else:
            print(sym1+(sym2*(width-2))+sym1)
main()
