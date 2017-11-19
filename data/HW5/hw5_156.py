def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    symbol = str(input("Please enter a symbol for the box outline: "))
    filler = str(input("Please enter a symbol for the box fill: "))
    middle = []
    ends = []
    ends.append(symbol)
    ends.append(symbol)
    middle.append(symbol)
    for i in range(1,width-1):
        middle.append(filler)
        ends.append(symbol)
    middle.append(symbol)
    for k in range(0,width):
        print(ends[k],end="")
    print("\n")
    for l in range(1,height-1):
        for j in range(0,width):
            print(middle[j],end="")
        print("\n")
    for m in range(0,width):
        print(ends[m],end="")
    print("\n")
main()
