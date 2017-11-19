def main():
    index = 0
    widthPrompt = int(input("What is the width of the box? "))
    heightPrompt = int(input("What is the height of the box? "))
    outsideSymbol = str(input("What character is the outside of the box made of? "))
    insideSymbol = str(input("What character is the inside of the box made of? "))
    print(outsideSymbol * widthPrompt)
    if heightPrompt > 2:
        for index in list(range(heightPrompt - 2)):
            print(outsideSymbol + insideSymbol * (widthPrompt - 2) + outsideSymbol)
    if heightPrompt != 1:
        print(outsideSymbol * widthPrompt)
main()
