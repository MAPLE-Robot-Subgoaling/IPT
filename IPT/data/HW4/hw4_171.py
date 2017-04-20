
def main():
    x = int(input("Please enter a positive integer: "))
    if x < 0:
        x = x * -1
        print("Your integer was made positive")
    while x != 1:
        if x % 2 == 0:
            x = x/2
            print(x)
        elif x % 2 == 1:
            x = (x*3)+1
            print(x)
    print("current height is now one!")

main()
