def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box fill: ")
    for x in range(height):
        line = ""
        for y in range(width):
            if x == 0 or x == height - 1 or y == 0 or y == width - 1:
                line = line + outline 
            else:
                line = line + fill
        print (line)
main()
