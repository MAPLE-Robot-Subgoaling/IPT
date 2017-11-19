def main():
    print("This program only accepts temperature in Celcius and Kelvin.")
    temp = float(input("What is the temperature?"))
    scale = input("What scale is the temperature measured in? Please enter 'C' for Celcius or 'K' for Kelvin")
    if scale == "C":
        if temp > 0:
            if temp < 100:
                print("Water is in its normal liquid state")
            else:
                print("Water is in its gaseous state, and has become steam")
        else:
            print("Water is in its solid state, and has become ice")
    if scale == "K":
        if temp > 273.16:
            if temp < 373.16:
                print("Water is in its normal liquid state")
            else:
                print("Water is in its gaseous state, and has become steam")
        else:
            print("Water is in its solid state, and has become ice")
main()
