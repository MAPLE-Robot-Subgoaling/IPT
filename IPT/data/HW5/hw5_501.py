

def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline= (raw_input("Please enter a symbol for the box outline: "))
    fill= (raw_input("Please enter a symbol for the box fill: "))

    for y in range (0, height):
        output = ""
        for x in range (0, width):
            if(y == 0 or y == (height-1) or x == 0 or x == (width-1)):
                output = output + outline
            else:
                output = output + fill
        print(output)
main()
