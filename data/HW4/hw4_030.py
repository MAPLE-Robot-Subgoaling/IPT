STOP_HEIGHT = 1
def main ():
 	hailHeight = int ( input ("Please enter the starting height of the hailstone: "))
 	while hailHeight != STOP_HEIGHT:
 		if hailHeight % 2 == 0:
 			print ("Hail is currently at", hailHeight)
 			hailHeight = hailHeight  // 2
 		else:
 			print ("Hail is currently at", hailHeight)
 			hailHeight = hailHeight * 3 + 1
 	print ("Hail stopped at height 1.")
main ()