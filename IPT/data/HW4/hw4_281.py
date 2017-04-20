
def main():
    
    numHail = int(input("Please enter the starting height of the hailstone:" , ))
    
    while numHail != 1:
        
        if (numHail % 2 == 0):
            print("Hail is currently at height" , numHail ,)
            numHail = numHail // 2
        
        elif (numHail % 2 != 0):          
            print("Hail is currently at height" , numHail , )
            numHail = numHail * 3 + 1
    
    print("Hail stopped at height 1")
    
main()
