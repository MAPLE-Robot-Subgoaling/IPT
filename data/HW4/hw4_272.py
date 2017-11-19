def main():
    int1=int(input("Please enter the starting height of the hailstorm: "))
    while int1 != 1:
        print("Hail is currently at height",int(int1))
        if int1 % 2 == 0:
            int1=int1/2
        elif int1 % 2 == 1:
            int1=int1*3+1
    print("Hail stopped at height 1")
main()
