# Adam Benali
from decoder import decode
def encoder(password):
    newPassword = ""
    for i in password:
        newPassword += str(int(i)+ 3 % 10)
    return newPassword

if __name__ == "__main__":
    password = ""
    running = True
    while running:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        user_input = int(input("Please enter an option:"))
        if user_input == 1:
            password = input("Please enter your password to encode:")
            password = encoder(password)
            print("Your password has been encoded and stored!")
        elif user_input == 2:
            decoded = decode(password)
            print(f"The encoded password is {password}, and the original password is {decoded}")
        else:
            running = False







