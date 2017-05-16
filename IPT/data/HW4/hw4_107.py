

def main():

    height = int(input("Please enter the starting height of the hailstone: "))
    print("Hail is currently at height",height)

    while height >= 3:
        if height % 2 == 0:
            height=int(height/2)
            print("Hail is currently at height", height)
        elif height%2 != 0:
            height=int((height * 3) + 1)
            print("Hail is currently at height", height)
    print("Height is stopped at height 1")
main()
































    























































