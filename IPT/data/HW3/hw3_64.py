
def main():

    temperature = input("Please enter a temperature: ")

    unit = str(input("Please enter 'C' for Celsius, or 'K' for Kelvin: "))

    if(temperature <= "0" and unit == "C"):
        
        print("At this temperature, water is a (frozen) solid")

    elif(temperature > "0" and temperature < "100" and unit == "C"):
        
        print("At this temperature, water is a liquid")

    elif(temperature >= "100" and unit == 'C'):

        print("At this temperature, water is a gas")



    elif(temperature <= "273.15" and unit == "K"):

        print("At this temperature, water is a (frozen) solid")

    elif(temperature > "273.15" and temperature < "373.15" and unit == "K"):

        print("At this temperature, water is a liquid")
        
    elif(temperature >= "373.15" and unit == "K"):

        print("At this temperature, water is a gas")


main()


