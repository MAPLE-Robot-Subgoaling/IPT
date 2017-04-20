

def main():
    print("Welcome to the hail storm generator")
    currentHeight=int(input("Please enter the height of the hailstone."))
    if (currentHeight == 0):           # Making sure Zero is not input. 0 leads to infinite loop.
        print("The height you entered is Zero. Please enter height greater than zero.")
    if (currentHeight != 0) :          # Loop only if input value is not zero.
        while currentHeight != 1:      # Loop until currentHeight becomes 1.
            modValue=currentHeight%2
            if (modValue == 0):        # Check for even number.
                print("Hail is currently at height ",currentHeight)
                currentHeight=int(currentHeight/2)
            elif (currentHeight != 1): # Check for odd number.
                print("Hail is currently at height ", currentHeight)
                currentHeight=((currentHeight*3)+1)
        else:    # Current value is 1.
            print("Hail is currently at height 1.")
            

main()
