
def main():

    numOne = int(input("Pick a positive integer."))
    while numOne !=1:
        print(numOne)
        if (numOne%2)== 0:
            numOne =  (numOne/2)
            print (numOne)
        elif (numOne%2)== 1:
            numOne = (numOne*3)+1
            print (numOne)
            
       
main()
