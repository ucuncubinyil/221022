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

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}


child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily2 = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)
print(myfamily2)


print(myfamily["child1"]["name"]) # çok boyutlu liste !!!

list1 = [ 1, 2, 3, 4, 5 ]
list2 = [ 6, 7, 8, 9, 0 ]
list3 = [ 11, 22, 33 ]

sozluk = { "x": list1, "y": list2, "z": list3 }

print(sozluk)
print(sozluk["x"][0])

sozluk["x"][0] = 15
print(sozluk["x"][0])