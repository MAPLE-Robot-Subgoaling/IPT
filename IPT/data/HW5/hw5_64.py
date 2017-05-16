
def main():

    length = int(input("Please enter a positive integer below 12(length): "))                       #lenth of box and keeping the number small to make the output easier to read
    height = int(input("Please enter a positive integer below 12(height): ")) #width of box
    outer_symbol = input("Enter a letter to be the border of the box: ")
    inner_symbol = input("Enter a letter to fill the box: ")

    for i in range(height):
        print(i)



main()
