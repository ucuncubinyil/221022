#### Tuple: Sabit Liste ###
# Listelerden farkı değiştirilemez !

"""
# Veri tabanında detaylı göreceğiz
sabit_liste =  () # boş bir tuple oluşturma yöntemi 1
sabit_liste2 =  tuple() # boş bir tuple oluşturma yöntemi 2
"""

tercihler = (1, 2, 3, 4, 5, "Mehmet", 2.25, False)

print(tercihler)

for tercih in tercihler:
    print(tercih)

print(tercihler.index("Mehmet"))
print(tercihler[5])
print(tercihler[tercihler.index("Mehmet")])

tuple2 = (1, 2, [3, 4])
print(tuple2[2][1])
print(len(tercihler))
print(tercihler.count("Mehmet"))
