##################### AKIŞ KONTROL : IF ELIF ELSE ########################################
# Program akışında bir sonuc,durum ve değere göre program akışı
# devam edecek ise if elif else deyimleri kullanılır.
# Karar yapıların if ve else 1 kez tanımlanır.
# alternatif bütün durumlar elif keyword'ü tekrar tekrar
# yazılarak kullanılablir

"""
if koşul:
	yapılmak istenilen
elif koşul2:
	yapılmak istenilen
else:
	eğer koşullar doğru değil ise burası çalışır

"""

"""
sayi = 6

if sayi > 6:
	print("Sayi değişkeni 6 dan büyüktür")
elif sayi == 6:
	print("Sayi değişkeni 6 ya eşittir")
else:
	print("Sayi değişkeni 6 dan küçüktür")
"""

"""
# Haftanın kaçıncı günüdeyiz? ekrana gün adını yazdıralım
gun = int(input("Haftanın gün sayısını giriniz: "))
if gun == 1:
	print("Pazartesi")
elif gun == 2:
	print("Salı")
elif gun == 3:
	print("Çarşamba")
elif gun == 4:
	print("Perşembe")
elif gun == 5:
	print("Cuma")
elif gun == 6 or gun == 7:
	print("Haftasonu")
else:
	print("Yanlış gün girdiniz !!!")

"""
# SORU: Klavyeden girilen değer: 100'den büyükse karesini,
# küçükse küpünü ekrana yazdıran prog.
"""
sayi = int(input("Sayı: "))

if sayi >100:
	print(sayi**2)
elif sayi < 100:
	print(sayi**3)
else:
	print(sayi)
"""
# Klavyeden girilen sayı çift ise:
# Ekrana sayı çifttir yazılacak,
# değilse tektir yazılacak
# çift ise 4 ile çarpsın, tek ise 9 ile toplasın
"""
sayi =  int(input("Sayi"))

if sayi %2 == 0:
	print("Sayı çiftir")
	print(sayi*4)
else:
	print("Sayı tektir")
	print(sayi+9)
"""
# Kullanıcıdan alınan sayının aralığını belirleyiniz
#  0-10  11-20

# sayi = int(input("Sayi"))
#
# if 0 < sayi  and sayi < 11: # 0-10
# 	print("0-10")
# elif 10 < sayi and sayi < 21:
# 	print("10-20")
# else:
# 	print("Aralık tanımlı değil")


# Klavyeden girilen 4 sayıdan tek ve çift olanları ayrı
# ayrı toplayarak ekrana yazdırınız..
"""
tek_toplam = 0
cift_toplam = 0

s1 = int(input("Birinci sayıyı giriniz:  "))
if s1 % 2 == 0:
    # cift_toplam = cift_toplam +s1
    cift_toplam += s1
else:
    tek_toplam += s1

s2 = int(input("İkinci sayıyı giriniz:  "))
if s2 % 2 == 0:
    # cift_toplam = cift_toplam +s1
    cift_toplam += s2
else:
    tek_toplam += s2

s3 = int(input("Üçüncü sayıyı giriniz:  "))
if s3 % 2 == 0:
    # cift_toplam = cift_toplam +s1
    cift_toplam += s3
else:
    tek_toplam += s3

s4 = int(input("Dördüncü sayıyı giriniz:  "))
if s4 % 2 == 0:
    # cift_toplam = cift_toplam +s1
    cift_toplam += s4
else:
    tek_toplam += s4

print(f"Çift sayıların toplamı : {cift_toplam}")
print(f"Tek sayıların toplamı: {tek_toplam}")
"""
"""
## Kullanıcıdan vize final not girilmesi istensin
# not aralığı 0 ile 100 arasında olmalıdır.
## vize ve finalin ortalaması alınsın.
## 0-44 : Kaldınız
## 45-69: Geçtiniz
##70-84: İyi
## 85-100: Pekiyi

vize_not = float(input("Vize Notunuzu Giriniz: "))
final_not = float(input("Final Notunuzu Giriniz: "))

if (0 <= vize_not <= 100) and (0 <= final_not <= 100):

    ortalama = (vize_not * 0.4) + (final_not * 0.6)
    print(ortalama)

    if 0 <= ortalama < 45:
        print("Kaldınız !")
    elif 45 <= ortalama < 70:
        print("Geçtiniz")
    elif 70 <= ortalama < 85:
        print("İyi")
    else:
        print("Pekiyi")

else:
    print("Vize ve Final Notları 0-100 arasında olmalıdır")
"""

# Kullanıcıdan isim,yaş,maaş ve çocuk sayısı alalım

"""
    Eğer kullanıcının yaşı 45'in altındaysa;
        çocuk sayısına bakılacak ve çocuk sayısı 3^ten az ise çocuk başına 250₺,
         değilse çocuk başına 200₺ maaşa eklenecek
    Eğer kullanıcının yaşı 45 ve üzerinde ise:
        çocuk başına para verilmeyecek direk 500₺ maaşa eklenecek.
    Ekrana "Nesrin Yılmaz Maaşınız: 4000₺" yazılacak.
"""
"""

isim = input("İsminiz: ")
yas = int(input("Yaşınız: "))
maas = float(input("Maaşınız: "))
cocuk_sayisi = int(input("Çocuk sayısı"))

if 45 > yas > 18:

    if 3 > cocuk_sayisi >= 0:
        maas += cocuk_sayisi * 250
        # maas = maas+(cocuk_sayisi * 250)
    else:
        maas += cocuk_sayisi * 200
elif 45 <= yas < 66:
    maas += 500

else:
    print("Belirlenen yaş aralığında değilsiniz...")

print(f"{isim} çalışanının maaşı : {maas}")
"""

# Kullanıcı Gİriş Paneli Tasarlayınız.

"""
    Kullanıcıadı/Email ve şifre ile giriş sağlanacak
        Giriş Başarılı ise ekrana "Giriş Başarılı" yazsın
        Değilse
            Kullanıcıya kayıt olmak ister misiniz?
                Hayır ise PEKİ!!!
                Evet Kullanıcıadı, ad, soyad,email,şifre ve şifre tekrarı alarak kayıt yapalım.
                    şifre ve şifretekrarın aynı olması
"""
"""
kullanici_adi = "mehmetnuri"
email = "info@mehmetnuri.net"
sifre = "1234"

print("----------------------------GİRİŞ PANELİ----------------------------")
user_name = input("Kullanıcı Adınız veya Email Adresiniz: ")
password = input("Şifreniz: ")

if (user_name == kullanici_adi or user_name == email) and (password == sifre):
    print("Giriş başarılı")
else:
    cevap = input("Giriş başarısız. Kayıt olmak ister misiniz?(E/H)").upper()  # e ->E

    if cevap == "E":
        kullanici_adi = input("Kullanıcı adınız: ")
        email = input("Email adresiniz")
        sifre = input("Şifreniz")
        sifre2 = input("Şifreniz tekrar: ")

        if sifre2 == sifre:
            print("Hoş geldiniz")
        else:
            print("Şifreler birbirini tutmuyor")
    elif cevap == "H":
        print("Peki")

    else:
        print("Hatalı seçim")
"""
# Girilen 3 sayıyı büyüklük olarak karşılaştıran python uygulamasını yapınız.

a = int(input("1. sayı"))
b = int(input("2. sayı"))
c = int(input("3. sayı"))

if a > b and a > c:
    print(f"En büyük sayı: {a}")
elif b > a and b > c:
    print(f"En büyük sayı: {b}")
else:
    print(f"En büyük sayı: {c}")
