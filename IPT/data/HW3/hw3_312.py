
def main():
    temp = input("Please enter the temperature: ")
    temp = float(temp)
    scale = input("Please enter 'C' for Celsius, 'F' for Fahrenheit, or 'K' for Kelvin: ")
    if(scale == "K"):
        temp += 273.15
    elif(scale == "F"):
        temp -= 32
        temp *= (5 / 9)
    
    if(temp <= 0):
        print("The water is a frozen solid.")
    elif(temp >= 100):
        print("The water is a gas.")
    else:
        print("The water is a liquid.")

main()
