def main():
    wideth= int(input("Gib me wide"))
    longth = int(input("Gibe me long"))
    border = input("gibe boder pls")
    filling = input("gib filling pls")
    for a in range(longth):
        if(a == 0 or longth-a == 1):
            print(border*wideth)
        else:
            for b in range(wideth):
                if(b == 0):
                    print(border, end="")
                elif (wideth-b == 1):
                    print(border)
                else:
                    print(filling, end="")
main()
