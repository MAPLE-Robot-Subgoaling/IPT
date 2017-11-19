def main():
    temperature = float(input("Enter the temperature: "))
    units = input("Enter C for celsius or K for kelvin: ").lower()
    if(units == "k"):
        temperature -= 273.15
        if(temperature <= 0):
            print("The water is frozen")
        elif(temperature > 0 and temperature < 100):
            print("The water is a liquid")
        else:
            print("The water is a gas")
main()
