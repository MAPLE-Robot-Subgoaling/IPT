
def main():
   height = int(input("Please enter the starting height of the hailtstone: "))
   print("Hail is currently at height " + str(height))
   while not(height == 1):
      if ((height % 2) == 0):
          height = int(height / 2)
      else:
          height = int((3 * height) + 1)
      print("Hail is currently at height " + str(height))
   print("Hail stopped at height 1")

main()
