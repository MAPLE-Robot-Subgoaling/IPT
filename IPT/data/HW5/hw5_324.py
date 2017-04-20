


def main():
    width =  int(input("Enter the width of the box: "))
    height = int(input("Enter the height of the box: "))
    outline =    input("Enter the symbol the box will be outlined in: ")
    filler =     input("Enter the symbol the box will be filled with: ")
    
    for r in range(0, height):
        line = ""
        for c in range(0, width):
            if(r == 0 or c == 0 or r == height - 1 or c == width - 1):
                line += outline
            else:
                line += filler
        print(line)

main()
