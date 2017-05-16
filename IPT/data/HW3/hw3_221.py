
def main():
    temp = float(input("Please enter the tempreature"))
    degree = input("Please enter'C' for Celsius or 'K' for Kevin")
    if degree == "C":
        if temp <= 0:
            print("At this tempreature water is (frozen) solid")
        elif temp < 100:
            print("at this tempreature, water is liquid")
        else:
            print("At this tempreature, water is gas")
    elif degree == "K":
        if temp <= 273.16:
            print("At this tempreature , water is frozen")
        elif temp < 373.16:
            print("At this tempreature, water is liquid")
        else:
            print("At this tempreature, water is gas")
    else:
        print("Please enter uppercase 'C' or 'K'")
main()
