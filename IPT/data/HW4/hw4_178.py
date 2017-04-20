



def main():

    number2 = int(input("Enter the starting height of hailstone: "))
    number1 = []
    number1.append(number2)
    while number2 > 1:
        if number2 % 2 == 0:
            number2 = number2 / 2
        else:
            number2 = (number2 * 3) + 1
        number1.append(int(number2))

    print ("The current length is: " + str(number1))
main()
