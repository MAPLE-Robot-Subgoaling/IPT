
def main() :
   
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter a symbol for the box outline: ")
    filler = input("Please enter a symbol for the box fill: ")

    for y in range(height) :
        row = ""
        for x in range(width) :
            if x == 0 or x == (width - 1) or y == 0 or y == (height - 1) :
                row = row + outline
            else :
                row = row + filler
        print(row)

main()
