
def main():
    num1= int(input("Please enter the starting height of the hailstone: "))
    while num1 != 1:
        print("Hail is currently at height",num1)
        if num1 % 2 == 0:
            num1 = num1//2
        elif num1 % 2 == 1:
            num1 = (3*num1)+1
            
    if num1 == 1:
        print("Hail stopped at height 1")
main()
