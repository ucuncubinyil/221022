"""
Marka
Model
Fiyat
İşlemci
Ram
Ram Tipi
Harddisk
Harddisk Tipi
Anakart
Güç
Enerji Sınıfı
"""


class Bilgisayar:

    def __init__(self):
        self.__marka = str()
        self.__model = str()
        self.__fiyat = float()
        self.__islemci = str()
        self.__ram = int()
        self.__ram_tipi = str()
        self.__hard_disk = float()
        self.__hard_disk_tipi = str()
        self.__ana_kart = str()
        self.__guc = str()
        self.__enerji_sinifi = str()

    @property
    def marka(self):
        return self.__marka

    @marka.setter
    def marka(self, value: str):
        try:
            self.__marka = value
        except ValueError:
            print("Marka sadece String tipinde olmalıdır")

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value: str):
        try:
            self.__model = value
        except ValueError:
            print("Model sadece String tipinde olmalıdır")

    @property
    def fiyat(self):
        return self.__fiyat

    @fiyat.setter
    def fiyat(self, value: float):
        try:
            self.__fiyat = value
        except ValueError:
            print("Fiyat sadece Float tipinde olmalıdır")

    @property
    def islemci(self):
        return self.__islemci

    @islemci.setter
    def islemci(self, value: str):
        try:
            self.__islemci = value
        except ValueError:
            print("İşlemci sadece String tipinde olmalıdır")

    @property
    def ram(self):
        return self.__ram

    @ram.setter
    def ram(self, value: int):
        try:
            self.__ram = value
        except ValueError:
            print("Ram kapasitesi sadece Integer tipinde olmalıdır")

    @property
    def ram_tipi(self):
        return self.__ram_tipi

    @ram_tipi.setter
    def ram_tipi(self, value: str):
        try:
            self.__ram_tipi = value
        except ValueError:
            print("Ram tipi sadece String olmalıdır")

    @property
    def hard_disk(self):
        return self.__hard_disk

    @hard_disk.setter
    def hard_disk(self, value: float):
        try:
            self.__hard_disk = value
        except ValueError:
            print("Harddisk Boyutu sadece Float tipinde olmalıdır")

    @property
    def hard_disk_tipi(self):
        return self.__hard_disk_tipi

    @hard_disk_tipi.setter
    def hard_disk_tipi(self, value: str):
        try:
            self.__hard_disk_tipi = value
        except ValueError:
            print("Harddisk tipi String tipinde olmak zorundadır")

    @property
    def ana_kart(self):
        return self.__ana_kart

    @ana_kart.setter
    def ana_kart(self, value: str):
        try:
            self.__ana_kart = value
        except ValueError:
            print("Anakart String tipinde olmalıdır")

    @property
    def guc(self):
        return self.__guc

    @guc.setter
    def guc(self, value: str):
        try:
            self.__guc = value
        except ValueError:
            print("Güç sadece String tipinde olmalıdır")

    @property
    def enerji_sinifi(self):
        return self.__enerji_sinifi

    @enerji_sinifi.setter
    def enerji_sinifi(self, value: str):
        try:
            self.__enerji_sinifi = value
        except ValueError:
            print("Enerji Sınıfı sadece String tipinde olmaldır")
