def main():
    arrayWidth = int(input("What is the width of the box: "))
    arrayHeight = int(input("What is the height of the array: "))
    arrayOutside = str(input("What is the bodrer of the array: "))
    arrayInside = str(input("What is the interal part of the array: "))
    n = 0
    for n in range(0, arrayHeight):
        if (n == 0 or n == arrayHeight - 1 ):
            print(arrayOutside * arrayHeight)
        else:
            print(arrayOutside + (arrayInside * (arrayWidth - 2) ) + arrayOutside)
main()
