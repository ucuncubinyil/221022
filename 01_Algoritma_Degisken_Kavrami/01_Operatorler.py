# OPERATÖRLER

# Karşılaştırma Operatörleri

# Karşılaştırma operatörleri sadece mantıksal cevap döner (True-False)

# 1. Eşit mi ?          ==
# 2. Eşit değil mi ?    !=
# 4. Büyüktür            >
# 5. Küçüktür            <
# 6. Büyük Eşit          >=
# 7. Küçük Eşit          <=
"""
a = 5
b = 6

print( a == b )
print( a != b )
print( b > a )
print( a < b )
print( b >= a )
print( a <= b )
"""
# Aritmatik Operatörler
"""
    +,-,* :toplama,çıkarma,çarpma
    /     :ondalıklı bölme (10/4=2.5)
    //    :bölümün tamsayı kısmını verir (10//4=2)
    %     : Moda alma


"""
"""
c = 5
d = 3

print( c + d )  # Toplama işlemi
print( c - d )  # Çıkarma işlemi
print( c * d )  # Çarpma İşlemi
print( c / d )  # Bölme İşlemi
print( c // d )  # Tam Bölme İşlemi
print( c % d )  # Mod Alma İşlemi

# Tek Çift Kontrolü
cift_mi = 23
kalan =  cift_mi % 2
cevap = kalan == 0 # Eşitlik operatörü kullanıldı
print(cevap)
"""
# Mantıksal Operatörler AND (VE)
# 00 = 0        => FF = F
# 01 = 0        => FT = F
# 10 = 0        => TF = F
# 11 = 1        => TT =T

"""
kullanici_adi =  "ali"
sifre =  "15"

kullanici =  input("Kullanıcı Adınız : ")
kullanici_sifre =  input("Şifreniz")

kontrol =  kullanici_adi == kullanici and sifre == kullanici_sifre
print(kontrol)

"""

# MANTIKSAL VEYA (OR) (VEYA)# 00 = 0
#  01 = 1       FT      => T
#  10 = 1       TF      => T
#  11 = 1       TT      => T

sayi = 36

kontrol = sayi > 36 or sayi >= 36
print( kontrol )

kontrol = sayi > 101 or sayi < 1
print( kontrol )

# NOT Anahtar Kelimesi

sayi = 21
sayi = not sayi  # sayi sayi değil mi
sayi = sayi != sayi
print( sayi )

# IS Anahtar Kelimesi

sayi = 23
sayi2 = 23

kontrol = sayi is sayi2
print( kontrol )
kontrol = sayi == sayi2,
