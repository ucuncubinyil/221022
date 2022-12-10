"""
  Topla, Çıkar, Çarp , Bol
  class metot şeklinde olsun
  """
from SifirCarpmaException import SifirCarpmaException
class Matematik():

    @classmethod
    def topla(cls, s1: int, s2: int):
        return s1 + s2

    @classmethod
    def cikar(cls, s1: int, s2: int):
        return s1 - s2

    @classmethod
    def carp(cls, s1: int, s2: int):
        try:
            if s1 == 0 or s2 == 0:
                raise SifirCarpmaException
            return s1 * s2
        except SifirCarpmaException:
            print("Sayılardan hiç biri sıfır(0) olamaz")

    @classmethod
    def bol(cls, s1: int, s2: int, tam_sayi=False):
        try:
            sonuc = s1 / s2
            if tam_sayi == True:
                return int(sonuc)
            else:
                return sonuc
        except ZeroDivisionError:
            print("Hiç bir sayı sıfıra bölünemez!")
