def main():

    width = int(input("Please enter the width: "))
    height = int(input("Please enter the height: "))
    outline = input("Please enter the symbol to be outlined with: ")
    fill = input("Please enter the symbol to be filled with: ")
    for i in range(height):
        for j in range(width):
            if (i != 0 and j != 0 and i != height-1 and j != width-1):
                print(fill, end="")
            else:
                print(outline, end ="")
        print()

main()
