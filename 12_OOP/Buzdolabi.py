class BuzDolabi:
    # CONSTRUCTOR METHOD
    """
    Kurucu method: class'tan instance alındığında otomatik olarak çalışan bir methoddur.
    __init__ ismiyle tanımlanır.
    Eğer kurucu metodu tanımlamazsak görünmez olrak
    default da def __init__(self): şeklinde kendisi otomatik tanımlar.
    """

    def __init__(self):
        self.marka = str()
        self.model = str()
        self.fiyat = 0.0

    def bilgi_yaz(self):
        print(f"Marka:{self.marka}, Model:{self.model}, Fiyat:{self.fiyat}")

    @staticmethod  # static metotları hem class hem de nesne üzerinden direk kullanabilirsiniz.
    def fiyat_hesapla(fiyat: float, faiz_orani: float):
        print(f"Fark {fiyat * (faiz_orani * 0.25)}")
        print(f"Toplam Ödenecek Olan Fiyat: {(fiyat + (fiyat * (faiz_orani * 0.25)))}")
