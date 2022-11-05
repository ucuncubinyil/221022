# DÖNGÜLER
# WHILE  -  FOR

# 1 ile 10 arasındaki sayıları ekrana yazdırınız.
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# print(7)
# print(8)
# print(9)
# print(10)

"""
while(kosul):
    kosul true olduğu sürece bu kod bloğu çalışır.
"""
"""
i = 1
while i < 11:
    print(i)
    if i == 3:
        break
    i += 1
"""
# BREAK => Döngüyü kırar
# CONTINUE => Döngüyü başa sarar


"""
while True: # program kapatılana kadar yada döngü kırılana kadar çalıştırr
	print("Mehmet Nuri")
	break
"""
"""
while True:
    print("Mehmet Nuri")
    break
"""

# 90 ile 100 arasındaki sayıları ekrana yazdırınız.
"""
sayi = 90

while sayi <= 100:
    print(sayi)
    sayi += 1
"""
# 1-1000 arasındaki tek ve çift sayıların toplamlarını ayrı
# ayrı hesaplayan kodu yazınız if else ve while kullanın sadece
"""
tek_toplam = 0
cift_toplam = 0
sayi = 1
while sayi <= 10:

    if sayi % 2 == 0:
        cift_toplam += sayi
    else:
        tek_toplam += sayi

    sayi += 1

print(f"1-1000 arasıdaki tek sayıların toplamı {tek_toplam}")
print(f"1-1000 arasıdaki çift sayıların toplamı {cift_toplam}")
"""

"""
# 70 ile 55 arasındaki sayılarda 3'e tam bölünenleri ekrana yazdırınız
"""

"""
sayi = 70
while sayi >= 55:
    if sayi % 3 == 0:
        print(sayi)
    sayi -= 1

sayi = 55
while sayi <= 70:
    if sayi % 3 == 0:
        print(sayi)
    sayi += 1

"""

# SORU: 1'den kullanıcının girdiği sayıya kadar
# olan sayıların karesini ekrana yazdıran program.
"""
baslangic = 1
bitis =  int(input("Kaça kadar ?"))

while baslangic <= bitis:
    print(baslangic ** 2)
    baslangic += 1

# Ödev: 1'den kullanıcının girdiği sayıya kadar
# olan sayıların eğer tek ise karesini , çift ise küpünün
# toplamını ayrı ayrı hesaplayan kod parçacığı
"""

"""
baslangic = 1
bitis =  int(input("Lütfen bir sayı giriniz"))
tek_toplam = 0
cift_toplam = 0

while baslangic <= bitis:
    if  baslangic %2==0:
        cift_toplam += baslangic **3
    else:
        tek_toplam += baslangic**2
    baslangic += 1

print(tek_toplam)
print(cift_toplam)
"""

# SORU: Klavyeden girilen deger 'çık' ise döngüden
# çıkılacak. değilse toplama işlemi gerçekleştirilecek.
"""
toplam = 0
while True:
    cevap = input("Lütfen bir sayı girin veya çıkmak için çık yazın").upper()

    if cevap == "ÇIK":
        break
    else:
        toplam += int(cevap)

print(toplam)
"""

# SORU: 1-100 arasındaki sayıların toplayan program.
# Ancak aşağıdak durumlarda sayıyı toplama eklemeyecek
# * Sayı 7'nin katı ise toplama eklenmesin
# * Sayı'nın 3 katının 7 fazlası 37'nın katı ise döngüden çıkılsın.
"""
sayi = 1
toplam = 0
while sayi <= 100:
    if sayi % 7 == 0:
        sayi += 1
        continue
    kat = (sayi * 3) + 7

    if kat % 37 == 0:
        print("Kat", kat)
        break
    toplam += sayi
    sayi += 1

print(toplam)

"""
# SORU: Klavyeden girilen sayının faktöriyelini hesaplayan program
# Faktoriyel => 5! => 1*2*3*4*5=120

"""
sayi = int(input("Faktöryeli alınacak sayıyı girin: "))
sayac = 1
sonuc = 1
while sayac <= sayi:
    sonuc *= sayac
    sayac += 1
    
print(f"{sayi}! =  {sonuc}")
"""

# SORU:
"""
    Kullanıcıadı/Email ve şifre ile giriş sağlanacak. 3 defa giriş hakkı vardır.
        Giriş Başarılı ise ekrana "Giriş Başarılı" yazsın
        Değilse
            Kullanıcıya kayıt olmak ister misiniz?
                Hayır ise PEKİ!!!
                Evet Kullanıcıadı, ad, soyad,email,şifre ve şifre tekrarı
                alarak kayıt yapalım.
                    şifre ve şifretekrarın aynı olması
"""
"""
kullanici_mail = "info@mehmetnuri.net"
kullanici_adi = "mehmetnuri"
sifre = "1234"
hak = 3
giris_basarili = False

while True:

    print("##############KULLANICI GİRİŞİ##############")

    while hak > 0:

        user_name =  input("Kullanıcı adınız veya email adresiniz:")
        password =  input("Şifreniz")

        hak -= 1
        if ( kullanici_adi == user_name or  kullanici_mail == user_name  )  and (password == sifre):
            print("Başarılı")
            giris_basarili = True
            break

        else:
            print(f"Giriş bilgileriniz hatalı kalan hakkınız {hak}")
            continue

    if  hak == 0:
        print("Hakkınız kalmadı")
        break

    if giris_basarili:
        break
"""
# SORU: Kullanıcıdan alınan sayının asal olup olmadığını ekran yazdırınız.
# Asal sayı 1 ve kendisinden başka hiç bir sayıya bölünmeyen sayıdır. 13
asal_mi = True
i = 2
s = int(input("Asallığı kontrol edilecek sayıyı giriniz: "))
while i < s:
    if s % i == 0:
        asal_mi = False
        break
    i += 1

if asal_mi:
    print("Sayı asal")
else:
    print("Asal değil")
