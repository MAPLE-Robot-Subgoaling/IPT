
boiling_point_Kelvin = 373
boiling_point_Celsius = 100
freezing_point_Kelvin = 273
freezing_point_Celsius = 0
states = [ "At this temperature, water is a (frozen) solid." , "At this temperature, water is a liquid." , "At this temperature, water is a gas." ]

def main():
    degree = float(input("Please enter the temperature: "))
    scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")

    if( scale == "K" ):
        if( degree > boiling_point_Kelvin ):
            print( states[2] )
        elif( degree < freezing_point_Kelvin):
            print( states[0] )
        else:
            print( states[1] )

    elif( scale == "C"):
        if( degree > boiling_point_Celsius ):
            print( states[2] )
        elif( degree < freezing_point_Celsius ):
            print( states[0] )
        else:
            print( states[1] )

main()
