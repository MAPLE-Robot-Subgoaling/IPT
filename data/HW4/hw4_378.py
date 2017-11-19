def main():
    enteredNum = int(input("Please enter the starting height of the hailstone:  "))
    print("Hail is currently at height :", enteredNum)
    while enteredNum != 1:
        isEven = enteredNum % 2
        if isEven == 0:
            enteredNum = enteredNum / 2
            print("Hail is currently at height:  ", enteredNum)
        if isEven != 0:
            enteredNum = (enteredNum * 3) + 1
            print("Hail is currently at height:  ", enteredNum)
    print("Hail stopped at hight :", enteredNum)
main()
