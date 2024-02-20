plaintext = input("Enter plaintext: ")
integer = int(input("Enter integer: "))

print("Your ciphertext is: ", end="")
for char in plaintext:
    print(chr(ord(char)^integer), end="")