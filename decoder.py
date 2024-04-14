def decoder(password):
    decoded_password = ''

    for digit in password:
        new_digit = (int(digit) - 3) % 10
        decoded_password += str(new_digit)

    return decoded_password
