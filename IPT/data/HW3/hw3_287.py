

def main():

    temp = input("Please enter the water temperature:  ")
    temp = int(temp)
    convTemp = int(convTemp)

    tempScale = input("Enter 'C' for Celsius or 'K' for Kelvin: ")
    tempScale = str(tempScale)

    if tempScale == "C":
        convTemp = (temp * 9/5) + 32
    elif tempScale == "K":
        convTemp = ((temp * 9/5) + 32) + 100

    if 
