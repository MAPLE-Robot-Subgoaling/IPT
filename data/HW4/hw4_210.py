def main():
    hail = int(input("Please enter the starting height of the hailstone: "))
    while hail!=1:
        print("Hail is currently at height ",hail)
        if hail%2==1:
            hail=int(3*hail+1)
        else:
            hail=int(hail/2)
    print("The hail stopped at height",hail)
main()
