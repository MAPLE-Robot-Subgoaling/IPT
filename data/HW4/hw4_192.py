def main():
    height = int(input("Please enter the height of the hail: "))
    while height != 1:
        if height % 2 == 0:
            height = height / 2
            print("The height is", height)
        else:
            height = (height * 3) + 1
            print("The height is", height)
    print("The height is 1 and the heilstorm has subsided.")
main()
