def main():
    startHeight=int(input("Please enter the start height of the hailstone: "))
    print("Hail is currently at height", startHeight)
    while startHeight % 2 == 0 and startHeight > 1:
        startHeight= (startHeight // 2)
        print("Hail is currently at height",startHeight)
        while startHeight % 2 != 0 and startHeight > 1:
              startHeight= (startHeight*3) + 1
              print("Hail is currently at height",startHeight)
    print("Hail stopped at height", startHeight)
main()
