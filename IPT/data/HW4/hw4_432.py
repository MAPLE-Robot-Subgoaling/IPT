
def main():
	height = int(input('How tall? '))
	while 1 < height:
		height = height / 2 if height % 2 == 0 else (3 * height) + 1
		print('Height:', height)
	print('Height reached 1, exiting..')
main()
