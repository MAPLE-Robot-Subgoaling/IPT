def main():
    hailHeight = int(input("Please enter the starting height of hailstone: "))
    print(hailHeight)
    while hailHeight != 1:
        if hailHeight % 2 == 0:
            hailHeight = hailHeight // 2 
            print("Hail is currently at height" , hailHeight)
        elif hailHeight % 2 != 0:
            hailHeight = (hailHeight * 3) + 1
            print("Hail is currently at height" , hailHeight)
    print("Hail stopped at height 1")                         
main()
