

def main():
    

    number = int(input('Please enter the starting height of a hailstone. '))
    
    while number > 1:
        print('Hail is currently at height:', number)
        mod = number % 2
        if mod == 0:
            number = number // 2

        elif mod != 0:
            number = (number * 3) + 1 

    print('Hail stopped at height:',number)

main()


    
