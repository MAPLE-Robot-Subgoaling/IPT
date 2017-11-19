def main():
   width = int(input("Please enter the width for the box:"))
   height = int(input("Please enter a height for the box:"))
   symbol_outline = input("Please enter a symbol for the box outline:")
   symbol_fill = input("Please enter a symbol for the box fill:")
   widthList = list(range(0, width + 1))
   heightList = list(range(0, height))
   for n in heightList:
      if n == 0 or n == height-1:
         print(symbol_outline*width)
      else:
         print(symbol_outline + (symbol_fill*(width-2)) + symbol_outline)
main()
