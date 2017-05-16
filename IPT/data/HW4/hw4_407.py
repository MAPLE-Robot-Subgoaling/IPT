
def main():
    userInput = int(input("Please input a number: "))
    while userInput != 1:
        print("Your hail is currently at", userInput)
        if userInput % 2 == 0:
            userInput = userInput / 2
        elif userInput % 2 != 0:
            userInput = (userInput * 3) + 1
    print("Hail stopped at 1")
main()
