
def main():
    num = int(input("Please enter the starting height of the hailstone: "))
    while num != 1:
        if num%2 == 0:
            num = num/2
        else:
           num = (num*3)+1     
        print("Hail is currently at height",num)
    print("Hail stopped at height 1")
main()
