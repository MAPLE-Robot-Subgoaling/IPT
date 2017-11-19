def main():
    length = int(input("Please enter a positive integer below 12(length): "))                       
    height = int(input("Please enter a positive integer below 12(height): ")) 
    outer_symbol = input("Enter a letter to be the border of the box: ")
    inner_symbol = input("Enter a letter to fill the box: ")
    for i in range(height):
        print(i)
main()
