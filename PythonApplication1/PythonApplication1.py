from math import *
print("Tere! Olen sinu uus sõber - Python!")
name=input("kuidas su nimi on?")
print(name,"oi kui ilus nimi!")
keha_indeks=input("Kas ma leian sinu keha indeksi? 0-ei, 1-jah=>")
try: 
    if int(keha_indeks)==1:
        pikkus=int(input("pikkus"))
        mass=float(input("mass"))
        indeks=mass/(0.01*pikkus)**2
        print(name+"! Sinu keha indeks on:",round(indeks,2))