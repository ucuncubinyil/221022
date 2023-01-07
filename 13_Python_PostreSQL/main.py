# Python PostgreSQL Bağlantısı
# pip install psycopg2
# Bağlantı Bilgilerim
# host = tai.db.elephantsql.com
# database = mfwuaoxb
# user = mfwuaoxb
# password = dzIg8R3uvXrH4XIFgdMb5p_1vjtCsIO4

# ENV hatası Set-ExecutionPolicy -Scope CurrentUser RemoteSigned -Force

import psycopg2

db = psycopg2.connect(
    user="mfwuaoxb",
    password="dzIg8R3uvXrH4XIFgdMb5p_1vjtCsIO4",
    host="tai.db.elephantsql.com",
    port="5432",
    database="mfwuaoxb"
)

# İmleç Veritabanı bağlantısı ile komutlarımızı
# gönderebilmek için aracı bir imleç oluşturmamız gerekiyor.
imlec = db.cursor()


# print(db.get_dsn_parameters())

def create_isimler_table():
    komut_create = """
        CREATE  TABLE isimler(
            id SERIAL PRIMARY KEY ,
            ad VARCHAR NOT NULL ,
            soyad VARCHAR NOT NULL 
        );
    """
    imlec.execute(komut_create)
    db.commit()


def insert_user_table():
    komut = """
    INSERT INTO  isimler(ad,soyad) values ('MEHMET', 'ÖZTÜRK');
    """

    imlec.execute(komut)
    db.commit()

def  get_all_records():

    komut = """Select * from isimler"""

    imlec.execute(komut)

    kayitlar = imlec.fetchall()

    for kayit in kayitlar:
        print("ID:", kayit[0],  "AD:", kayit[1],  "SOYAD:", kayit[2])
        # print(type(kayit))
        # print("Id: " + str(kayit[0]))
        # print("Ad: " + str(kayit[1]))
        # print("Soyad: " + str(kayit[2]))


def  update_record():
    komut = """
    UPDATE  isimler  SET ad= 'VELİ' WHERE  id = 1;
    """
    imlec.execute(komut)
    db.commit()

def delete_record():
    komut = """Delete From isimler  where id=1"""
    imlec.execute(komut)
    db.commit()

# create_isimler_table()
# insert_user_table()
# get_all_records()
# update_record()
delete_record()