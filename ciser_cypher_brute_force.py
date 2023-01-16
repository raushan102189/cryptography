def ciser_decrypter_brute(text):
    result = ""
    number = [0,1,2,3,4,5,6,7,8,9]
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for key in range(26):
        for i in range(len(text)):
            chara = text[i]
            if chara in alphabet:
                result += alphabet[(alphabet.index(chara) - key) % 26]
            elif chara in number:
                result += number[(number.index(chara) - key) % 10]
            else:
                result += chara
     
        print(key, result)
        print("*" * 50)
        result = ""

print(ciser_decrypter_brute(" ajdbjqw120189"))