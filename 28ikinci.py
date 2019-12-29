# ödev.Knedisine argüman olarak bir degeri sifreleyen ve verilen şifreyi eski orjinal haline geri çeviren
# iki fonkisyon barındıran bir class yazın. görülen konular prensipler..//

class ürün:
    def __init__(self):
        self.tedarikcisirket = "e-corp"


yeniürün = ürün()


class product:
    def __init__(self, fiyat):
        self.__unitprice = None
        if fiyat>0:
            #self.__unitprice=fiyat
        else:
            print("lütfen düzgün fiyat giriniz. ürün fiyatı belirlenemedi")
        def ürünbilgilerinigöster(self):
            return self.__unitprice