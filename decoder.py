def decoder(password):
    newPassword = ""
    for i in password:
        newPassword += (int(i) - 3)
    return newPassword