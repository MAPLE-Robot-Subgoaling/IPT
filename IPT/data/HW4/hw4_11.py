
def main():
    startingHeight = (int)(input("What is the starting height of the hailstone? "))
    currentHeight = startingHeight
    trackingHail = True
    while(trackingHail):
         if(currentHeight == 1):
             print("Hail stopped at height", currentHeight)
             trackingHail = False
         else:
             print("Hail is currently at height", currentHeight)
             if(currentHeight % 2 == 0):
                 currentHeight = (int)(currentHeight / 2)
             else: #currentHeight is odd
                 currentHeight = (currentHeight * 3) + 1

main()
