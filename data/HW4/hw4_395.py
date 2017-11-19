def main():
	currentHeight = int(input("Please enter the hail's starting height: "))
	if currentHeight == 1:
		print("The hail has stopped")
		exit
	while currentHeight % 2 == 0 :
	    currentHeight = (currentHeight // 2)
	    print("Hail is currently at height ",currentHeight)
	    if currentHeight == 1 :
	    	exit
	    if currentHeight % 2 !=0 and currentHeight != 1 :
		    currentHeight = ((currentHeight * 3) + 1)
		    print("Hail is currently at height ",currentHeight)
	    if currentHeight == 1 :
		    print("Hail stopped at height 1")
		    exit
	while currentHeight % 2 != 0 and currentHeight != 1 :
		currentHeight = ((currentHeight * 3) + 1)
		print("Hail is currently at height ",currentHeight)
		while currentHeight % 2 == 0 :
			currentHeight = (currentHeight // 2)
			print("Hail is currently at height ",currentHeight)
			if  currentHeight == 1 :
				print("Hail stopped at height 1")
				exit
main()
