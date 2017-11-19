def main():
    hail = int(input("Starting height of a hailstone "))
    while (hail != 1):
        if (hail % 2 == 0):
            hail = hail // 2
        else:
            hail = (hail * 3) +1
        print("Hail is currently at ",hail)
    print("hail is done")
main()
