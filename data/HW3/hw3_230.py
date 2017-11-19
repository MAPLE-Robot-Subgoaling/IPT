def main():
    temperature = int(input("Please enter the temperature: "))
    tempScale = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if (tempScale == "C"):
        if (temperature >= 100):
            print("At this temperature, water is a gas")
        if (temperature < 100 and temperature > 0):
            print("At this temperature, water is a liquid")
        if (temperature <= 0):
            print("At this temperature, water is a solid")
    if (tempScale == "K"):
        if (temperature >= 373):
            print("At this temperature, water is a gas")
        if (temperature < 373 and temperature > 273):
            print("At this temperature, water is a liquid")
        if (temperature <= 273):
            print("At this temperature, water is a solid")
main()
