
BOILING_C=100
FROZEN_C=0
BOILING_K=373.15
FROZEN_K=273.15

def main():
    temp=float(input("Please enter the tempurature: "))
    degree=input("Please enter 'c' for celcius or 'k' for kelvins: ")
    if degree == "c":
        if temp <= FROZEN_C:
            print("At this tempurature, water is (frozen) solid.")
        elif temp >=BOILING_C:
            print("At this tempurature, water is a gas.")
        else:
            print("At this tempurature, water is a liquid.")
    elif degree=="k":
        if temp <= FROZEN_K:
            print("At this tempurature, water is (frozen) solid.")
        elif temp >= BOILING_K:
             print("At this tempurature, water is a gas.")
        else: 
            print("At this tempurature, water is a liguid.")
main()
