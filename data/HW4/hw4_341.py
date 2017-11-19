def main():
    hail1 = int(input("Enter the starting height of the hailstone: "))
    while(hail1 != 1):
        if(hail1 % 2 == 1):
            hail1 = hail1 * 3 + 1
            print("Hail is currently at height", int(hail1))
        if(hail1 % 2 == 0):
            hail1 = hail1/2
            print("Hail is currently at height", int(hail1))
    print("Hailstone stopped at height", int(hail1))
main()
