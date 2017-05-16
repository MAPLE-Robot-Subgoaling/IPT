
def main():
    userTemp = float(input("Please enter the temperature: "))
    tempVari = input("Please enter 'C' for Celsius, or 'K' for Kelvin: ")

    if userTemp <= 0 and tempVari == C:
        print("At this temperature, water is a (frozen) solid.")
    if userTemp > 0 or userTemp < 100 and tempVari == C:
        print("At this temperature, water is a liquid.")
    if userTemp > 100 and tempVari == C:
        print("At this temperature, water is a gas.")

    if userTemp <= 273.15 and tempVari == K:
        print("At this temperature, water is a (frozen) solid.")
    if userTemp > 273.15 or usertemp < 373.15 and tempVari == K:
        print("At this temperature, water is a liquid.")
    if userTemp > 373.15 and tempVari == K:
        print("At this temperature, water is a gas.")

main()
