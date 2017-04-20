
def main():
    positiveNum = int(input("Hail is currently at height: "))
    if positiveNum < 0:
        print("Error: Number must be positive")
        positiveNum = int(input("Hail is currently at height: "))
        while(positiveNum != 1):
            if positiveNum % 2 == 0:
                positiveNum = positiveNum/2
                print("Hail is currently at height: ", positiveNum)
            else:
                positiveNum = (positiveNum * 3) + 1
                print("Hail is current at height: ", positiveNum)
        print("Hail stopped at height: ", positiveNum)
    else:
        while(positiveNum != 1):
            if positiveNum % 2 == 0:
                positiveNum = positiveNum/2
                print("Hail is currently at height: " , positiveNum)
            else:
                positiveNum = (positiveNum * 3) + 1
                print("Hail is currently at height: " ,positiveNum)
        print("Hail stopped at height: " , positiveNum)
main()
