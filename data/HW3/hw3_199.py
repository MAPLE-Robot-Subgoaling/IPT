def main():
    CFZ = 0
    CBL = 100
    KFZ = 273.15
    KBL = 373.15
    temp = float(input("Please enter the temperature"))
    ck = input("Please enter 'c' for celcius or 'k' for kelvin")
    if ( ck == "c" ):
        if ( temp <= CFZ ):
            print("at this temperature, water is frozen")
        elif ( temp > CFZ and temp <= CBL ):
            print("at this temperature, water is liquid")
        elif ( temp > CBL ):
            print("at thsi temperature, water is a gas")
    elif ( ck == "k" ):
        if ( temp <= KFZ ):
            print("at this temperature, water is frozen")
        elif ( temp > KFZ and temp <= KBL ):
            print("at this temperature, water is liquid")
        elif ( temp > KBL ):
            print ("at this temperature, water is a gas")
main()
