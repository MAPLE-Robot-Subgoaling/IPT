


def main():

    print("Welcome to my program that will help you make a box")

    width = int(input("Please enter the width of the box:"))
    height = int(input("Please enter the height of the box:"))
    firstSymbol = input("Please enter a symbol for the box outline:")
    secondSymbol = input("Please enter a symbol for the box fill:")

    
    for x in range(0,1):
        if width and height == 1:
            print(firstSymbol)
        else:
            print(firstSymbol*width)
            for x in range(0,height-2):
                print(firstSymbol*1 + secondSymbol*(width-2) + firstSymbol*1)
            print(firstSymbol*width)
        


main()
