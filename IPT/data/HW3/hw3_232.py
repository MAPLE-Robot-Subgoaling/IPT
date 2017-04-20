
def main():
    temp = float(input("Please enter the temperature: "))
    userChoice = raw_input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if userChoice == "C":
        if(temp <= 0):
            print("At this temperature, water is a solid.")
        elif(temp >=100):
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")
    elif userChoice == "K":
        if(temp <= 273.15):
            print("At this temperature, water is a solid.")
        elif(temp >= 373.15):
            print("At this temperature, water is a gas.")
        else:
            print("At this temperature, water is a liquid.")
    else:
        print("Invalid input somewhere.")
main()
