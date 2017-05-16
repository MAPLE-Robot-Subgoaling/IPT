
def main():
    height=0
    SENTINEL=1
    height =int(input("Enter starting height of hailstone, or '1' to stop:"))

    while(height!=1):
        if(height%2==0):
            height=height/2
            print("Hail is currently at height",height)
        elif(height%2!=0):
            height=(height*3)+1
            print("Hail is currently at height",height)        
    print("Hail is stopped at 1")
    
            
main()
