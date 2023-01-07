import psycopg2
from config import config


class Uygulama:

    def __init__(self):
        self.conn = None
        self.params = config()
        self.cursor = None
        self.connect()

    def __del__(self):

        if self.conn is not  None:
            self.conn.close()


    def connect(self):
        try:

            self.conn = psycopg2.connect(**self.params)
            self.cursor = self.conn.cursor()
        except(Exception, psycopg2.DataError) as err:
            print(err)

    def insert_user(self, ad: str, soyad: str):
        sql = """
            INSERT INTO isimler(ad,soyad)
            VALUES (%s, %s)
        """
        try:
            self.cursor.execute(sql, (ad, soyad))
            self.conn.commit()
            print(f"Kaydetme işlemi başarılı.")
        except(Exception, psycopg2.DataError) as err:
            print(err)

    def list_records(self,):
        isimler_liste = tuple()

        try:
            self.cursor.execute("Select  * from isimler")
            isimler_liste = self.cursor.fetchall()
            self.conn.commit()
        except (Exception, psycopg2.DataError) as err:
            print(err)


        return isimler_liste

    def insert_isimler_list(self, isimler_listesi: list):
        sql = """
                INSERT INTO isimler(ad, soyad)
                VALUES (%s, %s)
        """
        try:
            self.cursor.executemany(sql, isimler_listesi)  # Çoklu kayıt metodu
            self.conn.commit()
            print("Veriler eklendi")
        except (Exception, psycopg2.DataError) as err:
            print(err)

