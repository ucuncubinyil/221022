class Uye:

    def __init__(self):
        ad = str()  # default olarak public
        soyad = str()
        __tc = str()  # private bir field
        self.kaydet()

    def kaydet(self):
        self.ad = input("Ad: ")
        self.soyad = input("Soyad: ")

        TC = input("T.C.: ")
        if len(TC) == 11 and TC.isnumeric():
            self.__tc = TC
        else:
            self.__tc = 0

    def bilgi(self):
        print(f"Ad: {self.ad}, "
              f"Soyad: {self.soyad},"
              f" T.C.:{self.__tc}")
