
K="K"
C="K"

def main():
    
    tem = float (input("Please enter the temperature: "))
    measur = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")
    if (measur == C and tem <= 0) or (measur == K and tem <= 32): 
        print(" At this temperature, water is a (frozen) solid.")
    elif (measur == C and (tem >0 and tem <100)) or (measur== K and (tem > 32 and tem< 212)):
        print("At this temperature, water is a liquid.")
    else:
        print("At this temperature, water is a gas.")

main()
