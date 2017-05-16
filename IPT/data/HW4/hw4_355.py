

def main():
   heightOfHailstone = int(input("Please enter the starting height of the hailstone:",))
   if heightOfHailstone >0:
      while heightOfHailstone != 1:  # Check while loop condition
         print("Hail is currently at height", int(heightOfHailstone ))
         if heightOfHailstone  % 2!=0 :   # Check for odd Numbers
            heightOfHailstone  = 3*heightOfHailstone  + 1
                  
         else:                                # Formula for even numbers
      
            heightOfHailstone  =heightOfHailstone  / 2
      print("Hail stopped at",int(heightOfHailstone)  )

   else :
      print("Your entering data is wrong. Please check again.")
main()


