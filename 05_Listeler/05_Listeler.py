############### LİSTE list() #####################
"""

liste = list() # boş bir liste 1. yöntem
liste2 = [] # tavsiye edilmeyen
liste3 = [2,"Mehmet", 22.3, False]

print(liste3)
for element in liste3:
    print(element)

#Listeye eleman ekleme
print(liste)
liste.append("Kelime") # tavsiye edilen yöntem
liste +=[6] #tavsiye edilmeyen yöntem
print(liste)

"""
"""
liste = [1, "Elma", 3, 4, 5, True, 7, 8, 9, 10]

#Listenin içindeki herhangi bir değere index numarasıyla erişmek
print(liste[5])
sonuc = liste[5]
print(sonuc)

# Listeden eleman silme
del liste[1] # tavsiye edilmeyen yöntem (index no ile)
print(liste)

liste.remove(12) # tavsiye edilen (değer arama ile)
print(liste)
"""
"""
# Çoklu veri ekleme
liste =  list()

#1. yöntem tavsiye edilmeyen
liste += ["Veli","Ali","Deli"]
print(liste)

# 2. yöntem tavsiye edilen
liste.append("Kerim")
liste.append("Kemal")
liste.append("Kazım")
print(liste)

#Eleman sayısına ulaşmak
print(len(liste))
print(liste[-2]) # tersten eleman okuma  (index no ya göre)

#Liste parçalama
print(liste[0:2]) # id si 0 ve 1 olan elemanları alır ve liste olarak döner
print(liste[:2]) # id si en baştan 2'ye kadar olan elemanları al 2 ye sahip olanı alma
print(liste[2:]) # id si 2 ve 2 den sonraki elemanları al ve liste olarak dön
"""

"""
# *** Listede verilen index veri ekleme ***

rakamlar = [1, 2, 3, 4, 5, 6, 7]
print(rakamlar)
print(rakamlar[4])

rakamlar[4] = "Kerimcan"
print(rakamlar[4])
print(rakamlar)

# Araya ekleme
rakamlar.append("Ali")
print(rakamlar)

rakamlar.insert(0,"Veli") # ilk parametre hangi indexe koyulacağını belirtir.
print(rakamlar)
"""
"""
# # *** Listedeki değerin index'ine ulaşma ***
rakamlar = [1, 2, 3, 4, 5, 6, 7]

print(rakamlar.index(3))

sayilar = [ 10, 20, 30, 40, 10, 20, 20 ]
print(sayilar.index(20)) # ilk gördüğü 20 nin indexini verir
print(sayilar.index(20,4)) # aramaya 4. eleman ve sonrasından basla

# *** Listedeki bir değerin kaç defa eklendiğini bulma ***
print(sayilar.count(20)) # değerin kaç defa tekrar edildiğini verir
"""
"""

# SORU: Listedeki 20 değerlerinin indexlerini ekrana yazdırınız.
sayilar = [ 10, 20, 30, 40, 20, 20, 20 ]

for sayi in range(len(sayilar)):
    if sayilar[sayi] == 20:
        print(sayi)


"""

"""
# LİSTE SIRALAMA
rakamlar = [1, 9, 7, 6, 20]

rakamlar.sort() # küçükten büyüğe sıralama
print(rakamlar)

rakamlar.sort(reverse=True) # büyükten küçüğe sıralama
print(rakamlar)


# TÜRKÇE DİLİ AYARLAMA
import  locale
locale.setlocale(locale.LC_ALL, "tr_TR.UTF-8")

sehirler = [ "ZONGULDAK", "ÇANKIRI", "SİVAS", "BURSA", "OSMANİYE", "ADANA", "MALATYA"]

sehirler.sort(key=locale.strxfrm)
print(sehirler)

sehirler.sort(key=locale.strxfrm, reverse=True)
print(sehirler)

"""

"""
#### Listeden değerleri dışarı atma

rakamlar = [5, 69, 76, 654, 5456, 6478, 156, 658, 48]

print(rakamlar)
rakamlar.pop()  # varsayılan olarak son değeri listeden siler
print(rakamlar)

rakamlar.pop(2)  # indise göre elemanı siler
print(rakamlar)
rakamlar.remove(5) # değere göre
print(rakamlar)


##### bir değerin listede var olup olmadığı kontrol etme
deger = 565698
if deger in rakamlar:
    rakamlar.pop(rakamlar.index(deger))

print(rakamlar)


sehirler = [ "ZONGULDAK", "KONYA", "BURSA", "İZMİR", "ANTALYA", "MALATYA" ]

if "İZMİR" in sehirler:
    print("İzmir listede")
    
"""
"""
# Liste birleştirme
liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
birlesmis = liste1 + liste2  # birinci yöntem
print(birlesmis)

# ikinci yöntem
listem = list()
for i in liste1:
    listem.append(i)

for i in liste2:
    listem.append(i)

print(listem)
print( max(listem) ) # listedeki en büyük elemanın değerini verir
print( min(listem) ) # listedeki en küçük elemanın değerini verir
"""
# *** Tek satırda for yazma işlemi ***
"""
liste = list()

for sayi in range(1,11):
    liste.append(sayi)

print(liste)


rakamlar =  [  sayi for sayi in range(1,11)  ]
print(rakamlar)
"""

"""
# SORU 10 ile 100 arasındaki çift sayıları bir listeye atın.

rakamlar = [sayi for sayi in range(10, 101, 2)]
print(rakamlar)

cift_sayilar = list()
for sayi in range(10, 101, 2):
    cift_sayilar.append(sayi)

print(cift_sayilar)
"""
"""
liste = [44, 33, 55, 66] # adresi kadıköy

liste2 = liste # liste değişkeninin ramdeki adresi
liste.append("Kerim")

print(liste2)

liste2 = liste.copy() # yeni adres oluştur ve içine liste deki değerleri at
print(liste)
print(liste2)
liste.append("Kerim")
print(liste2)
"""

"""
### ALIŞTIRMALAR ###
# SORU: Kullanicidan 10 adet sayı alıp listeye
# atın ve sonrasında listenin aritmetik ortalamasını bulun.
"""
"""
sayi_listesi = list()

for i in range(1, 11):
    sayi = int(input(f"{i}. sayınız: "))
    sayi_listesi.append(sayi)

print(sum(sayi_listesi) / len(sayi_listesi))
"""

# 1. 1-100 arasında 20 adet rastgele sayı üretin ve
# aynı numara içerde olmadan listeye atın.
"""
import random

sayilar = list()

while len(sayilar) < 20:
    sayi = random.randint(1, 100)
    if sayi not in sayilar:
        sayilar.append(sayi)

print(sayilar)

sayilar2 = list()

for i in range(1, 30):
    if len(sayilar2) < 20:
        sayi = random.randint(1, 20)
        if sayi not in sayilar2:
            sayilar2.append(sayi)
        else:
            continue
    else:
        break

print(len(sayilar))
print(len(sayilar2))

tek_sayilar = list()
cift_sayilar = list()

for i in sayilar:
    if i %2 ==0:
        cift_sayilar.append(i)
    else:
        tek_sayilar.append(i)

print(tek_sayilar)
print(cift_sayilar)
"""

"""
# SORU: Klavyeden alınan 5 kelimeyi bir listeye atın.
# : Girilen 6. kelimenin listede olup olmadığını ekrana yazdırınız.
"""
"""
sayac = 1
kelimeler = list()

while sayac < 7:
    kelime = input("Kelimeyi girin")

    if sayac < 6:
        if kelime not in kelimeler:
            kelimeler.append(kelime)
            sayac +=1
        else:
            print(f"Bu kelime zaten listede mevcut KELIME: {kelime}")
    else:
        if kelime in kelimeler:
            print(f"{kelime} kelimesi kelimeler listesinde mevcut")
            break
        else:
            print(f"{kelime} kelimesi kelimeler listesinde mevcut değil")
            break
"""

### ÇOK BOYUTLU LİSTELER

cokBoyutlu = [ [ 1, 2, [9,8,7] ], [ 4, 5, 6 ] ]# 2x3 matris(liste)

print(cokBoyutlu[0][0])
print(cokBoyutlu[0][1])
print(cokBoyutlu[0][2])


print(cokBoyutlu[1][0])
print(cokBoyutlu[1][1])
print(cokBoyutlu[1][2])

print(cokBoyutlu[0][2][2])
