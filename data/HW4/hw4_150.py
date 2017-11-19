def main():
    hail = int(input("Please enter the starting height of the hailstone: "))
    while (hail!=1):
        print("Hail is currently at height %i" %(hail))
        if (hail%2)!=0:
            hail = (hail*3)+1
        else:
            hail = (hail/2)
    print("Hail stopped at height %i" %(hail))
main()
