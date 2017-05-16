

def main():
    
    height =int(input("Please enter in the starting height of the hail "))
    
    while height != 1:
        if( height % 2 == 0): 
            height = height // 2
            print("Hail is currently at height", height)
        elif ( height % 2 != 0):
            height = (height * 3)+ 1
            print("Hail is currently at height", height)
    if (height == 1):
        print("hail stopped at 1")


main()    
