
def main():

   hailHeight= int(input("What is the current height of the hailstone? "))
  
   while hailHeight!= 1:
       print("The current height of the hailstone is",hailHeight)
      
       if hailHeight % 2 == 0:
         hailHeight= hailHeight/2

       elif hailHeight % 2 == 1:
         hailHeight=( hailHeight * 3) + 1 

   print("The current height of the hailstone is ",hailHeight)

main()
