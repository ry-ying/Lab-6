def encode(password):
    encoded = ""
    for letter in password:
        encoded += str(int(letter)+3)
    return encoded


if __name__ == "__main__":
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print("")
        menu_option = int(input("Please enter an option: "))

        if menu_option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
            print("")

        # Add menu option 2 (decoder) option here

        elif menu_option == 3:
            break