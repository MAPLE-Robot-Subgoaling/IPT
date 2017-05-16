



def main():
 

   currentHeight = int(input("Please enter the starting height of the hailstone:"))

   while currentHeight > 0:

    
        if currentHeight % 2 == 0:
           height = currentHeight / 2
           print("Hail is currently", currentHeight)
           print(" Hail is currently", height)     

        elif currentHeight % 2 != 0:
           height = currentHeight *3 - 1
           print("Hail is currently at", currentHeight)
           print("Hail is currently at", height)  
           

   print("Hail stopped at 1")

main()
