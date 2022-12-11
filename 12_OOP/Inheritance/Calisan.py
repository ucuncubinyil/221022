class Calisan:

    def __init__(self, isim:str, maas:int, departman:str):
        print("Çalışan sınıfının init fonksiyonu")
        self.isim = isim
        self.maas = maas
        self.departman = departman

    def bilgi_goster(self):
        print("Çalışan bilgileri")
        print(f"İsim : {self.isim} Maaş: {self.maas},"
              f" Departman: {self.departman}")

    @classmethod
    def departman_degis(cls, yeni_departman, calisan):
        print("Departman Değiştiriliyor")
        calisan.departman = yeni_departman
