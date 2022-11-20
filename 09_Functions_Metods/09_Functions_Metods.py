################# FONKSİYONLAR #####################
"""
Programımızda belirli bir işi yapan kod bloklarının tekrar kullanılması durumunda tekrar yazılmadan çağrılmasını
sağlayan modüllerdir.
Yani bir modülü 1 defa tanımlayıp istediğimiz zaman istediğimiz kadar kullanabilmemizi sağlar.
Fonksiyonlar yazdığımız programın modüler olmasını sağlar, ayrıca okunabilirliği artırır.
Fonsksiyonlar 2'ye ayrılır.
    Değer Döndüren Fonk. => parametreli ve parametresiz
    Değer Döndürmeyen Fonk. => parametreli ve parametresiz
"""

# Fonksiyon Tanımlama

"""
Deger döndürmeyen
def fonksiyonismi(varsa parametre):
	bu fonksiyonda çalıştırılacak kodlar yazılır
Deger döndüren
def fonksiyonismi(varsa parametre):
	bu fonksiyonda çalıştırılacak kodlar yazılır
	return deger
"""

"""
# Değer döndürmeyen ve parametre almayan metod-fonksiyon
def yaz():
    print("Merhaba Fonksiyon")


def isim_yaz(isim):
    print(f"Merhaba   {isim}")


def isim_yaz2(isim: str):
    print(f"isim {isim}")


yaz()
isim_yaz(12)
isim_yaz2("12")
"""
"""

# Değer döndüren

def topla():
    sonuc = 1 + 1
    return sonuc

def toplama(s1: int, s2: int):
    return s1 + s2

print(toplama(10, 2))

sonuc = topla()
print(sonuc)
print(topla())
"""

# global keyword; fonksiyon içerisindeki değişkenleri local olmaktan çıkartır.

ad = "Mehmet"  # Global değişken


def degistir():
    global sayi1, sayi2
    global ad

    ad = "Mehmet Nuri"
    sayi1, sayi2 = 10, 20
    print(sayi1, sayi2)


degistir()
print(ad)

######### ALIŞTIRMALAR ##########
# SORU: Kullanıcıdan 2 sayı 1 işlem alalım ve alınan sayılara
# verilen işlemi uygulayan ve ekrana yazdıran fonksiyonu yazınız.
#
"""
def dort_islem(s1: int, s2: int, islem: str):
    if islem == "+":
        return s1 + s2

    elif islem == "-":
        return s1 - s2

    elif islem == "*":
        return s1 * s2

    elif islem == "/":
        if s2 == 0:
            print("Hiç bir sayı sıfıra bölünemez")
            return s1 / 1
        else:
            return s1 / s2


toplama = dort_islem(15, 20, "+")
print(toplama)

bolme =  dort_islem(15,2,"/")
print(bolme)
print(int(bolme))


while True:
    cevap = input("İşlem yapmak ister misiniz ?(E/H)").upper()

    if cevap == "E":
        sayi1 =  int(input("Sayı 1: "))
        sayi2 =  int(input("Sayı 2: "))
        islem =  input("İşlem seçiminiz(+,-,*,/): ")

        sonuc =  dort_islem(sayi1,sayi2, islem)
        print(sonuc)
    else:
        break
"""

## SORU: Kendisine gönderilen sayı adedince klavyeden girilen ismi alıp listeye atan fonksiyonu yazınız.
#

"""
def isim_yaz():
    isim_liste = list()

    sayi = int(input("Kaç kişi listeye atılacak"))

    for i in range(sayi):
        isim = input(f"{i + 1}. kişi")
        isim_liste.append(isim)

    print(isim_liste)


# isim_yaz()

# liste =  list()
#
# def isim_ekle(parametre1: str, parametre2: list):
#     parametre2.append(parametre1)
#
#
# sayi = int(input("Kaç kişi eklenecek: "))
# for i in range(sayi):
#     isim = input(f"{i+1}. Kişi :")
#     isim_ekle(isim, liste)
#
# print(liste)

def birden_fazla(*sayilar):

    for i in sayilar:
        print(i)


# birden_fazla(1,2,3,4,5,6,7,8)

# Kendisine sayılardan oluşan listenin toplamını hesaplayan metodu yazın
"""

"""
def topla(*sayilar):
    toplam = 0
    for i in sayilar:
        toplam += i

    return toplam


sonuc = topla(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(sonuc)
"""
# Kendisine gönderilen karakter,en,boy parametrelerine göre
# ekrana karakterden oluşan bir dikdörtgen oluşturan fonksiyonu yazınız.

"""
oooooooo
oooooooo
oooooooo
oooooooo
"""



def ciz(karakter: str, en: int, boy: int):
    """
    Bu fonksiyon harfe göre çizim yapar
    :param karakter: Ekranda görünecek karakteri temsil eder
    :param en: Bu karakterin kaç defa yan yana yazılacağını belirtir
    :param boy: Bu işlemin kaç kez alt alta yapılacağını belirtir
    :return: Çizim
    """
    for i in range(boy):
        print(karakter * en)



ciz("o", 10, 5)
