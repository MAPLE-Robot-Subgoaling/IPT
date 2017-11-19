def main():
    def waterState():
        print('This program will tell you the molecular phase of water ')
        print(' ')
        print('at a given temperature in Celsius or Kelvin. ')
        print(' ')
        givenTemp = float(input('Please enter a temperature: '))
        print(' ')
        print('Is your temperature measured in Celsius or Kelvin? ')
        print(' ')
        isCelsius = input('Please enter C for Celsius or K for Kelvin: ')
        print(' ')
        if isCelsius == 'C':
            isCelsius = True
        else:
            isCelsius = False
        if (isCelsius == True and givenTemp <= 0.0) or (isCelsius == False and givenTemp <= 273.15):
            print('Water is solid at the given temperature. Your water is frozen.')
        elif (isCelsius == True and givenTemp > 0.0 and givenTemp < 100.0) or (isCelsius == False and givenTemp > 273.15 and givenTemp < 373.15):
            print('Water is liquid at the given temperature. Your water can form to any shape. ')
        elif (isCelsius == True and givenTemp >= 100.0) or (isCelsius == False and givenTemp >= 373.15):
            print('Water is gaseous at the given temperature. Your water has no shape.')
    waterState()
    print(' ')
    input('Enter any key to exit: ')
main()
