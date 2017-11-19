def main():
    num = int(input("Input a positive integer: "))
    print(num)
    while num != 1:
        if num % 2 == 0:
            num = num/2
            print(int(num))
        else:
            num = 3*num + 1
            print(int(num))
main()
