-- Yorum satırı
-- SQL (Structure Query Language)

-- DML -> İç mimar -> Data Manupilation Language
-- DDL -> İnşaat mühendisi -> Data Defination Language

-- DDL
---  CREATE ->OLUŞTUR  ALTER -> GÜNCELLE  DROP -> SİL
-- RENAME ->YENİDEN ADLANDIR , TRUNCATE -> SIFIRLA


CREATE TABLE ogrenciler(
    id SERIAL PRIMARY KEY,
    ad varchar(100),
    soyad varchar(100),
    cinsiyet varchar(10)
);

--- VERİ EKLEME
INSERT INTO ogrenciler(ad,soyad,cinsiyet)
VALUES ('Mehmet Nuri', 'Öztürk', 'ERKEK');


INSERT INTO  ogrenciler(AD, SOYAD, CINSIYET)
VALUES ('Ahmet', 'Doğan', 'ERKEK');

--- Çoklu Kayıt Ekleme
INSERT INTO  ogrenciler(AD, SOYAD, CINSIYET)

VALUES ('Ayşe İrem', 'Şahin', 'KADIN'),
       ('İlsu', 'Özkaba', 'KADIN'),
       ('Ünzile', 'Arslan', 'KADIN');


--- SORGULAMALAR

-- Tablo seçme
SELECT * FROM  ogrenciler; -- ogrenciler tablosunu bütün kolonları ile getir

SELECT  ad, soyad, cinsiyet FROM  ogrenciler; -- Belirlemiş olduğum kolonları getir

SELECT  ad FROM  ogrenciler; --Sadece belirlediğim bir kolonu getir.

select ad as ABC from ogrenciler;

select  ad  || ' ' || soyad  as AD_SOYAD, cinsiyet from ogrenciler;

-- SORGULAMA
select * from  ogrenciler WHERE id = 1;
select * from  ogrenciler where  ad = 'Mehmet Nuri';
select ad, soyad from ogrenciler where ad = 'İlsu'; -- tam eşleme
select * from ogrenciler where  ad like '%e%'; -- ad kolonu içindeki kayıtlarda e harfi olanları getir
select * from  ogrenciler where  ad like 'A%'; -- A ile başlayan kayıtları getir
select  * from  ogrenciler where  ad like   '%t'; -- t ile biten kayıtları getir




