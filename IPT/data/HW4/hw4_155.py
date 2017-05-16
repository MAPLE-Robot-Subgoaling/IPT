
def main():
    MINLENGTH = 1
    currentHeight =int(input("Please enter the starting height of the hailstone: "))
    print(currentHeight)
    while currentHeight > MINLENGTH:
        if currentHeight % 2 == 0:
           currentHeight /= 2
           print(currentHeight)
        else:
           currentHeight = (currentHeight * 3) + 1
           print(currentHeight)
main()
