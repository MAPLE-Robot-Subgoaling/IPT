def main():
    Width = int(input("Please enter the width of the box: "))
    Height = int(input("Please enter the height of the box: "))
    Symbol1 = input("Please enter a symbol for the box outline: ")
    Symbol2 = input("Please enter a symbol for the box fill: ")
    for x in range(0,1):
        print(Symbol1*Width)
    for x in range(0,Height-2):
        print(Symbol1,Symbol2*(Width-2),Symbol1)
    if(Height > 1):
        for x in range(0,1):
            print(Symbol1*Width)
main()
