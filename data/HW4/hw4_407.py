hailHt = int(input("Please enter the starting height of the hailstone: "))
print("Hail is currently at height", hailHt)
while hailHt != 1:
    while hailHt % 2 == 1:
        hailHt = int((hailHt *3) + 1)
        print("Hail is currently at height", hailHt)
    while hailHt % 2 == 0:
        hailHt = int(hailHt / 2)
        print("Hail is currently at height", hailHt)
print("Hail stopped at height 1")
