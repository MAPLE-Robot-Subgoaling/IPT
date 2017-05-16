
def main():

	userTemp = float(input("Please enter the temperature: "))
	userTempUnits = input("If this temperature is in Celsius please enter 'C' and if it is in Kelvin please put 'K': ")
	FREEZING_POINT_C = 0
	FREEZING_POINT_K = 273.15
	LIQUID_POINT_C = 33
	LIQUID_POINT_K = 306.15
	GAS_POINT_C = 100
	GAS_POINT_K = 373.15

	if userTemp <= FREEZING_POINT_C and userTempUnits == 'C':
		print("At this temperature, water is a (frozen) solid")
	if userTemp <= FREEZING_POINT_K and userTempUnits == 'K':
		 print("At this temperature, water is a (frozen) solid")
	elif userTemp >= FREEZING_POINT_C and userTemp <= GAS_POINT_C and userTempUnits == 'C':
		print ("At this temperature, water is in a liquid state")
	elif userTemp >= FREEZING_POINT_K and userTemp <= GAS_POINT_K and userTempUnits == 'K':
		print ("At this temperature, water is in a liquid state")
	elif userTemp >= GAS_POINT_C and userTempUnits == 'C':	
		print("At this temperature, water is in a gas state")
	elif userTemp >= GAS_POINT_K and userTempUnits == 'K':
		print("At this temperature, water is in a gas state")




main()
