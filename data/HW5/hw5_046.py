def main():
    width = int(input('What is the width of the box: '))
    height = int(input("What is the height of the box: "))
    outlined = input('What symbol will the box be outlined in: ')
    filled = input('What symbol will the box be filled with: ')
    print (outlined * width)
    for i in range(height - 2):
        print(outlined + filled * (width - 2) + outlined)
    if height > 1:
        print (outlined * width)
main()
