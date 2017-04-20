def main():
    start=int(input("Please enter starting height of the hailstone:"))
    while start <=0:
        print("The start height needs to be positive.")
        start=int(input("Please enter the starting height of the hailstone:"))
    if start != 1:
        print("Hail is currently at height", start)
    while(start>1):
        if(start%2==0):
            start=start//2
            if start !=1:
                print("Hail is currently at height",start)
        elif(start%2==1):
            start=(start*3)+1
            if start !=1:
                print("Hail is currently at height",start)
    print("Hail stopped at height",start)


main()
