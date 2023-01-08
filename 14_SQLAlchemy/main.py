# pip install psycopg2
# pip install SQLAlchemy
# Bağlantı Formulu
# "postgresql://kullanci_adi:şifre@sunucu_adresi:port/veritabanı_adi"

from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    text)

db_connection_url = "postgresql://ojerfdbw:s2sK21OrGEeHBSEzJYp5F5qs4otnr_5D@hansken.db.elephantsql.com:5432/ojerfdbw"
server = create_engine(db_connection_url, echo=True)
meta = MetaData()

ogrenciler = Table(
    "ogrenciler", meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("adi", String),
    Column("soyadi", String)
)

meta.create_all(server)


# Tek Kayıt Ekleme
def ogrenci_ekle():
    baglanti = server.connect()
    sorgu = ogrenciler.insert().values(adi="Mehmet", soyadi="Öztürk")
    baglanti.execute(sorgu)
    baglanti.close()
    print("Öğrenci Eklendi !")


# ogrenci_ekle()


def coklu_kayit():
    baglanti = server.connect()
    baglanti.execute(ogrenciler.insert(), [
        {"adi": "Cansu", "soyadi": "Kaç"},
        {"adi": "Fatma", "soyadi": "Deniz"}
    ])
    baglanti.close()
    print("Çoklu öğrenci eklendi !")


# coklu_kayit()

# select * from ogrenciler

def get_ogrenciler():
    baglanti = server.connect()
    sorgu = ogrenciler.select()
    cikti = baglanti.execute(sorgu)
    cikti = list(cikti)
    baglanti.close()
    print(cikti)


# get_ogrenciler()

# Query => Sorgu

# select  ogrenciler.adi, ogrenciler.soyadi from ogrenciler where id = 3;
def get_ogrenci_by_id():
    baglanti = server.connect()
    query = text("select  ogrenciler.adi, ogrenciler.soyadi from ogrenciler where id = :parametre")
    sonuc = baglanti.execute(query, parametre=3).fetchone()
    print(sonuc)
    baglanti.close()


# get_ogrenci_by_id()

def get_ogrenciler_by_id_between():
    baglanti = server.connect()
    query = text("select * from ogrenciler where id between :x and :y")
    results = baglanti.execute(query, x=3, y=5).fetchall()
    print(results)
    baglanti.close()


# get_ogrenciler_by_id_between()

def get_ogrenci_by_adi(adi: str):
    connection = server.connect()
    query = text("Select * From ogrenciler where ogrenciler.adi like :adi")
    result = connection.execute(query, adi="%" + adi + "%").fetchall()
    print(result)
    connection.close()

# get_ogrenci_by_adi("a")

#Güncelleme
def ogrenci_guncelle():
    connection = server.connect()
    query = ogrenciler.update().where(ogrenciler.c.id == 3).values(adi="Burak", soyadi="Duman")
    connection.execute(query)
    connection.close()
    print("Kayıt Güncellendi !")

# ogrenci_guncelle()

#Silme
def ogrenci_sil_by_id(id:int):
    connection = server.connect()
    query = ogrenciler.delete().where(ogrenciler.c.id == id)
    connection.execute(query)
    connection.close()
    print(f"{id} ye sahip kayıt silindi !")


# ogrenci_sil_by_id(4)

# Toplu Silme
def toplu_ogrenci_sil():
    connection = server.connect()
    query= ogrenciler.delete().where(ogrenciler.c.id > 3)
    connection.execute(query)
    connection.close()
    print("3 ten büyük id ye sahip olan kayıtlar silindi !")


toplu_ogrenci_sil()
