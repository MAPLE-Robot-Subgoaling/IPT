def main():
    print("Welcome to the hail storm generator")
    currentHeight=int(input("Please enter the height of the hailstone."))
    if (currentHeight == 0):           
        print("The height you entered is Zero. Please enter height greater than zero.")
    if (currentHeight != 0) :          
        while currentHeight != 1:      
            modValue=currentHeight%2
            if (modValue == 0):        
                print("Hail is currently at height ",currentHeight)
                currentHeight=int(currentHeight/2)
            elif (currentHeight != 1): 
                print("Hail is currently at height ", currentHeight)
                currentHeight=((currentHeight*3)+1)
        else:    
            print("Hail is currently at height 1.")
main()
