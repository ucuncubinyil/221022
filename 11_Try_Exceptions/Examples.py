from datetime import datetime


def dosyayi_oku():
    dosya = None
    try:
        dosya = open("sayiListesi.txt", "r")
    except FileNotFoundError:
        print("Dosya Bulunamadı!")
    else:
        satir_listesi = dosya.readlines()
        print(satir_listesi)
    finally:
        if dosya is not None:
            dosya.close()


# dosyayi_oku()


def personel_kaydet():
    while True:
        dosya = None
        try:
            personel_sayisi = int(input("Personel sayınız :"))
            dosya = open("PERSONEL.txt", mode="w", encoding="utf-8")
        except ValueError:
            print("Sadece sayı girin")
            continue
        except Exception as error:
            print(f"Bir hata oluştu {type(error).__name__} Hata Tarihi: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ")
            break
        else:
            dosya.write("####################PERSONEL BİLGLERİ####################\n")
            for personel in range(personel_sayisi):
                print(f"{personel + 1}. Personel Bilgileri")
                ad = input("Ad")
                soyad = input("Soyad")
                dogum_yili = input("Doğum Yılı")
                dosya.write(f"AD: {ad}      SOYAD: {soyad}      DOĞUM YILI: {dogum_yili}\n")
        finally:
            if dosya is not None:
                dosya.close()
                break


personel_kaydet()
