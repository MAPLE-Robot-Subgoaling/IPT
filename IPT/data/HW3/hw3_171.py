
K_CONSTANT = 273.15

def main():
    print("This program will print out the state of water at a given temperature.")
    temp = float(input("Please enter the temperature: "))
    scale = str(input("Please enter 'C' for Celsius, or 'K' for Kelvin': "))
    if scale == 'K':
        temp = temp - K_CONSTANT
    if temp > 0 and temp < 100:
        print("The current state is liquid")
    if temp >= 100:
        print("The current state is gas")
    if temp <= 0:
        print("The current state is solid")
    

main()
