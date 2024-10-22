def encode(password):
    encoded = ""
    for letter in password:
        new_digit = (int(letter) + 3) % 10 
        encoded += str(new_digit)
    return encoded

def decode(encoded_password):
    decoded = ""
    for letter in encoded_password:
        new_digit = (int(letter) - 3)  
        if new_digit < 0:  
            new_digit += 10
        decoded += str(new_digit)
    return decoded


if __name__ == "__main__":
    last_encoded_password = None
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
            last_encoded_password = encode(password)
            print("Your password has been encoded and stored!")
            print("")

        elif menu_option == 2:
            if last_encoded_password:
                decoded_password = decode(last_encoded_password)
                print(f"The encoded password is {last_encoded_password}, and the original password is {decoded_password}")
                print("")
            else:
                print("No encoded password found. Please encode a password first.")
                print("")
        elif menu_option == 3:
            break
