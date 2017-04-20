
def main():
    width = int(input("What is the width of the box? "))
    height = int(input("What is the height of the box? "))
    border = input("What is the outside of the box made of? ")
    fill = input("What is the inside of the box made of? ")
    for h in range(height):
        if h == 0 or h == height - 1:
            print(border*width)
        else:
            print(border + fill*(width-2) + border)

main()
