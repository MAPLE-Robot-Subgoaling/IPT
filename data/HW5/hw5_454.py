def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outline = input("Please enter a symbol for the box outline: ")
    fill = input("Please enter a symbol for the box fill: ")
    for x in range(0, height):
        if x == 0 or x== height-1:
            for y in range(0, width):
                print(outline, end = "")
        else:
            for y in range(0, width):
                if y == 0 or y == width-1:
                    print(outline, end ="")
                else:
                    print(fill, end ="")
        print("\n", end ="")
main()
