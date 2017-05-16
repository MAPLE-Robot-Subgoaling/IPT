
def main():

    height = int(input('What is the starting height of the hailstorm?  '))
    while height > 2: 
          if (height % 2) == 0:
             height = height/2
             print('Hail is currently at height', height)
          elif (height % 2) == 1:
             height =(height*3) + 1
             print('Hail is currently at height', height)
    
    print('Hail has stopped at height 1')
main()
