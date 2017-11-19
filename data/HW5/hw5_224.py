def main():
    width = int(input("Width of box? "))
    hight = int(input("height of box? "))
    outline = input("Symbol for outline? ")
    fill = input("symbol for inside of box ")
    strPrint = ""
    for i in range (0, width):
        if (i == 0 or i == hight - 1):
            for j in range(0, width):
                strPrint = strPrint + outline
            print(strPrint)
            strPrint = ""
        else:
            strPrint = outline
            for j in range(0, width - 2):
                strPrint = strPrint + fill
            strPrint = strPrint + outline
            print(strPrint)
            strPrint = ""
main()
