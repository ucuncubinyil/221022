# Dosya  Dizin(Klasör)

# Windows C:\\Users\\kullanici_adi
# MAC  /Users/kullanici_adi/dizin_adi
# Linux  /home/kullanici_adi/dizin_adi

"""
open()      => Dosya açma komutu
system()    => Kullanırken çok dikkat edeceğimiz bir methoddur.
getcwd()    => Sistemin şuan işlem yaptığı dizin döndürülür.
chdir()     => Farklı bir dizine geçmemizi sağlar.
listdir()   => Bulunduğumuz dizinde mevcut dosyaları getirir.
mkdir()     => Bulunduğumuz dizinde yeni klasör açar.
rmdir()     => İçi boş olan bir klasörü siler.
rename()    => İsim değiştirir
path()      => Bir dosya veya klasörün var olup olmadığını kontrol etmek istediğimizde path.exists() komutu kullanırız.
"""
"""
import os
print(os.getcwd()) # ŞUAN ÇALIŞTIĞIM DİZİN
os.chdir("C:\\") # C: DİZİNİNE GİT
print(os.getcwd()) # C: DİZİNİNDEYİM
print(os.listdir()) # ŞUANKİ DİZİNİN KLASÖRLERİNİ LİSTELE (LİSTE)
dizin_listesi =  os.listdir()

for dizin_adi in dizin_listesi:
    print(dizin_adi)

if not os.path.exists("C:\\TEST"): # eğer bu dizin yoksa
    os.mkdir("C:\\TEST") # C:/TEST

if not os.path.exists("C:\\TEST\\MEHMET"):
    os.mkdir("C:\\TEST\\MEHMET")
"""
"""
### SORU: C:\\TEST\\YIL-AY-GUN isminde bir klasör açınız.

from datetime import datetime

import os

dosya_yolu = "C:\\TEST"
if not os.path.exists(dosya_yolu):
    os.mkdir(dosya_yolu)

zaman = datetime.now().strftime("%Y-%m-%d")
print(zaman)

if not os.path.exists(dosya_yolu + "\\" + zaman):
    os.mkdir(dosya_yolu + "\\" + zaman)

"""

import os

os.system("calc")
print(os.system("hostname"))
print(os.system("ipconfig /all"))
