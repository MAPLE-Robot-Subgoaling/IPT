

def main():
    
    num1 = int(input("Please enter the starting height of the hailstorm: "))
    print("Hail is currently at height ", num1)
    while num1 > 1 and num1 % 2 == 1:
        num1 = (num1 * 3) + 1
        print("Hail is currently at height ", num1)
        while num1 > 1 and num1 % 2 == 0:
            num1 = num1 / 2
            print("Hail is currently at height ", num1)
            
    while num1 > 1 and num1 % 2 == 0:
        num1 = num1 / 2
        print("Hail is currently at height ", num1)
        while num1 > 1 and num1 % 2 == 1:
            num1 = (num1 * 3) + 1
            print("Hail is currenyl at height ", num1)
   
    print("Hail has stopped at height 1")
    

main()
