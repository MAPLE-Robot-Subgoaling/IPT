def main():
	boxWidth=input("Please enter the width of the box:")
	boxHeigth=input("Please input the height of the box:")
	boxOutline=input("Please input the symbol for the box outline:")
	boxFill=input("Please input the symbol for the inside of the box:")
	emptyString2=" "
	emptyString=""
	integerboxWidth=int(boxWidth)
	integerboxHeigth=int(boxHeigth)
	line1=emptyString+(integerboxWidth*boxOutline)
	halfboxHeigth=int(float(integerboxHeigth/2))
	emptySpace=int(float(((integerboxWidth)/2)-1))
	emptySpace2=int(emptySpace-1)
	print(line1)
	lines=range(halfboxHeigth)
	for index in lines:
		print(boxOutline,emptyString2*emptySpace,boxOutline)
	print(boxOutline,emptyString*emptySpace,boxFill,emptyString*emptySpace2,boxOutline)
	for index in lines:
		print(boxOutline,emptyString2*emptySpace,boxOutline)
	print(line1)
main()
