
def main():

 num = int(input("Please enter the height of the hailstone: "))
 
 while num != 1:
               
   if num % 2 == 0:
      num = num/2
      print("the height is currently at ", num )
   else: 
      num = (num * 3)+1
      print("the height is currently at ", num)




main()
