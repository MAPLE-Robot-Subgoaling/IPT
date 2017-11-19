def main():
    startHeight = int(input("Please enter a positive integer: "))
    print("Hail is currently at height",startHeight)
    newHeight = startHeight
    while newHeight > 1:
        if newHeight % 2 == 0 or newHeight == 2:
            newHeight = int(newHeight / 2)
        else:
            newHeight = int((newHeight * 3) + 1)
        print("Hail is currently at height",newHeight)
main()
