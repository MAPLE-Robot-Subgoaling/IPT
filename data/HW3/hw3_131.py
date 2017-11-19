def main():
    temperature = float(input('Please enter the temperature. '))
    scale =  input('Please enter "'"C"'" for Celcius and "'"K"'" for Kelvin. ')
    if scale == 'C':
        if temperature >= 100:
            print('At this temperature, water is a gas.')
        elif temperature >0:
            print('At this temperature, water is a liquid.')
        else:
            print('At this temperature, water is a solid.')
    elif scale == 'K':
        if temperature >= 373:
            print('At this temperature, water is a gas.')
        elif temperature > 273:
            print('At this temperature, water is a liquid.')
        else:
            print('At this temperature, water is a solid.')
    else:
        print('Please use either K or C.')
main()
