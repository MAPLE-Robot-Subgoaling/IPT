
def main():
    sentinel = True
    height = int(input("What is the starting height of the hailstone? "))
    while sentinel:
        if height == 1:
            sentinel = False
            print("Hail stopped at height 1")
        elif height % 2 == 0:
            print("Hail is currently at height", height)
            height = height // 2
        elif height % 2 == 1:
            print("Hail is currently at height", height)
            height = (height * 3) + 1 



main()
