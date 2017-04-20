
def main():

    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box fill: ")

    for x in range(0,height):
        row = ""
        for y in range(0,width):
            if x == 0 or y == 0 or y == width-1 or x == height -1:
                row = row + outline
            else:
                row = row + fill
        print(row)

main()
