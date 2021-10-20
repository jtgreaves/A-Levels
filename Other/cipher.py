letter = input("What character would you like") 
shift = int(input("How much is the cipher shift? "))

print("New letter", chr(ord(letter) + shift))
