"""

kare = pow(4, 2)
print(kare)

def us_al(taban:int, us:int):
    # Formül = taban **  us
    return taban ** us

kare2 = us_al(1543, 32)
print(kare2)
"""
"""
"""
## Bir müşterim dolar'ını euro'ya çevirmek
# istiyor ben dolar/euro endeksini bilmediğim için doları tl => tl euro
# 1 $ => 18.59₺
# 1€ => 19.36  TL
"""

dolar_kuru = 18.59
euro_kuru = 19.36


# to tl => dolar_kuru * miktar
# to_euro => miktar / euro_kuru
def dolar_to_tl(dolar: float, kur: float):
    return (dolar * kur)


def tl_to_euro(tl: float, kur: float):
    return (tl / kur)


# 100 $
dolar_tl_sonucu = dolar_to_tl(100, dolar_kuru)
tl_euro_sonucu = tl_to_euro(dolar_tl_sonucu, euro_kuru)

print(f"100$ => {dolar_tl_sonucu} ₺ dir")
print(f"{dolar_tl_sonucu} ₺  => {tl_euro_sonucu} € dur")
"""

# Kendisine gönderilen sınırsız sayının ortalamasını döndüren fonksiyonu yazınız..
## 1,2,3 => 1+2+3 /3
"""
def ortlama(*sayilar):
    toplam = 0

    for sayi in sayilar:
        toplam += sayi

    return toplam / len(sayilar)


sonuc = ortlama(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(sonuc)

"""

"""
# iki sayıyı karşılaştırıp büyük olanı dönderen fonk. yaz
def max_of_two(x: int, y: int):
    if x > y:
        return x  # return görülen yerde else ye gerek yok 
    # return görünce python sonraki satıra geçmez
    return y


print(max_of_two(1, 2))


# 3 sayıyı karşılaştırıp büyük olanı dönderen fonk. yaz
def max_of_three(x: int, y: int, z: int):
    return max_of_two(x, max_of_two(y, z))  # öz yenilemeli fonksiyon


print(max_of_three(1, 2, 3))
"""

"""
# Kendisine parametre olarak gönderilen yazının tersini dönderen fonk. yaz
def reverse_string(text: str):
    rstr = ""
    index = len(text)
    while index > 0:
        rstr += text[index - 1]
        index -= 1
    return rstr

print(reverse_string("Mehmet")) #temheM
"""

"""
# Faktöryel hesaplayan fonk. yaz

def faktoryel_al(n: int):
    if n == 0:
        return 1
    else:
        return n * faktoryel_al(n - 1)


print(faktoryel_al(5))
"""

"""
# Kendisine parametre olarak gönderilen sayının
# daha önceden belirlenmiş olan sayı aralığında (1,20)
# olup olmadığını dönderen fonk. yaz

def test_range(n: int):
    if n in range(1, 21):
        print(f"{n} sayı aralığı içindedir")
    else:
        print(f"{n} sayı aralığı içinde değildir")


test_range(20)
"""

"""
# Kendisine parametre olarak gönderilen metin içinde
# büyük ve küçük harflerin sayısını dönderen fonk. yaz

def string_test(text: str):
    count_dic = {"UPPER_CASE": 0, "LOWER_CASE": 0}

    for character in text:
        if character.isupper():  # Karakter büyük harf mi
            count_dic["UPPER_CASE"] += 1
        elif character.islower():  # Karakter küçük harf mi
            count_dic["LOWER_CASE"] += 1
        else:  # Eğer karakter özel bir karakter ise !#?_& ..vb
            pass

    return count_dic


print(string_test("Merhaba Mehmet !"))
"""

"""
# Verilen listedeki tekrar eden elemanları silerek
# temiz bir liste oluşturan fonk. yaz
def unique_test(number_list: list):
    unique_list = list()
    for number in number_list:
        if number not in unique_list:
            unique_list.append(number)
    return unique_list


numbers = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
print(unique_test(numbers))
"""

"""
# Kendisine parametre olarak gönderilen sayının
# asal olup olmadığını dönen fonk. yaz

def test_prime(n: int):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2, n):
            if n % x == 0:
                return False
        return True


print(test_prime(4))

from math import sqrt


def is_prime(n: int):
    if n <= 1 or (n % 2 == 0 and n > 2):
        return False
    return all(n % i for i in range(3, int(sqrt(n)) + 1, 2))


print(is_prime(13))
"""

"""

# Kendisine verilen listedeki elemanları tek ve çift olarak ayrı ayrı
# listeye atıp sonucu sözlük olarak dönderen fonk. yaz
def test_dict(numbers: list):
    tek_liste = list()
    cift_liste = list()
    result_dic = {"TEK": tek_liste, "CIFT": cift_liste}
    for number in numbers:
        if number % 2 == 0:
            cift_liste.append(number)
        else:
            tek_liste.append(number)
    return result_dic

print(test_dict([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
"""

"""
# Kendisine parametre olarak gönderilen sayının mükemmel sayı
# olup olmadığını dönderen fonk. yaz.
# Örn 6
def perfect_test(n: int):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x

    return sum == n


print(perfect_test(28))
# 123456 = 6
"""

"""
# Kendisine parametre olarak gönderilen sayının
# pascal ücgenine göre açılımını yazan fonk. yaz
def pascal_triangle(n: int):
    trow = [1]
    y = [0]

    for x in range(max(n, 0)):
        print(trow)
        trow = [1 + r for l, r in zip(trow + y, y + trow)]
    return n >= 1

print(pascal_triangle(6))

"""

"""
# Kendisine parametre olarak gönderilen sayıya kadar olan sayıların karelerini
# liste olarak dönen fonk. yaz.

def pow_list_test(n: int):
    pow_list = list()
    for i  in range(1, (n+1)):
        pow_list.append(i**2)

    return pow_list

print(pow_list_test(100))

"""

"""
def kare_al(x: int):
    return x ** 2

sonuc = kare_al(5)
print(sonuc)

sonuc = (lambda x: x ** 2)(5)
print(sonuc)

kare_al = lambda x: x ** 2

print(kare_al(8))
"""

"""
def hesapla(number: int):
    return lambda x: x * number

sonuc =  hesapla(5)(2)
print(sonuc)
"""
"""
# map(func, iter1) şeklinde kullanılır.
# Yani elinizdeki bir fonksiyona, elinizdeki
# bir datanın elemanlarını sırasıyla gönderir
# ve sonucu tek bir obje olarak geri döner.
# Ben aşağıdaki örneklerde hep liste kullandım
# iterasyona sokulabileceği için ama veri tipi
# liste olmak zorunda değil demet v.s. de olabilirdi.
# Döngü içine alınabilen bir data olması yeterli.

sayi_listesi = [2, 3, 4]


def kare_al(sayi: int):
    return sayi ** 2

sonuc = list(map(kare_al, sayi_listesi))
print(sonuc)

sonuc2 = list(map(lambda x: x ** 2, sayi_listesi))
print(sonuc2)
"""

"""

#
# Zip()
# Kelimenin çevirisine baktığımızda zip,
# fermuar anlamına geliyor ve tam olarak da
# bu anlamda kullanılıyor. 2 listeyi birbiri indisleri üzerine
# birleştiriyor. Bunu yaparken de en kısa elemanlı listenin
# uzunluğunu baz alıyor.


isim_listesi = ["AHMET", "MEHMET", "KENAN", "ALİ"]
yas_listesi = [2, 3, 4]

sonuc = zip(isim_listesi, yas_listesi)
print(sonuc)

sonuc2 = list(sonuc)
print(sonuc2)

print(type(sonuc2[0])) #sonuc tuple



"""

"""
# Reduce()

from functools import reduce

numara_listesi = [1, 66, 99, 101, 333, 4454]


def find_max(a: int, b: int):
    if a > b:
        return a
    return b


def find_min(a: int, b: int):
    if a < b:
        return a
    return b


sonuc = reduce(find_max, numara_listesi)
print(sonuc)

sonuc = reduce(find_min, numara_listesi)
print(sonuc)
"""

"""
# Filter()

kisiler = ['Sinan', 'Erdinç', 'Mehmet']
tarihler = [2018, 2017, 2020]
ziplenmis = zip(kisiler,tarihler)

sonuc =  list(filter(lambda eleman: 2018 <= eleman[1] <= 2020, ziplenmis))
print(sonuc)

list_number = [2, 4, 6, 8, 9, 10, 12, 13]

cift_sayilar = list(filter(lambda x: (x % 2 == 0), list_number))
print(cift_sayilar)

filtrelenmis_liste = filter(lambda x: (x > 7) and (x < 10), list_number)
print(list(filtrelenmis_liste))
"""

"""
def kalin_yap(fn):
    def wrapped():  # sarmallanmış fonksiyon
        return "<b>" + fn() + "</b>"

    return wrapped


def alti_cizili(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"

    return wrapped


@kalin_yap  # anatasyon -> decorator
@alti_cizili
def selam():
    return "Merhaba"

print(selam())



def test(a):
    def add(b):
        nonlocal a
        a += 1
        return a + b

    return add


sonuc = test(4)
print(sonuc(4))


def abc():
    x = 1
    y = 2
    str = "Test yazım"
    print("Python fonksiyon")


print(abc.__code__.co_nlocals)
"""
"""
from  time import sleep

sleep(1)
print("Selam")
sleep(5)
print("Selam")
"""
"""

def islem(a: int):
    return a + 15


islem2 = lambda a: a + 15
print(islem2(5))


def islem_3(x, y):
    return x * y


islem4 = lambda x, y: x * y
print(islem4(10, 20))


def us_al(taban: int, us: int):
    return taban ** us


islem5 = lambda taban, us: taban ** us
print(islem5(2, 3))

"""
"""
# Liste deki elemanları küçükten büyüğe notuna göre sıralayın
sonuclar = [("Matematik", 90), ("Türkçe", 70), ("Fizik", 95), ("Kimya", 65)]
print(sonuclar)

sonuclar.sort(key=lambda x: x[1])  # Küçükten büyüğe göre sıralar
sonuclar.sort(key=lambda x: x[1], reverse=True)  # Büyükten küçüğe göre sıralar
print(sonuclar)
"""
"""
# Listedeki telefonlar marka isimlerine göre a-z ye sıralansın
telefonlar = [
    {"marka": "Samsung", "model": "S3", "renk": "mavi"},
    {"marka": "Apple", "model": "11", "renk": "kırmızı"},
    {"marka": "Xioami", "model": "xx", "renk": "mor"},
    {"marka": "Realme", "model": "abc", "renk": "turuncu"},
]
print(telefonlar)

telefonlar.sort(key= lambda x: x["marka"])
print(telefonlar)

telefonlar.sort(key= lambda x: x["marka"], reverse=True)
print(telefonlar)

modeller = sorted(telefonlar, key=lambda x: x["marka"])
print(modeller)
"""
"""
# tek ve çift sayıları ayrı ayrı listeye atan lambda fn-nk.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cift_sayilar = list(filter(lambda x: x % 2 == 0, nums))
tek_sayilar = list(filter(lambda x: x % 2 != 0, nums))

print(cift_sayilar)
print(tek_sayilar)
"""

"""
# ile_basliyor lamda fonksiyonum girmiş oldğum kelimenin
# P ile başlayıp başlamadığını mantıksal olarak döndürsün(True,False)
ile_basliyor = lambda x: True if x.startswith("P") else False

print(ile_basliyor("Python"))
print(ile_basliyor("Java"))
"""
"""
# Bu günün yılını ayını gününü saatini dakikasını saniyesini dönderen
# lambda ifadelerini yazın.
from datetime import datetime

now = datetime.now()
print(now)

year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day

hour = lambda x: x.hour
minute = lambda x: x.minute
sec = lambda x: x.second

print(year(now))
print(month(now))
print(day(now))
print(hour(now))
print(minute(now))
print(sec(now))

"""

"""
# İki listedeki elamanları karşılaştırarak farklı olan elemanları listeleyen progr. yaz.
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]


def fark_bul(list1: list, list2: list):
    fark = list(filter(lambda x: x not in list2, list1))
    return fark


print("Orjinal Liste")
print(list1)
print(list2)

print("Fark Listesi")
print(fark_bul(list1, list2))

"""
"""
# Elimizde colors = ["red", "black", "white", "green", "orange"] listesi var
# Bu liste içindeki elemanlardan ack içeren elemanları bulan fonk.yaz.


def bul(text: str):
    if "ahmet" in text:
        print("Ahmet yazının içinde")

bul("Merhaba ahmet")



def find_string(text: list, find_text: str):
    result = list(filter(lambda x: find_text in x, text))
    return result


colors = ["red", "black", "white", "green", "orange"]
print("Orjinal Liste")
print(colors)

aranacak = input("ARanacak kelimeyi gir")
print("Kelime aranıyor...")
print(find_string(colors, aranacak))
"""

"""
# İki adet listemiz var birinci listede bulunan elemanlar ikinci listede de vardır
# bu ikinci listede bulunan elemanları liste1 e göre karşılaştırıp
# aynı olanları veren fonk. yaz

def fark_bul(l1: list, l2: list):
    result = [list(filter(lambda x: x in l1, sublist)) for sublist in l2]
    return result


liste1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
liste2 = [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
#  12, 7, 11, 1, 5,8

print(fark_bul(liste1, liste2))
"""

"""
# Elimdeki listeyi tersten yazdıran lambda ifadesini yazınız..

def reverse_string_on_list(list1: list):
    result = list(map(lambda x: "".join(reversed(x)), list1))
    return result


color_list = ["Red", "Pink", "Yellow", "Orange", "Hue"]

print(reverse_string_on_list(color_list))
"""

# ÖDEV
# Elimdeki listede tekrar eden değerleri silen ve birbiri ile çarpan fonk. yazın.
# Lambda ifadesi ile de yazın
"""

# Listedeki elemanları birbiri ile çarpan lambda fonk. yazın
# reduce kullanın

from functools import reduce


def multiple_list(list1: list):
    result = reduce(lambda x, y: x * y, list1)
    return result


num_list = [4, 3, 2, 1, -1, 5, -5]

print(multiple_list(num_list))
"""

"""
# Elimizdeki tuple bulunan string olarak tanımlanmış değerleri int e çeviren
# lambda ifadesini yazın.
def tuple_to_int(tup1: tuple):
    result = tuple(map(lambda x: (int(x[0]), int(x[2])), tup1))
    return result


num_tuple = (("233", "ABC", "33"), ("1453", "mayıs", "29"), ("1923", "ekim", "29"), ("1920", "nisan", "23"))

print(tuple_to_int(num_tuple))
"""


# Elimdeki listede None değeri olmadan listeyi yeniden yazan fonk. yaz.

def remove_none(list1: list):
    result = filter(lambda y: y is not None, list1)
    return list(result)


nums = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]

print(remove_none(nums))