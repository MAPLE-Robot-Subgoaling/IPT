
def main():
  width = int(input("Please enter the desired width of the box: "))
  height = int(input("Please enter the desired height of the box: "))
  border = input("Please enter a symbol to border the box: ")
  fill = input("Please enter a symbol to fill the box: ")
  inBorder = width - 2
  for h in range(height):
    if h != 0 and h != (height - 1):
      print(border + (fill * inBorder) + border)
    else:
      print(border * width)
      
          

main()
