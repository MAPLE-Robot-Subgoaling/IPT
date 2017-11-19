def main():
    for listNum in range(101, 0, -1):
        if listNum % 5 == 0 and listNum % 6 == 0:
            print("Thirty days hath September")
        elif listNum % 6 == 0:
            print("I'll believe six impossible things before breafast")
        elif listNum % 5 == 0:
            print("Where do you see yourself in five years")
        else:
            print(listNum)
main()
