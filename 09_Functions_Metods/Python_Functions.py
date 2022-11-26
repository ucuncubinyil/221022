#Hazır Fonksiyonlar

"""
capitalize()    İlk harfi büyüğe çevirir
count()         Bir dizide belirtilen değerin kaç defa tekrarlandığının sayısını döner
endswith()      Bir dizide belirtilen değer ile bittiğini kontrol eder Boolean
find()          Dizide belirtilen değeri bulur ve index numarasını da verir
isalpha()       Metnin tamamen karakterlerden oluşup oluşmadığını kontrol eder
isdecimal()     Metnin noktalı sayı olup olmadığını kontrol eder
isdigit()       Metinin sayısal olup olmadığını kontrol eder
lstrip()        Yazının soldaki boşluğunu siler
rstrip()        Yazının sağdaki boşluğunu siler
strip()         Yazının hem sağdan hem soldan boşluğunu siler
split()         Metni belirtilen ayraca göre böler  ve diziye çevirir

"""
yazi =  "merhaba ben mehmet nuri öztürk"


capitalize_deneme = yazi.capitalize()
print(capitalize_deneme)

print(yazi.endswith("öztürk"))

dosya_adi =  "deneme,jkad,hasdlkj.pdf"

dosya_adi_liste = dosya_adi.split(".")
print(dosya_adi_liste)
if dosya_adi_liste[1].endswith("pdf"):
    print("Dosya bir pdf dosyasıdır")


kelimeler = "Bugün.hava.çok.sıcak.değildi"

kelimeler_listesi =  kelimeler.split(".",2) # listeye en fazla 2 eleman alır
print(kelimeler_listesi)

kelimeler = "Bugün.hava.çok.sıcak.değildi"
kelimeler_listesi =  kelimeler.split(".")
print(kelimeler_listesi[-2])

universite = "Yıldız Teknik Üniversitesi"
universite_listesi =  universite.split(" ")
print(universite_listesi)