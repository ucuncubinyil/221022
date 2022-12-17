class Calisan:
    def __init__(self):
        self.ad = "Mehmet Nuri"
        self.soyad = "ÖZTÜRK"

    def _bilgi(self): #protected
        print(f"AD: {self.ad}, SOYAD: {self.soyad}")

    def ekrana_yaz(self):
        self._bilgi()
