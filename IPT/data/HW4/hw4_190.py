





def main ():

    hailStorm = int(input("Please enter the starting height of the Hailstorm: "))

    

    while hailStorm != 1:
        print ("Hail is currently at height " ,hailStorm) # prints out current height

        mod1 = int(hailStorm % 2) #checks to see if mod is 0

        if mod1 == 0:
    
            hailStorm = int(hailStorm/2)
    
        elif mod1 !=0 :
            hailStorm = int(hailStorm*3)+1
    

    if hailStorm == 1:
        print("Hail stopped at height ", hailStorm)
        exit ()



main ()
