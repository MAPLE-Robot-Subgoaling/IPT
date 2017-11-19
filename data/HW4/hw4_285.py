def main():
     startingHight = int(input('PLease enter the starting hight at the hailstone: '))
     if startingHight == 1: 
                         sys. exit()    
     while startingHight > 1 : 
                        if  startingHight % 2 == 0:
                            startingHight = startingHight/2 
                            print('Hail is currently at hight', startingHight)
                        else: 
                            startingHight = (startingHight * 3) + 1 
                            print('Hail is currently at hight', startingHight)
main()
