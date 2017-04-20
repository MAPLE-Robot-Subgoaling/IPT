

def main():
   w = int(input("Please enter the width of the box: "))
   h = int(input("Please enter the height of the box: "))
   outside = input("Please enter a symbol for the box outline: ")
   inside = input("Please enter a symbol for the box fill: ")

   for in range(w):
      for j in range(h):
         print(outside * if in [0, h-1] or j in [0, w-1] else inside, end = '')
      print()

main()
