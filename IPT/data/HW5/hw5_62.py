def main():
    width = int(input("Enter width"))
    height = int(input("Enter height"))
    symbol = input("Enter symbol")
    fill = input("Enter fill")
    for i in range(height-1):
       for e in range(width-1):
           if i ==0:
               print(symbol)
           elif i == height-1:
               print(symbol)
           else:
               if e == 0:
                   print(symbol)
               elif e== width-1:
                   print(symbol)
               else:
                   print(fill)
main()
