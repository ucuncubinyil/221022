import random as rd

print(rd.random()) #0-1 arasında rastgele bir sayı verir
print(rd.randint(0,100)) # Verilen aralık içinde rast gele tam sayı verir
print(rd.uniform(0,100)) #Verilen aralık içinde rast gele noktalı sayı verir
print(rd.randrange(0,100)) # Verilen aralık içinde rast gele tam sayı üretir  aralık min ve max değeri dahil olmaz
print(rd.randrange(1,100,3)) #Verilen aralık içinde rast gele tam sayı üretir. 3 e bölümünde kalanı 1 olanları verir

print( rd.uniform( 100000.0000, 999999.9999 ) )

