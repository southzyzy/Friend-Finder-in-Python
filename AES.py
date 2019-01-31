from Crypto.Cipher import AES
from passlib.hash import sha256_crypt
import hashlib
import os, sys


def encrypt():
    # Prompt the user to enter a passphrase
    # pass_phrase = raw_input("Please enter a passphrase to encrypt the user profiles: ")
    pass_phrase = "ICT1002"

    # Hash the passphrase with salts
    hashed_pass_phrase = sha256_crypt.encrypt(pass_phrase)

    # Using the SHA-256 Hash Algorithm to pad a 32-byte passphrase
    original_pass_phrase_padded = hashlib.sha256(pass_phrase).digest()

    # The path where the dating profiles are stored
    CURENT_DIR = os.path.dirname(__file__)  # specify current directory

    # The directory in which the dating profile are stored
    profile_directory = os.path.join(CURENT_DIR, "keys/")
    files = [file for file in os.listdir(profile_directory) if file.endswith(".txt")]

    # Initialization vector
    IV = 16 * '\x00'

    # Set the Block mode of AES
    mode = AES.MODE_CFB
    encryptor = AES.new(original_pass_phrase_padded, mode, IV=IV)

    # Encrypt all the user profile files
    for file in files:
        # Input the file to be encrypted
        filename = profile_directory + file
        input_file = open(filename, "rb")

        data_to_be_encrypted = input_file.read()

        input_file.close()

        # Encrypt the contents of the file
        ciphertext = encryptor.encrypt(data_to_be_encrypted)

        # Write encrypted contents to a new file
        encrypted_file_name = filename + ".bin"

        encrypted_output_file = open(encrypted_file_name, "wb")

        encrypted_output_file.write(hashed_pass_phrase + "::" + ciphertext)

        # remove the original file
        os.remove(filename)


def decrypt():
    # Prompt the user to enter a passphrase
    # pass_phrase = raw_input("Please enter a passphrase to decrypt the user profiles: ")
    pass_phrase = "ICT1002"

    # The path where the dating profiles are stored
    CURENT_DIR = os.path.dirname(__file__)  # specify current directory

    # The directory in which the dating profile are stored
    profile_directory = os.path.join(CURENT_DIR, "keys/")
    files = [file for file in os.listdir(profile_directory) if file.endswith(".bin")]

    for file in files:
        filename = profile_directory + file
        input_file = open(filename, "rb")
        file_contents = input_file.read()
        input_file.close()

        hashed_pass_phrase = file_contents.split("::")[0]
        cipherText = file_contents.split("::")[1]

        if sha256_crypt.verify(pass_phrase, hashed_pass_phrase) == True:
            # Using the SHA-256 Hash Algorithm to pad a 32-byte passphrase
            hashed_pass_phrase = hashlib.sha256(pass_phrase).digest()

            # Initialization vector
            IV = 16 * '\x00'

            # Set the Block mode of AES
            mode = AES.MODE_CFB
            decryptor = AES.new(hashed_pass_phrase, mode, IV=IV)

            plain = decryptor.decrypt(cipherText)
            return plain

        else:
            print "Incorrect passphrase entered."
            sys.exit(0)
