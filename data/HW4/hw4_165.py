def main():
    MIN_HAIL_HEIGHT = 1
    EVEN = 0
    ODD = 1
    MOD = 2
    hailHeight = int(input("Please enter the starting height of the hailstone: "))
    while hailHeight < MIN_HAIL_HEIGHT:
        print("Hail height is not valid. Must be greater than 0.")
        hailHeight = int(input("Please enter the starting height of the hailstone: "))
    while hailHeight != MIN_HAIL_HEIGHT:
        if hailHeight % MOD == EVEN:
            hailHeight = hailHeight // 2
        elif hailHeight % MOD == ODD:
            hailHeight = hailHeight * 3 + 1
        if hailHeight != MIN_HAIL_HEIGHT:
            print("Hail is currently at height", hailHeight)
    print("Hail stopped at height", hailHeight)
main()
