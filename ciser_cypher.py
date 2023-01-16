#making ciser cypher encryption and decryption normal with word 



def ciser_encrypt(text, key):
    result = ""

    number = [0,1,2,3,4,5,6,7,8,9]
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(text)):
        chara = text[i]
        if chara in alphabet:
            result += alphabet[(alphabet.index(chara) + key) % 26]
        elif chara in number:
            result += number[(number.index(chara) + key) % 10]
        else:
            result += chara
    return result
def ciser_decrypt(text, key):
    result = ""

    number = [0,1,2,3,4,5,6,7,8,9]
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(text)):
        chara = text[i]
        if chara in alphabet:
            result += alphabet[(alphabet.index(chara) - key) % 26]
        elif chara in number:
            result += number[(number.index(chara) - key) % 10]
        else:
            result += chara
    return result
def key_maker(keys):
    key = 0
    try:
        key = int(keys)
    except:
        alphabhate = "abcdefghijklmnopqrstuvwxyz"
        numbers = "1234567890"
        
        for i in range(len(keys)):
            if keys[i] in alphabhate:
                key += alphabhate.index(keys[i]) +1
            elif  keys[i] in numbers:
                key += numbers.index(keys[i]) +1
    return key


run = "y"
while run == "y":
    print("1. Encrypt")
    print("2. Decrypt")
    choice = input("Enter your choice: ")
    if choice == "1":
        text = input("Enter the text: ")
        user_key = int(input("Enter the key: "))
        key = key_maker(user_key)
        print("Encrypted text:\n " + ciser_encrypt(text, key))
    elif choice == "2":
        text = input("Enter the text: ")
        user_key = int(input("Enter the key: "))
        key = key_maker(user_key)
        print("Decrypted text:\n " + ciser_decrypt(text, key))
    run = input("Do you want to continue? (y/n): ")
    