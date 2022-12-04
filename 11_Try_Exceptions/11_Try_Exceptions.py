#### TRY CATCH - TRY EXCEPT ####

"""
try:
    #hata kontrolü yapılacak kod blogu
except:
    # Hata oluştuğunda yapılacak işlem
"""
"""
try:
    sayi = int(input("Lütfen bir sayı giriniz:"))
except ValueError:
    print("Lütfen sadece sayı giriniz !!")
except:
    print("Bir hata oluştu")
"""
"""
try:
    sayi1 = int(input("Birinci sayı"))
    sayi2 = int(input("İkinci sayı"))
    sonuc = sayi1/sayi2
except ValueError:
    print("Lütfen sayı olarak giriniz")
except ZeroDivisionError:
    print("0 a bölünme hatası!!")
except IndexError:
    print("Tanımlı olmayan Index")
except MemoryError:
    print("Bilgisayar belleği yetersiz!!")
except ImportError:
    print("Import edilen dosyaya erişilemiyor!!!")
except OverflowError:
    print("Değişkenin kapasitesi aşıldı")
except:
    print("Geri kalan bütün durumlar için çalışır...")
"""
"""
while True:
    try:
        sayi = int(input("Sayı gir"))
        print(sayi)
        break
    except ValueError:
        print("Lütfen sayı giriniz")
        continue
"""

# HATA FIRLATMA  raise()
"""
try:
    not1 = int(input("Not1"))

    if not1 < 0 or not1 > 100:
        raise Exception  # Manuel hatayı fırlatıyorum
except ValueError:
    print("Lütfen sadece sayı giriniz")
except Exception:
    print("Not aralığı 0-100 arasında olmalıdır")
"""
"""
#ASSERT idaa edilen
kontrol_eposta = "info@mehmetnuri.net"
try:
    eposta = input("Mail adresiniz")
    assert eposta == kontrol_eposta
    print("Mail adresi eşit")
except AssertionError:
    print("Mail adresi sistemdeki kayıtlı maile eşit değil")
"""

"""
# Kullanıcıdan 2 sayı 1 işlem al  işlemler daha önce tanımlanmış metodlar olsun
# işlemler +-*/ den biri değil ise assert fırlatsın
# ValueErorr olduğunda tekrar veri istesin
# ZeroDivision için tekrar veri istesin

def topla(param1: int, param2: int):
    return param1 + param2


def cikar(param1: int, param2: int):
    return param1 - param2


def carp(param1: int, param2: int):
    return param1 * param2


def bol(param1: int, param2: int):
    return param1 / param2


def islem_yap():
    param1 = int(input("Sayı 1"))
    param2 = int(input("Sayı 2"))

    islem = input("Toplama(+), Çıkarma(-), Çarpma(*), Bölme(/)")

    assert islem == "+" or islem == "-" or islem == "*" or islem == "/"

    if islem == "+":
        print(topla(param1, param2))
    elif islem == "-":
        print(cikar(param1, param2))
    elif islem == "*":
        print(carp(param1, param2))
    elif islem == "/":
        print(bol(param1, param2))


while True:
    try:
        islem_yap()
        break
    except ValueError:
        print("Sadece sayı girişi yapın")
        continue
    except ZeroDivisionError:
        print("Hiç bir sayı sıfıra bölünemez")
        continue
    except AssertionError:
        print("Hatalı işlem seçimi")
        continue
    except Exception:
        print("Bir hata oluştu")
"""
"""
a = [1, 2, 3]

try:
    a.get()
except BaseException as eror:
    print(f"Hata oluştu {eror}")
"""
"""
liste= [1,5,9,11]

try:
    print(liste[2])
    print(liste.get())
except BaseException as hata:
    print(f"{type(hata).__name__} ") # Hatanın hangi exception olduğunu bulur
"""

# Finally
"""
f = None  # Tipi olmayan boş bir değer 
try:
    f = open("test2.txt")
except FileNotFoundError:
    print("Dosya bulunamadı")

except:
    print("Dosya açılamadı")

finally:
    # Hata olsa da olmasada çalışır
    if f is not None:
        f.close()
    print("Ben her şekilde çalışırım")

print("Program devam ediyor")
"""
"""
from OzelHata import OzelHata

try:
    x = 1
    raise OzelHata
except OzelHata:
    print("Özel hata oluştu")
except:
    print("Bir hata oluştu")
else:
    print("Hata oluşmadı")
finally:
    print("Ben her şekilde çalışırım")
"""

from UniversiteNotException import UniversiteNotException
from  datetime import datetime

try:
    not1 = int(input("Not1"))

    if not1 < 0 or not1 > 100:
        raise UniversiteNotException  # Manuel hatayı fırlatıyorum

except UniversiteNotException:
    print(f"Not aralığı 0-100 olmalıdır. Hata Tarihi ve saati {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ")
except ValueError:
    print("Lütfen sadece sayı giriniz")
except Exception:
    print("Bir hata oluştu")
else:
    print("Hata oluşmadı")
finally:
    print("Ben yine çalıştım")
