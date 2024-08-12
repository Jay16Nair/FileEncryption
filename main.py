from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def save_key(key, key_file):
    with open(key_file, 'wb') as file:
        file.write(key)

def load_key(key_file):
    with open(key_file, 'rb') as file:
        return file.read()
    
def encrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as file:
        data = file.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    with open(output_file, 'wb') as file:
        file.write(encrypted_data)

    print(f"File '{input_file}' has been encrypted and saved as '{output_file}'")

def decrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as file:
        encrypted_data = file.read()

    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)

    with open(output_file, 'wb') as file:
        file.write(decrypted_data)

    print(f"File '{input_file}' has been decrypted and saved as '{output_file}'")

if __name__ == '__main__':
    key = generate_key()
    key_file = 'FileEncryption/encryption_key.key'
    save_key(key, key_file)
    print(f"Encryption key has been generated and saved as '{key_file}'")

    input_file = 'FileEncryption/text.txt'
    encrypted_file = 'FileEncryption/encrypted_file.txt'
    decrypted_file = 'FileEncryption/decrypted_file.txt'

    encrypt_file(input_file, encrypted_file, key)
    decrypt_file(encrypted_file, decrypted_file, key)
