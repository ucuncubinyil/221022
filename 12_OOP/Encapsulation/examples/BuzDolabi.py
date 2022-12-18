from BeyazEsya import BeyazEsya


class BuzDolabi(BeyazEsya):

    def __init__(self):
        self.__hacim = float()
        self.__kapak_sayisi = int()
        self.__wifi = bool()
        self._wifi_str = str()

    @property
    def hacim(self):
        return self.__hacim

    @hacim.setter
    def hacim(self, value: float):
        self.__hacim = value

    @property
    def kapak_sayisi(self):
        return self.__kapak_sayisi

    @kapak_sayisi.setter
    def kapak_sayisi(self, value: int):
        self.__kapak_sayisi = value

    @property
    def wifi(self):
        return self.__wifi

    @wifi.setter
    def wifi(self, value: bool):
        self.__wifi = value
        self._wifi_str = value

    @property
    def wifi_str(self):
        if self.__wifi:
            self._wifi_str = "VAR"
            return self._wifi_str
        else:
            self._wifi_str = "YOK"
            return self._wifi_str

    @wifi_str.setter
    def wifi_str(self, value: bool):
        self.__wifi = value
        if value:
            self._wifi_str = "VAR"
        else:
            self._wifi_str = "YOK"

    def __repr__(self):

        info = dict()

        info["maka"] = self.marka
        info["model"] = self.model
        return info

    def __str__(self):
        return  f"""
Marka               :{self.marka}
Model               :{self.model}
Enerji Sınıfı       :{self.enerji}
Fiyat               :{self.fiyat}
Kapak Sayısı        :{self.kapak_sayisi}
Hacim               :{self.hacim}
Wi-Fi               :{self.wifi_str}
        """
