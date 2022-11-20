masalar = {
    "Masa-1": "F", "Masa-2": "F",
    "Masa-3": "F", "Masa-4": "F",
    "Masa-5": "F"
}

corbalar = {
    "1-Mercimek": "7.00",
    "2-Ezogelin": "7.00",
    "3-Yayla": "6.00"
}

baliklar = {
    "1-Mezgit": "27.00",
    "2-Palamut": "32.00",
    "3-Çupra": "40.00"
}
etler = {
    "1-Pirzola": "56.00",
    "2-Biftek": "65.00",
    "3-Lokum": "45.00"
}
makarnalar = {
    "1-Bonolezli": "35.00",
    "2-Körili": "35.00",
    "3-Spagetti": "35.00"
}

arasicaklar = {
    "1-İçli Köfte": "20.00",
    "2-Sigara Böreği": "40.00",
    "3-Patso": "10.00"
}

salatalar = {
    "1-Çoban": "20.00",
    "2-Sezar": "50.00",
    "3-Mevsim": "35.00"
}
icecekler = {
    "1-Kola": "10.00",
    "2-Ayran": "5.00",
    "3-Şalgam": "15.00",
    "4-Su": "10.00"
}

siparisler = dict()
while True:

    menu = int(input("""
                Sipariş Almak İçin      :1
                Hesap Almak İçin        :2
                Menü Güncellemek İçin   :3
                Çıkış İçin              :4
                Seçiminiz:
    """))

    if menu == 4:
        break

    elif menu == 1:

        while True:
            print("""
############################################### Nusret' e Hoş Geldiniz ###############################################
            """)

            kisi_sayisi = int(input("Kaç kişisiniz ?"))

            musteri_masasi = str()
            for masa in masalar:
                if masalar[masa] == "F":
                    musteri_masasi = masa
                    masalar[masa] = "T"
                    break
            siparis = dict()

            for kisi in range(kisi_sayisi):

                print(f"{kisi + 1} . müşteri siparişi")

                while True:
                    print("""
                            1- Çorba Çeşitleri
                            2- Balık Çeşitleri
                            3- Et Çeşitleri
                            4- Makarna Çeşitleri
                            5- Arasıcak Çeşitleri
                            6- Salata Çeşitleri
                            7- İçecek Çeşitleri
                    """)

                    secim = int(input("Seçiminiz: "))

                    if secim == 1:
                        for corba in corbalar:
                            print(f"{corba} :{corbalar[corba]}₺")

                        corba_secim = int(input("Çorba Seçiminiz:"))

                        if corba_secim == 1:

                            siparis["Mercimek Çorbası"] = "7.00"
                        elif corba_secim == 2:
                            siparis["Ezogelin Çorbası"] = "7.00"
                        elif secim == 3:
                            siparis["Yayla Çorbası"] = "7.00"
                        else:
                            print("Hatalı çorba seçimi")
                            continue
                    elif secim == 2:

                        for balik in baliklar:
                            print(f"{balik} {baliklar[balik]} ₺")

                        secim_balik = int(input("Balık Seçiminiz: "))

                        if secim_balik == 1:
                            siparis["Mezgit"] = "27.00"
                        elif secim_balik == 2:
                            siparis["Palamut"] = "35.00"
                        elif secim_balik == 3:
                            siparis["Çupra"] = "45.00"
                        else:
                            print("Hatalı balık seçimi")
                            continue
                    elif secim == 3:

                        for et in etler:
                            print(f"{et} {etler[et]} ₺")

                        secim_et = int(input("Et Seçiminiz: "))

                        if secim_et == 1:
                            siparis["Pirzola"] = "56.00"
                        elif secim_et == 2:
                            siparis["Biftek"] = "65.00"
                        elif secim_et == 3:
                            siparis["Lokum"] = "45.00"
                        else:
                            print("Hatalı et seçimi")
                            continue
                    elif secim == 4:
                        for makarna in makarnalar:
                            print(f"{makarna} {makarnalar[makarna]} ₺")

                        secim_makarna = int(input("Makarna Seçiminiz: "))

                        if secim_makarna == 1:
                            siparis["Bonolezli"] = "35.00"
                        elif secim_makarna == 2:
                            siparis["Körili"] = "35.00"

                        elif secim_makarna == 3:
                            siparis["Spagetti"] = "35.00"
                        else:
                            print("Hatalı Makarna Seçimi")
                            continue

                    elif secim == 5:
                        for arasicak, fiyat in arasicaklar.items():
                            print(f"{arasicak} {fiyat} ₺")

                        secim_arasicak = int(input("Arasıcak Seçiminiz: "))

                        if secim_arasicak == 1:
                            siparis.update({"İçli Köfte": "20.00"})
                        elif secim_arasicak == 2:
                            siparis.update({"Sigara Böreği": "40.00"})
                        elif secim_arasicak ==3:
                            siparis.update({"Patso":"10.00"})
                        else:
                            print("Hatalı Arasıcak Seçimi")
                            continue
                    elif secim == 6:
                        for salata, fiyat in salatalar.items():
                            print(f"{salata} {fiyat} ₺")

                        secim_salata = int(input("Salata Seçiminiz: "))

                        if secim_salata == 1:
                            siparis.update({"Çoban Salatası": "20.00"})
                        elif secim_salata == 2:
                            siparis.update({"Sezar Salata":"40.00"})
                        elif secim_salata == 3:
                            siparis.update({"Mevsim Salatası": "20.00"})
                        else:
                            print("Hatalı Salata Seçimi")
                            continue

                    elif secim == 7:

                        for icecek, fiyat in icecekler.items():
                            print(f"{icecek} {fiyat} ₺")

                        secim_icecek = int(input("İçecek Seçiminiz: "))

                        if secim_icecek == 1:
                            siparis.update({"Kola": "8.00"})
                        elif secim_icecek == 2:
                            siparis.update({"Ayran": "10.00"})
                        elif secim_icecek == 3:
                            siparis.update({"Şalgam":"15.00"})
                        elif secim_icecek ==4:
                            siparis.update({"Su": "10.00"})
                        else:
                            print("Hatalı İçecek Seçimi")
                            continue
                    else:
                        print("Hatalı Seçim")
                        continue

                    cevap =  input("Başka bir arzunuz var mı ?(E/H)").upper()

                    if cevap == "E":
                        continue
                    elif cevap == "H":
                        siparisler.update({masa: siparis})
                        print(siparisler)
                        break
                    else:
                        print("Hatalı seçim")
                        continue

            break

    elif menu == 2:
        print("Hesap Bölümü")
        for siparis,deger in siparisler.items():
            print(f"{siparis} ======================>>> , {deger}")

        hesap =  0

        masa_hesabi =  input("Hangi masa hesabı alınacak ?")
        for i in siparisler["Masa-"+masa_hesabi].values():
            hesap += float(i)
        print(hesap)

        hesap_odendi_mi =  input("Hesap ödendi mi ?(E/H)").upper()

        if hesap_odendi_mi == "E":
            masalar["Masa-"+masa_hesabi] = "F"

        for masa, deger in masalar.items():
            print(f"{masa} ===>> {deger}")


