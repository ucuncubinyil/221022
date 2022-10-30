# DÖNGÜLER
# WHILE  -  FOR

# 1 ile 10 arasındaki sayıları ekrana yazdırınız.
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# print(7)
# print(8)
# print(9)
# print(10)

"""
while(kosul):
    kosul true olduğu sürece bu kod bloğu çalışır.
"""
"""
i = 1
while i < 11:
    print(i)
    if i == 3:
        break
    i += 1
"""
# BREAK => Döngüyü kırar
# CONTINUE => Döngüyü başa sarar


"""
while True: # program kapatılana kadar yada döngü kırılana kadar çalıştırr
	print("Mehmet Nuri")
	break
"""
"""
while True:
    print("Mehmet Nuri")
    break
"""

# 90 ile 100 arasındaki sayıları ekrana yazdırınız.
"""
sayi = 90

while sayi <= 100:
    print(sayi)
    sayi += 1
"""
# 1-1000 arasındaki tek ve çift sayıların toplamlarını ayrı
# ayrı hesaplayan kodu yazınız if else ve while kullanın sadece
"""
tek_toplam = 0
cift_toplam = 0
sayi = 1
while sayi <= 10:

    if sayi % 2 == 0:
        cift_toplam += sayi
    else:
        tek_toplam += sayi

    sayi += 1

print(f"1-1000 arasıdaki tek sayıların toplamı {tek_toplam}")
print(f"1-1000 arasıdaki çift sayıların toplamı {cift_toplam}")
"""

"""
# 70 ile 55 arasındaki sayılarda 3'e tam bölünenleri ekrana yazdırınız
"""

"""
sayi = 70
while sayi >= 55:
    if sayi % 3 == 0:
        print(sayi)
    sayi -= 1

sayi = 55
while sayi <= 70:
    if sayi % 3 == 0:
        print(sayi)
    sayi += 1

"""

# SORU: 1'den kullanıcının girdiği sayıya kadar
# olan sayıların karesini ekrana yazdıran program.

baslangic = 1
bitis =  int(input("Kaça kadar ?"))

while baslangic <= bitis:
    print(baslangic ** 2)
    baslangic += 1

# Ödev: 1'den kullanıcının girdiği sayıya kadar
# olan sayıların eğer tek ise karesini , çift ise küpünün
# toplamını ayrı ayrı hesaplayan kod parçacığı