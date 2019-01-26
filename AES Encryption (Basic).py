from Crypto.Cipher import AES

import hashlib
import os, sys

#Passphrase 
pass_phrase = '0123456789abcdef'

#Using the SHA-256 Hash Algorithm to pad a 32-byte passphrase
hashed_pass_phrase = hashlib.sha256(pass_phrase).digest()


def encryption_aes():
    #The path where the dating profiles are stored
    profile_path = "C:\Users\Ryan\Desktop\Test"

    #The directory in which the dating profile are stored 
    profile_directory = os.listdir(profile_path)
 
    #Initialization vector
    IV = 16 * '\x00'

    #Set the Block mode of AES 
    mode = AES.MODE_CFB
    encryptor = AES.new(hashed_pass_phrase, mode, IV=IV)


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

        

encryption_aes()
decryption_aes()

        












