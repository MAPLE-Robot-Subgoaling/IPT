
def main ():
    num = int(input("Please enter the starting height of the hailstorm. "))
    numE = num % 2
    numO = num * 3 + 1
    while(num != 1):
        if (num % 2) != 0:
            num = ((num * 3) + 1)
            print("Hail is currently at the height " , num ,)
        elif (num % 2) == 0:
            num = num/2
            print("Hail is currently at the height " , num ,)
        if num == 1:
            print("Hail stopped at height " , num ,)
        
main()
