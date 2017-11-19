def main():
    print("Let's see if we can simulate the movement of a hailstone in a storm.")
    height = input("Enter a number for the starting height of the hailstone:   ")
    calcHeight = int(height)
    while calcHeight != 1:
          if calcHeight % 2  == 0:
             calcHeight = int(height) // 2
          elif calcHeight % 2 > 0:
             calcHeight = (int(height) * 3) + 1
    print("Hail stopped at height of 1.")
main()
