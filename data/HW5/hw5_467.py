def main():
    width = int(input("Please enter the width of the box: "))
    sym_out = input("Please enter a symbol for the box outline: ")
    if width != 1: 
        for w in len(width):
            print w * sym_out
main()
