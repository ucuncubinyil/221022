class Universite:

    def __init__(self):
        self.__vize = 0
        self.__final = 0

    def get_vize(self):
        return self.__vize

    def set_vize(self, param: int):
        if (param < 0 or param > 100):
            while True:
                print("Hatalı vize notu girişi! "
                      "Vize not aralığı 0-100 olmalıdır")
                vize_not = int(input("Vize notunuzu giriniz: "))

                if (vize_not < 0 or vize_not > 100):
                    continue
                else:
                    self.__vize = vize_not
                    break
        else:
            self.__vize = param

    vize = property(get_vize, set_vize)

    @property
    def final(self):
        return self.__final

    @final.setter
    def final(self, param: int):
        if (param < 0 or param > 100):
            while True:
                print("Hatalı final notu girişi! "
                      "Final not aralığı 0-100 olmalıdır")
                final_not = int(input("Final notunuzu giriniz: "))

                if (final_not < 0 or final_not > 100):
                    continue
                else:
                    self.__final = final_not
                    break
        else:
            self.__final = param

    def ortalama(self):

        sonuc = (self.__vize * 0.4) + (self.__final * 0.6)

        print(f"Ortalama: {sonuc}")
