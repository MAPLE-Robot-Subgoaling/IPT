
def main():
    
    width = int(input("How many characters wide do you want the box to be? "))
    height = int(input("How many characters tall do you want the box to be? "))
    outline = input("Which character shoud the outline be made of? ")
    fill = input("Which character should the box be filled with? ")
    hList = list(range(0, height - 2))
    print(outline * width)
    for q in hList:
        print(outline + fill * (width - 2) + outline)
    print(outline * width)

main()
