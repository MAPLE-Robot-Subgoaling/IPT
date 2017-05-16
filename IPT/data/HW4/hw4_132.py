
def main() :
  currentHeight = int(input('Please enter the starting height of the hailstone: '))
  while (currentHeight != 1) :
    if (currentHeight % 2 == 0) :
      print('Hail is currently at height', int(currentHeight))
      currentHeight = int(currentHeight / 2)
    elif (currentHeight % 2 == 1) :
      print('Hail is currently at height', int(currentHeight))
      currentHeight = int((currentHeight * 3) + 1)
  else :
    if (currentHeight == 1) :
      print('Hail stopped at height 1')

main()

