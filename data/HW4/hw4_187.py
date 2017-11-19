def main():
    sth = int(input("Please enter the starting height of the hailstone: "))
    while sth != 1:
        if (sth % 2 == 0):
            sth = int(sth / 2)
            if (sth != 1):
                print("the stone is currently at height",sth)
        elif (sth % 2 == 1):
            sth = int(sth * 3 + 1)
            if (sth != 1):
                print("the stone is currently at height",sth)
    print("hail stopped at height 1")
main()
