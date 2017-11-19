def main():
    temp = int(input("What is the temperature?"))
    scale = input("Please enter C for celsius or K for Kelvin.")
    if (scale == "C" and temp >= 100) or (scale == "K" and temp >= 373):
        print("Your water is a gas.")
    elif (scale == "C" and (temp < 100 and temp > 0)) or (scale =="K" and (temp < 373 and temp > 273)):
        print("Your water is a liquid.")
    else: print("Your water is a solid.")
main()
