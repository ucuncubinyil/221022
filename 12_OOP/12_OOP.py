###################################################################
############### OOP: Object Oriented Programming ##################
################ Nesneli Yöneliklik Programlama ###################
###################################################################

'''
OOP: büyük projeler yazılacağı zamanlarda, proje temelini oluşturma aşamasından
başlayarak analiz sentez kodlama sınama ve onarım gibi yaşam döngüsü adımlarında daimi olarak
uyugulanması ve takip edilmesi gerekli bir yapıdır.
En büyük kazancı proje temelini oluşturan yapıların bir bütün halinde(object)
tutulması ve yapınların özelliklerinin(field) alt başlıklar halinde yapıya özel olmasını sağlar.
Kayıt güncelleme,silme veya okuma işlemlerinde object (nesne) sayesinde veri bütünlüğü sağlanmış
ve tek bir işlemle manipüle edeilmiş olur.

-- OOP 4 Temeli Vardır:
    1-Inheritance(Kalıtım)
    2-Encapsulation(Kapsülleme)
    3-Polymorphism(Çok Biçimlilik)
    4-Abstraction(Soyutlama)

'''

## Bir okulunuz olduğunu ve öğrenci kaydı yapılacağını düşünelim.
# Her öğrencinin ad,soyad,tc,dogumtarihi gibi bilgileri kayıt edilecektir.

"""
Ad =  "Mehmet Nuri"
sOyad =  "Öztürk"
tc = 1234
dogum_tarihi =  "20.11.1993"


ad = "Ferdi"
soyad =  "Aslan"
tc = 46534
dogum_tarihi = "11.11.2011"

"""
"""
from Ogrenci import Ogrenci

## class'tan örnek alma işlemine instance(örneklem) denir. class örneğine OBJECT(nesne) denir.
ogrenci1 = Ogrenci()
ogrenci1.ad = "Ahmet"
ogrenci1.soyad = "Öztürk"
ogrenci1.dogum_tarihi = "20.11.1555"
ogrenci1.tc = 1234

print(ogrenci1.ad)

ogrenci1.bilgi_yaz()

ogrenci2 = Ogrenci()
ogrenci2.ad = input("Öğrenci Adı")
ogrenci2.soyad = input("Öğrenci Soyad")
ogrenci2.tc = int(input("TC"))
ogrenci2.dogum_tarihi = input("Doğum Tarihi")

ogrenci2.bilgi_yaz()

"""
"""
# ****** Class Object yapısında 3 tür method tanımlanır.
# 1.selfmethod (Nesne Method) : Nesne üzerinde erişilen ve kullanılan methodlar.
# 2.classmethod (Sınıf Method) : Sınıf üzerinde erişilen ve kullanılan methodlar.
# 3.staticmethod (Statik Method): # Sınıf veya Nesne üzerinde erişilen ve kullanılan methodlar.



"""
"""
from Uyeler import Uyeler

x = Uyeler()
x.name = "Ahmet"
x.last_name = "Turan"
x.user_name = "ahmet_turan"
x.phone = "5555555555"
x.password = "123456"

print(x.user_name)

info = x.info()

for k, v in info.items():
    print(k, v)


liste  = list()
liste.append(x)

print(Uyeler.ara("ahmet_turan", liste))
aranan_dic = Uyeler.ara("ahmet_turan", liste)
print(aranan_dic)
"""
"""

from Insan import Insan


a = Insan()
a.ad =  input("Bebeğin Adı")
a.soyad =  input("Bebeğin Soyadı")

Insan.konus(a)
a.konusma()



bebek_listesi = list()

while True:
    Insan.kaydet(bebek_listesi)
    cevap = input("Bebek eklemeye devam etmek istiyor musunuz ?(E/H) ").upper()

    if cevap == "E":
        continue
    elif cevap == "H":
        Insan.yazdir(bebek_listesi)
        break
    else:
        print("Hatalı seçim !")
        continue
        


from Buzdolabi import BuzDolabi

arcelik = BuzDolabi()
arcelik.marka = "ARÇELİK"
arcelik.model = "XZCZDA"
arcelik.fiyat = 15000.00

arcelik.bilgi_yaz()

arcelik.fiyat_hesapla(arcelik.fiyat, 2)

BuzDolabi.fiyat_hesapla(arcelik.fiyat, 2)
"""

"""
from Matematik import Matematik

topla = Matematik.topla(1, 3)
print(topla)
cikar = Matematik.cikar(5, 2)
print(cikar)

bolme = Matematik.bol(1, 3)
print(bolme)

bolme2 = Matematik.bol(15, 5, True)
print(bolme2)

bolme3 = Matematik.bol(15, 0, True)
print(bolme3)

carpma = Matematik.carp(1, 0)
print(carpma)

carpma2 = Matematik.carp(1, 9)
print(carpma2)

"""

from Personel import Personel

personel1 = Personel()

personel1.kaydet()

Personel.listele()