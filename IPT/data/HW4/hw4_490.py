
def main():

	height = int(input('Please enter height: '))

	print('The height is now ', height)

	while height != 1:
		
		if height % 2 == 0:	# number is even when there's no remainder
			height = height / 2
			print('The height is now ', height)

		else:
			height = (height * 3) + 1
			print('The height is now ', height)





main()
