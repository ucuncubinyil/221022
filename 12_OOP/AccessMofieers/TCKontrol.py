"""

Tc No = d1 d2 d3 d4 d5 d6 d7 d8 d9 c1 c2

c1 = ( (d1 + d3 + d5 + d7 + d9) * 7 - (d2 + d4 + d6 + d8) ) mod10 2

c2 = ( d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9 + c1 ) mod10 0

10. karakter c1 == 11.karakter 11. karakter
 # 1. 3. 5. 7. ve 9. hanelerin toplamının 7 katından, 2. 4. 6. ve 8. hanelerin toplamı çıkartıldığında,
elde edilen sonucun 10'a bölümünden kalan, yani Mod10'u bize 10. haneyi verir.

Kurallar:
* 11 hanelidir.
* Her hanesi rakamsal değer içerir.
* İlk hane 0 olamaz.
* 1. 3. 5. 7. ve 9. hanelerin toplamının 7 katından, 2. 4. 6. ve 8. hanelerin toplamı çıkartıldığında, elde edilen sonucun 10'a bölümünden kalan, yani Mod10'u bize 10. haneyi verir.
* 1. 2. 3. 4. 5. 6. 7. 8. 9. ve 10. hanelerin toplamından elde edilen sonucun 10'a bölümünden kalan, yani Mod10'u bize 11. haneyi verir.


"""


def TCKontrol(value):
    value = str(value)

    # 11 haneli olmalı

    if not len(value) == 11:
        return False
    # sadece rakamlardan oluşmalı

    if not value.isnumeric():
        return False

    # ilk hane sıfır
    if int(value[0]) == 0:
        return False

    digits = [int(d) for d in str(value)]

    # 1. 2. 3. 4. 5. 6. 7. 8. 9. ve 10. hanelerin toplamından elde edilen sonucun
    # 10'a bölümünden kalan, yani Mod10'u bize 11. haneyi verir.

    if not sum(digits[:10]) % 10 == digits[10]:
        return False

        # 1. 3. 5. 7. ve 9. hanelerin toplamının 7 katından, 2. 4. 6. ve 8. hanelerin toplamı çıkartıldığında,
        # elde edilen sonucun 10'a bölümünden kalan, yani Mod10'u bize 10. haneyi verir.

    if not (((7 * sum(digits[:9][-1::-2])) - sum(digits[:9][-2::-2])) % 10) == digits[9]:
        return False

    # bunların hepsini geçti
    return  True