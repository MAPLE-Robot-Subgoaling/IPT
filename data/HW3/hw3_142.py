def questionThree():                                                                                                                                                           
    KEVLIN_AT_ZERO_CELCIUS = 273.15;                                                                                                                                           
    WATER_BOILING_POINT = 100;                                                                                                                                                 
    WATER_FREEZING_POINT = 0;                                                                                                                                                  
    temp = input("Please enter in a temperature(include the letter): \n")                                                                                                      
    temp = temp.strip()                                                                                                                                                        
    temperatureValue = float(temp[0:len(temp) - 1])                                                                                                                            
    if temp.lower()[len(temp) - 1] == "k":                                                                                                                                     
            temperatureValue = temperatureValue - KEVLIN_AT_ZERO_CELCIUS                                                                                                       
    if temperatureValue <= WATER_FREEZING_POINT:                                                                                                                               
        print("Water is frozen at ", temperatureValue, " C")                                                                                                                   
    elif temperatureValue > WATER_FREEZING_POINT:                                                                                                                              
        if temperatureValue < WATER_BOILING_POINT:                                                                                                                             
            print("Water is a liquid at ", temperatureValue, " C")                                                                                                             
        else:                                                                                                                                                                  
            print("Water is a gas at ", temperatureValue, " C")                                                                                                                
questionThree()
