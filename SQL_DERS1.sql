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




-- BİRDEN FAZLA KOŞUL
SELECT *
FROM ogrenciler
where ad like '%e%'
  AND id = 3;
SELECT *
FROM ogrenciler
where ad like '%e%'
   or id = 3;
select *
from ogrenciler
where id = 3
   or ad like '%e%'
   or cinsiyet like '%E%';

--ARİTMETİKSEL SORGULAMA

select *
from ogrenciler
where id = 2; -- ID Sİ 2 YE EŞİT OLAN KAYDI GETİR
select *
from ogrenciler
where id > 2; -- ID Sİ 2 DEN BÜYÜK OLAN KAYITLAR
SELECT *
FROM ogrenciler
where id >= 2;
select *
from ogrenciler
where id < 1564;
select *
from ogrenciler
where id <= 145;
select *
from ogrenciler
where id != 3;
select *
from ogrenciler
where id <> 3;
select *
from ogrenciler; -- büyük projelerde kullanmayın
select *
from ogrenciler
where ad is not null; -- adı boş olmayan kayıtlar
select *
from ogrenciler
where ad is null;

--SIRALAMA İŞLEMİ
select *
from ogrenciler
order by id; -- küçüken büyüğe sıralar
select *
from ogrenciler
order by id desc; -- büyükten küçüğe sıralama
select *
from ogrenciler
order by ad; -- a dan z ye
select *
from ogrenciler
order by ad desc;
-- z den a ya


-- IN SORGULAMA
select *
from ogrenciler
where id in (1, 4, 6)
  and ad is not null;

select *
from ogrenciler
where ad in ('Mehmet Nuri', 'Ahmet')
order by id desc;


----  id , user_name, password, email, created_on
-- user_name uniqe boş olmayacak , şifre boş olmayacak, email uni bol olmayacak


CREATE TABLE accounts
(
    id         SERIAL PRIMARY KEY,
    user_name  VARCHAR(50) UNIQUE  NOT NULL,
    password   VARCHAR(100)        NOT NULL,
    email      VARCHAR(100) UNIQUE NOT NULL,
    created_on TIMESTAMP
);


INSERT INTO accounts (user_name, password, email, created_on)
values ('mehmet_nuri', '123456', 'info@mehmetnuri.net', current_timestamp);

INSERT INTO accounts (user_name, password, email, created_on)
values ('ahmet_can', '123456', 'ahmet@can.com', current_timestamp),
       ('berk_can', '123456', 'berk@can.com', current_timestamp),
       ('fatma_ak', '123456', 'fatma@ak.com', current_timestamp),
       ('kerem_er', '123456', 'kerem@er.com', current_timestamp),
       ('ali', '123456', 'ali@ali.com', current_timestamp);

--BASİT ZAMAN İŞLEMLERİ

select *
from accounts
where CAST(created_on AS DATE) > '2022-12-01';

--- iç içe sorgu

SELECT *
FROM accounts
WHERE id IN (SELECT id
             FROM accounts
             WHERE user_name LIKE '%i%');


select *
from accounts
where id in (select id from accounts where id in (select id from accounts where id in (1, 3)));


---var olan tabloya guncelleneme
ALTER TABLE accounts
    ADD COLUMN birth_year INT;
--KOLON EKLEME

-- KAYIT GÜNCELLENEME

UPDATE accounts
set birth_year = 1993
where id = 1; --  tehlikeli
update accounts
set birth_year = 2000
where birth_year is null;

-- tablo isim değiştirme

ALTER TABLE accounts
    RENAME TO hesaplar;
ALTER TABLE hesaplar
    RENAME TO accounts;


------------------

create table yazarlar
(
    id           serial primary key,
    yazar_adi    varchar(100) unique not null,
    yazar_soyadi varchar(100) unique not null
);


create table kitaplar
(
    id         serial primary key,
    kitap_adi  varchar not null,
    basim_yili int,
    yazar_id   int,

    CONSTRAINT FK_YAZARLAR
        FOREIGN KEY (yazar_id)
            REFERENCES yazarlar (id)
);

INSERT INTO yazarlar(yazar_adi, yazar_soyadi)
values ('ORHAN', 'PAMUK'),
       ('REŞAT NURİ', 'GÜLTEKİN');


INSERT INTO kitaplar (kitap_adi, basim_yili, yazar_id)
VALUES ('VEBA GECELERİ', 1993, 2);


INSERT INTO kitaplar (kitap_adi, basim_yili, yazar_id)
VALUES ('DEMİR EV', 2022, 1);


INSERT INTO kitaplar (kitap_adi, basim_yili, yazar_id)
VALUES ('KARA KİTAP', 2021, 1);


---  JOINLER

-- LEFT JOIN

select k.kitap_adi, y.yazar_adi, y.yazar_soyadi
from yazarlar y
         left join kitaplar k on k.yazar_id = y.id
where kitap_adi = 'VEBA GECELERİ';


select k.kitap_adi, concat(y.yazar_adi, ' ', y.yazar_soyadi) as yazar_ad_soyad
from yazarlar y
         left join kitaplar k on k.yazar_id = y.id
where kitap_adi = 'VEBA GECELERİ';



create table yayin_evi
(
    id       serial primary key,
    ad       varchar,
    vergi_no varchar
);


alter table kitaplar
    add column yayin_evi_id int;

alter table kitaplar
    add constraint FK_YAYIN_EVI foreign key (yayin_evi_id) references yayin_evi (id);


INSERT INTO yayin_evi(ad, vergi_no)
VALUES ('PAPATYA YAYIN EVİ', 12364),
       ('PEGASUS YAYIN EVİ', 6548);



select concat(y.yazar_adi, ' ', y.yazar_soyadi) as yazar_ad_soyad,
       k.kitap_adi,
       k.basim_yili,
       ya.ad                                    as yayin_evi
from kitaplar k
         left join yazarlar y on y.id = k.yazar_id
         left join yayin_evi ya on ya.id = k.yayin_evi_id
where y.yazar_adi = 'ORHAN'
  and y.yazar_soyadi = 'PAMUK';


----


create table contacts
(
    id           serial primary key,
    account_id   int,
    contact_name varchar(100) not null,
    phone        varchar(15)  not null,
    email        varchar(100),

    constraint fk_accounts
        foreign key (account_id)
            references accounts (id)
);


insert into contacts(account_id, contact_name, phone, email)
values (1, 'Ahmet', '+9054546546', 'ahmet@ahmet.com');

select *
from contacts c
         left join accounts a on a.id = c.account_id;



select c.contact_name, c.phone, c.email, a.user_name
from contacts c
         left join accounts a on a.id = c.account_id;


select *
from contacts
         inner join accounts a on a.id = contacts.account_id;


select *
from contacts
where account_id in (select id
                     from accounts);

select  * from  contacts
right join accounts a on a.id = contacts.account_id;



-- tablodan veri siler
delete FROM accounts where id = 7;


create table employee(

    id serial primary key ,
    ad  varchar not null ,
    soyad varchar not null ,
    yonetici_id int,

    foreign key (yonetici_id)
                     references employee(id)
                     on delete cascade
                     on update  cascade
);

insert into employee(ad, soyad, yonetici_id)
values ('AHMET', 'KOÇ', NULL),
       ('HASAN', 'KALYONCU', 1),
       ('MURAT', 'DOĞRAMACI', 1),
       ('KEMAL', 'DERVİŞ', NULL),
       ('CENGİZ', 'KURT', 4),
       ('CEZMİ', 'KALORİFER', 4);


SELECT  concat( m.ad, ' ', m.soyad ) as ad_soyad , e.ad as  yonetici_ad FROM employee e
INNER JOIN employee m ON m.yonetici_id = e.id where e.id = 1;

delete  from employee where  id = 1;


delete  from  yayin_evi  where  id = 1;

drop  table  IF EXISTS employee; -- tabloyu silme




