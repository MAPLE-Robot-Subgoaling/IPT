
def main():

    height = int(input("Please enter the starting height of the hailstorm: "))
    print()
    while height != 1: #intilizes loop
        if height % 2 == 0: #proceeds if loop is even
            newheight = (height/2) 
            height = newheight  #sends value to height and continues loop until it is 1
            if height == 1: #tells user current value and when it finally reaches 1
                print("Hail stopped at height 1")
            else:
                print("Hail is currently at height", int(newheight))


        else: #proceeds if value is odd
            newheight = (height * 3) + 1 
            height = newheight #sends to height and continues loop until it is 1
            if height == 1:
                print("Hail stopped at height 1")
            else:
                print("Hail is currently at height", int(newheight))
    print()
main()
