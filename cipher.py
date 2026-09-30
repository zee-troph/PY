

# simple caesar cipher - Text based application
SHIFT = 3
def encrypt_text(text):
    encrypted = ""
    
    for ch in text:
        encrypted += chr(ord(ch) + SHIFT)
        
    return encrypted

def decrypt_text(text):
    decrypted = ""
    
    for ch in text:
        decrypted += chr(ord(ch) - SHIFT)
        
    return decrypted

# Save text to file
def save_text_to_file(text, filename):
    with open(filename, "a") as file:
        file.write(text + "\n")
    print(f"Text saved to {filename} successfully.")

# Main program
while True:
    print("\nSimple Caesar Cipher")
    print("1. Encrypt Text")
    print("2. Decrypt Text") 
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")        
    
    if choice == "1":
        text = input("Enter the text to encrypt: ")
        encrypted_text = encrypt_text(text)
        print("Encrypted Text:", encrypted_text)
        save_text_to_file(encrypted_text, "encrypted.txt")
    elif choice == "2":
        text = input("Enter the text to decrypt: ")
        decrypted_text = decrypt_text(text)
        print("Decrypted Text:", decrypted_text)
        save_text_to_file(decrypted_text, "decrypted.txt")
    elif choice == "3":
        print("Goodbye...")
        break
    else:
        print("Invalid choice. Please try again.")
        
        