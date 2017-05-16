
def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box fill: ")
    line = ""

    for i in range(0, height):
        for j in range (0, width):
            if i != height -1 and i != 0 and j != width-1 and j != 0:
                line = line + " " +  fill
            else:
                line = line + " " + outline
        print(line)
        line = ""



main()
