#Contributer: Zachary Allarey

def encode_password(password):
    encoded = ""
    for digit in password:
        new_digit = str((int(digit) + 3) % 10)
        encoded += new_digit
    return encoded

def decode_password(encoded_password):
    decoded = ""
    for digit in encoded_password:
        original_digit = str((int(digit) - 3) % 10)
        decoded += original_digit
    return decoded

def menu():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = input("Please enter an option: ")
        if option == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode_password(password)
            print("Your password has been encoded and stored!")
        elif option == "2":
            if 'encoded_password' in locals():
                decoded_password = decode_password(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}")
            else:
                print("Please encode a password first.")
        elif option == "3":
            break

if __name__ == "__main__":
    menu()

