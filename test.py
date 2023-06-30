import random

def Generator(pertanyaan):
     chars = "<>+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
     password = ""

     #pertanyaan = int(input("Berapa panjang kata sandi yang ingin kamu generate: "))

     for i in range(pertanyaan):
          password = password + random.choice(chars)
     #print(password)
     return password