# Date Time Kütüphanesi

import datetime  # hepsini içeri alır

from datetime import datetime, date, timedelta  # sadece belirli metotları alır

import locale
locale.setlocale(locale.LC_ALL, "tr_TR.utf8") # Python a Türkçe konuş diyoruz

"""
zaman = datetime.now()  # şuan ki zamanı
print(zaman)  # Şuanki zaman
print(zaman.day)  # Şuanki zamanın gününü verir
print(zaman.month)  # Şuanki zamanın ayını verir
print(zaman.year)  # Şuanki zamanın yılını verir

print(zaman.hour)  # Şuanki zamanın saatini verir
print(zaman.minute)  # Şuanki zamanın dakikasını verir
print(zaman.second)  # Şuanki zamanın saniyesini verir
print(zaman.microsecond)  # Şuanki zamanın mikrosaniyesini verir

# Dışardan bir veriyi date time kullanarak dönüştürme işlemi

zaman2 = datetime(1993, 11, 20)  # yil-ay-gun   => yyyy-mm-dd

print(zaman2.year)
print(zaman2.date())
"""


#### ZAMAN FORMATLAMA #####
"""
%d      :   RAKAM İLE GÜNÜ
%m      :   RAKAM İLE AYI
%Y      :   RAKAM İLE 4 HANELİ YILI VERİR
%y      :   RAKAM İLE 2 HANELİ YILI VERİR
%b      :   YAZI ILE 3 HANELİ AYI VERİR
%H      :   RAKAM İLE SAATİ VERİR
%M      :   RAKAM İLE DAKİKAYI VERİR
%S      :   RAKAM İLE SANİYEYİ VERİR
%a      :   YAZI İLE 3 HANELİ GÜNÜ VERİR
%A      :   YAZI İLE TAM GÜN ADINI VERİR
%D      :   AY/GÜN/YIL OLARAK ZAMANI VERİR
"""
zaman = datetime.now()

print(zaman.strftime("Bu gün günlerden : %A"))
print(zaman.strftime("Bu gün günlerden : %D"))
print(zaman.strftime("Bu gün günlerden : %a"))

# YIL-AY-GUN--SAAT:DAKİKA:SANİYE--GÜNADI
# 2022-11-26--15:30:20--CUMARTESİ

fzaman = zaman.strftime("%Y-%m-%d--%H:%M:%S--%A")
print(fzaman)

zlist = fzaman.split("--")
print(zlist)

tarih = zlist[0]
print(tarih)

tarih_list = zlist[0].split("-")
print(tarih_list)

zaman_list = zlist[1].split(":")
print(zaman_list)

print(zlist[2])
for karakter in zlist[2]:
    print(karakter)


bu_gun  = date.today()
print(bu_gun)

dogum_tarihi =  date(1993,11,20)

print( (bu_gun -dogum_tarihi) /365 )

bir_hafta_once =  bu_gun - timedelta(14)
print(bir_hafta_once)

from  DogumTarihi import age

dogum_tarihi = date(2000,10,12)
print(age(dogum_tarihi))