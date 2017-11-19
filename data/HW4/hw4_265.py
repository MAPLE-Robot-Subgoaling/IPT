def main():
   heightOfHailstone = int(input("Please enter the starting height of the hailstone:",))
   if heightOfHailstone >0:
      while heightOfHailstone != 1:  
         print("Hail is currently at height", int(heightOfHailstone ))
         if heightOfHailstone  % 2!=0 :   
            heightOfHailstone  = 3*heightOfHailstone  + 1
         else:                                
            heightOfHailstone  =heightOfHailstone  / 2
      print("Hail stopped at",int(heightOfHailstone)  )
   else :
      print("Your entering data is wrong. Please check again.")
main()
