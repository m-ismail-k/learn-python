# Kategori  => ürünleri göster,
# kayıtlı kategorilerigöster
class kategori:
    kategoriler = []

    def __init__(self, kategoriismi, kategoriacıklaması):
        self.isim = kategoriismi
        self.açıklama = kategoriacıklaması
        self.urunleri = []
        kategori.kategoriler.append(kategoriismi)

    def urunlerigöster(self):
        for x in self.urunleri:
            print(x)

    def kayitlikategorilerigöster(self):
        for x in kategori.kategoriler:
            print(x)


isim = input("kategori ismini girin ")
açıklaması = input("kategori açıklamasını girin")
yenikategori = kategori(isim, açıklaması)
ürünler = input("kategoriye it ürünler lütfen virgül ile yazınız")
eklenecekürünler= ürünler.split(',')

for i in eklenecekürünler:
    yenikategori.ürünleri.append(i)
print("eklediğiniz ürünler")
for i in yenikategori.urunleri:
    print(i)
print(kategori.kategoriler)