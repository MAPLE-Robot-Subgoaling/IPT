def main():
    num1 = int(input("Please enter the starting height of the hailstone:"))
    while num1 != 1:
        if (num1)% 2 == 0:   
            num1 = (num1)/2
        else:
            num1 = (num1*3)+1 
        print("Hail us currently at height ", num1) 
    print("Hail stopped at height 1")
main()
