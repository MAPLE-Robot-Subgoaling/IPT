def main():
    temperature = float(input("What is the temperature: "))
    print("Please enter C for Celsius or K for Kelvin")
    choice = input("Celsius or Kelvin: ")
    if(choice == "K"):
        tempc = (temperature - 273.15)
        if (tempc < 0):
            print("Water is solid at this temperature.")
        elif ((tempc > 0)and(tempc < 100)):
            print("Water is a liquid at this temperature.")
        elif (tempc > 100):
            print("Water is a gas at this temperature.")
    if(choice == "C"):
        if (temperature < 0):
            print("Water is solid at this temperature.")
        elif ((temperature > 0)and(temperature < 100)):
            print("Water is a liquid at this temperature.")
        elif (temperature > 100):
            print("Water is a gas at this temperature.")

main()
