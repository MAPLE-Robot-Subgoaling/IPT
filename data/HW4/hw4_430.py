def main():
    height = int(input("Please enter the starting height of the hailstorm: "))
    print()
    while height != 1: 
        if height % 2 == 0: 
            newheight = (height/2) 
            height = newheight  
            if height == 1: 
                print("Hail stopped at height 1")
            else:
                print("Hail is currently at height", int(newheight))
        else: 
            newheight = (height * 3) + 1 
            height = newheight 
            if height == 1:
                print("Hail stopped at height 1")
            else:
                print("Hail is currently at height", int(newheight))
    print()
main()
