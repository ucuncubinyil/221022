class BeyazEsya:

    def __init__(self):
        self.enerji = str()
        self.marka = str()
        self.fiyat = 0.0
        self.model = str()

    def  bilgi_ver(self):
        print(f"Marka: {self.marka}, Model: {self.model},"
              f" Enerji {self.enerji} Fiyat: {self.fiyat}")
