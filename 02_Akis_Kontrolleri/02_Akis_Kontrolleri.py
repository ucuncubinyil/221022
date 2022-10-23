##################### AKIŞ KONTROL : IF ELIF ELSE ########################################
# Program akışında bir sonuc,durum ve değere göre program akışı
# devam edecek ise if elif else deyimleri kullanılır.
# Karar yapıların if ve else 1 kez tanımlanır.
# alternatif bütün durumlar elif keyword'ü tekrar tekrar
# yazılarak kullanılablir

"""
if koşul:
	yapılmak istenilen
elif koşul2:
	yapılmak istenilen
else:
	eğer koşullar doğru değil ise burası çalışır

"""

"""
sayi = 6

if sayi > 6:
	print("Sayi değişkeni 6 dan büyüktür")
elif sayi == 6:
	print("Sayi değişkeni 6 ya eşittir")
else:
	print("Sayi değişkeni 6 dan küçüktür")
"""

"""
# Haftanın kaçıncı günüdeyiz? ekrana gün adını yazdıralım
gun = int(input("Haftanın gün sayısını giriniz: "))
if gun == 1:
	print("Pazartesi")
elif gun == 2:
	print("Salı")
elif gun == 3:
	print("Çarşamba")
elif gun == 4:
	print("Perşembe")
elif gun == 5:
	print("Cuma")
elif gun == 6 or gun == 7:
	print("Haftasonu")
else:
	print("Yanlış gün girdiniz !!!")

"""
# SORU: Klavyeden girilen değer: 100'den büyükse karesini,
# küçükse küpünü ekrana yazdıran prog.
"""
sayi = int(input("Sayı: "))

if sayi >100:
	print(sayi**2)
elif sayi < 100:
	print(sayi**3)
else:
	print(sayi)
"""
# Klavyeden girilen sayı çift ise:
# Ekrana sayı çifttir yazılacak,
# değilse tektir yazılacak
# çift ise 4 ile çarpsın, tek ise 9 ile toplasın
"""
sayi =  int(input("Sayi"))

if sayi %2 == 0:
	print("Sayı çiftir")
	print(sayi*4)
else:
	print("Sayı tektir")
	print(sayi+9)
"""
# Kullanıcıdan alınan sayının aralığını belirleyiniz
#  0-10  11-20

sayi = int(input("Sayi"))

if 0 < sayi  and sayi < 11: # 0-10
	print("0-10")
elif 10 < sayi and sayi < 21:
	print("10-20")
else:
	print("Aralık tanımlı değil")


	
	
	
	
	