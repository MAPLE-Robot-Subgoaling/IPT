def main():
    widNum = int(input("What do you want the width to be?: "))
    lengNum = int(input("What do you want the legnth to be?: "))
    sym1 = input("What symbol do you want the outside of the box to be?: ")
    sym2 = input("What symbol do you want the inside of the box to be?: ")
    print(sym1*widNum)
    for h in range(lengNum-2):
        print(sym1+sym2*(widNum-2)+sym1)
    print(sym1*widNum)
main()
