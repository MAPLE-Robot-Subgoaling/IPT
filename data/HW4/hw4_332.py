def main():
    x = int(input("Please enter the starting height of the hailstone: "))
    while x != 1:
        if x % 2 == 0:
            x = x/2
            print("Hail is currently at height",x)
        elif x % 2 != 0:
            x = (x*3)+1
            print("Hail is currenlty at height",x)
    print("Hail stopped at height 1")
main()
