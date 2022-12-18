from Bilgisayar import Bilgisayar


class DizUstu(Bilgisayar):

    def __init__(self):
        self.__batarya = float()
        self.__hoparlor = str()
        self.__web_cam = bool()
        self.__ekran_karti = bool()
        self.__web_cam_str = str()
        self.__ekran_karti_str = str()

    @property
    def batarya(self):
        return self.__batarya

    @batarya.setter
    def batarya(self, value: float):
        try:
            self.__batarya = value
        except ValueError:
            print("Batarya kapasitesi sadece Float tipinde olmalıdır")

    @property
    def hoparlor(self):
        return self.__hoparlor

    @hoparlor.setter
    def hoparlor(self, value: str):
        try:
            self.__hoparlor = value
        except ValueError:
            print("Hoparlör sadece String tipinde olmalıdır")

    @property
    def ekran_karti(self):
        return self.__ekran_karti

    @ekran_karti.setter
    def ekran_karti(self, value:bool):
        try:
            self.__ekran_karti = value
            if value:
                self.__ekran_karti_str = "VAR"
            else:
                self.__ekran_karti_str = "YOK"
        except ValueError:
            print("Ekran Kartı sadece Boolean değer alabilir")


    @property
    def web_cam(self):
        return self.__web_cam

    @web_cam.setter
    def web_cam(self, value: bool):
        try:
            self.__web_cam = value
            if value:
                self.__web_cam_str = "VAR"
            else:
                self.__web_cam_str = "YOK"
        except ValueError:
            print("Web Cam sadece Boolean değer alabilir")

    @property
    def web_cam_str(self):
        return self.__web_cam_str

    @web_cam_str.setter
    def web_cam_str(self, value: str):
        try:
            self.__web_cam_str = value
        except ValueError:
            print("Web Cam sadece String değer alabilir")


    def __str__(self):
        return f"""
Marka               :{self.marka}
Model               :{self.model}
Fiyat               :{self.fiyat}
İşlemci             :{self.islemci}
Ram Kapasitesi      :{self.ram}
Ram Tipi            :{self.ram_tipi}
Harddisk Kapasitesi :{self.hard_disk}
Harddisk Tipi       :{self.hard_disk_tipi}
Anakart             :{self.ana_kart}
Güç                 :{self.guc}
Enerji Sınıfı       :{self.enerji_sinifi}
Batarya Kapasitesi  :{self.batarya}
Hoparlör            :{self.hoparlor}
Web Cam Var Mı      :{self.web_cam_str}
Ekran Kartı Var Mı  :{self.__ekran_karti_str}
        """
