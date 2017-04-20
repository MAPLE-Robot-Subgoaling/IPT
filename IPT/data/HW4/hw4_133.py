def main():
    x = int(input("Please enter the starting height of the hailstone: "))
    while(x != 1):
        print("Hail is currently at height " + str(x))
        if(x % 2 == 0):
            x = int(x/2)
        elif(x % 2 !=0):
            x = int((x*3)+1)
    print("Hail stopped at height " + str(x))
main()
