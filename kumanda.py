from random import randint as r
import sys


class kumanda:
    def __init__(self, tvdurum="kapalı", tvses=0, kanallistesi=["trt"], kanal="trt"):
        print("kumnda nesnemiz oluşmaktadır")
        self.tvsesi = tvses
        self.tvdurumu = tvdurum
        self.kanallistesi = kanallistesi
        self.kanal = kanal

    def seszaltarttır(self):
        while true:
            karakter = input("ses azaltmak için '<',arttırmak için'>'çıkış için 'q' tuşuna basın ")
            if karakter == '<':
                if (self.tvsesi != 0):
                    self.tvsesi -= 1
