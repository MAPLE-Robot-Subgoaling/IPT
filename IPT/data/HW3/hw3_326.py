
def main():
    temp=int(input("Please enter the temperature:"))
    degree=input("Please enter 'C' for Celsius, or 'K' for Kelvin:")

    if degree=="C": 
        if temp<100:
            print("At this temperature, water is a liquid")
        elif temp<=0:
            print("At this temperature, water is a solid")
        elif  temp>=100:
            print("At this temperature, water is a gas")
    

    if degree=="K":
        if temp<373:
            print("At this temperature, water is a liquid")
        elif  temp<=273:
            print("At this temperature, water is a solid")
        elif  temp>=373:
            print("At this temperature, water is a gas")
main()
