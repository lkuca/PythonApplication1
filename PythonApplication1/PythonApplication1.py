

from math import * 
print("Tere! Olen sinu uus sõber - Python!") 
name=input("Kuidas su nimi on? ") 
print(name+", oi kui ilus nimi!") 
try:
    a=input("! Kas leian Sinu keha indeksi? 0-ei, 1-jah => ") 
    if int(a)==1: 
        pikkus=int(input('tell me your "pikkus": ')) 
        mass=float(input('tell me your "mass": ')) 
        indeks=int(mass/(0.01*pikkus)**2) 
        print(name,"Sinu keha indeks on:",round(indeks,1))
        if indeks<16:
            print("Tervisele ohtlik alakaal")
            pass
        elif indeks>16 and indeks<19:
            print("Alakaal")
            pass
        elif indeks>19 and indeks<25:
            print("Normaalkaal")
            pass
        elif indeks>25 and indeks<30:
            print("Ülekaal")
            pass
        elif indeks>30 and indeks<35:
            print("Rasvumine")
            pass
        elif indeks>35 and indeks<40:
            print("Tugev rasvumine")
            pass
        elif indeks>40:
            print("Tervisele ohtlik rasvumine")
            pass
    else:
        print("Kahju! See on väga kasulik info!")
        print()
        print("Kohtumiseni,",name," Igavesti Sinu, Python!")
except:
    print("ValueError")