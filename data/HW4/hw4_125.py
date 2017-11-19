def main():
    username = input("Please enter your username: ")
    bypass = 0
    while bypass != 1:
        if len(username) < 2:
            print("Username is too short, must be at least 2 characters")
            username = input("Please enter your new username: ")
        elif len(username) <= 8 and len(username) >= 2  and username[-1:] != "1" :
            print("Username must end with a '1'.")
            username = input("Please enter your new username: ")
        elif len(username) > 8:
            print("Username is too long. Must be no longer than 8 characters.")
            username = print("Please enter your new username: ")
        elif len(username) <= 8 and len(username) >= 2 and username[-1:] == "1":
            print("Thank you for choosing username: ", username)
            bypass = 1
        else:
            print("It didn't work.")
            bypass = 1
main()
