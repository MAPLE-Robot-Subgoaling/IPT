
def main():
    
    temp = float(input("What temperature would you like to test:"))
    tempMode = input("Is this temperature in Kelvin or Celcius? Enter K or C:")

    if temp <= 0 and tempMode == "C" or temp <= 273 and tempMode == "K":
        print("At", str(temp) + tempMode, "water would be freezing.")
    if 0 < temp < 100 and tempMode =="C" or 273 < temp < 373 and tempMode == "K":
        print("At", str(temp) + tempMode, "water would be liquid.")
    if temp >= 100 and tempMode == "C" or temp >= 373 and tempMode == "K":
        print("At", str(temp) + tempMode, "water would be boiling.")

main()
