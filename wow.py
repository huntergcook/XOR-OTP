import sys
import random

def encrypt(message,key):
    code = 0b00000000
    noise = " - - - NOISE: "

    #Message encryption - - XOR
    for mesPoint in message:
        code = code + ord(mesPoint)
        code = code << 8
    code = code >> 8
    code = code ^ key

    print("\n")
    print("Code:")
    print(code)
    print("\n")

def decrypt(code,key):
    plain = ''
    decode = code ^ key
    while decode > 0:
        plain = chr(decode & 0b11111111) + plain
        decode = decode >> 8

    print("\n")
    print("Message:")
    print(plain)
    print("\n")

def keyGen(keyInput):
    first= 1
    key1 = ''
    key2 = ''
    for keyPoint in keyInput:
        if keyPoint == "^":
            first = 0
            continue
        if first == 1:
            key1 = key1 + keyPoint
        if first == 0:
            key2 = key2+ keyPoint
    key1 = int(key1)
    key2 = int(key2)
    return pow(key1,key2)



#Main Loop
while 1:
    print("XOR Encryption - Hunter G. Cook - 2019")
    print("e = Encrypt, d = Decrypt, q = Quit")
    keeb = input()
    print("\n")

    if keeb=="e":
        print("Enter message to be encrypted:")
        message = input()
        print("Enter Key in the form of X^Y:")
        key = keyGen(input())
        encrypt(message,key)

    if keeb=="d":
        print("Enter code to be decrypted:")
        code = int(input())
        print("Enter in the form of X^Y:")
        key = keyGen(input())
        decrypt(code,key)
    if keeb=="q":
        break
