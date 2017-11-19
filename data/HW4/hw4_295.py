def main():
    userNum = int(input("Please enter the starting height of the hailstorm: "))
    currHeight = 1
    dRemainder = userNum % 2
    print("Hail is currently at height", userNum)
    while userNum != currHeight:
        if dRemainder == 0:
            userNum = int(userNum / 2)
            print("Hail is currently at height", userNum)
            dRemainder = userNum % 2
        else:
            userNum = int(userNum * 3 + 1)
            print("Hail is currently at height", userNum)
            dRemainder = userNum % 2
    print("Hail stopped at height 1")
main()
