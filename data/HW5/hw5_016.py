def main():
    width = int(input("enter width of box "))
    height = int(input("enter height of box "))
    outline = input("enter a symbol for the outline of the box ")
    fill =  input("enter a symbol for the fill of the bod")
    top = outline * width
    print(top)
    for i in range (0, height -2):
         inside = (width -2)*fill
         print(outline, inside, outline)
    if height >= 2:
          print(top)
main()
