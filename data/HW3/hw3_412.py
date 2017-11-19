def main():
    temp = float(input("Please enter a temperature:"))
    temptype =  str(input("Enter 'C' for Celcius or 'K' for Kelvin:"))
    if temptype == "C":
        if temp < 0:
            print("Water is frozen at", temp)
        if temp > 100:
            print("Water is gas at", temp)
        else:
            print("Water is liquid at", temp)
    elif temptype == "K":
        if temp < 273:
            print("Water is frozen at", temp)
        if temp > 373:
            print("Water is gas at", temp)
        else:
            print("Water is liquid at", temp)
main()
