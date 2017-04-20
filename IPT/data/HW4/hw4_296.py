
def main():
    number = int(input("Enter a positive number: "))
    print("Hail is currently at height",number)
    while number!=1:
        if number % 2 == 0:
            number = int(number/2)
            print("Hail is currently at height", number)
        else:
            number = int((number*3)+1)
            print("Hail is currently at height", number)
    print("Hail stopped at height 1.")
main()
