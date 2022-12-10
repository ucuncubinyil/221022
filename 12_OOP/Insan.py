class Insan:
    ad = str()
    soyad = str()

    @classmethod
    def konus(cls, nesne):
        print(f"Ad :{nesne.ad}, Soyad: {nesne.soyad}")

    def konusma(self):
        print(f"Ad :{self.ad}, Soyad: {self.soyad}")

    @classmethod
    def yazdir(cls, insan_listesi: list):
        for insan in insan_listesi:
            print(insan.ad, insan.soyad)

    @classmethod
    def kaydet(cls, insan_listesi: list):
        insan = Insan()
        insan.ad = input("İnsan Adı:")
        insan.soyad = input("İnsan Soyadı:")
        insan_listesi.append(insan)
