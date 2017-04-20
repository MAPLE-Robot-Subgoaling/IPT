
def main():
    FINAL_HGT = 1
    hailHgt = int(input("Please enter the starting height of the hailstone: "))
    while hailHgt != FINAL_HGT:
        hailCur = hailHgt % 2
        print("Hail is currently at height", hailHgt)
        if hailCur == 0:
            hailHgt = hailHgt // 2
        else:
            hailHgt = hailHgt * 3 + 1
    print("Hail stopped at height", FINAL_HGT)

main()
