
def main():

    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    boxO = input("Please enter a symbol for the box outline: ")
    boxF = input("Please enter a symbol for the box fill: ")

    print(boxO * width)
    for n in range(height - 2):
        print(boxO + boxF * (width - 2) + boxO)
    
    print(boxO * width)
main()
            
