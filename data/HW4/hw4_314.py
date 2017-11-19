def main():
    startInt=int(input("Please enter the starting height of the hailstone: "))
    endCondition = False
    updatedInt=startInt
    print("Hail is currently at height", updatedInt)
    while endCondition == False:
        if updatedInt == 1:
            print("Hail stoppped at height 1")
            endCondition = True
        elif updatedInt%2 == 0:
            updatedInt =int(updatedInt / 2)
            print("Hail is currently at height", updatedInt)
        elif updatedInt%2 == 1:
            updatedInt = int((updatedInt*3) + 1)
            print("Hail is currently at height", updatedInt)
main()
