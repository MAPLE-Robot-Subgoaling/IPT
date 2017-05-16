def main():
    boxWidth=int(input("Please enter the width of the box:"))
    boxHeight=int(input("Please enter the height of the box:"))
    sym1=input("Please enter a symbol for the box outline:")
    sym2=input("Please enter a symbol for the box fill:")
    innerHeight = boxHeight - 2
    innerWidth = boxWidth - 2
    innerRow = sym1 + sym2 * innerWidth + sym1
    counterList = [0] * innerHeight
    print(sym1*boxWidth)
    for a in counterList:
        print(innerRow)
    if boxHeight != 1:
        print(sym1*boxWidth)
        
    
main()
