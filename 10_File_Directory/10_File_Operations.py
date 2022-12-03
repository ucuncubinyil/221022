########## DOSYA İŞLEMLERİ  ###########
"""
DOSYA YETKİ MODLARI:
w:  sadece yazma yetkisi ile açar. (dosya var ise siler yeniden oluşturur.yoksa oluşturur.)
r:  sadece okuma yetkisi ile açar.
a:  sona ekleme yetkisi ile açar. (dosya yoksa oluşturur.)
x:  yazma yetkisi ile açar. (yoksa oluşturur. varsa hata verir.)

w+: yazma + okuma yetkisi ile açar. (dosya var ise siler yeniden oluşturur.yoksa oluşturur.)
r+  okuma + yazma yetkisi ile açar.
a+  ekleme + okuma yetkisi ile açar. (dosya yoksa oluşturur.)
"""
"""
import os

os.chdir("C:\\TEST\\2022-12-03")
print(os.getcwd())

dosya_yolu = os.getcwd() + "\\birinci.txt"
print(dosya_yolu)

dosya = open(dosya_yolu, mode="a+")
dosya.write("Mehmet Nuri\n")
dosya.close() # altın kural !!!
"""
### SORU: 1 - 10 sayıların karelerini kare.txt isimli bir dosyaya aşağıdaki formatla yazdırınız.
"""
    1 sayısının karesi: 1
    2 sayısının karesi: 4
    3 sayısının karesi: 9
    ...
    ...
    ...
"""
"""
import os

os.chdir("C:\\TEST\\2022-12-03")

dosya = open("kare.txt", mode="w", encoding="utf-8")

for sayi in range(1, 11):
    dosya.write(f"{sayi}    sayısının karesi       {sayi ** 2}\n")

dosya.close()


dosya = open("kare.doc", mode="w", encoding="utf-8")

for sayi in range(1, 11):
    dosya.write(f"{sayi}    sayısının karesi       {sayi ** 2}\n")

dosya.close()


dosya = open("kare.csv", mode="w", encoding="utf-8")

for sayi in range(1, 11):
    dosya.write(f"{sayi}    sayısının karesi       {sayi ** 2}\n")

dosya.close()
"""
### SORU: 1-100 arası üretilen 10 adet sayıyı Rastgele.txt isimli bir dosyaya aşağıdaki formatta yazdıran program

"""
    Zaman                   OlaySırası              RastgeleSayı
    10.11.2021 19:00:01          1                        25
    10.11.2021 19:00:02          2                        12
    10.11.2021 19:00:03          3                        1
    10.11.2021 19:00:04          4                        76
    10.11.2021 19:00:05          5                        45
    10.11.2021 19:00:06          6                        11
    ...
    ...
"""
# import os
# from datetime import datetime
# from random import randint
#
# if not os.path.exists("C:\\TEST"):
#     os.mkdir("C:\\TEST")
#
# if not os.path.exists("C:\\TEST\\2022-12-03"):
#     os.mkdir("C:\\TEST\\2022-12-03") # make directory
#
# os.chdir("C:\\TEST\\2022-12-03") #change directory
#
# dosya = open("Rastgele.txt", mode="w", encoding="utf-8")
# dosya.write("""
#     ZAMAN                               OLAY SIRASI                     RASTGELE SAYI
#     -----                               -----------                     -------------
# """)
#
# for i in range(1, 11):
#     zaman = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
#     sayi = randint(1, 100)
#     dosya.write(f"""
# {zaman}                       {i}                             {sayi}
#     """)
#
# dosya.close()
"""


### SORU: KUllanıcıdan alınan küçük sayıdan büyük sayıya kadar olan sayıları txt dosyasında alt alta yazdırınız.
import os
baslangic = int(input("Başlangıç sayısı :"))
bitis = int(input("Bitiş sayısı :"))

if not os.path.exists("C:\\TEST"):
    os.mkdir("C:\\TEST")

if not os.path.exists("C:\\TEST\\2022-12-03"):
    os.mkdir("C:\\TEST\\2022-12-03") # make directory

os.chdir("C:\\TEST\\2022-12-03") #change directory

dosya = open("sayilar2.csv", "w")
for sayi  in range(min(baslangic, bitis), max(baslangic,bitis)):
    dosya.write(f"{sayi}\n")
dosya.close()
"""
"""
# DOSYA OKUMA

import  os


os.chdir("C:\\TEST\\2022-12-03") #change directory

dosya =  open(os.getcwd()+"\\"+"Personel.txt", mode="r", encoding="utf-8")

satir_listesi =  dosya.readlines()
yeni_liste = list()

for satir  in satir_listesi:
        satir_deger  = satir.split("\t\t")

        for i in satir_deger:
            listem =  i.split(":")
            print(listem)
            yeni_liste.append(listem[1].replace("\n", ""))


print(satir_listesi)

print(yeni_liste)
dosya.close()
"""
"""
# pip install pandas
# windows hata verirse  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser 
import pandas as pd

df = pd.read_csv('C:\\TEST\\2022-12-03\\maasim.csv', usecols = ['isim','maas'], delimiter=';')
print(df)

"""
"""
# SORU: sayiListesi.txt isimli bir dosya oluşturunuz içinde çift  ve tek sayılar karışık olacak şekilde 10 ader sayı ekleyiniz.
import os

if not os.path.exists("C:\\TEST"):
    os.mkdir("C:\\TEST")

if not os.path.exists("C:\\TEST\\2022-12-03"):
    os.mkdir("C:\\TEST\\2022-12-03")  # make directory

os.chdir("C:\\TEST\\2022-12-03")
dosya = open("sayiListesi.txt", "w")
for i in range(10):
    sayi = int(input(f"{i + 1}. sayı"))

    dosya.write(f"{sayi}\n")
dosya.close()

# sayiListesi.txt dosyasını okuyarak çiftleri çift.txt, tekleri tek.txt dosyasına yazdırınız.

dosya = open("sayiListesi.txt", "r")
tek_dosya = open("tek.txt", "w")
cift_dosya = open("cift.txt", "w")

sayilar =  dosya.readlines()
dosya.close()
for sayi in sayilar:
    if int(sayi) %2 ==0:
        cift_dosya.write(f"{sayi}\n")
    else:
        tek_dosya.write(f"{sayi}\n")
cift_dosya.close()
tek_dosya.close()
"""
# Kullanıcıdan personel sayısını al , her personel için ad, soyad dogumyılı bilgilerini alarak personel.txt
# dosyasına yaz

import os

if not os.path.exists("C:\\TEST"):
    os.mkdir("C:\\TEST")

if not os.path.exists("C:\\TEST\\2022-12-03"):
    os.mkdir("C:\\TEST\\2022-12-03")  # make directory

os.chdir("C:\\TEST\\2022-12-03")
personel_sayisi = int(input("Personel sayınız :"))

dosya = open("PERSONEL.txt", mode="w", encoding="utf-8")
dosya.write("####################PERSONEL BİLGLERİ####################\n")

for personel in range(personel_sayisi):
    print(f"{personel + 1}. Personel Bilgileri")
    ad = input("Ad")
    soyad = input("Soyad")
    dogum_yili = input("Doğum Yılı")
    dosya.write(f"AD: {ad}      SOYAD: {soyad}      DOĞUM YILI: {dogum_yili}\n")

dosya.close()
