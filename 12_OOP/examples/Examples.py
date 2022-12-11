from BuzDolabi import BuzDolabi
from CamasirMakinesi import CamasirMakinesi

""""
arcelik = BuzDolabi()
arcelik.marka = "Arçelik"
arcelik.model = "XCV"
arcelik.fiyat = 16000.00
arcelik.enerji = "16KW"
arcelik.hacim = 1000
arcelik.donducu_kapak_mevki = True
arcelik.kapak_sayisi = 4

arcelik.bilgi_ver()
arcelik.kaydet()
"""

bosh_camasir = CamasirMakinesi()
bosh_camasir.marka = input("Çamaşır markası")
bosh_camasir.model = "AAW"
bosh_camasir.fiyat = 10000.00
bosh_camasir.enerji = "5KW"
bosh_camasir.kurutma = False
bosh_camasir.sivi_deterjan = True
bosh_camasir.yikama_kapasitesi = 9
bosh_camasir.hizli_yikama = True

bosh_camasir.bilgi_ver()

bosh_camasir.kaydet()
