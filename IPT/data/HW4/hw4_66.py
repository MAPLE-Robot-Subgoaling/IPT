


def main():
    print("please enter height of hailstone?")
    num = int(input())
    while (num != 1):
        if (num < 0):
            num = (num * (-1))
        if (num % 2 == 0):
            num = (num/2)
            print("num = ", int(num))
        else:
            num = ((num * 3) + 1)
            print("num = ", int(num))


            

    







main()









