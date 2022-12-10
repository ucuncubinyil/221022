class Ogrenci():
    ad = ""
    soyad = str()
    tc = 0
    dogum_tarihi = str()

    # self=> nesneyi temsil ediyor ve bu methodun nesne üzerinden kullanılabileceğini gösteriyor.
    def bilgi_yaz(self):
        print(f"AD: {self.ad} Soyad: {self.soyad} "
              f"Tc: {self.tc}, "
              f"DogumTarihi {self.dogum_tarihi}"
              )