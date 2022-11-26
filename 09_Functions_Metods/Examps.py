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


# Kendisine parametre olarak gönderilen sayıya kadar olan sayıların karelerini
# liste olarak dönen fonk. yaz.

def pow_list_test(n: int):
    pow_list = list()
    for i  in range(1, (n+1)):
        pow_list.append(i**2)

    return pow_list

print(pow_list_test(100))