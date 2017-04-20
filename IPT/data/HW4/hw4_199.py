
def main():
    
    print() #Seperates text.

    
    print("Welcome to hailstone simulator!") #Greets the player.
    print("The storm outside is howling.") #Provides context of storm.
    heightHailstone = int(input("How high do you want to drop your hailstone? ")) #Asks for startingheight of stone.
    
    print() #Seperates text.

    while heightHailstone != 1: #Keeps running so long as height is not 1...
        
        if (heightHailstone % 2) == 0: #When height is even integer...
            heightHailstone = int(heightHailstone / 2)
        elif (heightHailstone % 2) == 1: #When height is odd integer...
            heightHailstone = int((heightHailstone * 3) + 1)
        
        print("Hail is currently at height", heightHailstone) #Displays height of stone.

    print("Hailstone has landed.") #When the height is 1, the stone will have stopped

    print() #Seperates text.

main()
