def main():
    location = int(input("Please enter the starting height of the hailstone:",))
    while location > 1:
        if(location == 1):
            print("")
        elif location % 2 == 0:
            location = (location // 2)
            print("Hail is currently at location",location)
        elif location % 2 != 0:
            location = (location * 3) + 1
            print("Hail is currently at location",location)
    print("Hail stopped at height",location)
main()
