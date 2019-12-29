class Egitmen:
    isim = None
    bildigidiller = []

    def Bildigidillerigoster(self):
        for x in self.bildigidiller:
            print(x)


cagri = Egitmen()
cagri.isim = "cagri yolyapar"
cagri.bildigidiller.append("c#")
cagri.bildigidiller.append("java")

print(cagri.isim)

fatih = Egitmen()
fatih.isim = "fatih günalp"
print(fatih.isim)