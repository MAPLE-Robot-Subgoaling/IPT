 
def main():


    userHailStone = int(input("Please enter the starting height of the hailstone: "))

    if userHailStone != 1 :

       print("Hail is currently at", userHailStone)

       CONSTANT = 2

       remainder = userHailStone % CONSTANT 
              
       if  remainder >=0 :

           if  remainder == 0:

               numEven = userHailStone // CONSTANT
                
               print("Hail is currently at height", numEven)
                
               remainder = numEven % CONSTANT

           elif  remainder != 0 :
                
               CONSTANT_ODD = 3
 
               ODD_ADDITION = 1
 
               numOdd = (userHailStone *  CONSTANT_ODD) + ODD_ADDITION
                      
               print("Hail is currently at height", numOdd)
                             
               remainder = numOdd % CONSTANT


           else :

                 print("Hail stopped at height 1.")
                                      
       else :
 
             print("Hail stopped at height 1.")   


    else :

          print("Hail stopped at height 1.")

main()
  

              
