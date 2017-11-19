def main()
temp = float(input("Please enter a temprature"))
sign = str(input("please enter a degree"))
if sign == "C":
    if temp > 100:
        print("water is boiling")
    elif temp < 0:
        print("water is frozen")
    else:
        print("water is a liquid")
else:
    if temp >373.16:
        print("water is boiling")
    elif temp < 273.16:
        print("water is freezing")
    else:
        print("Water is liquid")
main()
