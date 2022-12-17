# Inheritance #
"""
from  Calisan import  Calisan


calisan1 = Calisan("Mehmet Nuri","36000", "AR-GE")

calisan1.bilgi_goster()

Calisan.departman_degis("IT", calisan1)

calisan1.bilgi_goster()

"""

from Yonetici import Yonetici

yonetici1 =  Yonetici("Hakan", 16000, "Ar-Ge", 12)
yonetici1.bilgi_goster()

Yonetici.departman_degis("IT", yonetici1)
yonetici1.bilgi_goster()

yonetici1.zam_yap(500)

yonetici1.bilgi_goster()