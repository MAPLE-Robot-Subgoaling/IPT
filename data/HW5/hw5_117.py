def main():
    width = int(input("Please enter the width of the box: "))
    height = int(input("Please enter the height of the box: "))
    outbox = input("Please enter a symbol for the box outline: ")
    fillbox = input("Please enter a symbol for the box fill: ")
    topbotbox = width * outbox
    midbox = outbox + ((width - 2) * fillbox) + outbox
    print(topbotbox)
    for i in range(0, (height-2) , 1):
        print(midbox)
    print(topbotbox)
main()
