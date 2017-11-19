def main():
    h = int(input("Please enter the starting height of the hailstone: "))
    print("Hail is currently at height ", h)
    while h != 1:
        if h % 2 == 0:
            h = h // 2
        elif h % 2 == 1:
            h = (h*3) + 1
        if h != 1:
            print("Hail is currently at height ", h)
    print("Hail stopped at height ", h)
main()
