def main():
    waterTemp = "" 
    celsiusOrKelvin = "" 
    celsiusCheck = "C" 
    celsiusToKelvin = 273 
    trueKelvinTemp = "" 
    FUSION_STATE = 273 
    VAPORIZATION_STATE = 373 
    print("Hell, this program will help declare what state of water is at a given temperature.")
    waterTemp = float(input("Please enter a temperature: "))
    celsiusOrKelvin = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if celsiusOrKelvin == celsiusCheck: 
        trueKelvinTemp = waterTemp + celsiusToKelvin 
    else:
        trueKelvinTemp = waterTemp 
    if trueKelvinTemp <= FUSION_STATE:
        print(" At ",waterTemp,", water is a solid")
    else:
        if trueKelvinTemp > FUSION_STATE and trueKelvinTemp < VAPORIZATION_STATE:
            print(" At ",waterTemp,", water is a liquid")
        else:
            if trueKelvinTemp >= VAPORIZATION_STATE:
                print(" At ",waterTemp,", water is a gas")
main()
