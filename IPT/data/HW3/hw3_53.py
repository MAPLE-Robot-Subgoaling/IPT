


def main() :

    temperature= float(input('Please enter the temperature: '))

    scale= input("Please enter 'C' for Celsius,or 'K' for Kelvin: ")


    if scale == "C":
        
        if temperature > 0 and temperature  < 100 :
            print('At this temperature, water is liquid.')
        
        elif temperature <= 0:          
            print('At this temperature, water is (frozen) solid.')

        else:
            print('At this temperature, water is gas.')



    else:

        if temperature <= 273:
            print('At this temperature, water is (frozen) solid.')

        elif temperature > 273 and temperature  < 373:
            print('At this temperature, water is liquid')
        
        else:
            print('At this temperature, water is gas.')



main()
