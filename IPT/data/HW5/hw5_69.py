
def main():
    width = int(input("Enter the width of the box: "))
    height = int(input("Enter the height of the box: "))
    outer = str(input("Enter a character for the box outline: "))
    inner = str(input("Enter a character for the box fill: "))
    for h in range(height):
        if h == 0 or h == height-1 :
            print(outer*width)
        else:
           print(outer + inner*(width-2) + outer)
main()
