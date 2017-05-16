
def main():
    temperature = float(input("What is the temperature?"))
    tempScale = input("Enter C for Celsius or K for kelvin")
    
    if tempScale == "C":
        if temperature <= 0:
            print("Water will be a solid at this temperature")

        elif temperature >= 100:
            print("Water will be a gas at this temperature")
    
        else:
            print("Water will be a liquid at this temperature")
    
    else:
        if temperature <= 273.15:
            print("Water will be a solid at this temperature")
    
        elif temperature >= 373.15: 
            print("Water will be a gas at this temperature")
    
        else: 
            print("Water will be a liquid at this temperature")
    
main()
