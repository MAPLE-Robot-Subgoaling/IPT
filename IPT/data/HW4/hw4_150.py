

def main():

    EVEN = 0 
    ODD = 1  

    height = int(input("Please enter starting height of the hailstorm: "))
    
    print("Hail is currently at height" ,  height)

    while height !=1:
        if height % 2 == EVEN:
           height =  height // 2
           print("Hail is currently at height" ,  height)
        elif height % 2 == ODD:
            height = height * 3 +1
            print("Hail is currently at height" ,  height)
    

    print("Hail stopped at height 1")






main()
