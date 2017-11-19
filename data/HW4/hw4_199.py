def main():
    startHigh = int(input("Please enter the starting height of the hailstone: "))
    STOP_HIGH = 1
    if startHigh == STOP_HIGH:
        print("The hailstone has stopped.")
    else:
        while startHigh != STOP_HIGH:
            if startHigh % 2 == 0:
                startHigh = startHigh//2
                print("Hail is currently at height",startHigh)
            else:
                startHigh = startHigh*3+1
                print("Hail is currently at height",startHigh)
        print("The hailstone has stopped at height",STOP_HIGH)
main()
