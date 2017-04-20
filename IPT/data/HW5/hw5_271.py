
def main():
    
    width=int(input("Please enter the width of the box: "))
    length=int(input("Please enter the height of the box: "))
    outline=input("Please enter the symbol for the box outline: ")
    filler=input("Please enter the symbol for the box fill: ")
    print(outline*width)
    for i in range(0,length-2):
        print(outline,filler*(width-2),outline)
    print(outline*width)
main()
