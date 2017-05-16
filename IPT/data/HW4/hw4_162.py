import time # only using this for fun, I hope it doesn't cause any trouble

def main():
    height = int(input("Enter the starting height of the particle: "))
    while(height == 0):
        print("The particle already hit the ground, so there is nothting to simulate. Retry.")
        height = int(input("Enter the starting height of the particle: "))

    print("Simulating...")
    time.sleep(2)
    while(height != 1):
        if(height % 2 == 0):
            height = int(height / 2)
        else:
            height = int(height * 3 + 1)
            
        if(height != 1):
            print("The height of the particle is " + str(height))
        time.sleep(0.01)

    print("\nThe hailstone has hit the ground.")

main()
    
        
