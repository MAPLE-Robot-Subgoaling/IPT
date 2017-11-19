def main():
    num = int(input("Enter a positive integer: "))
    while (num > 1):
        print("Hail is currently at height " + str(num) )
        if( num % 2 == 0):
            num = num // 2
        else:
            num = (num * 3) + 1
main()
