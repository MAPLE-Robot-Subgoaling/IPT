def main():
    hail_h=int(input("Please enter the starting height of the hailstone: "))
    while hail_h>1:
        print("The hail is currently at height",hail_h)
        if hail_h%2==0:
            hail_h=hail_h//2
        else:
            hail_h=hail_h*3+1
    print("The hail stopped at height",hail_h)
main()
