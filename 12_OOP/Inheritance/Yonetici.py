from Calisan import Calisan


class Yonetici(Calisan):

#Override
    def __init__(self, isim:str, maas:int, departman:str, kisi_sayisi: int):
        print("Yönetici Sınıfı init fonksiyonu")
        self.isim = isim
        self.maas = maas
        self.departman = departman
        self.kisi_sayisi = kisi_sayisi

    def zam_yap(self, zam_miktari):
        self.maas += zam_miktari

    def bilgi_goster(self): # Ovveride (İptal-Revize)
        super().bilgi_goster() # Super anahtar kelimesi miras aldığımız sınıfı temsil eder
        print("Yönetici Bilgileri")
        print(f"İsim : {self.isim} Maaş: {self.maas},"
              f" Departman: {self.departman},"
              f" Kişi Sayısı: {self.kisi_sayisi}")
