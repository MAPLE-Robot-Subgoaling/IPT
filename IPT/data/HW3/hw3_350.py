
def main():
    temp = input("Enter the temperature: ")
    scale = input("Enter 'C' for Celsius or 'K' for Kelvin: ")
    if (temp > "100") and (scale == "C"):
       print("Water is a gas at this temperature")
    elif (temp > "373.2") and (scale == "K"):
        print("Water is a gas at this temperature")
    elif (temp <= "0") and (scale == "C"):
        print("Water is a soild at this temperature")
    elif (temp <= "273.2") and (scale == "K"):
        print ("Water is a soild at this temperatre")
    elif (temp <= "100") and (scale == "C"):
        print("Water is a liquid at this temperature")
    elif (temp <= "373.2") and (scale == "K"):
        print("Water is a liqid at this temperature")
main()
