

def main():
    height = float(input(" enter the starting height of the hail storm"))
        
    print("Hail is currently at the height,", height)
	
    while height != 1:
        if (height % 2) == 0:
            height = (height //2)
            print(" Hail is currentl at the height,",height)
        else:
            height = (height * 3) + 1
            print(" hail is currently at the height,", height)

        
                
    print(" Hail stopped at height 1")
  

    


main()
