def main():
    temp = float(input("Please enter the Temperature: "))
    ck = (input("Please enter 'C' for Celsius, or 'K' for Kelvin: "))
    ck.upper()
    if temp <= 0 and ck == 'C':
        print("At this temperature your water is frozen! Burrr!... ")
    elif 100 > temp > 0 and ck == 'C': 
        print("Your water is still water... not boiling or frozen. ")
    elif temp >= 100:
        print("Your water is boiling!")
    elif temp <= 273 and ck == 'K':
        print("At this temperature your water is frozen! Burrr!... ")
    elif 373 > temp > 273 and ck == 'K':
        print("Your water is still water... not boiling or frozen. ")
    elif temp > 373 and ck == 'K':
        print("Your water is boiling!")
    else: 
        print("Sorry, invalid....")
main()
