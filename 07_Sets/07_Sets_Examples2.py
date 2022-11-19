# SORU:
# 1-15 arasında 5'er adet sayı üretip 2 farklı kümeye kaydediniz.
# Daha Sonra iki kümeyi ekrana yazdırınız.

from random import randint

kume1 = set()
kume2 = set()

for i in range(5):
    while True:
        sayi = randint(1, 15)
        if len(kume1) < 6:
            if sayi not in kume1:
                kume1.add(sayi)
                break
            else:
                print(f"Bu sayı kümede mevcut: {sayi}")
                continue
        else:
            continue

    while True:
        sayi = randint(1, 15)
        if len(kume2) < 6:
            if sayi not in kume2:
                kume2.add(sayi)
                break
            else:
                print(f"Bu sayı kümede mevcut: {sayi}")
                continue
        else:
            continue

print(kume1)
print(kume2)

kume3 = set()
kume4 = set()

while len(kume3) < 5:
    sayi = randint(1, 15)
    if sayi not in kume3:
        kume3.add(sayi)
print(kume3)

while len(kume4) < 5:
    sayi = randint(1, 15)
    if sayi not in kume4:
        kume4.add(sayi)
print(kume4)



a =  5

print("A nın değeri ",a)
print("A nın değeri {}".format(a))
print(f"A nın değeri {a}  dır b nin değeri  {a}")