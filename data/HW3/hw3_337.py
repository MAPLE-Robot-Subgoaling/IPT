def main():
    temperature = float(input('Please enter the temperature: '))
    scale = input('Please enter C for Celsius, or K for Kelvin: ')
    if (temperature <= 0) and (scale == 'C'):
        print ('At this tmeperature, water is a (frozen) solid.')
    elif (temperature >= 100) and (scale == 'C'):
        print ('At this temperature, water is a gas.')
    elif (0<temperature<100) and (scale== 'C'):
        print ('At this temperature, water is a liquid.')    
    elif (temperature <= 273) and (scale == 'K'):
        print ('At this temperature, water is a (frozen) solid.')
    elif (temperature >=373) and (scale == 'K'):
        print ('At this temperature, water is a gas.')
    elif (273<temperature<373) and (scale == 'K'):
        print ('At this temperature, water is a liquid.')
main()
