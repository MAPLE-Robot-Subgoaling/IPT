def main():
    temperature = float(input('What is the termperature?: '))
    scale = input("Enter 'C' for Celsius and 'K' for Kelvin: ")
    if scale == 'C':
        if temperature <= 0:
            print('At this temperature, water is a solid')
        elif temperature > 0 and temperature < 100:
            print('At this temperature, water is a liquid')
        else:
            print(' At this temperature, water is a gas')
    elif temperature <= 273.16:
        print('At this temperature, water is a solid')
    elif temperature > 273.16 and temperature < 373.16:
        print('At this temperature, water is a liquid')
    else:
        print(' At this temperature, water is a gas')


main()
