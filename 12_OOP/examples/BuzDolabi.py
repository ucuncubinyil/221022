from BeyazEsya import BeyazEsya
import os

class BuzDolabi(BeyazEsya):

    def __init__(self):
        self.kapak_sayisi = 0
        self.hacim = 0
        self.donducu_kapak_mevki = False

    def bilgi_ver(self):
        super().bilgi_ver()
        print(f"""Kapak Sayısı:     {self.kapak_sayisi} 
        Hacim:      {self.hacim} Dondurucu Kapak Mevkii
        {self.donducu_kapak_mevki}""")
    def kaydet(self):
        dizin = "/home/mehmet/Ders/"  # C:\\TEST\\
        if not os.path.exists(dizin):
            os.mkdir(dizin)

        dosya = None
        try:
            dosya_yolu = dizin + "DuzDolabi.txt"
            dosya = open(dosya_yolu, mode="a+", encoding="utf-8")
            yazi = f"""Marka:      {self.marka}    Model:{self.model}
            Enerji:     {self.enerji}   Fiyat:      {self.fiyat}
            Kapak Sayısı:       {self.kapak_sayisi} Hacim:      {self.hacim}
            Dondurucu Kapak Mevki:      {self.donducu_kapak_mevki}"""
            dosya.write(yazi)
        except Exception:
            print("Dosya yazılırken bir hata oluştu")
        finally:
            if dosya is not None:
                dosya.close()
