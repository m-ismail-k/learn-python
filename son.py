class Personel:
    isim = None
    soyIsim = None
    yas = None
    boy = None
    kilo = None
    Tcno = ""

    def __init__(self, isim, soyIsim, yas, boy, kilo):
        self.isim = isim
        self.soyIsim = soyIsim
        self.yas = yas
        self.boy = boy
        self.kilo = kilo
        if kilo <= 90:
            print("{} az kilo ver ayı".format(self.isim, self.soyIsim))
        print("{}isimli yeni bir dangalak kayıt edildi :))) ".format(self.isim, self.soyIsim))


isim = input("lütfen isminizi giriniz")
soyisim = input("lütfen soyisminizi giriniz")
yas = input("lütfen yaşınızı giriiz")
boy=input("lütfen boyunuzu giriniz")
kilo=("lütfen kilonuzu giriniz")
cagri = Personel(isim, soyisim, yas,boy,kilo)
