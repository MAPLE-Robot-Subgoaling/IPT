

def main():

    
    
    current_height = int(input("Please enter a positive integer: "))

    while current_height !=1:
        
        if (current_height%2)==0:
                current_height = int(current_height/2)
                print ("Hail is currently at height "+str(current_height))
        
        elif (current_height%2)!=0:
                current_height =int((current_height*3)+1)
                print ("Hail is currently at height "+str(current_height))
        
 
    print ("Hail stopped at height "+str(current_height))
                
    






main()
