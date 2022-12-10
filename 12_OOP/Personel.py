# SORU:
"""
Personel isimli bir class tanımlayın
Nesne Nitelikleri: ad,soyad,tc,telefon,adres,maas
__init__ fonksiyonu ile kullanıcıdan bu özellikler sorularak doldurulsun
Kaydet() isimli method Personel.txt adında bir dosyaya kaydetsin
Bir tane sınıf üzerinden erişebilir Listele() adında bir method tanılayın dosyadaki verileri okuma işlemi gerçekleştirsin
"""

import os


class Personel():

    def __init__(self):
        while True:
            try:
                self.ad = input("Personel Adı: ")
                self.soyad = input("Personel Soyadı: ")
                self.tc = input("Personel T.C. Kimlik Numarası: ")
                self.telefon = input("Personel Telefon Numarası: ")
                self.adres = input("Personel Adresi: ")
                self.maas = float(input("Personel Maaşı"))
                break
            except ValueError:
                print("Lütfen veri tipini doğru giriniz !")
                continue

    def kaydet(self):
        dosya = None
        try:
            dizin = "C:\\TEST\\"
            if not os.path.exists(dizin):
                os.mkdir(dizin)
            kayitli_dosya = dizin + "Personel.txt"
            dosya = open(kayitli_dosya, mode="a+", encoding="utf-8")
            dosya.write(f"Ad: {self.ad}\t\tSoyad: {self.soyad}\t\t"
                        f"T.C.: {self.tc}\t\tAdres: {self.adres}\t\t"
                        f"Maaş: {self.maas}\n")

        except Exception as error:
            print("Dosya kayıt edilirken hata oluştu")
            print(f"Hata Sınıfı: {type(error).__name__} ")
        finally:
            if dosya is not None:
                dosya.close()

    @classmethod
    def listele(cls):
        dosya = None
        try:
            dosya = open("C:\\TEST\\Personel.txt", mode="r", encoding="utf-8")
            satirlar = dosya.readlines()
            for satir in satirlar:
                print(satir)
        except FileNotFoundError:
            print("Dosya bulunamadı !")
        except Exception as error:
            print("Dosya okunurken  hata oluştu")
            print(f"Hata Sınıfı: {type(error).__name__} ")
        finally:
            if dosya is not None:
                dosya.close()
