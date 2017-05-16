
def main():
    
    WIDTH = int(input("Please enter the width of the box: "))
    HEIGHT = int(input("Please enter the height of the box: "))
    OUTLINE = input("Please enter the symbol for the outline of the box: ")
    FILLING = input("Please enter the symbol for the inside of the box: ")
    
    def edge():
        print(OUTLINE*WIDTH)
    def inside():
        print(OUTLINE + FILLING*(WIDTH-2) + OUTLINE)

    
    for x in range(HEIGHT):
        if(x == 0 or x==HEIGHT-1):
            edge()
        else:
            inside()
   
main()
