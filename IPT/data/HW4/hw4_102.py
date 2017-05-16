





def main():
    startingHeight = int(input("What is the starting height?"))

    
        
    


    while(startingHeight % 2 == 0):
        startingHeight =  int(startingHeight / 2)
        print("The height of the storm is", startingHeight)


        


        while(startingHeight % 2 == 1 and startingHeight != 1):
            startingHeight = ((startingHeight) * 3) + 1          
            print("The height of the storm is", startingHeight)





        
    while(startingHeight % 2 == 1 and startingHeight != 1):
        startingHeight = (startingHeight * 3) + 1
        print("The height of the storm is", startingHeight)


    


        while(startingHeight % 2 == 0):
            startingHeight = int(startingHeight/2) 
            print("The height of the storm is", startingHeight)
    
                      



main()
