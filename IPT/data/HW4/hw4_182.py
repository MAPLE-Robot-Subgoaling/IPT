
def main():
    height = int(input("Please input the starting height of the hailstone: "))# Asks for the starting height of the hail
    hailStop = 1 # height at which the hailstone will stop
    evenOdd = height % 2 # Checks to see if the height is even or odd
    evenHeight = 0 # Sets the condition for an even or odd height
    even = height // 2 # Divides an even height by 2 to receive new height
    odd = (height * 3) + 1 # Multiplies and adds 1 to an odd height to receive a new height
    if height == hailStop: # Sets a condition in case the user inputs a height of 1
        print("The hail stopped at height 1") # informs user that hail stopped
    while height != hailStop: # Executes a while loop to measure the hailstone in the storm
        if evenOdd == evenHeight: # Filters out even heights
            even = height // 2 # Divides an even height by 2 to receive new height
            height = even # Sets the height to the new value
            evenOdd = height % 2 # Redefines the evenOdd algorithim
            if height == hailStop: # sets a condition for if the hail is at 1 in order to not restate the height of the hail if it is at 1
                print("Hail stopped at height 1")
            else: # if it isn't one just iterates back as normal    
                print("Hail is currently at height", height) # Tells user the current height of hail
        elif evenOdd != evenHeight: # Filters out odd heights
            odd = (height * 3) + 1 # Multiplies and adds 1 to an odd height to receive a new height
            height = odd # Sets the height to the new value
            evenOdd = height % 2 # Redefines the evenOdd algorithim
            print("Hail is currently at height", height) # Tells user the current height of hail
main()    
