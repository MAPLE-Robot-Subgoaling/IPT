def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    edge = input("Please enter a symbol for the box outline: ")
    inside = input("Please enter a symbol for the box fill: ")
    for i in range(0, width):
        for j in range(0, height):
            if(i == width-1 or j == height-1 or i == 0 or j == 0):
                print (edge, end = '')
            else:
                print(inside, end = '')
        print('')
main()
