import hashlib
from cryptography.fernet import Fernet

# Generates a hash (sha256 algo) out of the given argument.
def string_to_hash_func(string_to_hash):
    string_encoded = string_to_hash.encode()

    hash_container = hashlib.sha256()
    hash_container.update(string_encoded)
    hashed_string = hash_container.hexdigest()

    return hashed_string

# Ecrypts the first arguments using the second argument as the key.
def fernet_info_encrypting(information_to_encrypt, fernet_key):

    f = Fernet(fernet_key)
    information_to_encrypt_b = information_to_encrypt.encode()
    encrypted_information = f.encrypt(information_to_encrypt_b)

    return encrypted_string

# Decrypts the first arguments using the second argument as the key.
def fernet_info_decrypting(information_to_decrypt, fernet_key):

    f = Fernet(fernet_key)
    information_to_decrypt_b = information_to_decrypt.encode()
    decrypted_information = f.decrypt(information_to_decrypt_b)

    return decrypted_information

### FErnet only works while passing bytes therefore the passed input from the 
### user has either to be decoded or encoded.

# Decodes the password from the database. Calls first the above writeen 
# decrypting function and then decodes the bytes into a regular format.
def password_to_decrypt(pw_database, fernet_key):
    password_to_decrypt_decrypted = fernet_info_decrypting(pw_database, fernet_key)
    password_to_decrypt_decrypted_d = password_to_decrypt_decrypted.decode()

    return password_to_decrypt_decrypted_d
# Encodes the input from the user. And then decodes the bytes back into a string
# so that it can be written into the dictionary.
def password_to_encrypt(input_user, fernet_key):
    password_fer = fernet_info_encrypting(input_user, fernet_key)
    password_fer_encoded = password_fer.decode()

    return password_fer_encoded