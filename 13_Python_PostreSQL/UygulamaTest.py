from Uygulama import Uygulama

ahmet = Uygulama()

liste = ahmet.list_records()
print(liste)

ahmet.insert_user("KAHRAMAN", "ALİ")


liste = ahmet.list_records()
print(liste)