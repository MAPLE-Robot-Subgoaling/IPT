def main():
 width =int(input("Enter your desired width:", ))
 height = int(input("Enter your desired height:", ))
 outline = input("Enter your symbol for box outline:", )
 fill = input("Enter your symbol for the box fill:", )
 newwidth = width - 2
 if width == 1 and height == 1:
  print(outline)
 elif width == 1:
  print(width * outline)
  for s in range(height-2):
   print(outline)
  print(width*outline)
 else:
  print(width * outline)
  for s in range(height-2):
   print(outline + fill * newwidth + outline)
  print(width*outline)
main()
