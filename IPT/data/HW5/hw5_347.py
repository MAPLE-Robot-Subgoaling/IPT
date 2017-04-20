def main():
    width = int(input("Please enter a width: "))
    height = int(input("Please enter a height: "))
    symbol1 = input("Please enter a symbol: ")
    symbol2 = input("Please enter a different symbol: ")
    length = 0
    print(symbol1*width)
    for n in range(height - 2):
        print(symbol1+(symbol2*(width - 2))+symbol1)
    if height > 1:
        print(symbol1*width)

main()
