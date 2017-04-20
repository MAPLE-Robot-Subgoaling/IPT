
def main():

    temp = float(input("What is the temperature? "))

    scale = input("Enter C for Celsius or K for Kelvin: ")

    if scale == "K" and temp <= 273:

        print("The water is frozen solid")
    
    elif scale == "K" and temp >= 273 and temp <=373:

        print("The water is a liquid")

    elif scale == "K" and temp > 373:

        print("The water is a gas")

    if scale == "C" and temp <= 0:

        print("The water is frozen solid")

    elif scale == "C" and temp >= 0 and temp <=100:

        print("The water is a liquid")

    elif scale == "C" and temp > 100:

        print("The water is a gas")

main()
