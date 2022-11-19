kume = {11, 22, 33, 44}
kume2 = {33, 44, 55, 66, 77, 88, 99}

"""
#  Küme Farkı Bulma
kume_fark = kume - kume2  # 1. yöntem tavsiye edilmeyen
kume_fark2 = kume2 - kume
print(kume_fark)
print(kume_fark2)

kume_fark = kume.difference(kume2)  # tavsiye edilen yöntem
kume_fark2 = kume2.difference(kume)
print(kume_fark)
print(kume_fark2)
"""

#Küme Birleşim
"""
kume_birlesim =  kume.union(kume2)
print(kume_birlesim)

for eleman in kume_birlesim:
    print(eleman)


print(12 in kume_birlesim)
"""
"""
# Var olan kümeye baska bir kümenin elemanlarını elkeyip güncellemek
turkiye = {"apple", "banana", "cherry"}
afrika = {"pineapple", "mango", "papaya"}
turkiye.update(afrika)
print(turkiye)

# Eleman silme
turkiye.remove("papaya")
print(turkiye)

turkiye.discard("eleman")
print(turkiye)

# İlk elemanı siler
turkiye.pop()
print(turkiye)

# Kümeyi temizleme
turkiye.clear()
print(turkiye)

del turkiye # ramden siler
# print(turkiye) # hata verir

"""


# Alt Küme
print(f"Küme kümesi  Küme2 kümesinin alt kümesi midir?: {kume.issubset(kume2)}")

#Üst Küme
print(f"Küme kümesi  Küme2 kümesinin üst kümesi midir?: {kume.issuperset(kume2)}")

#Ayrık Küme
print(f"Küme kümesi  Küme2 kümesinin ayrık kümesi midir?: {kume.isdisjoint(kume2)}")
