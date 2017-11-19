def main():
    w=int(input("Please enter the width of the rectangle: "))
    h=int(input("Please enter the height of the box: "))
    s=input("Please enter a symbol for the box outline: ")
    fs=input("Please enter a symbol for the box fill: ")
    print(s * w)
    for i in range(0, (h - 2)):
        print(s + fs * (w - 2) + s)
    if h > 1:
        print(s * w)
main()
