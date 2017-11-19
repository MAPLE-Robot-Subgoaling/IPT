def main():
    height  = (int)(input("let me get a positive int"))
    while height != 1:
        print(height)
        if height % 2 == 0:
            height = height // 2 
        elif height % 2 == 1:
            height = height * 3 + 1
    print(height)
    print("it has stopped")
main()
