"""
from BuzDolabi import BuzDolabi

arcelik = BuzDolabi()

arcelik.marka = "Arçelik"
arcelik.model = "CXS"
arcelik.fiyat = 15000.30
arcelik.enerji = "A++"
arcelik.hacim = 18.00
arcelik.kapak_sayisi = 2
arcelik.wifi = True


print(arcelik.__repr__())
"""

# print(f"""
# Marka:          {arcelik.marka}
# Model:          {arcelik.model}
# Fiyat:          {arcelik.fiyat}
# Enerji Sınıfı:  {arcelik.enerji}
# Hacim:          {arcelik.hacim}
# Kapak Sayısı:   {arcelik.kapak_sayisi}
# Wifi:           {arcelik.wifi_str}
# """)

# sihirli metodlar -> magicmethods
# class PrintList(object):
#
#     def __init__(self, nesne):
#         self.my_list = nesne
#
#     def __repr__(self):
#         return str(self.my_list)
#
#
# printList = PrintList(["a", "b", "c"])
#
# print(printList.__repr__())

"""
liste1 = ["a","b","c"]
liste2 = ["d","e","f"]

print("Liste ilk hal")
print(liste1+liste2)

print("Listeleri __add__ metodu ile ekle")

print(liste1.__add__(liste2))

"""

"""
class Musteri:

    def __new__(cls):
        print("New metodu çalıştı")
        inst = object.__new__(cls)
        return inst

    def __init__(self):
        print("Constructure metodu çalıştı")

        self.ad = "Mehmet"
        self.bakiye = 10000

    def __str__(self):  # Nesneyi yazdırdığımızda ekrana çıkacak olan değeri verir
        return f"Ad: {self.ad} Bakiye:{self.bakiye}"


a = Musteri()
print(a.ad)

print(a)

"""

"""
class Distance:

    def __init__(self, x=None, y=None):
        self.ft = x
        self.inc = y

    def __ge__(self, x):  # >= grand equal

        value1 = self.ft * 12 + self.inc
        value2 = x.ft * 12 + x.inc

        if value1 >= value2:
            return True
        else:
            return False


d1 = Distance(2, 1)
d2 = Distance(2, 1)

print(d1>=d2)
"""
"""
from BuzDolabi import BuzDolabi

arcelik = BuzDolabi()

arcelik.marka = "Arçelik"
arcelik.model = "CXS"
arcelik.fiyat = 15000.30
arcelik.enerji = "A++"
arcelik.hacim = 18.00
arcelik.kapak_sayisi = 2
arcelik.wifi = True


print(arcelik)

"""

from DizUstu import DizUstu

x_laptop = DizUstu()
x_laptop.marka = input("Dizüstü Bilgisayarınızın Markası: ")
x_laptop.model = input("Dizüstü Bilgisayarınızın Modeli")
x_laptop.fiyat = input("Dizüstü Bilgisayarınızın Fiyatı: ")
x_laptop.islemci = input("Dizüstü Bilgisayarınızın İşlemcisi: ")
x_laptop.ram = input("Dizüstü Bilgisayarınızın Ram Kapasitesi: ")
x_laptop.ram_tipi = input("Dizüstü Bilgisayarınızın Ram Tipi: ")
x_laptop.hard_disk = input("Dizüstü Bilgisayarınızın Harddisk Kapasitesi: ")
x_laptop.hard_disk_tipi = input("Dizüstü Bilgisayarınızın Harddisk Tipi: ")
x_laptop.ana_kart = input("Dizüstü Bilgisayarınızın Anakartı: ")
x_laptop.guc = input("Dizüstü Bilgisayarınızın Gücü")
x_laptop.enerji_sinifi = input("Dizüstü Bilgisayarınızın Enerji Sınıfı: ")
x_laptop.batarya = float(input("Dizüstü Bilgisayarınızın Batarya Kapasitesi: "))
x_laptop.hoparlor = input("Dizüstü Bilgisayarınızın Hoparlörü: ")
x_laptop.web_cam = input("Dizüstü Bilgisayarınızın Web Cam Var Mı?")
x_laptop.ekran_karti = input("Dizüstü Bilgisayarınızın Ekran Kartı Var Mı?")

print(x_laptop)
