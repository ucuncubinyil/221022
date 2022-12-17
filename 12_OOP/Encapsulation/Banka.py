from Utils import Utils


class Banka:
    def __init__(self):
        self.__isim = ""
        self.__soyisim = ""

        self.__tc = ""
        self.__iban = ""

    @property
    def isim(self):
        return self.__isim

    @isim.setter
    def isim(self, value: str):
        self.__isim = value

    @property
    def soyisim(self):
        return self.__soyisim

    @soyisim.setter
    def soyisim(self, value: str):
        self.__soyisim = value

    @property
    def tc(self):
        return self.__tc

    @tc.setter
    def tc(self, value: str):
        while True:
            if (Utils.tc_kontrol(value)):
                self.__tc = value
                break
            else:
               try:
                   print("T.C. Geçersiz")
                   tc = int(input("T.C. Numarası"))
                   if (Utils.tc_kontrol(tc)):
                       self.__tc = tc
                       break
                   else:
                       continue
               except ValueError:
                   continue

    @property
    def iban(self):
        return self.__iban

    @iban.setter
    def iban(self, value):
        while True:
            if (Utils.iban_control(value)):
                IBAN = value[0].upper() + value[1].upper() + value[2:]
                self.__iban = IBAN
                break
            else:
                print("IBAN Geçersiz")
                IBAN_K = input("IBAN Numarası")
                if (Utils.iban_control(IBAN_K)):
                    IBAN = IBAN_K[0].upper() + IBAN_K[1].upper() + IBAN_K[2:]
                    self.__iban = IBAN
                    break
                else:
                    continue

    def bilgi_yaz(self):
        print(f"TC: {self.__tc}  IBAN: {self.iban}")
