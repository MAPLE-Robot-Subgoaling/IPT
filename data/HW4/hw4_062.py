def main():
    hailStormNum = int(input("Please insert a positive integer, which is the starting height of the hailstorm: "))
    while hailStormNum != 1:
        if hailStormNum % 2 == 0:
            hailStormNum = hailStormNum / 2
            hailStormNum = int(hailStormNum)
            print (hailStormNum)
        else:
            hailStormNum = hailStormNum * 3 + 1
            hailStormNum = int(hailStormNum)
            print (hailStormNum)
    print ("This is the final height of the hailstorm.")
main()
