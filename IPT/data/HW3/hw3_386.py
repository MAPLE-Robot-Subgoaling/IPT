
def main():
    waterTemp = "" #Temp user inputs
    celsiusOrKelvin = "" #The temperature unit the user inputs
    celsiusCheck = "C" #checks to see if program needs to convert celsius to kelvin
    celsiusToKelvin = 273 #converts celsius temperate to kelvin
    trueKelvinTemp = "" #Final Temperature of all in Kelvin
    FUSION_STATE = 273 #Kelvin temp at which water changes states between solid and liquid
    VAPORIZATION_STATE = 373 #Kelvin temp at which water changes from liquid to gas
    
    print("Hell, this program will help declare what state of water is at a given temperature.")
    waterTemp = float(input("Please enter a temperature: "))
    celsiusOrKelvin = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    
    if celsiusOrKelvin == celsiusCheck: #checks to see if temp was in celius
        trueKelvinTemp = waterTemp + celsiusToKelvin #converst celsius temp to Kelvin
    else:
        trueKelvinTemp = waterTemp #stays the same if Kelvin was input temp

    if trueKelvinTemp <= FUSION_STATE:
        print(" At ",waterTemp,", water is a solid")
    else:
        if trueKelvinTemp > FUSION_STATE and trueKelvinTemp < VAPORIZATION_STATE:
            print(" At ",waterTemp,", water is a liquid")
        else:
            if trueKelvinTemp >= VAPORIZATION_STATE:
                print(" At ",waterTemp,", water is a gas")
main()
    
