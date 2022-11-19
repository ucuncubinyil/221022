### Set : Kume ###

kume = set() # Küme tanımlama yötemi 1
kume2  = {} # Küme tanımlama yöntemi 2

# Önemli Not:  set ile dolu küme oluşturulamaz. Nedeni performans
# kaybı. Önce boş oluşturulur sonra içeri veri atılır
kume_3 = {1,2,3}
print(kume_3)

kume.add("A") # kümeye eleman ekleme
kume.add("C") # kümeye eleman ekleme
kume.add("D") # kümeye eleman ekleme
kume.add("E") # kümeye eleman ekleme
print(kume)

kume.remove("A") # İçerde değer varsa siler yoksa hata verir
print(kume)

kume.discard("C") # remove dan farkı  hata patlatmaz
print(kume)

print(len(kume)) # Eleman sayısı


