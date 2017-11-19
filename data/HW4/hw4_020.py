def main():
    height = int(input("In put a whole number: "))
    print(height)
    while height != 1:
        if (height%2 == 0):
            height = height/2
        elif (height%2 == 1):
            height = height *3 + 1
        else:
            print("There is a horrible error")
        print(height)
    print("The hail has stopped.")
main()
