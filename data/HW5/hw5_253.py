def main():
	width = int(input("please enter the width of the box "))
	height = int(input("please enter the height of thebox "))
	sym = input("please enter a symbol for the outline ")	
	fill = input("please enter a fill symbol ") 
	for h in range(height):
		for w in range(width):
			print(sym if h in(0,height-1) or w in(0,width-1) else fill, end = ' ')  				
		print()			 
main()	
