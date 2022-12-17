class Utils:

    def tc_kontrol(value):
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

        on_birinci_hane = sum(digits[:10]) % 10

        if not on_birinci_hane == digits[10]:
            return False

            # 1. 3. 5. 7. ve 9. hanelerin toplamının 7 katından, 2. 4. 6. ve 8. hanelerin toplamı çıkartıldığında,
            # elde edilen sonucun 10'a bölümünden kalan, yani Mod10'u bize 10. haneyi verir.
        onuncu_hane = (((7 * sum(digits[:9][-1::-2])) - sum(digits[:9][-2::-2])) % 10)

        if not onuncu_hane == digits[9]:
            return False

        # bunların hepsini geçti
        return True

    def iban_control(value: str):

        # ilk iki karakter harf olmalı

        if not value[0].isalpha() and value[1].isalpha():
            return False

        # ilk iki karakter sonrası 12 haneli ve numara olmalı
        if (not (len(value[2:]) == 12) and (value[2:].isnumeric())):
            return False

        return True
