def main():
    wBox = int(input("Please enter the width of the box: "))
    hBox = int(input("Please input the height of the box: "))
    outSymb = str(input("Please enter a symbol for the box outline: "))
    inSymb = str(input("Please enter a symbol for the box fill: "))
    insideBox = (wBox - 2)
    print(wBox*outSymb)
    for x in range(hBox - 2):
        print(outSymb + (inSymb * insideBox) + outSymb)
    print(wBox*outSymb)
main()
