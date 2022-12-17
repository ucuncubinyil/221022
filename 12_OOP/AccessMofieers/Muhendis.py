from Calisan import Calisan


class Muhendis(Calisan):

    def __init__(self):
        self.ad = "Ahmet"
        self.soyad = "Mehmet"

    def bilgi_ver(self):
        print(f"Ad: {self.ad}, Soyad: {self.soyad}")

    def yaz(self):
        self._bilgi()
