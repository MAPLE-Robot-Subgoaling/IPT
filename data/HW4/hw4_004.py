def main():
    startH = int(input("What is the starting height of the hailstone?"))
    print("The hailstone is currently at height ", startH)
    while (startH != 1 and startH > 1):
        if (startH % 2 == 0):
            startH = (startH // 2)
            print("The hail is currently at height ", startH)
        else:
            startH = ((startH * 3) + 1)
            print("The hail is currently at height ", startH)
    if startH == 1:
            print("The hail stopped at height 1")
main()
