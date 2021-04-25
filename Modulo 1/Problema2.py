
import string

clave = 'VCHPRZGJNTLSKFBDQWAXEUYMOI'

plaintext = input('Ingrese la palabra a encriptar: ')

alfabeto = string.ascii_uppercase

ciphertext = ''

for letra in plaintext.upper():
    for a in alfabeto:
        if letra == a:
            ciphertext += clave[alfabeto.index(letra)]
    
print(ciphertext)