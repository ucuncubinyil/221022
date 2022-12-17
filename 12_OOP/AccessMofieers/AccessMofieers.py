# ACCESS MODIFIERS : public, private , protected

# public:  Yazılım dillerinde genel erişime
# açık anlamına gelir. Herhangi bir erişim
# belirleyicisi verilmez ise default olarak
# public verilir.
"""
from Muhendis import Muhendis

ahmet = Muhendis()
ahmet.ad = "Ahmet"
ahmet.soyad = "Turan"

ahmet.bilgi_ver()
"""

# private: Yazılım dillerinde saddece
# tanımlandığı sınıf içerisinden erişilebilir
# anlamına gelir. '__' iki altçizgi öne koyularak
# tanımlanır
"""
from Uye import Uye

a = Uye()
a.bilgi()
"""
"""
from TCKontrol import TCKontrol
from  Utils import Utils

a = TCKontrol("10361780220")
print(a)

b = Utils.TCKontrol("10361780220")

print(b)
"""

# protected:  Sınıf içinde public ama sınıf dışında sadece miras alınan
# (inheritance) sınfılardan erişilebilir. '_' tek alt çizgi ile tanımlanır.

from  Muhendis import Muhendis

a =  Muhendis()
a.ekrana_yaz()