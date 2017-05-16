
def main():
tempNum = input(float("Please enter the temperature: "))
tempForm = input(str("Please enter 'C' for Celcius, or 'K' for Kelvin: "))
for tempForm == ("C"):
    if tempNum > 99:
        print("This is a gas")
    elif 99 > tempNum > 0:
        print("This is a liquid")
    elif tempNum < 0:
        print("This is a solid")
for tempForm == ("K"):
    if tempNum > 273:
        print("This is a solid")
    elif 273 < tempNum < 373:
        print("This is a liquid")
    elif tempNum > 373:
        print("This is a gas")
main():
