from BeyazEsya import BeyazEsya
import  os

class CamasirMakinesi(BeyazEsya):

    def __init__(self):
        self.yikama_kapasitesi = 0
        self.hizli_yikama = False
        self.sivi_deterjan = False
        self.kurutma = False

    def bilgi_ver(self):
        super().bilgi_ver()
        print(f"""Yıkama Kapasitesi:{self.yikama_kapasitesi} Hızlı Yıkama:{self.hizli_yikama}
        Sıvı Detarjan: {self.sivi_deterjan} Kurutma: {self.kurutma}""")

    def  kaydet(self):

        dizin = "/home/mehmet/Ders/"

        if not os.path.exists(dizin):
            os.mkdir(dizin)

        dosya = None

        try:

            dosya_yolu =  dizin +"CamasirMakinesi.txt"
            dosya =  open(dosya_yolu, mode="a+", encoding="utf-8")

            yazi = f"""Marka:{self.marka} Model:{self.model},  Enerji:{self.enerji} Fiyat:{self.fiyat}
            Yıkama Kapasitesi:{self.yikama_kapasitesi} Sıvı Deterjan:{self.sivi_deterjan} 
            Hızlı Yıkama:{self.hizli_yikama} Kurutma:{self.kurutma}"""
            dosya.write(yazi)

        except Exception:
            print("Dosya yazılırken hata oluştu")
        finally:
            if dosya is not None:
                dosya.close()


