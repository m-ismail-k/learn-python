class Egitmen:
    def __init__(self, isim, soyad):
        self.Isim = None
        self.Soyad = soyad
        self.Bildigidiller = []

    def Bildigidillergöster(self):
        for x in self.Bildigidiller:
            print(x)


cagri = Egitmen("cagri", "yolyapar")
cagri.Bildigidiller.append("python")
cagri.Bİldigidiller.appned("java")

fatih = Egitmen("fatih", "günalp")
fatih.Bildigidiller.append("objective c")
fatih.Bildigidiller.append("java")

print("{} bildigi diller".format(cagri.isim))
print("{} bildigi diller".format(fatih.Isim))
fatih.Bildigidillerigöster()