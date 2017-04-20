
def main():


           Num = int(input("Please enter the starting height of the hailstone: "))
           print("Hail is currently at height", Num)
           while Num> 0 and Num != 1:
               if Num %2 == 0 :
                 Num -= Num/2
                 print("Hail is currently at height", Num)
               elif Num %2 == 1:
                 Num= (Num*3)+1
                 print("Hail is currently at height", Num)
           print("Hail is stopped at height", Num)





main()
