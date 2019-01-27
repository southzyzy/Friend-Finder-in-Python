from Crypto.Cipher import AES
from passlib.hash import sha256_crypt
import hashlib
import os, sys

hashed_pass_phrase_list = []

def encryption_aes():
    #Prompt the user to enter a passphrase 
    pass_phrase = raw_input("Please enter a passphrase to encrypt the user profiles: ")

    #Hash the passphrase with salts 
    hashed_pass_phrase = sha256_crypt.encrypt(pass_phrase)

    hashed_pass_phrase_list.append(hashed_pass_phrase)

    #Using the SHA-256 Hash Algorithm to pad a 32-byte passphrase
    original_pass_phrase_padded = hashlib.sha256(pass_phrase).digest()

    #The path where the dating profiles are stored
    profile_path = "C:\Users\Ryan\Desktop\Test"

    #The directory in which the dating profile are stored 
    profile_directory = os.listdir(profile_path)
 
    #Initialization vector
    IV = 16 * '\x00'

    #Set the Block mode of AES 
    mode = AES.MODE_CFB
    encryptor = AES.new(original_pass_phrase_padded, mode, IV=IV)

    #Encrypt all the user profile files 
    for file in profile_directory:
        if file.endswith(".txt"):
            
            #Input the file to be encrypted 
            input_file = open(file, "rb")

            data_to_be_encrypted = input_file.read()

            #Encrypt the contents of the file
            ciphertext = encryptor.encrypt(data_to_be_encrypted)

            #Write encrypted contents to a new file
            encrypted_file_name = file + ".bin"
            
            encrypted_output_file = open(encrypted_file_name, "wb")

            encrypted_output_file.write(ciphertext)


def decryption_aes():
    #Prompt the user to enter a passphrase 
    pass_phrase = raw_input("Please enter a passphrase to decrypt the user profiles: ")

    #Scenario 1: The user entered the correct passphrase 
    if sha256_crypt.verify(pass_phrase, hashed_pass_phrase_list[0]) == True:

        #Using the SHA-256 Hash Algorithm to pad a 32-byte passphrase
        hashed_pass_phrase = hashlib.sha256(pass_phrase).digest()

        #Initialization vector
        IV = 16 * '\x00'

        #Set the Block mode of AES
        mode = AES.MODE_CFB
        decryptor = AES.new(hashed_pass_phrase, mode, IV=IV)

        #The path where the dating profiles are stored
        profile_path = "C:\Users\Ryan\Desktop\Test"

        #The directory in which the dating profile are stored 
        profile_directory = os.listdir(profile_path)

        #Decrypt all of the encrypted profiles and display them 
        for file in profile_directory:
            if file.endswith(".bin"):
                
                input_file = open(file, "rb")

                cipher_text = input_file.read()

                plain = decryptor.decrypt(cipher_text)

                print plain
                
    #Scenario 2: The user entered an incorrect passphrase 
    else:
        print "Incorrect passphrase entered."


encryption_aes()
decryption_aes()










 





        












