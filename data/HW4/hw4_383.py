def main():
    current_Height = int(input("Please enter the starting height of the hailstone: "))
    print("Hail is currently at height",current_Height)
    while current_Height != 1:
        if current_Height%2 == 0:
            current_Height = int(current_Height/2)
            if current_Height == 1:
                print("Hail stopped at height",current_Height)
            else:
                print("Hail is currently at height",current_Height)
        elif current_Height%2 != 0:
            current_Height = (current_Height * 3) + 1
            if current_Height == 1:
                print("Hail stopped at height",current_Height)
            else:
                print("Hail is currently at height",current_Height)
main()
