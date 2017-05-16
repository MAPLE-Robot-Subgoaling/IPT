


def main():
    
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = str(input("Please enter a symbol for the box outline: "))
    fill = str(input("Please enter a symbox for the box fill: "))

    for index in range(height):
        line = ""
        if(index == 0 or index == height - 1):
            for number in range(width):
                line = line + outline
        if(index != 0 and index != height - 1):
            for number in range(width):
                if(number == 0 or number == width - 1):
                    line = line + outline
                if(number != 0 and number != width - 1):
                    line = line + fill
        print(line)
main()
