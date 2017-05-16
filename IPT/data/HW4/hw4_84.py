
def main() :

    userInput = int(input("Please enter the height of the hailstone: "))
    while userInput != 1:
        if (userInput % 2) == 0 :
            userInput = userInput // 2
        else :
            userInput = userInput * 3 + 1

        print("The hailstone is currently at height ", userInput)

    print("The hailstone stopped at height ", userInput)

main()
