import os, datetime

class Otomobil:

    def __init__(self, marka, model, renk, motor_hacmi, uretim_yili):
        self.marka = marka
        self.model = model
        self.renk = renk
        self.motor_hacmi = motor_hacmi
        self.uretim_yili = uretim_yili
        self.kaydet()

    def kaydet(self):
        dizin = "/home/mehmet/Ders/"  # C:\\TEST\\
        if not os.path.exists(dizin):
            os.mkdir(dizin)

        acik_dosya = None
        try:
            dosya = dizin + "OTOMOBIL_"+ str(datetime.date.today()) + ".txt"
            acik_dosya = open(dosya, mode="a+", encoding="utf-8")
            yazi = f"""
Marka       :{self.marka}
Model       :{self.model}
Renk        :{self.renk}
Motor Hacmi :{self.motor_hacmi}
Üretim Yılı :{self.uretim_yili}
            """
            acik_dosya.write(yazi)
        except Exception:
            print("Dosya yazılırken bir hata oluştu")
        finally:
            if acik_dosya is not None:
                acik_dosya.close()
