############ KAPSULLEME (Encapsulation) ############

# getter methodları private özelliklerin değerlerimi okumamızı sağlar. readonly
# setter methodları private özelliklere değer atamamızı sağlar.
"""
class Kapsul():

    def __init__(self):
        self.__gizli_ozellik = "mehmet"
        self.__tc = 0

    def get_tc(self):
        return self.__tc

    def set_tc(self, deger):
        self.__tc = deger


a = Kapsul()
a.set_tc("102")
print(a.get_tc())
"""

"""
### PROPERTY
class Personel:

    def __init__(self, isim):
        self.__isim = isim

    def get_isim(self):
        return self.__isim

    def set_isim(self, deger):
        self.__isim = deger

    ad = property(get_isim, set_isim)  # getter #setter


p = Personel("Ahmet")
p.ad = "ALi"  # p.set_isim("Ali")
print(p.ad)  # p.get_isim()
"""
"""
from  Universite import Universite

a = Universite()
a.vize = 101

a.final = 102

a.ortalama()
"""
### Bir banka müşteri kayıt sistemi oluşturulurken kayıt esnasında ad,soyad,tc(11 haneli) ve
# Iban(tr+12) bilgileri alınıyor.
# Gerekli kontrolleri sağlayarak müşteri kayıt platformunu oluşturunuz.

from  Banka import Banka


a =  Banka()

a.tc = "103a61780220"
a.iban = "tr123456789123"

a.bilgi_yaz()
print(a.tc)
print(a.iban)
