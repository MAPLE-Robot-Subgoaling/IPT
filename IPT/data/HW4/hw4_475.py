


def main() :

    
    num = 0
    
    num = int(input("Enter the starting height of the hailstone:"))
    
    while num > 1:
        
        if num % 2 == 0:
            num = num / 2
            num = int(num)
            print("Hail is currently at height:",num)
        else:
            num = num * 3 +1
            num = int(num)
            print("Hail is currently at height:",num)
    print("Hail has stopped at height:",num)

main()          
              

         
