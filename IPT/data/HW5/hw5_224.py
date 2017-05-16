
def main():

    width = int(input("Enter the width of the box :: "))
    height = int(input("Enter the height of the box :: "))
    outline = input("Enter the box outline symbol :: ")
    fill = input("enter the symbol for the box filler :: ")
    
    for x in range(width):
        for y in range(height):
            print(outline if x in [0, height-1] or y in [0, width-1] else fill, end = ' ')
        print()
main()
