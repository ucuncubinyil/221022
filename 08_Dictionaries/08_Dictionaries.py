################## DICTIONARY (SOZLUK) ########################
"""
sozluk = {}  # Sözlük
sozluk2 = dict()

"""
"""
sozluk = {"anahtar": deger, "anahtar": deger, "anahtar": deger}

"""

"""
bilgilerim = {
    "ad": "Mehmet Nuri",
    "soyad": "Öztürk",
    "yas": 29,
    "dogum_tarihi": "20.11.1993"
}

print(bilgilerim)
print(bilgilerim["ad"])
print(bilgilerim.keys())    # anahtarları list
print(bilgilerim.values())  # degerleri  list
print(bilgilerim.items())   # elemanları tuple

for anahtar in bilgilerim.keys():
    print(anahtar)

if "dogum_tarihi" in bilgilerim.keys():
    print(bilgilerim["dogum_tarihi"])


bilgilerim.clear() # sözlüğü temizler
print(bilgilerim)

"""
"""
s1 = {"ad": "Selim", "soyad": "Kaçar"}
s2 = {"soyad": "Kaçar", "ad": "Selim"}
s3 = {"soyad": "Varan", "ad": "Selim"}

print("s1 s2 ye eşit midir?", s1 == s2)
print("s1 s3 ye eşit midir?", s1 == s3)
"""

"""
kullanici_bilgileri = dict()

ad =  input("Adınız:")
kullanici_bilgileri["ad"] = ad

soyad = input("Soyad:")
kullanici_bilgileri["soyad"] = soyad

yas =  int(input("Yaş:"))
kullanici_bilgileri["yas"] =  yas

print(kullanici_bilgileri) # {'ad': 'Mehmet', 'soyad': 'Öztürk', 'yas': 23}

"""
"""
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

print(car)
car["year"] = 2020 # değer değiştirme
print(car)

car["color"] = "black"
print(car)

car.update({"color": "red" }) # değer değiştirme yöntem 2
print(car)

car.update({"hp": 36900}) # ekleme ve güncelleme için
print(car)

car.pop("hp") # keyi ve valuyu siler
print(car)

car.popitem() # son elemanı siler
print(car)

del car["year"]
print(car)
"""

"""
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

for a, d in car.items():
    print(a, d)

car2 = car.copy()  # car2 ye car sözlüğünü kopyalar yeni ram adresi üretir
print(car2)

car.update({"mehmet": 15})

car3 = dict(car) # ram adresini kopyalar
print(car3)

"""
"""
myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}

myfamily2 = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}

print(myfamily)
print(myfamily2)

print(myfamily["child1"]["name"])  # çok boyutlu liste !!!

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 0]
list3 = [11, 22, 33]

sozluk = {"x": list1, "y": list2, "z": list3}

print(sozluk)
print(sozluk["x"][0])

sozluk["x"][0] = 15
print(sozluk["x"][0])
"""

#### SORU: Kullanıcıdan alınan ad,soyad,yas,cinsiyet
# bilgilerini Personel isimli bir sözlükte saklayın ve
# ad soyad bilgisini sözlükten alarak ekrana yazdırınız.
"""

personel = dict()

ad = input("Adınız: ")
soyad = input("Soyadınız: ")
yas = int(input("Yaşınız: "))
cinsiyet = input("Cinsiyetiniz: ")

personel.update({"ad": ad})
personel.update({"soyad": soyad})
personel.update({"yas": yas})
personel.update({"cinsiyet": cinsiyet})

print(personel)
print(personel["ad"], " ", personel["soyad"])

"""

# SORU: Bir firmanın İnsan kaynakları,Bilgi İşlem ve
# Muhasebe departmanlarının çalışan listelerini yöneticiden
# isteyerek bir dict atınız
# ve ekrana istenilen bölümdeki çalışanları listeyiniz.

"""
IK = list()
IT = list()
MHSB = list()
firma = dict()

for i in range(1):
    IK.append(input("İnsan Kaynakları Personel Ad Soyad"))
    IT.append(input("Bilgi İşlem Personel Ad Soyad"))
    MHSB.append(input("Muhasabe Personel Ad Soyad"))


firma.update({"IK": IK})
firma.update({"IT": IT})
firma.update({"MHSB": MHSB})


secim =  input("Lütfen personel listesine erişmek isteğiniz departmanın kodunu giriniz(IT,IK,MHSB)")

for i in firma[secim]:
    print(i)
    
"""

"""
yasakli_liste = ["ı", "ş", "ğ", "ö", "ü", "ç", "İ", "Ş", "Ğ", "Ö", "Ü", "Ç"]
uygun_liste = ["i", "s", "g", "o", "u", "c", "I", "S", "G", "O", "U", "C"]

metin = input("Test için küçük harflerden oluşan ve türkçe karakterler içeren bir metin girin: ")

for i in metin:
    if i in yasakli_liste:
        indx = yasakli_liste.index(i)
        krkt = uygun_liste[indx]
        metin = metin.replace(i, krkt)

print(metin)

"""
"""
# SORU: sözlük uygulaması olsun Tr-Eng
#       sözlük={"siyah":"black"...}
#       kullanıcı 4 seçenekli bir menü verelim
#          1-Arama
           2-Çıkarma
           3-Listeleme
           4-Çıkış
        Kullanıcı 1'e basarsa ->
            - Aranacak kelimeyi giriniz:
            - Bu kelime dict varsa english karşılığını yazılır.
            - Yoksa uygulamayı geliştirmek istermisiniz?
                - E ise bu kelimenin ingilizce karşılığını alırız ve sözlüğe eklenir.
                - H ise Peki.. 
        Kullanıcı 2'e basarsa -> 
            - Çıkarılmak istenen kelime:
            - Kelime sözlükte varsa çıkartılır.
            - Yoksa uyarı verilir.
        Kullanıcı 3'e basarsa ->
            - Tum key value lar listenilir.
            - KEY -> VALUE
        Kullanıcı 4'e basarsa ->
            - Döngü sonlanır..
"""
