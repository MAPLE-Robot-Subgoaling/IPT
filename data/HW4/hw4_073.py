def main():
    number = int(input("Please enter the starting height of the hailstone: "))
    while number < 1:
        number = int(input("Please enter the starting height of the hailstone: "))
    while number > 1:
        if number % 2 == 0:
            number = number/2
            print("Hail is currently at height", int(number))
        elif number % 2 == 1:
            number = (number * 3)+1
            print("Hail is currently at height", int(number))
    print("Hail stopped at height",int(number))
main()
