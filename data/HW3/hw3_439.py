def main():
    temp =float(input("please enter the temperature"))
    symbol = input ("please enter 'c' for celsius, or 'k' for kelvin")
    if (symbol =="c"):
        if temp <= 0:
            print("at this temperature water is a solid")
        elif temp >0 and temp <100:
            print("at this temperature water is a liquid")
        else:
            print("at this temperature water is a gas")
    elif symbol =="k":
        if temp <= 273:
            print("at this temperature water is a solid")
        elif temp >273 and temp <373:
            print("at this temperature water is a liquid")
        else:
            print("at this temperature water is a gas")
main ()
