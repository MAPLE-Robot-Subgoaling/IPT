
def main():
    temp = int(input("Please enter in the temperature: "))
    scale = input("Please enter what the temperature is measured in (use K or C): ")
    if scale == "K":
        if temp >= 373:
            print("At this temperature, water is a gas") 
        elif temp <= 273:
            print("At this temperature, water is a solid")
        else:
            print("At this temperature, water is a liquid")
    else:
        if temp >= 100:
            print("At this temperature, water is a gas")
        elif temp <= 0:
            print("At this temperature, water is a solid")
        else:
            print("At this temperature, water is a liquid")
main()
