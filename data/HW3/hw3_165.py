def main():
    temp = float(input("Please enter the temperature"))
    specific = input("Please enter 'C' for celsius, or 'K' or kelvin")
    if(specific ==  'C') and (temp<=0): 
                 print ("At this temperature, water is frozen")
    elif (specific == 'C') and (temp<100 and temp>0):
                 print ("At this temperature, water is a liquid")
    elif (specific == 'C') and (temp>=100):
                 print ("At this temperature, water is a gas")    
    elif(specific ==  'K') and (temp<=273):
                 print ("At this temperature, water is frozen")
    elif (specific== 'K') and (temp<373 and temp>273):
                 print ("At this temperature, water is a liquid")
    elif (specific == 'K') and (temp>=373):
                 print ("At this temperature, water is a gas")
main()
