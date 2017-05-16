
def main():
    length = int(input("Please enter the length of the box: "))
    height = int(input("Please enter the height of the box: "))
    symb1 = input("Please enter a symbol for the outline of the box: ")
    symb2 = input("Please enter a symbol for the box fill: ")
    j = 1
    for j in range(1,height + 1):
        if j == 1 or j == height:
            print(symb1 * length)
            j = 1 + j
        else:
            print(symb1 + symb2 * (length - 2) + symb1)
            j = 1 + j
main()
