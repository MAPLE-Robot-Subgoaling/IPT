def main():
    w = int(input("Please enter the width of the box: "))
    h = int(input("Please enter the height of the box: "))
    sym1 = input("Please enter a symbol for the box outline: ")
    sym2 = input("Please enter a symbol for the inside of the box: ")
    fill = w - 2
    end = h - 1
    for m in range(h):
        if m == 0 or m == end:
            print(sym1 * w)
        else:
            print(sym1 + (sym2 * fill) + sym1)
main()
