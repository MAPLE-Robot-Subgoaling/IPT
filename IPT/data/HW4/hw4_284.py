


def main():
    num=int(input("Please enter the starting height of the hailstone:"))
    while num!=1:
        if num%2==0:
            print ("Hail is currently at height",num)
            num=num//2
        elif num%2==1:
            print ("Hail is currently at height",num)
            num=num*3+1
    if num==1:
        print("Hail stopped at height 1")


main()
