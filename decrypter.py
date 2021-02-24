###Simple xor brute force decryptor
import string as str

def decrypt(inpString, key):
    for i in range(len(inpString)):
        inpString = (inpString[:i] + chr(ord(inpString[i]) ^ ord(key)) + inpString[i + 1:])
        print(inpString[i], end = " ")

def gen_combos():
    combinations = []
    all_nums_and_letters = str.ascii_letters + str.digits
    for i in all_nums_and_letters:
        for j in all_nums_and_letters: 
            combinations.append(i+j)
    return combinations


##Main
input_string = input("Please enter the string you wish to be encrypted or decrypted")
brute_force = input("Do you have the key?")

if(brute_force == "Yes"):
    combos = gen_combos()
    for poss_key in combos:
        decrypt(input_string, poss_key)
else:
    key = input("Please enter key")
    decrypt(input_string,key)

    
    
     





