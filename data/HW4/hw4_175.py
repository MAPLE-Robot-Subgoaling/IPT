def main():
    height = int(input("Please enter the starting height of the hailstone:"))
    while height > 1:
       if height % 2 == 0:
           height = height / 2
           print("Hail is currently at the height ",height)
       elif height % 2 == 1:
           height = (height * 3) + 1
           print("Hail is current at the height ",height)
    if height == 1:
        print("Hail stopped at height 1")    
main()
