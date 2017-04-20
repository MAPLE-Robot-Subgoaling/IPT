
def main():

    width = int(input("Please enter the width of the box: "))
    length = int(input("Please enter the height of the box: "))
    symbOut = input("Please enter a symbol for the box outline: ")
    symbFill = input("Please enter a symbol for the box fill: ")
    boxRow = ""
    for i in range(0, length):
        if(i != 0 and i != length-1):
            boxRow += symbOut
            for x in range(width-2):
                boxRow += symbFill
            boxRow += symbOut
        else:
            for x in range(width):
                boxRow += symbOut
        print(boxRow)
        boxRow = ""
main()
