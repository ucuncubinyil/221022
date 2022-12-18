class BeyazEsya:
    def __init__(self):
        self.__marka = str()
        self.__enerji = str()
        self.__fiyat = float()
        self.__model = str()

    @property
    def marka(self):
        return self.__marka

    @marka.setter
    def marka(self, value: str):
        self.__marka = value

    @property
    def enerji(self):
        return self.__enerji

    @enerji.setter
    def enerji(self, value: str):
        self.__enerji = value

    @property
    def fiyat(self):
        return self.__fiyat

    @fiyat.setter
    def fiyat(self, value: float):
        self.__fiyat = value


    @property
    def model(self):
        return  self.__model

    @model.setter
    def model(self, value: str):
        self.__model = value
