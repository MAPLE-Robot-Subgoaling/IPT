def main():
    width = int(input("Width: "))
    height = int(input("Height: "))
    outSym = input("Symbol out: ")
    inSym = input ("Symbol in: ")
    outList = ((outSym) * width)
    inList = ((outSym) + (inSym) * (width - 2) + (outSym))
    for n in range(1):
        print(outList)
    for n in range(2, height):
        print (inList)
    if height > 1:
        for n in range(height, height + 1):
            print (outList)
main()
