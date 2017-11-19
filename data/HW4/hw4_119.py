def main():
 height = int(input("What is the hailstorms current height?"))
 print("The current height is:", height)
 while height != 1:
  if (height % 2) == 0:
   print("The current height is:", height//2)
   height = height//2
  else:
   print("The current height is:", (height*3)+1)
   height = (height*3)+1
 print("Hail stopped at height 1")
main()
