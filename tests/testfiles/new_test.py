def main():
    mpC = 0
    bpC = 100
    mpK = 273
    bpK = 373
    cel = 'C'
    kel = 'K'
    tempVar = float(input('Please enter the temperature: '))
    unitVar = input("Please enter 'C' for Celsius or 'K' for Kelvin: ")
    if unitVar == cel:
        if tempVar <= mpC:
            print('At this temperature, water is a frozen solid.')
        elif tempVar >= bpC:
            print('At this temperature, water is a gas.')
        else:
            print('At this temperature water is a liquid.')
    elif tempVar <= mpK:
        print('At this temperature, water is a frozen solid.')
    elif tempVar >= bpK:
        print('At this temperature, water is a gas.')
    else:
        print('At this temperature, water is a liquid.')


main()
