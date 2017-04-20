def main():
    Hailstorm=int(input("Please enter the starting height of the hailstone?"))
    Height=0
    invalid=True
    HailstormHeight=[]
    while invalid:
        if Hailstorm%2==1 and Hailstorm>1:
            print("Hail is currently at height", Hailstorm)
            Height=int((Hailstorm*3)+1)
            HailstormHeight.append(Height)
            Hailstorm=Height
            
        elif Hailstorm%2==0 and Hailstorm>1:
            print("Hail is currently at height", Hailstorm)           
            Height=int((Hailstorm/2))
            HailstormHeight.append(Height)
            Hailstorm=Height
            
        else:
            invalid=False 
    print("Hail stopped at 1")
                
              

main()
