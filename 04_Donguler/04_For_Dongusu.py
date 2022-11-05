##### FOR DONGUSU #####

"""
i =  1

while i <=10:
    print(i)
    i+=1
"""
"""
print(range(5)) # => 0-5 aralığındaki sayıları getirir bitiş değerini almaz
print(range(1,5)) # => 1-5 aralığındaki sayıları verir bitiş değerini almaz
print(range(1,9,3)) # =>  1,4,7 Başlangıçtan bitişe kadar sayıları 3 er 3 er alır


"""
"""
for i in aralık:
    yapılacak işlem
"""
"""
for i in range(1,11): #0-10 10 dahil
    print(i)

for elma in range(1,11,3):
    print(elma)

# Kadıköy

for harf in "Kadıköy":
    print(harf)
"""
##### ALIŞTIRMALAR #####
# 1 ile 40 arasındaki sayıları toplayan programı yazınız. 40 dahil.
"""
toplam = 0
for sayi in range(41):
    toplam += sayi

print(toplam)
"""
## SORU 20-40 arasındaki çift ve tek sayıların
# toplamlarını ayrı ayrı ekrana yazdırınız.
"""
tek_sayilarin_toplami = 0
cift_sayilarin_toplami = 0

for sayi in range(20, 41):

    if sayi % 2 == 0:
        cift_sayilarin_toplami += sayi
    else:
        tek_sayilarin_toplami += sayi

print(f"Tek sayıların toplamı  {tek_sayilarin_toplami}")
print(f"Çift sayıların toplamı  {cift_sayilarin_toplami}")
"""

# 1'den başlayarak Klavyeden girilen sayıya kadar
# olan sayılardan 4'e tam bölünenlerinin çarpımını yazdırınız
"""
carpim = 1
sayi = int(input("Sayi"))

for i in range(1, sayi + 1):
    if i % 4 == 0:
        carpim *= i
print(f"1-{sayi} arasındaki 4 e tam bölünen sayıların çarpımı {carpim}")

"""
# Kullanıcıdan girilen sayıya kadar olan sayıların çarpımını
# hesaplayın (Faktöryel Hesabı) 1-5 1.2.3.4.5
"""
carpim = 1
baslangic = int(input("Başlangıç:"))
bitis = int(input("Bitiş"))

if baslangic <= 0:
    baslangic = 1

if bitis <= 0:
    bitis = 1

for sayi in range(baslangic , bitis+1):
    carpim *= sayi

print(f"{baslangic}-{bitis}! = {carpim}")

"""
"""  
print("Elma"*2)

"""
"""  
*
**
***
****
*****
"""
"""  
for i in range(1, 6):
    print("*"*i)
  """

"""
*****************
*               *
*               *
*               *
*               *
*****************
"""
"""
for i in range(1,7):

    if i == 1 or i == 6:
        print("*"*17)

    else:
        print("*",(" "*15), "*", sep="")

"""
"""
            *
           ***
          *****
         *******
        *********
"""
"""
sayac = 1
for satir in range(1, 30):
    print(" " * (30 - satir), end="")
    print("$" * sayac)
    sayac += 2
"""
## ÇARPIM TABLOSU
"""
1 x 1 = 1 1 x 2 = 2 1 x 3 =3
2 x 1 = 2 ....
3 x 1 = 3 """
"""
for i in range(1,11):

    for j in range(1,11):
        print(i, "X", j, "=",(i*j), end= "\t\t\t")

    print()
"""

"""
for i in range(10,0,-1):
    print(i)

"""

"""
# SORU: Kullanıcıdan personel sayısını alınız.
# Personelin kaç çocuğu olduğunu isteyelim.
# Program her çocuk için "Çocuğunuz adına 1 ağaç dikilmiştir" yazsın
# Toplam dikilen ağaç sayısınıda ekrana yazdıralım.
"""
"""
toplam_dikilen_agac_sayisi = 0
personel_sayisi = int(input("Personel sayınız: "))

for personel in range(1, personel_sayisi + 1):

    while True:
        cocuk_sayisi = int(input(f"{personel}. personelin çocuk sayısı"))
        toplam_dikilen_agac_sayisi += cocuk_sayisi
        print("Çocuklarınız adına ", cocuk_sayisi , " ağaç dikilmiştir.")
        break

    for cocuk in range(cocuk_sayisi):
        print("Çocuğunuz adına 1 ağaç dikilmiştir.")

print(f"Toplam dikilen ağaç sayısı: {toplam_dikilen_agac_sayisi}")
"""

#### TAHMİN OYUNU ####
# Bilgisayar 1-100 arasında rastgele bir sayı üretsin.
# Kullanıcının 5 hakkı olsun ve sayıyı bilmeye çalışsın.
# Bilirse TEBRİKLER. bilemezse tekrar deneyiniz. hakkı biter hakkınız bitti yazsın.
# BONUS: tahmin değeri rastgele değerden büyük ise tahmininizi küçültünüz
#        tahmin değeri rastgele değerden küçük ise tahmininizi büyültünüz
"""
import  random
rast_gele_sayi =  random.randint(1,100)
for hak in range(1,6):
    tahmin = int(input("Tahmininiz"))
    if tahmin > rast_gele_sayi and hak <5:
        print("Tahmininizi küçültün")
    elif tahmin < rast_gele_sayi and hak <5:
        print("Tahmininizi büyültün")
    elif rast_gele_sayi == tahmin:
        print("Tebrikler")
        break
    else:
        print(rast_gele_sayi)
        print("😛 Hak bitti !")

"""
## kaçak yöntemler

toplam = 0

for sayi in range(1,101):
    toplam += sayi

print(toplam)

n = 100
formul = n * (n+1)/2
print(formul)