def main():
    width = int(input("Enter the width of the box"))
    length = int(input("Enter the length of the box"))
    symb = input("Enter a symbol for the outline of the box")
    symb2 = input("Enter a symbol for the box fill.")
    print(symb * width)
    for n in range(0, length-1):
        print( symb + symb2*(width-2) + symb)
    print(symb * width)
main()
