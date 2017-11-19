def main():
    a = int(input("Please enter the starting height of the hailstone: "))
    while a !=1:
        print("Hail is currently at height",int(a))
        if a %2== 0:
            a/=2
        else:
            a = a*3+1
    print("Hail stopped at height 1")
main()              
