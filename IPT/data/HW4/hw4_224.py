

def main():

    height = int(input("Enter the start height of the storm :: "))
    
    while (height != 1):
        if(height == 1):
            print("The storm as stopped.")
        if(height % 2 != 0 and height != 1):
            height = (height * 3) + 1
            print("Height is ", height)
        if(height % 2 == 0):
            height = height / 2
            print("Height is ", height)
    else:
        print("The storm has stopped.")
main()
                
        
        
