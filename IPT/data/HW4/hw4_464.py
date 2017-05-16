
def main():

    startingHeight = int(input("Please enter the starting height of the hailstone: "))
    SENTINEL = 1
   
    while startingHeight%2==0 and startingHeight!=SENTINEL:
        startingHeight = startingHeight/2
        print(startingHeight)
       
        while startingHeight%2!=0 and startingHeight!=SENTINEL:
            startingHeight = (startingHeight*3)+1
            print(startingHeight)
          
    while startingHeight%2!=0 and startingHeight!=SENTINEL:
        startingHeight = (startingHeight*3)+1
        print(startingHeight)

        while startingHeight%2==0 and startingHeight!=SENTINEL:
            startingHeight = startingHeight/2
            print(startingHeight)

    if startingHeight==SENTINEL:
        print("Hail stopped at height 1.")

main()
