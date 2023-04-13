import random
import string
import math

def convert_binary(msg):
    ordinal, bina = [], []
    resultado = ""
    for i in msg:
        ordinal.append(ord(i))
    for i in ordinal:
        bina.append(int(bin(i)[2:]))
        print(bina[len(bina)-1])
        resultado += str(bina[len(bina)-1])

    return resultado

ctrs = " " + string.punctuation + string.digits + string.ascii_letters
ctrs = list(ctrs)
key = ctrs.copy()

random.shuffle(key)
other_key = key.copy()
random.shuffle(other_key)

special_key = []

for letter in key:
    index = key.index(letter)
    special_key.append(other_key[len(other_key) -1 - index] + key[index])

mensage = input("Digite a mensagem a ser Encriptografada: ")
result = ""

for l in mensage:
    i = ctrs.index(l)
    result += special_key[i]

print(convert_binary(result))