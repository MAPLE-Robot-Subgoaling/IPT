def main():
    start = int(input("Please enter the starting hieght of the hailstone: "))
    while start != 1:
        if start % 2 == 0:
            start = start / 2
            print("hail is currently at ",start)
        elif start % 2 == 1:
            start = start * 3 + 1
            print("hail is currently at",start)
    print("the hailstone has stopped at hieght 1")
main()
