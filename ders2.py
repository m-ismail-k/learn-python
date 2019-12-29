from random import randint as r


class Karakter:
    isim = ""
    meslek = ""
    irki = ""
    level1 = 1
    can = 100
    enerjisi = 1

    def Saldir(self):
        return r(10, 20) + self.level

    def DefansYap(self):
        return r(5, 10) + self.level

    def Kaç(self):
        self.kacmısMi = True
        print("savaştan kaçtı KAAMİİİİL !!! ")

    def OzelVurus(self):
        if self.enerjisi == 0:
            print("enerjiniz olmadığı için özel vuruşa geçildi")
            return False
        else:
            self.enerjisi -= 1


oyuncu = Karakter()
oyuncu.isim = "ismail"
oyuncu.meslek = "abd"
oyuncu.silah = "kılıç"
oyuncu.irki = "türk"

bilgisayar = Karakter()
bilgisayar.isim = "tp"
bilgisayar.meslek = "bilgisayarişte"
bilgisayar.silah = "çakı"
bilgisayar.irki = "lenovo"

while True:
    sonuc = input("saldırmak için s'ye, kaçmak için de k'ye, özel vuruş için v tulşuna basabilirsiniz")
    if sonuc == 's':
        oyuncununHasari = oyuncu.Saldir() - bilgisayar.Defansyap()
        bilgisayarınhasari = bilgisayar.saldir() - oyuncu.defansyap()
    if oyuncununhasari > 0:
        bilgisayar.can -= oyuncununhsari
    if bilisayarinhasari > 0:
