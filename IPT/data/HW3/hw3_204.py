
def main():
    temp=float(input("Whats the temperture?"))
    form=input('Please enter "C" for Celsius, or "K" for Kelvin')
    if form == "K":
        if temp <= 273.15:
            print('At',temp,'K Water is Ice')
        elif temp >=373.15:
            print('At',temp,'K Water is Vapor')
        else:
            print('At',temp,'K Water is Liquid')
    elif form == "C":
        if temp <= 0:
            print('At',temp,'C Water is Ice')
        elif temp >=100:
            print('At',temp,'C Water is Vapor')
        else:
            print('At',temp,'C Water is Liquid')
    else:
         print('Are you sure you entered a proper value for the answers? Please try again!')
main()
