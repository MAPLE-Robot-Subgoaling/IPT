def main():
    wBox=int(input("Please enter the width of the box: "))
    hBox=int(input("Please enter the height of the box: "))
    symbOut=input("Please enter the symbol for the box outline: ")
    symbIn=input("Please enter the symbol for the box fill: ")
    print(symbOut*wBox)
    for h in range(0,(hBox-2)):
        print(symbOut+(symbIn*(wBox-2))+symbOut)
    if(hBox>1):
        print(symbOut*wBox)
main()
