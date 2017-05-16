
def main():

    inHeight = int(input("Please enter the starting height of the hailstone: "))
    print("The hailstone is currently at height" ,inHeight)

    count = 0
    print(inHeight)
    while inHeight != 1:
        if (inHeight % 2 == 0):
            take = inHeight // 2
            print("Hail is currently at height" ,take)
            inHeight = take
            count = count + 1
        else:
            take = (inHeight * 3) + 1
            print("Hail is currently at height" ,take)
            inHeight = take
            count = count + 1

main()
