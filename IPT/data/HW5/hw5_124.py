def main():
  width = int(input("Please enter the width of the box: "))
  height = int(input("Please enter the height of the box: "))
  outLine = input("Please enter a symbol for the box outline: ")
  fill = input("Please enter a symbol for the box fill: ")
  box= ""
  for y in range (0, height):
     for x in range(0, width):
      if((x==0 or x==width-1) or (y==0 or y==height-1)):
       box = box+outLine
       if x==width-1 :
         box=box+"\n"
      else:
       box = box+fill
  print(box)
  
main()
