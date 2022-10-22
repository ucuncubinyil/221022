##### DEĞİŞKEN (VARIABLE) ###

""""
DEĞİŞKENİN ADİ  = DEĞERİ -> SAYI YAZI KARAKTER MANTIKSAL


# alt tire _ yazılım dillerinde kabul göre tek özel karaktertir.
# isimlendirme kuralları (case-sensitive)
# yanlışlar: 5Sayi, Sayi-5, ?Sayi, ad soyad, ad-soyad, Sayi?, Sayi!
# doğrular:  sayi5, Sayi_5, _Sayi, adsoyad,  ad_soyad, Sayi_

# değişken tanımalama
# değişken adı = değer
"""

#
# ad = "Mehmet Nuri"  #  -> String veri tipi
# yas =  15           # ->integer ( tam sayı )
# maas = 36562.65     #  ->float ( noktalı sayı)
#
# print(ad)
# print(yas)
# print(maas)

## YAZIM STANDARTLARI
# camelCaseStandartı
# snake_case_standartı (Python un resmi standartı)
# PascalCaseStandartı (C# dili için geçerli)
# FULLCASESTANDARTI  FULL_CASE_STANDART
# kebap-case-standartı

# # TAM SAYI (INT)

# - sonsuz  -> + sonsuz


"""
sayi1 = 15
print( sayi1 )
sayi2 = 9999999999999999999999999
print( sayi2 )

print( type( sayi2 ) )  # bir değişkenin tipini öğrenme

# # Noktalı Sayılar (Float)
sayi3 = 25.6
print( sayi3 )
print( type( sayi3 ) )

# # Metinsel Veri Tipi (STRING)
gelistirici = "Hasan Durmaz"
yonetici = "Mehmet Nuri ÖZTÜRK"
print( gelistirici )
print( yonetici )
print( type( gelistirici ) )
print( type( yonetici ) )

# # Mantıksal Veri Tipi (Boolean ) True False
arabasi_var_mi = True  # EVET 1
ucagi_var_mi = False  # HAYIR 0
elma = 12

### '=' değer atama operatörümüzdür.

"""

# int ve float örneği
# bir öğrencinin iki notunun ortalamasını ekrana yazdıran program.

"""
not1 = 63
not2 = 90
sonuc =  (not1+not2)/2
print(sonuc) # sonuc float
print(type(sonuc))
print( int(sonuc)  ) # tip dönüşümü
print(type( int(sonuc) ))
"""

"""
# Birden fazla değişken tanımlama
c1 = c2 = c3 = 15  # 1. yöntem
print( c1 )
print( c2 )
print( c3 )

d1, d2, d3 = 12, 32, 44  # 2. yötem
print( d1 )
print( d2 )
print( d3 )

a1, a2 = a1, a3 = 88, 66 # 3. yöntem
print(a1)
print(a2)
print(a3)

print("C1 in değeri ", c1," asdasdd ", c2)
print(f"C1 in değeri {c1} C2 nin değeri {c2}") # tercih edilen
print("C1 in değeri {0} C2 nin değeri {1}".format(c1,c2))

adi, soyadi, maasi, araba_durumu = "Mehmet Nuri", "Öztürk", 36565.30, True
print(f"Ad: {adi} Soyad: {soyadi} Maaş: {maasi} Arabası Var Mı?: {araba_durumu}")
"""

"""
x1 = 5 # ram adresi bahceşehir
x2 = 7 # ram adresi kadıkoy
print( "Önceki" )
print( x1, x2 )

x2 = x1 # ram adresi kadkoy olan adresi bahcesehir olarak değiş
x1 = x2 # ram adresi bahçesehir olan adresi bahcesehir olarak değiş
print( "Sonraki" )
print( x1, x2 )
"""

##### KAÇIŞ KARAKTERLERİ #####
# \n new line
# \t TAB

# Mehmet"in adresi neresi ?
print("Mehmet\"in adresi neresi ?")
print("Mehmet'in adresi neresi ?")
print("Mehmet\nNuri\nÖztürk")
print("Mehmet\tNuri\tÖztürk")

adi, soyadi, maasi, araba_durumu = "Mehmet Nuri", "Öztürk", 36565.30, True

bilgiler = f"""
AD          :{adi}
SOYAD       :{soyadi}
MAAŞ        :{maasi} ₺
ARABA       :{araba_durumu}
"""
print(bilgiler)
