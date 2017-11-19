def main():
    hailHeight = int(input("Please enter the starting hight of the hailstones: "))
    while hailHeight > (1):
          hailWork = (hailHeight / 2)
          print("Hail is currently at height" , (hailWork))
    if hailHeight == 1:
        print("Hail stopped at height 1")
main()
