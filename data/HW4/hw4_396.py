def main():
    currentHieght= int(input("enter the current current  hieght of hailstone : "))
    d = currentHieght 
    test = currentHieght % 2
    while True:
        if(d == 1 ):
            print ('that is it cool you got the point ')
            break
        elif(test == 0):
            d = (d/2)
            test = d % 2
            print('the hail is currently at high',  d)
        elif ( test != 0 and currentHieght != 1):
            d = (d*3) + 1
            print ('hail is currently at high', d)
            test = d %2
main()
