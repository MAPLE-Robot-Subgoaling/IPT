def main():
    w_Box = int(input("Please enter the width of the box: "))
    h_Box = int(input("Please enter the height of the box: "))
    sym_Box = input("Please enter a symbol for the box outline: ")
    fill_Box = input("Please enter a symbol for the box fill: ")
    for b in range(h_Box+1):
        if b == 0 or b == h_Box:
            print(sym_Box * w_Box)
        elif b > 0 and b < h_Box-1:
            print(sym_Box + (fill_Box) * (w_Box - 2) + sym_Box)
main()
